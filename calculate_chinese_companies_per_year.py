import csv
import re
import os
from collections import defaultdict

# 中国公司关键词列表
chinese_keywords = [
    'Huawei', 'Alibaba', 'Tencent', 'ByteDance', 'Baidu', 'Lenovo',
    'ZTE', 'China Mobile', 'China Telecom', 'Loongson', 'Kylin Software',
    'Rockchip', 'OPPO', 'vivo', 'Xiaomi', 'Inspur', 'UnionTech',
    'NFSChina', 'Actions Microelectronics', 'New H3C', 'NetEase',
    'Meituan', 'JD.com', 'Didi', 'PDD', 'NIO', 'XPeng', 'Li Auto',
    'Horizon Robotics', 'SenseTime'
]

def extract_year(kernel_version):
    """从内核版本字符串中提取年份"""
    # 匹配括号中的日期，如 "Linux-6.13(2025-01-19)" -> 2025
    match = re.search(r'\((\d{4})-\d{2}-\d{2}\)', kernel_version)
    if match:
        return int(match.group(1))
    # 对于 "From Apr. 16 2005" 这样的格式
    match = re.search(r'From .* (\d{4})', kernel_version)
    if match:
        return int(match.group(1))
    return None

def is_chinese_company(contributor):
    """判断是否为中国公司"""
    for keyword in chinese_keywords:
        if keyword.lower() in contributor.lower():
            return True
    return False

def main():
    # 读取CSV文件
    csv_path = '/home/pi/helloworld/all_kernel_contribute_data_20260117.csv'
    
    # 存储每年的中国公司集合
    yearly_companies = defaultdict(set)
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            kernel_version = row['kernelversion']
            contributor = row['contributor']
            
            # 提取年份
            year = extract_year(kernel_version)
            if year and 2015 <= year <= 2025:
                # 判断是否为中国公司
                if is_chinese_company(contributor):
                    yearly_companies[year].add(contributor)
    
    # 计算每年的中国公司数量
    yearly_counts = {}
    for year in range(2015, 2026):
        yearly_counts[year] = len(yearly_companies.get(year, set()))
    
    # 打印结果
    print('2015-2025年中国公司贡献Linux内核的企业个数：')
    print('-' * 40)
    for year in range(2015, 2026):
        count = yearly_counts[year]
        print(f'{year}年: {count}家')
    print('-' * 40)
    
    # 生成简单的文本格式柱状图
    print('\n简单柱状图：')
    print('-' * 60)
    for year in range(2015, 2026):
        count = yearly_counts[year]
        bars = '█' * min(count, 50)  # 限制最大长度为50
        print(f'{year}年: {bars} ({count}家)')
    print('-' * 60)
    
    # 保存结果到文件
    output_dir = '/home/pi/helloworld'
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'chinese_companies_per_year.txt')
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('2015-2025年中国公司贡献Linux内核的企业个数\n')
        f.write('-' * 40 + '\n')
        for year in range(2015, 2026):
            count = yearly_counts[year]
            f.write(f'{year}年: {count}家\n')
        f.write('-' * 40 + '\n')
        f.write('\n简单柱状图：\n')
        f.write('-' * 60 + '\n')
        for year in range(2015, 2026):
            count = yearly_counts[year]
            bars = '█' * min(count, 50)
            f.write(f'{year}年: {bars} ({count}家)\n')
        f.write('-' * 60 + '\n')
    
    print(f'\n结果已保存到: {output_path}')
    
    return yearly_counts

if __name__ == '__main__':
    main()
