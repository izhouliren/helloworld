# 脚本用于更新all_companies.txt和company_map

import csv

# 所有中国公司列表，按领域分类
chinese_companies = {
    "互联网与云计算巨头": [
        ("Huawei", ["huawei.com", "huaweicloud.com", "huawei-partners.com"]),
        ("Alibaba", ["alibaba.com", "linux.alibaba.com"]),
        ("Tencent", ["tencent.com"]),
        ("ByteDance", ["bytedance.com"]),
        ("Baidu", ["baidu.com"]),
        ("Tao Bao", ["taobao.com"])
    ],
    "手机与消费电子": [
        ("Xiaomi", ["xiaomi.com"]),
        ("OPPO", ["oppo.com", "oneplus.com"]),
        ("vivo", ["vivo.com", "iqoo.com"]),
        ("ZTE", ["zte.com.cn"]),
        ("Lenovo", ["lenovo.com"]),
        ("Coolpad", ["coolpad.com"])
    ],
    "芯片与硬件设计": [
        ("Loongson", ["loongson.cn"]),
        ("Rockchip", ["rock-chips.com"]),
        ("Inspur", ["inspur.com"]),
        ("Actions Microelectronics", ["actions-semi.com"]),
        ("Kedacom", ["kedacom.com"]),
        ("Hanwang Tech", ["hanwang.com.cn"]),
        ("Lemote", ["lemote.com"])
    ],
    "操作系统与软件厂商": [
        ("Kylin Software", ["kylinos.cn", "kylinsec.com.cn"]),
        ("UnionTech", ["uniontech.com"]),
        ("Red Flag Linux", ["redflag-linux.com"]),
        ("Asianux", ["asianux.com"]),
        ("MaxWit", ["maxwit.com"]),
        ("NFSChina", ["nfschina.org"])
    ],
    "电信运营商": [
        ("China Mobile", ["chinamobile.com"]),
        ("China Telecom", ["chinatelecom.cn"]),
        ("DaTang Mobile", ["datangmobile.cn"])
    ]
}

# 首先更新all_companies.txt
def update_all_companies():
    """
    将所有中国公司添加到all_companies.txt文件中
    """
    # 读取现有公司
    existing_companies = set()
    try:
        with open('/home/pi/helloworld/all_companies.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    existing_companies.add(line)
    except FileNotFoundError:
        pass
    
    # 添加新公司
    new_companies = []
    for category, companies in chinese_companies.items():
        for company_name, _ in companies:
            if company_name not in existing_companies:
                new_companies.append(company_name)
    
    if new_companies:
        # 按字母顺序排序并添加到文件末尾
        new_companies.sort()
        with open('/home/pi/helloworld/all_companies.txt', 'a') as f:
            for company in new_companies:
                f.write(f"{company}\n")
        print(f"已向all_companies.txt添加 {len(new_companies)} 家新公司")
    else:
        print("all_companies.txt中已有所有公司")

# 更新company_map
def update_company_map():
    """
    将所有中国公司添加到calculate_vendor_contributions.py中的company_map
    """
    # 读取现有文件内容
    with open('/home/pi/helloworld/calculate_vendor_contributions.py', 'r') as f:
        content = f.read()
    
    # 构建新的company_map
    new_company_map = {
        "Huawei": ["huawei.com", "huaweicloud.com", "huawei-partners.com"],
        "Alibaba": ["alibaba.com", "linux.alibaba.com"],
        "Kylin Software": ["kylinos.cn", "kylinsec.com.cn"],
        "Tencent": ["tencent.com"],
        "ByteDance": ["bytedance.com"]
    }
    
    # 添加所有中国公司
    for category, companies in chinese_companies.items():
        for company_name, domains in companies:
            new_company_map[company_name] = domains
    
    # 生成新的company_map字符串
    map_str = "# 厂商域名到中文名称的映射表\n"
    map_str += "# 可以根据需要扩展这个映射表\n"
    map_str += "company_map = {\n"
    
    # 按字母顺序排序
    sorted_companies = sorted(new_company_map.items(), key=lambda x: x[0])
    
    for company_name, domains in sorted_companies:
        map_str += f"    \"{company_name}\": {domains},\n"
    
    map_str += "}"
    
    # 替换现有company_map
    import re
    new_content = re.sub(r'# 厂商域名到中文名称的映射表.*?company_map = \{.*?\}', map_str, content, flags=re.DOTALL)
    
    # 写入更新后的内容
    with open('/home/pi/helloworld/calculate_vendor_contributions.py', 'w') as f:
        f.write(new_content)
    
    print(f"已更新company_map，包含 {len(new_company_map)} 家公司")

# 主函数
def main():
    print("正在更新all_companies.txt...")
    update_all_companies()
    
    print("\n正在更新company_map...")
    update_company_map()
    
    print("\n更新完成！")

if __name__ == "__main__":
    main()