#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# 读取数据文件
data_file = 'all_kernel_contribute_data_20250112.csv'
df = pd.read_csv(data_file)

# 删除汇总行，只保留具体版本数据
df = df[df['kernelversion'] != 'From Apr. 16 2005']

# 选择主要的中国公司（去掉华为，加上小米和更多中国公司）
chinese_companies = ['Alibaba', 'ByteDance', 'Tencent', 'Baidu', 'Xiaomi', 'Kylin Software', 'Loongson', 'UnionTech', 'ZTE', 'China Mobile', 'Lenovo', 'Inspur', 'Dawning', 'Red Flag']

# 筛选中国公司的数据
df_chinese = df[df['contributor'].isin(chinese_companies)]

# 获取所有唯一的内核版本，并按版本号排序
all_versions = df['kernelversion'].unique().tolist()
# 转换为DataFrame以便排序
df_versions = pd.DataFrame({'kernelversion': all_versions})
# 提取主版本号和次版本号，确保正确排序（如6.10 > 6.9，处理3.0这种情况）
df_versions[['major', 'minor']] = df_versions['kernelversion'].str.extract(r'(\d+)\.(\d+)?').fillna(0).astype(int)
df_versions = df_versions.sort_values(['major', 'minor'])
sorted_versions = df_versions['kernelversion'].tolist()

# 创建一个完整的版本-公司矩阵
data_matrix = []
for version in sorted_versions:
    row = {'kernelversion': version}
    for company in chinese_companies:
        # 查找该版本该公司的贡献值，没有则为0
        contrib = df_chinese[(df_chinese['kernelversion'] == version) & (df_chinese['contributor'] == company)]['value'].sum()
        row[company] = contrib
    data_matrix.append(row)

# 转换为DataFrame
df_pivot = pd.DataFrame(data_matrix)

# 打印处理的版本数量
print(f"\n共处理了 {len(df_pivot)} 个内核版本")

# 设置内核版本为索引
df_pivot.set_index('kernelversion', inplace=True)

# 创建折线图
plt.figure(figsize=(20, 12), facecolor='white')
ax = plt.gca()
ax.set_facecolor('white')

# 定义颜色映射，为14个公司分配不同的颜色
colors = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6', '#1abc9c', '#e67e22', '#34495e', '#95a5a6', '#d35400', '#3498db', '#27ae60', '#c0392b', '#f1c40f']

# 为每个公司绘制折线，并添加数据标签
for i, company in enumerate(chinese_companies):
    # 绘制折线
    line = plt.plot(df_pivot.index, df_pivot[company], 
             marker='o', 
             markersize=5, 
             linewidth=2, 
             color=colors[i], 
             label=company, 
             alpha=0.8)[0]
    
    # 添加数据标签，但只显示较大值和关键版本
    for j, value in enumerate(df_pivot[company]):
        # 只显示大于200的值，或者每10个版本显示一个值
        if value > 200 or j % 10 == 0:
            plt.text(j, value + 5, f'{int(value)}', 
                     fontsize=7, 
                     fontweight='bold', 
                     color=colors[i], 
                     ha='center', 
                     va='bottom',
                     rotation=45)
    
    # 添加公司名称到最后一个数据点
    last_idx = len(df_pivot) - 1
    plt.text(last_idx, df_pivot[company].iloc[-1] + 5, company, 
             fontsize=8, 
             fontweight='bold', 
             color=colors[i], 
             ha='left', 
             va='center')

# 设置标题和标签
plt.title('Chinese Companies Contribution Across Linux Kernel Versions', fontsize=20, fontweight='bold', pad=20)
plt.xlabel('Kernel Version', fontsize=16, labelpad=15)
plt.ylabel('Contribution Value', fontsize=16, labelpad=15)

# 显示所有内核版本标签
xticks_indices = list(range(len(sorted_versions)))
xticks_labels = [label.split('(')[0] for label in sorted_versions]
plt.xticks(xticks_indices, xticks_labels, fontsize=7, rotation=90, ha='center')
# 调整x轴标签间距
plt.gca().tick_params(axis='x', pad=5)

# 优化y轴显示，使用千分位分隔符
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{int(x):,}'))
plt.yticks(fontsize=12)

# 添加图例，放在右上角
plt.legend(fontsize=12, loc='upper right', bbox_to_anchor=(1.05, 1), borderaxespad=0.)

# 添加网格线
ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
ax.set_axisbelow(True)

# 美化坐标轴
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)

# 调整布局，确保所有内容都能显示
plt.tight_layout(pad=3.0, rect=[0, 0, 0.9, 1])

# 保存图表
img_path = 'chinese_companies_contribution.png'
plt.savefig(img_path, dpi=300, bbox_inches='tight')
print(f"图表已保存为: {img_path}")

# 显示图表
plt.show()

# 打印数据摘要
print("\n数据摘要（前10个版本）：")
print(df_pivot.head(10))
print("\n公司列表：")
print(chinese_companies)
