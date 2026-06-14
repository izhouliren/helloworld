import os
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.font_manager as fm

# ================= 配置区域 =================
# CSV文件所在目录
CSV_DIR = "/home/pi/helloworld/2025_company_commits"

# 词云输出目录
OUTPUT_DIR = "/home/pi/helloworld/2025_company_wordclouds"

# 词云配置
IMAGE_WIDTH = 1920
IMAGE_HEIGHT = 1080
BACKGROUND_COLOR = "white"
MAX_WORDS = 150

# 尝试使用多种字体，确保中英文都能显示
FONT_PATHS = [
    "/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf",  # 中文字体
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",  # 英文字体
    "/usr/share/fonts/truetype/freefont/FreeSans.ttf",  # 备用英文字体
]

# 获取matplotlib可用字体列表，用于调试
print("正在检测matplotlib可用字体...")
available_fonts = [f.name for f in fm.fontManager.ttflist]
print(f"找到 {len(available_fonts)} 种可用字体")
# ===========================================

def setup_font():
    """
    设置字体，确保中英文都能显示
    """
    # 设置matplotlib的全局字体
    plt.rcParams['font.family'] = ['DejaVu Sans', 'Droid Sans Fallback']
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
    
    # 测试可用的字体文件
    for font_path in FONT_PATHS:
        if os.path.exists(font_path):
            print(f"使用字体: {font_path}")
            return font_path
    
    # 如果没有找到指定字体，使用默认字体
    print("警告: 未找到指定字体，使用默认字体")
    return None

def generate_individual_wordclouds():
    """
    为每个CSV文件生成单独的词云
    """
    # 创建输出目录
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"已创建输出目录: {OUTPUT_DIR}")
    
    # 设置字体
    font_path = setup_font()
    
    # 获取目录下所有CSV文件
    csv_files = [f for f in os.listdir(CSV_DIR) if f.endswith('.csv')]
    
    if not csv_files:
        print(f"错误: 在目录 {CSV_DIR} 中未找到CSV文件。")
        return
    
    print(f"找到 {len(csv_files)} 个CSV文件，正在为每个文件生成词云...")
    
    # 遍历所有CSV文件
    for csv_file in csv_files:
        file_path = os.path.join(CSV_DIR, csv_file)
        company_name = os.path.splitext(csv_file)[0].replace('_linux_commits_2026-01-21', '')
        
        try:
            # 读取CSV文件
            df = pd.read_csv(file_path, encoding='utf-8-sig')
            
            # 提取Subject列
            if 'Subject' in df.columns:
                subjects = df['Subject'].dropna().tolist()
                print(f"  {company_name}: 读取了 {len(subjects)} 条提交主题")
                
                if not subjects:
                    print(f"  {company_name}: 没有有效的提交主题，跳过")
                    continue
                
                # 合并所有主题为一个文本
                text = ' '.join(subjects)
                
                # 创建词云对象
                wordcloud = WordCloud(
                    font_path=font_path,  # 使用检测到的字体路径
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
                output_filename = f"{company_name}_wordcloud.png"
                output_path = os.path.join(OUTPUT_DIR, output_filename)
                wordcloud.to_file(output_path)
                print(f"  {company_name}: 词云已保存至 {os.path.abspath(output_path)}")
            else:
                print(f"  {company_name}: 未找到Subject列")
        except Exception as e:
            print(f"  {company_name}: 处理失败 - {e}")
    
    print(f"\n所有词云已生成，保存至目录: {os.path.abspath(OUTPUT_DIR)}")

if __name__ == "__main__":
    generate_individual_wordclouds()
