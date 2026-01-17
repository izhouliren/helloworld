#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd

# 使用项目中现有的数据文件
file_path = 'all_kernel_contribute_data_20250112.csv'
data = pd.read_csv(file_path)

# 数据处理：删除汇总行，只保留具体版本数据
data = data[data['kernelversion'] != 'From Apr. 16 2005']

# 筛选出中国相关的贡献者
chinese_companies = ['Alibaba', 'Huawei', 'Xiaomi', 'ByteDance', 'Tencent', 'Baidu', 'Kylin Software', 'Loongson', 'UnionTech', 'Red Flag', 'Inspur', 'Lenovo', 'ZTE', 'China Mobile', 'Sugon', 'Dawning']
df_chinese = data[data['contributor'].isin(chinese_companies)]

# 按内核版本分组，计算每个版本的中国贡献者总数量
df_chinese_by_version = df_chinese.groupby('kernelversion')['value'].sum().reset_index()

# 按内核版本排序（假设版本格式为X.X，转换为浮点数排序）
df_chinese_by_version['version_float'] = df_chinese_by_version['kernelversion'].str.extract(r'(\d+\.\d+)').astype(float)
df_chinese_by_version = df_chinese_by_version.sort_values('version_float')

# 创建图表 - 增大尺寸确保所有数据完整显示
plt.figure(figsize=(16, 30), facecolor='white')
ax = plt.gca()
ax.set_facecolor('white')

# 创建水平条形图 - 调整高度确保所有数据可见
positions = list(range(len(df_chinese_by_version)))
plt.barh(positions, df_chinese_by_version['value'], color='#e74c3c', height=0.8, edgecolor='black', linewidth=0.3)

# 设置标签 - 显示所有版本，优化样式避免重叠
labels = df_chinese_by_version['kernelversion'].tolist()
# 简化标签，只显示版本号和年份
formatted_labels = [f"{label.split('(')[0]} ({label.split('(')[1][:4]})" for label in labels]
plt.yticks(positions, formatted_labels, fontsize=8, rotation=0, ha='right')

# 优化x轴显示
plt.xticks(fontsize=12)
ax.tick_params(axis='x', which='major', pad=10)

# 计算总贡献数量
total_contrib = df_chinese_by_version['value'].sum()

# 添加标题和标签 - 优化位置和字体
plt.title('Chinese Developers Contribution by Kernel Version', fontsize=22, fontweight='bold', pad=20)
# 在标题下方添加总贡献数量
plt.text(0.5, 0.95, f'Total Contribution: {total_contrib:,}', 
         transform=ax.transAxes, fontsize=18, ha='center', color='#2c3e50')
plt.xlabel('Contribution Value', fontsize=16, labelpad=15)
plt.ylabel('Kernel Version', fontsize=16, labelpad=20)

# 美化坐标轴
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)

# 添加网格线 - 优化样式
ax.grid(axis='x', alpha=0.3, linestyle='--', linewidth=0.5, color='#95a5a6')
ax.set_axisbelow(True)  # 将网格线置于条形图下方

# 为每个条形添加数值标签，只显示较大值
for i, value in enumerate(df_chinese_by_version['value']):
    if value > 100:  # 只显示大于100的值标签，避免拥挤
        plt.text(value + 10, i, f'{value}', fontsize=7, va='center', fontweight='bold', color='#2c3e50')

# 反转Y轴，使最早版本在底部
plt.gca().invert_yaxis()

# 调整布局 - 确保所有内容都能显示
plt.subplots_adjust(left=0.15, right=0.95, top=0.95, bottom=0.02)

# 为图表添加统计信息
max_contrib = df_chinese_by_version['value'].max()
max_version = df_chinese_by_version.loc[df_chinese_by_version['value'].idxmax(), 'kernelversion']
plt.text(0.98, 0.005, f'Max Contribution: {max_contrib} (in {max_version.split("(")[0]})', 
         transform=ax.transAxes, fontsize=12, fontweight='bold', 
         ha='right', va='bottom', bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray', boxstyle='round'))

# 添加数据来源说明
plt.text(0.02, 0.005, 'Data Source: all_kernel_contribute_data_20250112.csv', 
         transform=ax.transAxes, fontsize=10, ha='left', va='bottom', color='#7f8c8d')

# 保存图表
img_path = 'chinese_developers_contribution.png'
plt.savefig(img_path, dpi=300, bbox_inches='tight')
print(f"Figure saved as {img_path}")

# 显示图表
plt.show()

print("\n数据摘要：")
print(df_chinese_by_version[['kernelversion', 'value']])
