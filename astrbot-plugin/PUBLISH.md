# 如何发布到新仓库

本目录包含了重构后的AstrBot版本插件。按照以下步骤发布到新仓库：

## 步骤 1: 创建新仓库

在GitHub上创建一个新的仓库，例如：`astrbot-elysian-realm-strategy`

## 步骤 2: 初始化并推送

在本地执行以下命令：

```bash
# 进入插件目录
cd astrbot-plugin

# 初始化git仓库
git init

# 添加所有文件
git add .

# 提交
git commit -m "Initial commit: AstrBot version of Elysian Realm Strategy plugin"

# 添加远程仓库（替换为你的仓库地址）
git remote add origin https://github.com/YourUsername/astrbot-elysian-realm-strategy.git

# 推送到GitHub
git push -u origin main
```

## 步骤 3: 完善仓库信息

1. 在GitHub仓库页面添加描述
2. 添加topics标签：`astrbot`, `plugin`, `honkai-impact-3`, `elysian-realm`
3. 更新README.md中的仓库链接
4. 创建Release发布版本

## 步骤 4: 发布到AstrBot插件市场（可选）

如果AstrBot有官方插件市场，可以按照其要求提交插件。

## 注意事项

- 这是一个全新的仓库，独立于原Mirai版本
- 记得更新README.md中的GitHub链接
- 考虑添加LICENSE文件
- 可以添加CI/CD配置进行自动化测试

## 目录结构

```
astrbot-plugin/
├── main.py              # 插件主文件
├── metadata.yaml        # 插件元数据
├── requirements.txt     # Python依赖
├── README.md           # 插件说明文档
├── .gitignore          # Git忽略文件
└── PUBLISH.md          # 本文件
```

## 相关链接

- 原Mirai版本: https://github.com/MskTmi/Bh3-ElysianRealm-Strategy
- AstrBot项目: https://github.com/AstrBotDevs/AstrBot
- 攻略图床: https://github.com/MskTmi/ElysianRealm-Data
