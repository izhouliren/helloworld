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
OUTPUT_DIR = "/home/pi/helloworld/2025_company_wordclouds_noto"

# 词云配置
IMAGE_WIDTH = 1920
IMAGE_HEIGHT = 1080
BACKGROUND_COLOR = "white"
MAX_WORDS = 150

# 使用新安装的Noto CJK字体（包含简体中文）
FONT_PATH = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"  # 包含Noto Sans CJK SC（简体中文）
# ===========================================

def setup_font():
    """
    设置字体，确保中英文都能显示
    """
    print(f"正在检查字体: {FONT_PATH}")
    if os.path.exists(FONT_PATH):
        print(f"✓ 字体文件存在")
    else:
        print(f"✗ 字体文件不存在")
        return False
    
    # 设置matplotlib的全局字体
    plt.rcParams['font.family'] = ['Noto Sans CJK SC', 'Noto Sans']
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
    
    return True

def generate_wordclouds():
    """
    为每个CSV文件生成单独的词云，使用Noto CJK字体
    """
    # 设置字体
    if not setup_font():
        print("字体设置失败，退出程序")
        return
    
    # 创建输出目录
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"已创建输出目录: {OUTPUT_DIR}")
    
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
                
                # 打印前100个字符，用于调试
                print(f"  {company_name}: 文本示例: {text[:100]}...")
                
                # 创建词云对象，明确指定使用简体中文
                wordcloud = WordCloud(
                    font_path=FONT_PATH,  # 使用Noto CJK字体
                    width=IMAGE_WIDTH,
                    height=IMAGE_HEIGHT,
                    background_color=BACKGROUND_COLOR,
                    max_words=MAX_WORDS,
                    collocations=False,  # 不显示词组
                    random_state=42,
                    font_step=1,  # 提高字体匹配精度
                    min_font_size=10,  # 最小字体大小
                    max_font_size=200  # 最大字体大小
                )
                
                # 生成词云
                print(f"  {company_name}: 正在生成词云...")
                wordcloud.generate(text)
                
                # 保存词云图片
                output_filename = f"{company_name}_wordcloud.png"
                output_path = os.path.join(OUTPUT_DIR, output_filename)
                wordcloud.to_file(output_path)
                print(f"  {company_name}: ✓ 词云已保存至 {os.path.abspath(output_path)}")
            else:
                print(f"  {company_name}: ✗ 未找到Subject列")
        except Exception as e:
            print(f"  {company_name}: ✗ 处理失败 - {e}")
    
    print(f"\n所有词云已生成，保存至目录: {os.path.abspath(OUTPUT_DIR)}")

if __name__ == "__main__":
    generate_wordclouds()
