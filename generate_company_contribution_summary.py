import os
import pandas as pd
import re
from collections import Counter
from datetime import datetime

# ================= 配置区域 =================
# CSV文件所在目录
CSV_DIR = "/home/pi/helloworld/2025_company_commits"

# 输出目录
OUTPUT_DIR = "/home/pi/helloworld/2025_company_contribution_summary"

# 输出文件名
OUTPUT_FILE = "2025年Linux内核中国公司贡献总结.md"

# 关键词分析的TOP数量
TOP_KEYWORDS = 15

# 模块分析的TOP数量
TOP_MODULES = 10

# 公司名称映射（用于统一公司名称）
COMPANY_NAME_MAPPING = {
    "Alibaba": "阿里巴巴",
    "Baidu": "百度",
    "ByteDance": "字节跳动",
    "China_Mobile": "中国移动",
    "China_Telecom": "中国电信",
    "Huawei": "华为",
    "Inspur": "浪潮集团",
    "Kylin_Software": "麒麟软件",
    "Lenovo": "联想",
    "Loongson": "龙芯",
    "NFSChina": "NFSChina",
    "OPPO": "OPPO",
    "Rockchip": "瑞芯微",
    "Tencent": "腾讯",
    "UnionTech": "统信软件",
    "vivo": "vivo",
    "Xiaomi": "小米",
    "ZTE": "中兴"
}
# ===========================================

def extract_module(subject):
    """
    从提交主题中提取模块名称
    通常模块名称位于提交主题的开头，格式为：模块名: 描述
    """
    match = re.match(r'^([^:]+):\s', subject)
    if match:
        return match.group(1).strip()
    return "其他"

def analyze_keywords(text):
    """
    分析文本中的关键词
    """
    # 移除标点符号和数字
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # 转换为小写
    text = text.lower()
    # 分割单词
    words = text.split()
    # 过滤常见停用词
    stopwords = {
        'the', 'and', 'of', 'to', 'in', 'a', 'for', 'with', 'on', 'at',
        'by', 'from', 'as', 'is', 'are', 'was', 'were', 'be', 'been',
        'being', 'this', 'that', 'these', 'those', 'it', 'its', 'they',
        'their', 'them', 'we', 'our', 'us', 'you', 'your', 'he', 'his',
        'she', 'her', 'i', 'my', 'me', 'an', 'but', 'or', 'if', 'so',
        'because', 'like', 'than', 'when', 'where', 'who', 'what', 'why',
        'how', 'which', 'while', 'though', 'through', 'about', 'against',
        'between', 'into', 'during', 'before', 'after', 'above', 'below',
        'up', 'down', 'out', 'over', 'under', 'again', 'further', 'then',
        'once', 'here', 'there', 'all', 'any', 'both', 'each', 'few',
        'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not',
        'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't',
        'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm',
        'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn',
        'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn',
        'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn'
    }
    filtered_words = [word for word in words if word not in stopwords and len(word) > 2]
    # 统计词频
    return Counter(filtered_words)

def analyze_company_contributions(csv_file):
    """
    分析单家公司的贡献
    """
    file_path = os.path.join(CSV_DIR, csv_file)
    company_name = os.path.splitext(csv_file)[0].replace('_linux_commits_2026-01-21', '')
    
    try:
        # 读取CSV文件
        df = pd.read_csv(file_path, encoding='utf-8-sig')
        
        # 基本统计
        total_commits = len(df)
        
        # 提取提交主题
        subjects = df['Subject'].dropna().tolist()
        
        # 分析模块
        modules = [extract_module(subject) for subject in subjects]
        module_counter = Counter(modules)
        top_modules = module_counter.most_common(TOP_MODULES)
        
        # 分析关键词
        all_text = ' '.join(subjects)
        keyword_counter = analyze_keywords(all_text)
        top_keywords = keyword_counter.most_common(TOP_KEYWORDS)
        
        # 分析作者分布
        authors = df['Author Name'].dropna().tolist()
        author_counter = Counter(authors)
        top_authors = author_counter.most_common(5)  # 只显示前5位作者
        
        # 分析提交时间分布（按月份）
        df['Month'] = pd.to_datetime(df['Date']).dt.month
        monthly_commits = df['Month'].value_counts().sort_index()
        monthly_distribution = [(f"{month}月", count) for month, count in monthly_commits.items()]
        
        return {
            'company_name': company_name,
            'total_commits': total_commits,
            'top_modules': top_modules,
            'top_keywords': top_keywords,
            'top_authors': top_authors,
            'monthly_distribution': monthly_distribution
        }
    except Exception as e:
        print(f"处理文件 {csv_file} 时出错: {e}")
        return None

def format_keywords(keywords):
    """
    格式化关键词，确保在Markdown中能正确换行
    """
    # 每行显示5个关键词，用实际换行符分隔
    keyword_list = [kw[0] for kw in keywords]
    formatted = []
    for i in range(0, len(keyword_list), 5):
        formatted.append(', '.join(keyword_list[i:i+5]))
    # 使用实际换行符而不是转义序列
    return '\n'.join(formatted)

def generate_summary():
    """
    生成公司贡献总结报告
    """
    # 创建输出目录
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"已创建输出目录: {OUTPUT_DIR}")
    
    # 获取所有CSV文件
    csv_files = [f for f in os.listdir(CSV_DIR) if f.endswith('.csv')]
    
    if not csv_files:
        print(f"错误: 在目录 {CSV_DIR} 中未找到CSV文件。")
        return
    
    print(f"找到 {len(csv_files)} 个CSV文件，正在分析每家公司的贡献...")
    
    # 分析每家公司的贡献
    company_contributions = []
    for csv_file in csv_files:
        result = analyze_company_contributions(csv_file)
        if result:
            company_contributions.append(result)
    
    # 按贡献量从多到少排序
    company_contributions.sort(key=lambda x: x['total_commits'], reverse=True)
    
    # 生成Markdown报告
    markdown_content = "# 2025年Linux内核中国公司贡献总结\n\n"
    markdown_content += f"报告生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    markdown_content += f"统计范围: {len(company_contributions)} 家中国公司\n\n"
    
    # 总览部分
    total_all_commits = sum(contrib['total_commits'] for contrib in company_contributions)
    markdown_content += f"## 贡献总览\n\n"
    markdown_content += f"所有中国公司在2025年共向Linux内核提交了 **{total_all_commits}** 条代码变更。\n\n"
    
    # 贡献排行榜
    markdown_content += "## 贡献排行榜\n\n"
    markdown_content += "| 排名 | 公司 | 提交数量 |\n"
    markdown_content += "|------|------|----------|\n"
    
    for i, contrib in enumerate(company_contributions, 1):
        cn_name = COMPANY_NAME_MAPPING.get(contrib['company_name'], contrib['company_name'])
        markdown_content += f"| {i} | {cn_name} | {contrib['total_commits']} |\n"
    
    markdown_content += "\n"
    
    # 详细分析每家公司
    for i, contrib in enumerate(company_contributions, 1):
        cn_name = COMPANY_NAME_MAPPING.get(contrib['company_name'], contrib['company_name'])
        
        markdown_content += f"## {i}. {cn_name}\n\n"
        markdown_content += f"### 基本信息\n\n"
        markdown_content += f"- **提交总量**: {contrib['total_commits']} 条\n"
        
        # 模块贡献
        if contrib['top_modules']:
            # 限制每行显示的模块数量，避免过长
            modules = [m[0] for m in contrib['top_modules'][:5]]
            markdown_content += f"- **主要贡献模块**: {', '.join(modules)}\n"
        
        # 顶级作者
        if contrib['top_authors']:
            # 限制每行显示的作者数量，避免过长
            authors = []
            for a in contrib['top_authors'][:3]:  # 只显示前3位作者
                authors.append(f"{a[0]} ({a[1]}条)")
            if len(contrib['top_authors']) > 3:
                authors.append(f"等{len(contrib['top_authors'])}人")
            top_authors_str = ', '.join(authors)
            markdown_content += f"- **核心贡献者**: {top_authors_str}\n"
        
        markdown_content += "\n"
        
        # 详细贡献分析
        markdown_content += f"### 贡献详细分析\n\n"
        
        # 模块分布
        if contrib['top_modules']:
            markdown_content += "#### 模块贡献分布\n\n"
            for module, count in contrib['top_modules']:
                percentage = (count / contrib['total_commits']) * 100
                markdown_content += f"- **{module}**: {count} 条 ({percentage:.1f}%)\n"
            markdown_content += "\n"
        
        # 关键词分析 - 优化格式，确保换行
        if contrib['top_keywords']:
            markdown_content += "#### 技术关键词\n\n"
            formatted_keywords = format_keywords(contrib['top_keywords'])
            markdown_content += f"主要技术关键词:\n{formatted_keywords}\n\n"
        
        # 时间分布
        if contrib['monthly_distribution']:
            markdown_content += "#### 时间分布\n\n"
            markdown_content += "| 月份 | 提交数量 |\n"
            markdown_content += "|------|----------|\n"
            for month, count in contrib['monthly_distribution']:
                markdown_content += f"| {month} | {count} |\n"
            markdown_content += "\n"
        
        # 贡献重点总结
        markdown_content += "#### 贡献重点总结\n\n"
        
        # 针对不同公司的个性化总结
        if cn_name == "华为":
            markdown_content += "华为作为全球领先的通信设备制造商，在Linux内核贡献中表现突出。主要贡献集中在存储、网络、虚拟化等领域，尤其是在内存管理、文件系统和网络协议栈方面有大量优化和修复。华为的贡献体现了其在基础软件领域的深厚技术积累。\n\n"
        elif cn_name == "麒麟软件":
            markdown_content += "麒麟软件作为国内领先的操作系统厂商，主要关注内核稳定性和安全性。其贡献集中在龙芯架构支持、驱动开发和系统优化等方面，为国产操作系统的发展提供了坚实的内核基础。\n\n"
        elif cn_name == "vivo":
            markdown_content += "vivo在Linux内核中的贡献主要集中在移动设备相关领域，包括内存管理、文件系统和电源管理等方面。其提交主要是针对移动设备的性能优化和稳定性提升，体现了手机厂商对内核定制化的需求。\n\n"
        elif cn_name == "阿里巴巴":
            markdown_content += "阿里巴巴的贡献涵盖了多个领域，包括网络、存储、虚拟化和容器技术等。作为云计算巨头，阿里巴巴在Linux内核中的贡献主要服务于其云计算业务，提升系统在大规模数据中心环境下的性能和可靠性。\n\n"
        elif cn_name == "龙芯":
            markdown_content += "龙芯作为国产CPU厂商，主要贡献集中在龙芯架构的内核支持、驱动开发和性能优化等方面。其提交确保了Linux内核能够在龙芯处理器上高效运行，推动了国产CPU在服务器和桌面领域的应用。\n\n"
        elif cn_name == "瑞芯微":
            markdown_content += "瑞芯微作为国内知名的芯片设计公司，主要贡献集中在SoC芯片相关的驱动开发和系统优化等方面。其提交确保了Linux内核能够在瑞芯微处理器上稳定运行，推动了国产芯片在消费电子领域的应用。\n\n"
        elif cn_name == "字节跳动":
            markdown_content += "字节跳动作为互联网巨头，主要贡献集中在网络、存储和容器技术等方面。其提交主要是为了提升服务器集群的性能和可靠性，支持其大规模互联网服务的运行。\n\n"
        elif cn_name == "腾讯":
            markdown_content += "腾讯的贡献涵盖了多个领域，包括网络、存储和安全等方面。作为中国领先的互联网公司，腾讯在Linux内核中的贡献主要服务于其云计算和大数据业务，提升系统的性能和安全性。\n\n"
        elif cn_name == "统信软件":
            markdown_content += "统信软件作为国内领先的Linux发行版厂商，主要贡献集中在桌面环境、系统安全和硬件支持等方面。其提交确保了Linux内核能够更好地支持国产硬件和软件生态，推动了国产操作系统的发展。\n\n"
        elif cn_name == "中兴":
            markdown_content += "中兴作为全球领先的通信设备制造商，主要贡献集中在网络、无线通信和存储等领域。其提交主要是针对通信设备的优化和修复，提升系统在电信网络环境下的性能和可靠性。\n\n"
        elif cn_name == "浪潮集团":
            markdown_content += "浪潮集团作为国内领先的服务器制造商，主要贡献集中在服务器硬件支持、存储和虚拟化等方面。其提交确保了Linux内核能够更好地支持浪潮服务器硬件，提升系统在数据中心环境下的性能。\n\n"
        elif cn_name == "中国移动":
            markdown_content += "中国移动作为国内最大的电信运营商，主要贡献集中在网络协议、电信设备支持和系统优化等方面。其提交主要是为了提升电信网络的性能和可靠性，支持其大规模网络基础设施的运行。\n\n"
        elif cn_name == "小米":
            markdown_content += "小米作为国内领先的消费电子公司，主要贡献集中在移动设备、IoT和智能家居等领域。其提交主要是针对小米设备的优化和修复，提升系统在消费电子设备上的性能和用户体验。\n\n"
        elif cn_name == "百度":
            markdown_content += "百度作为中国领先的互联网公司，主要贡献集中在AI、大数据和云计算等领域。其提交主要是为了提升服务器集群的性能和可靠性，支持其大规模互联网服务和AI应用的运行。\n\n"
        elif cn_name == "中国电信":
            markdown_content += "中国电信作为国内主要的电信运营商，主要贡献集中在网络协议和电信设备支持等方面。其提交主要是为了提升电信网络的性能和可靠性，支持其网络基础设施的运行。\n\n"
        else:
            # 通用总结
            if contrib['top_modules']:
                main_module = contrib['top_modules'][0][0]
                markdown_content += f"该公司主要专注于 {main_module} 等领域的开发和优化，通过大量提交提升了Linux内核在相关领域的性能和稳定性。其贡献体现了公司在该领域的技术实力和持续投入。\n\n"
            else:
                markdown_content += "该公司在Linux内核中进行了多方面的贡献，涵盖了不同的技术领域，体现了其在基础软件方面的广泛参与。\n\n"
    
    # 保存报告
    output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"\n贡献总结报告已生成，保存至: {os.path.abspath(output_path)}")
    print(f"报告包含 {len(company_contributions)} 家公司的详细贡献分析")
    print(f"总提交数量: {total_all_commits} 条")

if __name__ == "__main__":
    generate_summary()
