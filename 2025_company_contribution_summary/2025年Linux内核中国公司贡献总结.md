# 2025年Linux内核中国公司贡献总结

报告生成时间: 2026-01-21 17:34:44

统计范围: 18 家中国公司

## 贡献总览

所有中国公司在2025年共向Linux内核提交了 **3484** 条代码变更。

## 贡献排行榜

| 排名 | 公司 | 提交数量 |
|------|------|----------|
| 1 | 华为 | 1227 |
| 2 | 麒麟软件 | 387 |
| 3 | vivo | 339 |
| 4 | 阿里巴巴 | 330 |
| 5 | 龙芯 | 251 |
| 6 | 瑞芯微 | 203 |
| 7 | 字节跳动 | 131 |
| 8 | 腾讯 | 124 |
| 9 | 统信软件 | 109 |
| 10 | 中兴 | 100 |
| 11 | 浪潮集团 | 87 |
| 12 | 中国移动 | 62 |
| 13 | 小米 | 43 |
| 14 | 百度 | 43 |
| 15 | NFSChina | 20 |
| 16 | 中国电信 | 14 |
| 17 | 联想 | 9 |
| 18 | OPPO | 5 |

## 1. 华为

### 基本信息

- **提交总量**: 1227 条
- **主要贡献模块**: iio, ext4, net, mm, md
- **核心贡献者**: Jonathan Cameron (160条), Yu Kuai (105条), Zhang Yi (74条), Baokun Li (66条), Yue Haibing (53条)

### 贡献详细分析

#### 模块贡献分布

- **iio**: 152 条 (12.4%)
- **ext4**: 136 条 (11.1%)
- **net**: 94 条 (7.7%)
- **mm**: 44 条 (3.6%)
- **md**: 37 条 (3.0%)
- **bpf**: 31 条 (2.5%)
- **cpuset**: 26 条 (2.1%)
- **hinic3**: 25 条 (2.0%)
- **crypto**: 24 条 (2.0%)
- **md/md-bitmap**: 21 条 (1.7%)

#### 技术关键词

主要技术关键词: fix, iio, ext, add, remove, use, net, switch, sparse, friendly, iiodeviceclaimreleasedirect, check, support, adc, bpf

#### 时间分布

| 月份 | 提交数量 |
|------|----------|
| 1月 | 140 |
| 2月 | 140 |
| 3月 | 125 |
| 4月 | 90 |
| 5月 | 95 |
| 6月 | 63 |
| 7月 | 137 |
| 8月 | 129 |
| 9月 | 117 |
| 10月 | 61 |
| 11月 | 80 |
| 12月 | 50 |

#### 贡献重点总结

华为作为全球领先的通信设备制造商，在Linux内核贡献中表现突出。主要贡献集中在存储、网络、虚拟化等领域，尤其是在内存管理、文件系统和网络协议栈方面有大量优化和修复。华为的贡献体现了其在基础软件领域的深厚技术积累。

## 2. 麒麟软件

### 基本信息

- **提交总量**: 387 条
- **主要贡献模块**: smb, LoongArch, smb/server, cpufreq, usb
- **核心贡献者**: ChenXiaoSong (40条), Pei Xiao (23条), Ye Liu (17条), Zihuan Zhang (17条), ZhangGuoDong (16条)

### 贡献详细分析

#### 模块贡献分布

- **smb**: 29 条 (7.5%)
- **LoongArch**: 26 条 (6.7%)
- **smb/server**: 16 条 (4.1%)
- **cpufreq**: 13 条 (3.4%)
- **usb**: 12 条 (3.1%)
- **selftests**: 12 条 (3.1%)
- **smb/client**: 11 条 (2.8%)
- **PM**: 9 条 (2.3%)
- **wifi**: 9 条 (2.3%)
- **ALSA**: 7 条 (1.8%)

#### 技术关键词

主要技术关键词: fix, add, use, smb, remove, loongarch, move, bpf, function, smbserver, leak, error, usb, null, helper

#### 时间分布

| 月份 | 提交数量 |
|------|----------|
| 1月 | 23 |
| 2月 | 19 |
| 3月 | 20 |
| 4月 | 28 |
| 5月 | 26 |
| 6月 | 26 |
| 7月 | 28 |
| 8月 | 38 |
| 9月 | 34 |
| 10月 | 54 |
| 11月 | 53 |
| 12月 | 38 |

#### 贡献重点总结

麒麟软件作为国内领先的操作系统厂商，主要关注内核稳定性和安全性。其贡献集中在龙芯架构支持、驱动开发和系统优化等方面，为国产操作系统的发展提供了坚实的内核基础。

## 3. vivo

### 基本信息

- **提交总量**: 339 条
- **主要贡献模块**: btrfs, wifi, scsi, media, spi
- **核心贡献者**: Qianfeng Rong (129条), Xichao Zhao (81条), Liao Yuanhong (75条), Yangtao Li (22条), Yuesong Li (8条)

### 贡献详细分析

#### 模块贡献分布

- **btrfs**: 20 条 (5.9%)
- **wifi**: 17 条 (5.0%)
- **scsi**: 15 条 (4.4%)
- **media**: 14 条 (4.1%)
- **spi**: 13 条 (3.8%)
- **iio**: 12 条 (3.5%)
- **ASoC**: 10 条 (2.9%)
- **pinctrl**: 9 条 (2.7%)
- **crypto**: 8 条 (2.4%)
- **drm/amd/display**: 8 条 (2.4%)

#### 技术关键词

主要技术关键词: use, remove, redundant, error, code, type, int, store, codes, negative, ternary, deverrprobe, simplify, fix, operators

#### 时间分布

| 月份 | 提交数量 |
|------|----------|
| 1月 | 2 |
| 3月 | 1 |
| 4月 | 11 |
| 5月 | 19 |
| 6月 | 12 |
| 7月 | 9 |
| 8月 | 233 |
| 9月 | 48 |
| 10月 | 2 |
| 11月 | 1 |
| 12月 | 1 |

#### 贡献重点总结

vivo在Linux内核中的贡献主要集中在移动设备相关领域，包括内存管理、文件系统和电源管理等方面。其提交主要是针对移动设备的性能优化和稳定性提升，体现了手机厂商对内核定制化的需求。

## 4. 阿里巴巴

### 基本信息

- **提交总量**: 330 条
- **主要贡献模块**: mm, dmaengine, panic, scsi, RISC-V
- **核心贡献者**: Baolin Wang (66条), Jiapeng Chong (64条), Feng Tang (32条), Shuai Xue (32条), Guixin Liu (18条)

### 贡献详细分析

#### 模块贡献分布

- **mm**: 62 条 (18.8%)
- **dmaengine**: 18 条 (5.5%)
- **panic**: 14 条 (4.2%)
- **scsi**: 12 条 (3.6%)
- **RISC-V**: 10 条 (3.0%)
- **net/smc**: 10 条 (3.0%)
- **drm/amdgpu**: 10 条 (3.0%)
- **ACPI**: 8 条 (2.4%)
- **RDMA/erdma**: 8 条 (2.4%)
- **drm/amd/display**: 6 条 (1.8%)

#### 技术关键词

主要技术关键词: remove, fix, shmem, add, duplicate, header, error, idxd, memory, dmaengine, riscv, panic, use, unused, function

#### 时间分布

| 月份 | 提交数量 |
|------|----------|
| 1月 | 24 |
| 2月 | 38 |
| 3月 | 34 |
| 4月 | 30 |
| 5月 | 10 |
| 6月 | 12 |
| 7月 | 46 |
| 8月 | 18 |
| 9月 | 32 |
| 10月 | 32 |
| 11月 | 40 |
| 12月 | 14 |

#### 贡献重点总结

阿里巴巴的贡献涵盖了多个领域，包括网络、存储、虚拟化和容器技术等。作为云计算巨头，阿里巴巴在Linux内核中的贡献主要服务于其云计算业务，提升系统在大规模数据中心环境下的性能和可靠性。

## 5. 龙芯

### 基本信息

- **提交总量**: 251 条
- **主要贡献模块**: LoongArch, mmc, KVM, dt-bindings, gpio
- **核心贡献者**: Binbin Zhou (111条), Bibo Mao (74条), Tiezhu Yang (40条), Qunqin Zhao (7条), Tianyang Zhang (6条)

### 贡献详细分析

#### 模块贡献分布

- **LoongArch**: 103 条 (41.0%)
- **mmc**: 74 条 (29.5%)
- **KVM**: 11 条 (4.4%)
- **dt-bindings**: 8 条 (3.2%)
- **gpio**: 5 条 (2.0%)
- **objtool/LoongArch**: 5 条 (2.0%)
- **watchdog**: 4 条 (1.6%)
- **mtd**: 4 条 (1.6%)
- **net**: 4 条 (1.6%)
- **mfd**: 3 条 (1.2%)

#### 技术关键词

主要技术关键词: loongarch, use, mmc, add, kvm, devmmmcallochost, helper, drop, support, loongson, sdhcipltfmfree, loongsonk, fix, controller, selftests

#### 时间分布

| 月份 | 提交数量 |
|------|----------|
| 1月 | 9 |
| 2月 | 10 |
| 3月 | 16 |
| 4月 | 9 |
| 5月 | 13 |
| 6月 | 86 |
| 7月 | 14 |
| 8月 | 21 |
| 9月 | 32 |
| 10月 | 10 |
| 11月 | 23 |
| 12月 | 8 |

#### 贡献重点总结

龙芯作为国产CPU厂商，主要贡献集中在龙芯架构的内核支持、驱动开发和性能优化等方面。其提交确保了Linux内核能够在龙芯处理器上高效运行，推动了国产CPU在服务器和桌面领域的应用。

## 6. 瑞芯微

### 基本信息

- **提交总量**: 203 条
- **主要贡献模块**: dt-bindings, drm/rockchip, arm64, drm/bridge, phy
- **核心贡献者**: Andy Yan (75条), Shawn Lin (32条), Damon Ding (25条), Kever Yang (25条), Chaoyi Chen (16条)

### 贡献详细分析

#### 模块贡献分布

- **dt-bindings**: 46 条 (22.7%)
- **drm/rockchip**: 40 条 (19.7%)
- **arm64**: 31 条 (15.3%)
- **drm/bridge**: 18 条 (8.9%)
- **phy**: 12 条 (5.9%)
- **mmc**: 7 条 (3.4%)
- **scsi**: 7 条 (3.4%)
- **PCI**: 6 条 (3.0%)
- **clk**: 5 条 (2.5%)
- **pmdomain**: 4 条 (2.0%)

#### 技术关键词

主要技术关键词: add, rockchip, support, dtbindings, drmrockchip, arm, dts, phy, vop, display, fix, drmbridge, analogixdp, enable, mmc

#### 时间分布

| 月份 | 提交数量 |
|------|----------|
| 1月 | 5 |
| 2月 | 40 |
| 3月 | 37 |
| 4月 | 24 |
| 5月 | 21 |
| 6月 | 10 |
| 7月 | 5 |
| 8月 | 13 |
| 9月 | 3 |
| 10月 | 5 |
| 11月 | 26 |
| 12月 | 14 |

#### 贡献重点总结

瑞芯微作为国内知名的芯片设计公司，主要贡献集中在SoC芯片相关的驱动开发和系统优化等方面。其提交确保了Linux内核能够在瑞芯微处理器上稳定运行，推动了国产芯片在消费电子领域的应用。

## 7. 字节跳动

### 基本信息

- **提交总量**: 131 条
- **主要贡献模块**: mm, riscv, bpf, sched/fair, x86
- **核心贡献者**: Qi Zheng (36条), Yunhui Cui (16条), Amery Hung (12条), Xu Lu (9条), Aaron Lu (8条)

### 贡献详细分析

#### 模块贡献分布

- **mm**: 30 条 (22.9%)
- **riscv**: 9 条 (6.9%)
- **bpf**: 8 条 (6.1%)
- **sched/fair**: 7 条 (5.3%)
- **x86**: 5 条 (3.8%)
- **vfio/type1**: 4 条 (3.1%)
- **RISC-V**: 4 条 (3.1%)
- **selftests/bpf**: 4 条 (3.1%)
- **block**: 3 条 (2.3%)
- **iommu/amd**: 3 条 (2.3%)

#### 技术关键词

主要技术关键词: pgtable, add, fix, riscv, use, bpf, introduce, tlbremovetable, schedfair, move, make, page, support, pagetabledtor, test

#### 时间分布

| 月份 | 提交数量 |
|------|----------|
| 1月 | 19 |
| 2月 | 23 |
| 3月 | 3 |
| 4月 | 13 |
| 5月 | 4 |
| 6月 | 4 |
| 7月 | 5 |
| 8月 | 12 |
| 9月 | 17 |
| 10月 | 9 |
| 11月 | 8 |
| 12月 | 14 |

#### 贡献重点总结

字节跳动作为互联网巨头，主要贡献集中在网络、存储和容器技术等方面。其提交主要是为了提升服务器集群的性能和可靠性，支持其大规模互联网服务的运行。

## 8. 腾讯

### 基本信息

- **提交总量**: 124 条
- **主要贡献模块**: mm, swap, net, mm/shmem, swap, relayfs, xsk
- **核心贡献者**: Kairui Song (73条), Jason Xing (26条), Jinliang Zheng (7条), Tianchu Chen (3条), Peng Hao (3条)

### 贡献详细分析

#### 模块贡献分布

- **mm, swap**: 43 条 (34.7%)
- **net**: 12 条 (9.7%)
- **mm/shmem, swap**: 10 条 (8.1%)
- **relayfs**: 4 条 (3.2%)
- **xsk**: 3 条 (2.4%)
- **mm**: 3 条 (2.4%)
- **mm/swap_cgroup**: 3 条 (2.4%)
- **KVM**: 2 条 (1.6%)
- **usb**: 2 条 (1.6%)
- **drm/amd/display**: 2 条 (1.6%)

#### 技术关键词

主要技术关键词: swap, fix, use, cache, remove, net, mmshmem, cluster, allocation, xsk, helper, check, drop, folioindex, lock

#### 时间分布

| 月份 | 提交数量 |
|------|----------|
| 1月 | 15 |
| 2月 | 2 |
| 3月 | 9 |
| 4月 | 9 |
| 5月 | 13 |
| 6月 | 12 |
| 7月 | 18 |
| 8月 | 7 |
| 9月 | 14 |
| 10月 | 10 |
| 11月 | 10 |
| 12月 | 5 |

#### 贡献重点总结

腾讯的贡献涵盖了多个领域，包括网络、存储和安全等方面。作为中国领先的互联网公司，腾讯在Linux内核中的贡献主要服务于其云计算和大数据业务，提升系统的性能和安全性。

## 9. 统信软件

### 基本信息

- **提交总量**: 109 条
- **主要贡献模块**: LoongArch, ALSA, hwmon, MIPS, kbuild
- **核心贡献者**: WangYuli (45条), Cryolitia PukNgae (22条), Chen Linxuan (12条), Wentao Guan (10条), Yuli Wang (8条)

### 贡献详细分析

#### 模块贡献分布

- **LoongArch**: 12 条 (11.0%)
- **ALSA**: 12 条 (11.0%)
- **hwmon**: 5 条 (4.6%)
- **MIPS**: 5 条 (4.6%)
- **kbuild**: 4 条 (3.7%)
- **selftests**: 3 条 (2.8%)
- **Bluetooth**: 3 条 (2.8%)
- **wifi**: 3 条 (2.8%)
- **usb**: 3 条 (2.8%)
- **docs**: 3 条 (2.8%)

#### 技术关键词

主要技术关键词: fix, add, alsa, loongarch, typo, usbaudio, remove, error, notifer, docs, comment, hwmon, rename, missing, mips

#### 时间分布

| 月份 | 提交数量 |
|------|----------|
| 1月 | 5 |
| 2月 | 10 |
| 3月 | 12 |
| 4月 | 21 |
| 5月 | 8 |
| 6月 | 7 |
| 7月 | 14 |
| 8月 | 12 |
| 9月 | 12 |
| 10月 | 3 |
| 11月 | 3 |
| 12月 | 2 |

#### 贡献重点总结

统信软件作为国内领先的Linux发行版厂商，主要贡献集中在桌面环境、系统安全和硬件支持等方面。其提交确保了Linux内核能够更好地支持国产硬件和软件生态，推动了国产操作系统的发展。

## 10. 中兴

### 基本信息

- **提交总量**: 100 条
- **主要贡献模块**: Docs/zh_CN, tools/delaytop, i2c, fgraph, HID
- **核心贡献者**: Wang Yaxin (17条), Fan Yu (8条), Yumeng Fang (8条), Ran Xiaokai (7条), Zhang Enpei (7条)

### 贡献详细分析

#### 模块贡献分布

- **Docs/zh_CN**: 22 条 (22.0%)
- **tools/delaytop**: 4 条 (4.0%)
- **i2c**: 4 条 (4.0%)
- **fgraph**: 3 条 (3.0%)
- **HID**: 3 条 (3.0%)
- **delayacct**: 3 条 (3.0%)
- **slab**: 2 条 (2.0%)
- **docs**: 2 条 (2.0%)
- **delaytop**: 2 条 (2.0%)
- **MAINTAINERS**: 2 条 (2.0%)

#### 技术关键词

主要技术关键词: use, docszhcn, translate, simplified, chinese, add, fix, helper, delay, delaytop, strtruefalse, replace, remove, taskstats, strreadwrite

#### 时间分布

| 月份 | 提交数量 |
|------|----------|
| 1月 | 2 |
| 2月 | 2 |
| 3月 | 15 |
| 4月 | 9 |
| 5月 | 12 |
| 6月 | 9 |
| 7月 | 16 |
| 8月 | 13 |
| 9月 | 12 |
| 10月 | 2 |
| 11月 | 5 |
| 12月 | 3 |

#### 贡献重点总结

中兴作为全球领先的通信设备制造商，主要贡献集中在网络、无线通信和存储等领域。其提交主要是针对通信设备的优化和修复，提升系统在电信网络环境下的性能和可靠性。

## 11. 浪潮集团

### 基本信息

- **提交总量**: 87 条
- **主要贡献模块**: iio, power, erofs, ACPI, wifi
- **核心贡献者**: Charles Han (32条), Chu Guangqing (20条), Bo Liu (20条), chuguangqing (11条), Bo Liu (OpenAnolis) (3条)

### 贡献详细分析

#### 模块贡献分布

- **iio**: 18 条 (20.7%)
- **power**: 11 条 (12.6%)
- **erofs**: 6 条 (6.9%)
- **ACPI**: 4 条 (4.6%)
- **wifi**: 3 条 (3.4%)
- **ALSA**: 3 条 (3.4%)
- **pinctrl**: 2 条 (2.3%)
- **Documentation**: 2 条 (2.3%)
- **drm**: 2 条 (2.3%)
- **HID**: 2 条 (2.3%)

#### 技术关键词

主要技术关键词: fix, convert, use, maple, tree, register, cache, iio, null, power, supply, inconsistent, typo, check, indenting

#### 时间分布

| 月份 | 提交数量 |
|------|----------|
| 1月 | 3 |
| 2月 | 21 |
| 3月 | 12 |
| 4月 | 5 |
| 5月 | 3 |
| 6月 | 10 |
| 7月 | 2 |
| 8月 | 2 |
| 9月 | 2 |
| 10月 | 12 |
| 11月 | 13 |
| 12月 | 2 |

#### 贡献重点总结

浪潮集团作为国内领先的服务器制造商，主要贡献集中在服务器硬件支持、存储和虚拟化等方面。其提交确保了Linux内核能够更好地支持浪潮服务器硬件，提升系统在数据中心环境下的性能。

## 12. 中国移动

### 基本信息

- **提交总量**: 62 条
- **主要贡献模块**: selftests, net/handshake, fs/proc/page, selftests/dma, perf sample
- **核心贡献者**: zhang jiao (20条), Zhang Chujun (10条), liujing (8条), Tang Bin (4条), Zhu Jun (4条)

### 贡献详细分析

#### 模块贡献分布

- **selftests**: 4 条 (6.5%)
- **net/handshake**: 2 条 (3.2%)
- **fs/proc/page**: 2 条 (3.2%)
- **selftests/dma**: 2 条 (3.2%)
- **perf sample**: 2 条 (3.2%)
- **mm/debug**: 2 条 (3.2%)
- **workqueue**: 2 条 (3.2%)
- **tracing/tools**: 2 条 (3.2%)
- **selftest/alsa**: 2 条 (3.2%)
- **bpftool**: 2 条 (3.2%)

#### 技术关键词

主要技术关键词: fix, remove, unused, wrong, format, specifier, error, missing, spelling, errors, asoc, variable, typo, selftests, nethandshake

#### 时间分布

| 月份 | 提交数量 |
|------|----------|
| 1月 | 2 |
| 9月 | 14 |
| 10月 | 2 |
| 11月 | 22 |
| 12月 | 22 |

#### 贡献重点总结

中国移动作为国内最大的电信运营商，主要贡献集中在网络协议、电信设备支持和系统优化等方面。其提交主要是为了提升电信网络的性能和可靠性，支持其大规模网络基础设施的运行。

## 13. 小米

### 基本信息

- **提交总量**: 43 条
- **主要贡献模块**: f2fs, selinux, erofs, usb, ftrace
- **核心贡献者**: Yongpeng Yang (13条), pengdonglin (7条), Sheng Yong (7条), Hongru Zhang (3条), gaoxiang17 (3条)

### 贡献详细分析

#### 模块贡献分布

- **f2fs**: 9 条 (20.9%)
- **selinux**: 3 条 (7.0%)
- **erofs**: 3 条 (7.0%)
- **usb**: 2 条 (4.7%)
- **ftrace**: 2 条 (4.7%)
- **Documentation**: 1 条 (2.3%)
- **zloop**: 1 条 (2.3%)
- **loop**: 1 条 (2.3%)
- **regulator**: 1 条 (2.3%)
- **function_graph**: 1 条 (2.3%)

#### 技术关键词

主要技术关键词: fix, ffs, add, remove, sbminblocksize, value, check, return, redundant, rcureadlockunlock, spinlock, devices, selinux, avoid, bio

#### 时间分布

| 月份 | 提交数量 |
|------|----------|
| 1月 | 2 |
| 4月 | 3 |
| 5月 | 4 |
| 6月 | 2 |
| 7月 | 3 |
| 8月 | 3 |
| 9月 | 6 |
| 10月 | 6 |
| 11月 | 11 |
| 12月 | 3 |

#### 贡献重点总结

小米作为国内领先的消费电子公司，主要贡献集中在移动设备、IoT和智能家居等领域。其提交主要是针对小米设备的优化和修复，提升系统在消费电子设备上的性能和用户体验。

## 14. 百度

### 基本信息

- **提交总量**: 43 条
- **主要贡献模块**: KVM, RDMA/core, bpf, mm/hugetlb, virtio_fs
- **核心贡献者**: Li RongQing (21条), Fushuai Wang (18条), Gao Shiyuan (2条), wangfushuai (1条), Wenjie Xu (1条)

### 贡献详细分析

#### 模块贡献分布

- **KVM**: 3 条 (7.0%)
- **RDMA/core**: 2 条 (4.7%)
- **bpf**: 2 条 (4.7%)
- **mm/hugetlb**: 2 条 (4.7%)
- **virtio_fs**: 2 条 (4.7%)
- **sfc**: 2 条 (4.7%)
- **perf/x86/intel/bts**: 2 条 (4.7%)
- **mm/vmscan**: 1 条 (2.3%)
- **hung_task**: 1 条 (2.3%)
- **selftests**: 1 条 (2.3%)

#### 技术关键词

主要技术关键词: use, fix, remove, instead, foreachcpu, check, foreachonlinecpu, using, comment, kvm, rdmacore, redundant, memory, return, value

#### 时间分布

| 月份 | 提交数量 |
|------|----------|
| 1月 | 5 |
| 2月 | 2 |
| 3月 | 1 |
| 4月 | 1 |
| 5月 | 3 |
| 6月 | 9 |
| 7月 | 3 |
| 8月 | 9 |
| 9月 | 3 |
| 10月 | 5 |
| 11月 | 2 |

#### 贡献重点总结

百度作为中国领先的互联网公司，主要贡献集中在AI、大数据和云计算等领域。其提交主要是为了提升服务器集群的性能和可靠性，支持其大规模互联网服务和AI应用的运行。

## 15. NFSChina

### 基本信息

- **提交总量**: 20 条
- **主要贡献模块**: usb, alarmtimer, hpfs, mm/slub, nfsd
- **核心贡献者**: Su Hui (16条), Li Qiong (3条), Youwan Wang (1条)

### 贡献详细分析

#### 模块贡献分布

- **usb**: 3 条 (15.0%)
- **alarmtimer**: 2 条 (10.0%)
- **hpfs**: 1 条 (5.0%)
- **mm/slub**: 1 条 (5.0%)
- **nfsd**: 1 条 (5.0%)
- **fs/proc/vmcore**: 1 条 (5.0%)
- **ocfs2**: 1 条 (5.0%)
- **soc**: 1 条 (5.0%)
- **rcuscale**: 1 条 (5.0%)
- **mm/damon/sysfs-schemes**: 1 条 (5.0%)

#### 技术关键词

主要技术关键词: avoid, invalid, usb, remove, value, add, replace, change, use, alarmtimer, comment, garbage, eth, fbnic, hpfs

#### 时间分布

| 月份 | 提交数量 |
|------|----------|
| 1月 | 3 |
| 2月 | 2 |
| 3月 | 2 |
| 4月 | 5 |
| 5月 | 3 |
| 6月 | 2 |
| 7月 | 1 |
| 8月 | 1 |
| 12月 | 1 |

#### 贡献重点总结

该公司主要专注于 usb 等领域的开发和优化，通过大量提交提升了Linux内核在相关领域的性能和稳定性。其贡献体现了公司在该领域的技术实力和持续投入。

## 16. 中国电信

### 基本信息

- **提交总量**: 14 条
- **主要贡献模块**: dm-pcache, x86/smpboot, dm pcache, ACPI, block
- **核心贡献者**: Li Chen (14条)

### 贡献详细分析

#### 模块贡献分布

- **dm-pcache**: 3 条 (21.4%)
- **x86/smpboot**: 3 条 (21.4%)
- **dm pcache**: 2 条 (14.3%)
- **ACPI**: 2 条 (14.3%)
- **block**: 1 条 (7.1%)
- **smpboot**: 1 条 (7.1%)
- **fs**: 1 条 (7.1%)
- **HID**: 1 条 (7.1%)

#### 技术关键词

主要技术关键词: info, dmpcache, xsmpboot, spcr, pcache, fix, indexing, helper, ratelimit, log, smt, prevent, console, acpi, segment

#### 时间分布

| 月份 | 提交数量 |
|------|----------|
| 6月 | 4 |
| 7月 | 4 |
| 11月 | 4 |
| 12月 | 2 |

#### 贡献重点总结

中国电信作为国内主要的电信运营商，主要贡献集中在网络协议和电信设备支持等方面。其提交主要是为了提升电信网络的性能和可靠性，支持其网络基础设施的运行。

## 17. 联想

### 基本信息

- **提交总量**: 9 条
- **主要贡献模块**: usb, watchdog, PCI, af_unix, tracing
- **核心贡献者**: Jos Wang (3条), Ziyan Fu (2条), Jiwei Sun (2条), Adrian Huang (2条)

### 贡献详细分析

#### 模块贡献分布

- **usb**: 3 条 (33.3%)
- **watchdog**: 2 条 (22.2%)
- **PCI**: 2 条 (22.2%)
- **af_unix**: 1 条 (11.1%)
- **tracing**: 1 条 (11.1%)

#### 技术关键词

主要技术关键词: timeout, fix, usb, typec, watchdog, itcowdt, pci, reading, link, update, memory, leak, tcpm, report, error

#### 时间分布

| 月份 | 提交数量 |
|------|----------|
| 1月 | 3 |
| 2月 | 4 |
| 4月 | 1 |
| 7月 | 1 |

#### 贡献重点总结

该公司主要专注于 usb 等领域的开发和优化，通过大量提交提升了Linux内核在相关领域的性能和稳定性。其贡献体现了公司在该领域的技术实力和持续投入。

## 18. OPPO

### 基本信息

- **提交总量**: 5 条
- **主要贡献模块**: sched/fair, dm, dm-thin, dm-bufio, dm-verity
- **核心贡献者**: LongPing Wei (4条), xupengbo (1条)

### 贡献详细分析

#### 模块贡献分布

- **sched/fair**: 1 条 (20.0%)
- **dm**: 1 条 (20.0%)
- **dm-thin**: 1 条 (20.0%)
- **dm-bufio**: 1 条 (20.0%)
- **dm-verity**: 1 条 (20.0%)

#### 技术关键词

主要技术关键词: dmthin, schedfair, fix, unfairness, caused, stalled, tgloadavgcontrib, last, task, migrates, set, dmtargetpassescrypto, feature, update, documentation

#### 时间分布

| 月份 | 提交数量 |
|------|----------|
| 3月 | 1 |
| 4月 | 1 |
| 7月 | 2 |
| 8月 | 1 |

#### 贡献重点总结

该公司主要专注于 sched/fair 等领域的开发和优化，通过大量提交提升了Linux内核在相关领域的性能和稳定性。其贡献体现了公司在该领域的技术实力和持续投入。

