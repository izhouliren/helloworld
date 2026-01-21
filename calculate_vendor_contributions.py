import subprocess
import csv
import os
import re
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from collections import Counter

# ================= 配置区域 =================
# Linux 内核源码路径
REPO_PATH = "./linux"

# 统计时间段
START_DATE = "2025-01-01"
END_DATE = "2025-12-31"

# 可视化设置
PLOT_TITLE = "2025年Linux内核厂商贡献统计"
PLOT_FILENAME = "linux_vendor_contributions_2025.png"
TOP_N = 20  # 只显示贡献前N名的厂商
FONT_PATH = "/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf"  # 系统中的中文字体
# ===========================================

def get_all_commits(repo_path, start, end):
    """
    运行 git log 命令获取指定时间段内的所有提交
    """
    # 检查路径是否存在
    if not os.path.exists(os.path.join(repo_path, ".git")):
        print(f"错误: 在路径 '{repo_path}' 下未找到 Git 仓库。请修改脚本中的 REPO_PATH。")
        return []

    # 定义 git 命令
    cmd = [
        "git",
        "-C", repo_path,
        "log",
        "--no-merges",  # 排除合并请求
        f"--since={start}",
        f"--until={end}",
        "--date=short",
        "--pretty=format:%ae"  # 只获取作者邮箱
    ]

    try:
        # 执行命令
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
        
        if result.returncode != 0:
            print("Git 命令执行出错:", result.stderr)
            return []

        # 解析输出，去除空行
        emails = [line.strip() for line in result.stdout.strip().split('\n') if line.strip()]
        return emails
    except FileNotFoundError:
        print("错误: 未找到 git 命令，请确保系统中已安装 Git。")
        return []
    except Exception as e:
        print(f"发生未知错误: {e}")
        return []

def extract_domain(email):
    """
    从邮箱地址中提取域名
    """
    match = re.match(r'.+@(.+)', email)
    if match:
        return match.group(1)
    return "unknown"

# 厂商域名到中文名称的映射表
# 可以根据需要扩展这个映射表
company_map = {
    "Actions Microelectronics": ['actions-semi.com'],
    "Alibaba": ['alibaba.com', 'linux.alibaba.com'],
    "Asianux": ['asianux.com'],
    "Baidu": ['baidu.com'],
    "ByteDance": ['bytedance.com'],
    "China Mobile": ['chinamobile.com', 'cmss.chinamobile.com'],  # 包含中国移动系统软件有限公司
    "China Telecom": ['chinatelecom.cn'],
    "Coolpad": ['coolpad.com'],
    "DaTang Mobile": ['datangmobile.cn'],
    "Hanwang Tech": ['hanwang.com.cn'],
    "Huawei": ['huawei.com', 'huaweicloud.com', 'huawei-partners.com'],
    "Inspur": ['inspur.com'],
    "Kedacom": ['kedacom.com'],
    "Kylin Software": ['kylinos.cn', 'kylinsec.com.cn'],
    "Lemote": ['lemote.com'],
    "Lenovo": ['lenovo.com'],
    "Loongson": ['loongson.cn'],
    "MaxWit": ['maxwit.com'],
    "NFSChina": ['nfschina.com'],  # 修正域名，实际使用的是nfschina.com
    "OPPO": ['oppo.com', 'oneplus.com'],
    "Red Flag Linux": ['redflag-linux.com'],
    "Rockchip": ['rock-chips.com'],
    "Tao Bao": ['taobao.com'],
    "Tencent": ['tencent.com'],
    "UnionTech": ['uniontech.com'],
    "Xiaomi": ['xiaomi.com'],
    "ZTE": ['zte.com.cn'],
    "vivo": ['vivo.com', 'iqoo.com'],
}

def get_company_name(domain):
    """
    将域名映射为更友好的公司名称
    """
    domain_lower = domain.lower()
    
    # 遍历company_map，查找包含该域名的公司
    for company_name, domains in company_map.items():
        for d in domains:
            if d.lower() == domain_lower:
                return company_name
    
    # 如果没有找到，返回原域名
    return domain

def generate_bar_chart(contributions, title, filename, top_n=20):
    """
    生成柱状图
    """
    # 只显示前N名
    top_contributions = contributions.most_common(top_n)
    
    # 准备数据
    companies = [get_company_name(domain) for domain, _ in top_contributions]
    counts = [count for _, count in top_contributions]
    
    # 设置字体，使用字体列表以支持中英文混合显示
    plt.rcParams['font.family'] = ['Droid Sans Fallback', 'DejaVu Sans']
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
    
    # 创建图表
    plt.figure(figsize=(12, 8))
    
    # 绘制柱状图（改为纵向）
    bars = plt.bar(range(len(companies)), counts, color='skyblue')
    
    # 添加数据标签
    for i, bar in enumerate(bars):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5, 
                 f'{counts[i]}', ha='center')
    
    # 设置图表属性
    plt.xlabel('厂商', fontsize=12)
    plt.ylabel('提交数量', fontsize=12)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xticks(range(len(companies)), companies, fontsize=10, rotation=45, ha='right')
    plt.tight_layout()
    
    # 保存图表
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"图表已保存至: {os.path.abspath(filename)}")
    
    # 显示图表
    plt.show()

def save_contributions_to_csv(contributions, filename):
    """
    将贡献统计结果保存到CSV文件
    """
    with open(filename, mode='w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['厂商域名', '公司名称', '提交数量'])
        for domain, count in contributions.most_common():
            writer.writerow([domain, get_company_name(domain), count])
    print(f"统计结果已保存至: {os.path.abspath(filename)}")

if __name__ == "__main__":
    print(f"正在获取 {REPO_PATH} 中 {START_DATE} 至 {END_DATE} 期间的所有提交...")
    
    # 获取所有提交
    all_emails = get_all_commits(REPO_PATH, START_DATE, END_DATE)
    
    if not all_emails:
        print("未找到任何提交，程序退出。")
        exit(1)
    
    print(f"成功获取 {len(all_emails)} 条提交记录。")
    
    # 提取域名
    domains = [extract_domain(email) for email in all_emails]
    
    # 统计每个域名的提交数量
    contributions = Counter(domains)
    
    print(f"共识别出 {len(contributions)} 个不同的厂商域名。")
    
    # 保存结果到CSV文件
    csv_filename = f"linux_vendor_contributions_{START_DATE.split('-')[0]}.csv"
    save_contributions_to_csv(contributions, csv_filename)
    
    # 按公司名称合并贡献数量
    merged_contributions = Counter()
    
    # 遍历所有贡献记录
    for domain, count in contributions.items():
        # 获取公司名称
        company_name = get_company_name(domain)
        # 累加到对应公司
        merged_contributions[company_name] += count
    
    # 确保所有company_map中的公司都被包含，包括提交次数为0的
    all_company_names = list(company_map.keys())  # 所有公司名称
    
    # 初始化所有公司的贡献次数为0
    all_contributions = Counter()
    for company_name in all_company_names:
        all_contributions[company_name] = 0
    
    # 将实际贡献次数合并进去
    for company_name, count in merged_contributions.items():
        if company_name in all_company_names:
            all_contributions[company_name] = count
    
    # 生成柱状图，显示所有company_map中的厂商
    print(f"正在生成company_map中所有厂商的贡献柱状图...")
    generate_bar_chart(all_contributions, PLOT_TITLE, PLOT_FILENAME, len(all_contributions))
    
    print("\n程序执行完成！")
    
    # 按照贡献数量从高到低排序
    sorted_company_contributions = all_contributions.most_common()
    
    # 输出company_map中所有厂商的排名，包括提交次数为0的
    print("\ncompany_map中所有厂商的贡献排名：")
    for i, (company_name, count) in enumerate(sorted_company_contributions, 1):
        print(f"{i:2d}. {company_name:30} - {count:5d} 次提交")