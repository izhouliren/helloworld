import pandas as pd
import matplotlib
matplotlib.use('Agg')  # 使用非交互式后端，确保在无显示器环境中能生成图表
import matplotlib.pyplot as plt
import numpy as np

# 读取包含完整2025年数据的CSV文件
df = pd.read_csv('/home/pi/helloworld/all_kernel_contribute_data_20260117.csv')

# 定义中国公司列表
chinese_companies = [
    'Huawei', 'Alibaba', 'Rockchip', 'Kylin Software', 'Loongson',
    'vivo', 'ZTE', 'ByteDance', 'China Mobile', 'Inspur', 'OPPO',
    'Xiaomi', 'Lenovo', 'China Telecom', 'NFSChina', 'UnionTech',
    'Lemote', 'Coolpad', 'Beijing Rising Technology Co.', 'Hanwang Tech',
    'DaTang Mobile', 'SmartX', 'QuanTa', 'Baidu'
]

# 筛选出中国公司的数据
chinese_df = df[df['contributor'].isin(chinese_companies)]

# 筛选出2025年的数据（包括Linux-6.18(2025-11-30)和Linux-6.19(on-going)）
# 首先，我们查看所有的kernelversion值，了解数据结构
all_versions = df['kernelversion'].unique()
print("所有内核版本：", all_versions)

# 筛选2025年发布的版本和正在进行的版本
# 在这个文件中，2025年的数据包括多个版本
year_2025_df = chinese_df[
    chinese_df['kernelversion'].str.contains('2025') | 
    chinese_df['kernelversion'].str.startswith('Linux-6.13') |
    chinese_df['kernelversion'].str.startswith('Linux-6.14') |
    chinese_df['kernelversion'].str.startswith('Linux-6.15') |
    chinese_df['kernelversion'].str.startswith('Linux-6.16') |
    chinese_df['kernelversion'].str.startswith('Linux-6.17') |
    chinese_df['kernelversion'].str.startswith('Linux-6.18') |
    chinese_df['kernelversion'].str.startswith('Linux-6.19')
]

print("\n2025年中国公司贡献数据：")
print(year_2025_df)

# 按公司名称分组，计算2025年总贡献值
total_contributions = year_2025_df.groupby('contributor')['value'].sum().reset_index()

# 按贡献值排序
total_contributions = total_contributions.sort_values(by='value', ascending=False)

# 打印详细的总贡献值，以便与用户数据对比
print("\n2025年中国公司总贡献值（从6.13到6.19）：")
print(total_contributions)

# 设置中文字体，确保中文显示正常
# 移除SimHei和Arial Unicode MS，只使用系统可用的字体，并添加更多备选字体
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'WenQuanYi Micro Hei', 'Heiti TC', 'Arial', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# 简化图表标题和标签，减少中文使用，确保图表可读性


# 创建柱状图
plt.figure(figsize=(12, 8))
bars = plt.bar(total_contributions['contributor'], total_contributions['value'], color='#3498db')

# 添加标题和标签
plt.title('2025 Linux Kernel Contribution Rankings - Chinese Companies', fontsize=16)
plt.xlabel('Company Name', fontsize=14)
plt.ylabel('Contribution Value', fontsize=14)

# 旋转x轴标签，避免重叠
plt.xticks(rotation=45, ha='right', fontsize=12)

# 添加数值标签
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 50, f'{int(height)}',
             ha='center', va='bottom', fontsize=10)

# 调整布局
plt.tight_layout()

# 保存图表
plt.savefig('/home/pi/helloworld/linux_kernel_chinese_contributions.png', dpi=300)

# 显示图表
plt.show()
