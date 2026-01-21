import subprocess
import csv
import os
from datetime import datetime
import re

# ================= 配置区域 =================
# 请将此处改为你本地 Linux 内核源码的实际路径
# 例如: "/home/user/projects/linux" 或 "D:/code/linux"
REPO_PATH = "./linux" 

# 搜索条件
START_DATE = "2025-01-01"
END_DATE = "2025-12-31"

# 输出设置
OUTPUT_DIR = "2025_company_commits"  # 存放CSV文件的文件夹

# 厂商域名到中文名称的映射表
# 从calculate_vendor_contributions.py中导入
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
# ===========================================

def get_git_commits(repo_path, domain, start, end):
    """
    运行 git log 命令获取特定作者和时间段的提交
    """
    # 检查路径是否存在
    if not os.path.exists(os.path.join(repo_path, ".git")):
        print(f"错误: 在路径 '{repo_path}' 下未找到 Git 仓库。请修改脚本中的 REPO_PATH。")
        return []

    # 定义 git 命令
    # %h: 哈希简写, %an: 作者名, %ae: 作者邮箱, %ad: 日期, %s: 标题
    # 使用 |^| 作为分隔符，避免与提交信息中的逗号冲突
    cmd = [
        "git",
        "-C", repo_path,  # 指定在哪个目录下运行
        "log",
        "--no-merges",    # 排除合并请求，只看代码提交
        f"--author={domain}",
        f"--since={start}",
        f"--until={end}",
        "--date=short",   # 日期格式 YYYY-MM-DD
        "--pretty=format:%h|^|%an|^|%ae|^|%ad|^|%s"
    ]

    try:
        # 执行命令
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
        
        if result.returncode != 0:
            print("Git 命令执行出错:", result.stderr)
            return []

        # 解析输出
        commits = []
        raw_lines = result.stdout.strip().split('\n')
        
        if not raw_lines or raw_lines[0] == "":
            return []

        for line in raw_lines:
            parts = line.split('|^|')
            if len(parts) == 5:
                commits.append({
                    "Commit Hash": parts[0],
                    "Author Name": parts[1],
                    "Author Email": parts[2],
                    "Date": parts[3],
                    "Subject": parts[4]
                })
        return commits

    except FileNotFoundError:
        print("错误: 未找到 git 命令，请确保系统中已安装 Git。")
        return []
    except Exception as e:
        print(f"发生未知错误: {e}")
        return []

def save_to_csv(commits, company_name, output_dir):
    """
    将结果保存到 CSV 文件，文件名带公司名称和日期
    """
    if not commits:
        print(f"{company_name}: 未找到符合条件的提交，未生成文件。")
        return

    # 生成带日期的文件名
    now_str = datetime.now().strftime("%Y-%m-%d")
    # 清理文件名，移除特殊字符
    safe_company_name = re.sub(r'[^\w\d_-]', '_', company_name)
    filename = f"{safe_company_name}_linux_commits_{now_str}.csv"
    filepath = os.path.join(output_dir, filename)

    # CSV 表头
    headers = ["Date", "Author Name", "Author Email", "Subject", "Commit Hash"]

    try:
        with open(filepath, mode='w', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            for commit in commits:
                writer.writerow(commit)
        
        print(f"{company_name}: 成功！已找到 {len(commits)} 条提交。")
        print(f"结果已保存至: {os.path.abspath(filepath)}")
    except IOError as e:
        print(f"{company_name}: 保存文件时出错: {e}")

if __name__ == "__main__":
    # 创建输出目录（如果不存在）
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"已创建输出目录: {os.path.abspath(OUTPUT_DIR)}")
    
    # 遍历所有公司
    total_companies = len(company_map)
    for i, (company_name, domains) in enumerate(company_map.items(), 1):
        print(f"\n[{i}/{total_companies}] 正在处理公司: {company_name}")
        print(f"对应的邮箱后缀: {', '.join(domains)}")
        
        # 收集所有域名的提交
        all_commits = []
        for domain in domains:
            print(f"  正在搜索 @{domain} 的提交...")
            commits = get_git_commits(REPO_PATH, domain, START_DATE, END_DATE)
            all_commits.extend(commits)
        
        # 保存到CSV文件
        save_to_csv(all_commits, company_name, OUTPUT_DIR)
    
    print(f"\n所有公司的提交已处理完成！")
    print(f"CSV文件已保存至目录: {os.path.abspath(OUTPUT_DIR)}")