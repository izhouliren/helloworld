#!/usr/bin/env python3
"""
KPS Data Scraper - 从 remword.com 抓取 Linux Kernel 各版本企业贡献数据
生成 CSV: kernelversion,contributor,value,Percentage

逻辑源自 helloworld.ipynb，全面加固:
- 网络请求重试机制
- HTML 解析容错
- 正则匹配多种格式
- 进度显示
- 异常恢复
"""

import requests
import csv
import re
import time
import sys
import os
from datetime import datetime

# ====================== 配置 ======================
BASE_URL = 'https://remword.com/kps_result/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
TIMEOUT = 30
MAX_RETRIES = 3
RETRY_DELAY = 2
OUTPUT_FILE = 'all_kernel_contribute_data.csv'


# ====================== 工具函数 ======================

def fetch(url, retries=MAX_RETRIES):
    """带重试的 HTTP GET 请求"""
    for attempt in range(1, retries + 1):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
            resp.raise_for_status()
            resp.encoding = 'utf-8'
            return resp.text
        except requests.RequestException as e:
            msg = f"  WARN 请求失败 [{attempt}/{retries}]: {url} - {e}"
            print(msg, file=sys.stderr)
            if attempt < retries:
                time.sleep(RETRY_DELAY)
    return None


def parse_company_line(text):
    """
    解析 KPS 详情页中的公司行
    格式: No.1 Red Hat 284(16.46%)
    返回 (company_name, commit_count, percentage) 或 None
    """
    if not text or not text.strip():
        return None

    text = text.strip()
    # 精确匹配
    m = re.match(
        r'^No\.\d+\s+'
        r'(.+?)\s+'
        r'(\d+)\s*'
        r'\((\d+\.?\d*)%\)$',
        text
    )
    if m:
        return (m.group(1).strip(), int(m.group(2)), float(m.group(3)))

    # 宽松匹配(公司名可能含特殊字符)
    m2 = re.match(
        r'^No\.\d+\s+(.+?)\s+(\d+)\((\d+\.?\d*)%\)$',
        text
    )
    if m2:
        return (m2.group(1).strip(), int(m2.group(2)), float(m2.group(3)))

    return None


def extract_kernel_versions(html):
    """从主页面提取所有内核版本信息, 返回 [(version_name, detail_url), ...]"""
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    tables = soup.find_all('table')
    if len(tables) < 3:
        print("ERROR: 页面结构变更, 找不到第3个表格", file=sys.stderr)
        return []

    tr_tags = tables[2].find_all('tr')
    versions = []

    for tr in tr_tags:
        tds = tr.find_all('td')
        if len(tds) < 2:
            continue

        plist = tds[0].find_all('p')
        if not plist:
            continue
        ver_name = plist[0].get_text(strip=True)
        if not ver_name:
            continue

        alink = tds[1].find('a')
        if alink is None or not alink.get('href'):
            continue

        href = alink['href']
        # 构造绝对 URL
        if href.startswith('/'):
            detail_url = 'https://remword.com' + href
        elif href.startswith('.'):
            detail_url = BASE_URL.rstrip('/') + '/' + href.lstrip('./')
        elif href.startswith('http'):
            detail_url = href
        else:
            detail_url = BASE_URL.rstrip('/') + '/' + href

        versions.append((ver_name, detail_url))

    return versions


def extract_company_data(html):
    """从版本详情页提取公司贡献数据, 返回 [(name, count, pct), ...]"""
    from bs4 import BeautifulSoup, NavigableString, Tag
    soup = BeautifulSoup(html, 'html.parser')

    results = []
    for ul in soup.find_all('ul'):
        prev = ul.previous_sibling

        text = None
        if isinstance(prev, NavigableString):
            text = str(prev).strip()
        elif isinstance(prev, Tag):
            text = prev.get_text(strip=True)

        parsed = parse_company_line(text) if text else None
        if parsed is None:
            continue

        name, count, pct = parsed
        results.append((name, count, pct))

    return results


# ====================== 主流程 ======================

def main():
    print("=" * 60)
    print("KPS Data Scraper - Linux Kernel 企业贡献数据抓取")
    print(f"目标网站: {BASE_URL}")
    print(f"输出文件: {OUTPUT_FILE}")
    print(f"开始时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    # ---- Step 1: 获取主页面 ----
    print("\n[1/4] 正在获取版本列表...")
    main_html = fetch(BASE_URL)
    if not main_html:
        print("FATAL: 无法获取主页面, 退出。", file=sys.stderr)
        sys.exit(1)

    versions = extract_kernel_versions(main_html)
    if not versions:
        print("FATAL: 未能提取任何版本信息, 退出。", file=sys.stderr)
        sys.exit(1)

    print(f"  OK 共发现 {len(versions)} 个内核版本")

    # ---- Step 2: 初始化 CSV ----
    fieldnames = ['kernelversion', 'contributor', 'value', 'Percentage']
    with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

    total_rows = 0
    fails = 0

    # ---- Step 3: 逐个版本抓取 ----
    print("\n[2/4] 开始抓取各版本数据...")
    for idx, (ver_name, detail_url) in enumerate(versions, 1):
        sys.stdout.write(f"\r  [{idx}/{len(versions)}] {ver_name:<30}")
        sys.stdout.flush()

        html = fetch(detail_url)
        if not html:
            fails += 1
            continue

        companies = extract_company_data(html)
        if not companies:
            fails += 1
            continue

        with open(OUTPUT_FILE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            for name, count, pct in companies:
                writer.writerow({
                    'kernelversion': ver_name,
                    'contributor': name,
                    'value': count,
                    'Percentage': pct
                })
                total_rows += 1

        # 礼貌性延时
        time.sleep(0.3)

    print()

    # ---- Step 4: 完成 ----
    print("\n[3/4] 验证输出文件...")
    if os.path.exists(OUTPUT_FILE):
        file_size = os.path.getsize(OUTPUT_FILE)
        print(f"  OK 文件大小: {file_size:,} bytes")

    print("\n[4/4] 汇总")
    print("=" * 60)
    print(f"  总版本数: {len(versions)}")
    print(f"  写入行数: {total_rows}")
    print(f"  失败跳过: {fails}")
    print(f"  输出文件: {os.path.abspath(OUTPUT_FILE)}")
    print(f"  完成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)


if __name__ == '__main__':
    main()
