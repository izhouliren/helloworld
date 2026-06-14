import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# 读取CSV文件
df = pd.read_csv('all_kernel_contribute_data_20250112.csv')

# 删除"From Apr. 16 2005"的数据点
df = df[df['kernelversion'] != 'From Apr. 16 2005']

# 筛选出指定厂商的数据
target_companies = ['Alibaba', 'Huawei', 'Xiaomi']
df_target = df[df['contributor'].isin(target_companies)]

# 按kernelversion和contributor分组，确保每个版本每个厂商有唯一值
df_pivot = df_target.pivot(index='kernelversion', columns='contributor', values='value')

# 将缺失值替换为0
df_pivot = df_pivot.fillna(0)

# 创建折线图，使用更宽的尺寸来容纳所有x轴标签
plt.figure(figsize=(20, 8))

# 为每个厂商绘制折线并添加数据标签
for company in target_companies:
    if company in df_pivot.columns:
        plt.plot(df_pivot.index, df_pivot[company], marker='o', linewidth=2, markersize=5, label=company)
        # 显示所有数据点的标签
        for i, value in enumerate(df_pivot[company]):
            plt.text(i, value, f'{int(value)}', ha='center', va='bottom', fontsize=7, fontweight='bold')

# 设置图表标题和标签
plt.title('Kernel Contribution by Companies', fontsize=16, fontweight='bold')
plt.xlabel('Kernel Version', fontsize=13)
plt.ylabel('Contribution Value', fontsize=13)

# 优化Y轴显示，使用千分位分隔符
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{int(x):,}'))

# 调整Y轴的缩放范围，根据实际数据调整
plt.ylim(bottom=0, top=df_pivot.max().max() * 1.1)  # 预留10%的顶部空间

# 显示所有x轴标签，但优化显示
plt.xticks(rotation=60, ha='right', fontsize=9)

# 添加图例
plt.legend(fontsize=11, loc='upper left')

# 添加网格线
plt.grid(True, alpha=0.4, linestyle='--')

# 调整布局，增加底部边距以容纳旋转后的x轴标签
plt.tight_layout(pad=2.0)

# 设置字体大小
plt.tick_params(axis='both', labelsize=9)

# 保存图表
plt.savefig('kernel_contribution.png', dpi=300)

# 显示图表
plt.show()

print("图表已生成：kernel_contribution.png")
print("数据摘要：")
print(df_pivot)