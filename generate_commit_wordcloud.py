import os
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from datetime import datetime

# ================= 配置区域 =================
# CSV文件所在目录
CSV_DIR = "/home/pi/helloworld/2025_company_commits"

# 词云配置
FONT_PATH = "/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf"  # 中文字体路径
IMAGE_WIDTH = 1920
IMAGE_HEIGHT = 1080
BACKGROUND_COLOR = "white"
MAX_WORDS = 200

# 输出文件名
OUTPUT_FILENAME = f"linux_commit_wordcloud_{datetime.now().strftime('%Y-%m-%d')}.png"
# ===========================================

def generate_wordcloud():
    """
    生成提交主题的词云
    """
    # 读取所有CSV文件
    all_subjects = []
    
    # 获取目录下所有CSV文件
    csv_files = [f for f in os.listdir(CSV_DIR) if f.endswith('.csv')]
    
    if not csv_files:
        print(f"错误: 在目录 {CSV_DIR} 中未找到CSV文件。")
        return
    
    print(f"找到 {len(csv_files)} 个CSV文件，正在读取提交主题...")
    
    # 遍历所有CSV文件
    for csv_file in csv_files:
        file_path = os.path.join(CSV_DIR, csv_file)
        try:
            # 读取CSV文件
            df = pd.read_csv(file_path, encoding='utf-8-sig')
            
            # 提取Subject列
            if 'Subject' in df.columns:
                subjects = df['Subject'].dropna().tolist()
                all_subjects.extend(subjects)
                print(f"  {csv_file}: 读取了 {len(subjects)} 条提交主题")
            else:
                print(f"  {csv_file}: 未找到Subject列")
        except Exception as e:
            print(f"  {csv_file}: 读取失败 - {e}")
    
    if not all_subjects:
        print("错误: 未提取到任何提交主题。")
        return
    
    print(f"\n共提取到 {len(all_subjects)} 条提交主题，正在生成词云...")
    
    # 合并所有主题为一个文本
    text = ' '.join(all_subjects)
    
    # 创建词云对象
    wordcloud = WordCloud(
        font_path=FONT_PATH,
        width=IMAGE_WIDTH,
        height=IMAGE_HEIGHT,
        background_color=BACKGROUND_COLOR,
        max_words=MAX_WORDS,
        collocations=False,  # 不显示词组
        random_state=42
    )
    
    # 生成词云
    wordcloud.generate(text)
    
    # 保存词云图片
    wordcloud.to_file(OUTPUT_FILENAME)
    print(f"词云已保存至: {os.path.abspath(OUTPUT_FILENAME)}")
    
    # 显示词云
    plt.figure(figsize=(IMAGE_WIDTH/100, IMAGE_HEIGHT/100), dpi=100)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    generate_wordcloud()
