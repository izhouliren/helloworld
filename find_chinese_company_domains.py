import csv

# 已知中国公司的邮箱后缀映射
chinese_company_domains = {
    "Huawei": ["huawei.com", "huaweicloud.com", "huawei-partners.com"],
    "Alibaba": ["alibaba.com", "linux.alibaba.com"],
    "Kylin Software": ["kylinos.cn", "kylinsec.com.cn"],
    "Tencent": ["tencent.com"],
    "ByteDance": ["bytedance.com"],
    "Baidu": ["baidu.com"],
    "Lenovo": ["lenovo.com"],
    "Xiaomi": ["xiaomi.com"],
    "China Mobile": ["chinamobile.com"],
    "China Telecom": ["chinatelecom.cn"],
    "Inspur": ["inspur.com"],
    "Loongson": ["loongson.cn"],
    "ZTE": ["zte.com.cn"],
    "OPPO": ["oppo.com", "oneplus.com"],
    "vivo": ["vivo.com", "iqoo.com"],
    "Rockchip": ["rock-chips.com"],  # 瑞星微
    "MediaTek": ["mediatek.com"],    # 联发科
    "Realtek": ["realtek.com"]       # 瑞昱
}

def find_chinese_companies(csv_file):
    """
    从CSV文件中筛选出中国公司及其邮箱后缀
    """
    # 读取CSV文件
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # 跳过表头
        
        # 收集所有公司名称
        all_companies = set()
        for row in reader:
            if len(row) >= 2:
                all_companies.add(row[1])
    
    # 筛选出中国公司
    chinese_companies = set()
    for company in all_companies:
        if company in chinese_company_domains:
            chinese_companies.add(company)
    
    return sorted(chinese_companies)

def main():
    csv_file = "/home/pi/helloworld/all_kernel_contribute_data_20250201.csv"
    
    print("从CSV文件中筛选中国公司...")
    chinese_companies = find_chinese_companies(csv_file)
    
    print("\n找到的中国公司及其邮箱后缀：")
    print("=" * 60)
    for company in chinese_companies:
        domains = chinese_company_domains[company]
        print(f"公司名称：{company}")
        print(f"邮箱后缀：{', '.join(domains)}")
        print("-" * 60)
    
    print(f"\n总计：{len(chinese_companies)} 家中国公司")

if __name__ == "__main__":
    main()