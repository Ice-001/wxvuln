# 微信安全文章归档系统

[![GitHub Actions](https://github.com/gelusus/wxvl/actions/workflows/update_today.yml/badge.svg)](https://github.com/gelusus/wxvl/actions)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

> 🚀 **自动化安全资讯聚合工具** - 抓取、过滤、归档微信公众号安全文章，自动推送钉钉通知

## ✨ 核心功能

### 🔍 智能内容识别
- **多数据源采集**：Doonsec RSS、ChainReactors、BruceFeIix
- **智能关键词匹配**：覆盖漏洞利用、CTF、威胁情报等 10+ 安全领域
- **智能去重机制**：基于 URL 去重，避免重复文章

### 📊 专业报告生成
- **威胁类型分布**：漏洞利用、攻击技术、CTF、威胁情报等
- **漏洞类型分析**：Web安全、系统漏洞、网络攻击等
- **命中关键词追踪**：表格显示命中的关键词和详细分类
- **完整文章列表**：按威胁/漏洞类型分类的详细表格

### 📁 目录结构
```
md/
└── 2026/
    └── 2026-03/
        └── 2026-03-24.md
```

### 🔔 钉钉机器人通知
- **每日报告推送**：每天 14:00 北京时间自动推送
- **超长内容分片**：超过 4000 字符自动分片发送
- **加签模式认证**：安全的钉钉机器人配置

## 📰 数据来源

| 数据源 | 描述 | 更新频率 |
|--------|------|----------|
| **Doonsec** | 安全资讯 RSS，实时推送安全事件和漏洞预警 | 每日 |
| **ChainReactors** | GitHub 安全文章聚合，专注于漏洞复现和技术分析 | 每日 |
| **BruceFeIix** | 安全文章收集，涵盖威胁情报和安全运营 | 每日 |

## 📋 关键词分类

### 威胁类型分类
| 分类 | 关键词示例 |
|------|-----------|
| 漏洞利用 | CVE, CNVD, POC, EXP, 0day, 漏洞, 复现 |
| 攻击技术 | 注入, XSS, RCE, 命令执行, 内网, 域控 |
| 威胁情报 | 威胁情报, APT, 银狐, 勒索病毒 |
| 安全运营 | 安全运营, 漏洞运营, SRC |
| 信息泄露 | 信息泄漏, 数据泄露 |
| 供应链 | 供应链, 第三方组件 |
| 安全合规 | 合规, 等保, ISO27001, GDPR, 安全审计, 风险评估 |
| 数据安全 | 数据安全, 数据治理, 数据加密, DLP, 数据库安全 |
| CTF | WEB, PWN, CRYPTO, REVERSE, MISC, WriteUp, WP |

### 漏洞类型分类
| 分类 | 关键词示例 |
|------|-----------|
| Web安全 | SQL注入, XSS, CSRF, 文件上传, RCE |
| 系统漏洞 | 权限提升, 缓冲区溢出, 内核漏洞 |
| 应用漏洞 | 反序列化, 逻辑漏洞, 弱口令 |
| 网络攻击 | 钓鱼, 社会工程学, APT, 勒索软件 |
| 供应链 | 第三方组件, 开源漏洞, 依赖注入 |

### CTF 子分类
| 分类 | 关键词 |
|------|--------|
| WEB | SQL注入, XSS, SSRF, 文件上传, RCE, 反序列化 |
| PWN | 二进制, 缓冲区溢出, ROP, ret2, house of |
| CRYPTO | RSA, AES, 密码学, 椭圆曲线, 侧信道 |
| REVERSE | IDA, OD, 逆向, 反编译, 壳, 脱壳 |
| MISC | 隐写, 流量分析, 取证, 图片隐写 |
| WP | WriteUp, WP, 比赛, BugKu, CTFHub, AWD |

## 📄 报告模板

```markdown
# 2026-03-24 安全资讯

## 数据概览
- **总计**: 58 篇
- Doonsec: 50篇
- BruceFeIix: 8篇

## 威胁类型分布
- 漏洞利用: 14篇
- 攻击技术: 8篇
- CTF: 18篇
- 威胁情报: 4篇

## 漏洞类型分布
- Web安全: 12篇
- 系统漏洞: 5篇

## 🎯 威胁详情分析

### 漏洞利用
| 序号 | 来源 | 文章标题 | 命中关键词 | 详细分类 |
|------|------|----------|----------|----------|
| 1 | Doonsec | [CVE分析](链接) | CVE | 漏洞利用 |

### CTF
| 序号 | 来源 | 文章标题 | 命中关键词 | 详细分类 |
|------|------|----------|----------|----------|
| 1 | Doonsec | [SQL注入WriteUp](链接) | SQL注入 | WEB |

## 🔧 漏洞详情分析

### Web安全
| 序号 | 来源 | 文章标题 | 命中关键词 | 详细分类 |
|------|------|----------|----------|----------|
| 1 | Doonsec | [XSS攻击手法](链接) | XSS | Web安全 |

---

*生成时间: 2026-03-24 14:30:00 (北京时间)*
```

## 🛠️ 技术栈

- **Python 3.8+**：核心处理逻辑
- **requests**：HTTP 请求处理
- **xml.etree.ElementTree**：RSS 解析
- **logging**：详细日志记录

## ⚙️ 使用方法

### 本地运行

```bash
# 克隆项目
git clone https://github.com/gelusus/wxvl.git
cd wxvuln

# 安装依赖
pip install requests

# 处理当天数据
python3 run.py

# 处理指定日期
python3 run.py --date 2026-03-24

# 处理日期区间
python3 run.py --range 2026-03-01 2026-03-31

# 拉取历史数据
python3 run.py --history
```

### GitHub Actions 自动执行

每天 14:00 北京时间自动执行，发送钉钉通知。

### 钉钉机器人配置

1. 钉钉群 → 群设置 → 智能群助手 → 添加机器人 → 自定义
2. 安全设置选择 **"加签"**
3. 复制 `access_token` 和 `secret`

**GitHub Secrets 配置：**
| Secret | 说明 |
|--------|------|
| `DINGDING_ACCESS_TOKEN` | 钉钉机器人 access_token |
| `DINGDING_SECRET` | 钉钉加签密钥 |

## 📁 项目结构

```
wxvuln/
├── run.py                 # 主程序
├── data.json              # URL 记录（去重用）
├── md/                    # 报告存储目录
│   └── 2026/
│       └── 2026-03/
│           └── 2026-03-24.md
├── .github/
│   └── workflows/
│       └── update_today.yml  # 定时更新workflow
├── README.md
└── LICENSE
```

## ⚠️ 注意事项

1. **敏感信息**：代码中包含 Doonsec 的 session token，建议使用环境变量
2. **GitHub Actions**：需要配置 GitHub Secrets 才能发送钉钉通知
3. **数据去重**：依赖 `data.json` 文件，删除会导致重复处理

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License
