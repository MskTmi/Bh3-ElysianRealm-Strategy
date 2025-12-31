# 崩坏3往世乐土攻略插件 (AstrBot版)

> 基于AstrBot的崩坏3往世乐土攻略查询插件，可在聊天中根据关键词触发图片，快速获取往世乐土攻略

这是原 [Mirai-Console版本](https://github.com/MskTmi/Bh3-ElysianRealm-Strategy) 的AstrBot移植版本。

## 功能特性

- 🔍 关键词触发：在群聊中发送角色关键词即可获取对应的攻略图片
- 📥 自动获取：使用命令自动从GitHub获取最新攻略图片
- 🔄 一键更新：支持通过命令更新攻略图片
- ⚙️ 灵活配置：支持自定义触发词和攻略图片
- 🎯 简单易用：安装即用，无需复杂配置
- 🆕 **智能追踪**：自动追踪攻略更新时间
- 🔥 **最新攻略**：使用主唤醒词"最新攻略"快速查看最近更新的攻略

## 安装方法

### 前置要求

1. 已安装并运行 [AstrBot](https://github.com/AstrBotDevs/AstrBot)
2. 已安装 [Git](https://git-scm.com) 并添加到环境变量（用于获取和更新攻略）

### 安装步骤

1. 将本插件文件夹复制到AstrBot的 `data/plugins/` 目录下
2. 重启AstrBot或使用热重载命令加载插件
3. 私聊机器人或在群聊中发送 `/获取乐土攻略` 初次获取攻略图片

```bash
# 方式1: 直接下载到plugins目录
cd /path/to/astrbot/data/plugins/
git clone https://github.com/YourUsername/astrbot-elysian-realm-strategy.git elysian_realm_strategy

# 方式2: 通过AstrBot管理面板安装（如果支持）
# 在AstrBot管理界面中添加插件
```

## 使用方法

### 查询攻略

在群聊中发送角色关键词即可获取攻略图片，例如：

- 发送 `猫猫乐土` 获取帕朵菲利丝攻略
- 发送 `人律乐土` 获取人之律者攻略
- 发送 `大鸭鸭乐土` 获取次生银翼攻略
- 发送 `最新攻略` 或 `最新乐土攻略` 或 `最新乐土` 获取最近更新的攻略（**新功能**）

### 命令列表

| 命令 | 描述 |
|:-----|:-----|
| `/获取乐土攻略` 或 `/GetStrategy` | 首次获取乐土攻略图片（从GitHub克隆） |
| `/更新乐土攻略` 或 `/UpdateStrategy` | 更新乐土攻略到最新版本 |
| `/乐土指令 列表` 或 `/RealmCommand list` | 查看所有攻略和触发词 |
| `/乐土指令 添加 [图片名] [触发词]` | 为攻略添加触发词 |
| `/乐土指令 删除 [图片名]` | 删除一个攻略配置 |

### 使用示例

```
# 首次获取攻略
/获取乐土攻略

# 更新攻略
/更新乐土攻略

# 添加触发词（可以使用逗号分隔多个触发词）
/乐土指令 添加 菲莉丝 帕朵乐土,菲莉丝乐土,猫猫乐土

# 查看所有攻略
/乐土指令 列表

# 删除攻略
/乐土指令 删除 菲莉丝
```

## 攻略更新

### 图片更新

后续乐土更新可使用 `/更新乐土攻略` 获取新版攻略（推荐），或去 [图床](https://github.com/MskTmi/ElysianRealm-Data) 手动更新。

> 手动上传图床，在不弃坑的情况下可能会有一到两天延迟

### 触发词更新

- 使用 `/更新乐土攻略` 更新后，请使用 `/乐土指令 添加` 命令为新获取的攻略添加触发词
- 可以在 [这里](https://github.com/MskTmi/ElysianRealm-Data/releases) 查看最新的攻略触发词配置
- 或者在插件数据目录中手动编辑 `strategy_config.yaml` 文件

### 🆕 智能更新追踪

插件现在支持自动追踪攻略更新时间：

1. **自动检测更新**：使用 `/更新乐土攻略` 时，系统会自动检测哪些图片文件发生了变化
2. **时间戳记录**：每个更新的攻略都会记录更新时间
3. **主唤醒词**：使用 `最新攻略` 关键词可以快速查看最近更新的攻略，无需记住具体角色名称

**使用场景**：

攻略制作组通常每隔 40 天左右会更新攻略，但不是全部更新，而是更新其中一个或几个角色。现在你可以：

- 更新后直接发送 `最新攻略` 查看最近更新的内容
- 使用 `/乐土指令 列表` 查看所有攻略及其更新时间
- 不用担心错过新攻略的更新

**示例**：
```
用户: /更新乐土攻略
机器人: 乐土攻略更新完成
       更新的角色: Felis, Human
       [请]使用'/乐土指令 添加 [imageName] [command]'为新角色添加触发词
       例：/乐土指令 添加 菲莉丝 猫猫乐土
       或使用 '最新攻略' 查看最新更新的攻略

用户: 最新攻略
机器人: 最新更新的攻略：猫猫乐土 (更新于 2024-01-15)
       [发送帕朵菲利丝攻略图片]
```

## 配置说明

插件配置文件位于 AstrBot 数据目录下：

```
data/
├── plugin_data/
│   └── elysian_realm_strategy/     # 插件专用数据目录
│       ├── config.yaml              # 插件配置（仓库地址等）
│       └── strategy_config.yaml     # 攻略配置（角色名和触发词映射）
└── ElysianRealm-Data/              # 攻略图片数据（共享目录）
    ├── Human.png
    ├── Void.png
    └── ...
```

### config.yaml

```yaml
repository_url: "https://github.com/MskTmi/ElysianRealm-Data.git"
```

### strategy_config.yaml

新版本数据结构包含了攻略更新时间追踪：

```yaml
Felis:
  keywords:
    - 帕朵乐土
    - 猫猫乐土
    - 帕朵菲利丝乐土
    - 菲利丝乐土
  last_updated: '2024-01-15T10:30:00'  # 自动记录的更新时间
Human:
  keywords:
    - 人律乐土
    - 爱律乐土
  last_updated: '2024-01-10T08:20:00'
# ... 更多配置
```

**注意**：`last_updated` 字段会在攻略图片更新时自动设置，无需手动修改。使用 `/更新乐土攻略` 时，系统会自动检测哪些图片发生了变化并更新对应的时间戳。

## 自定义攻略

### 添加自定义攻略图

1. 将图片放置在 `data/ElysianRealm-Data/` 目录下
   > 支持主流图片格式（jpeg, png, gif）
2. 使用 `/乐土指令 添加 [图片文件名] [触发词]` 命令添加触发词

例如：
```
# 假设你放置了 菲莉丝.jpg 到 data/ElysianRealm-Data/ 目录
/乐土指令 添加 菲莉丝 猫猫乐土,菲莉丝乐土
```

### 自定义攻略仓库

如果你想使用自己的攻略仓库：

1. [Fork ElysianRealm-Data](https://github.com/MskTmi/ElysianRealm-Data/fork) 或创建新仓库
2. 修改 `data/elysian_realm_strategy/config.yaml` 中的 `repository_url`
3. 删除 `data/ElysianRealm-Data/` 文件夹（如果存在）
4. 执行 `/获取乐土攻略` 从新仓库获取图片

## 常见问题

### Q: 无法获取攻略？

A: 请确保：
- 已安装 Git 并添加到环境变量
- 网络连接正常，可以访问 GitHub
- `data/ElysianRealm-Data` 目录不存在（首次获取时）

### Q: 如何手动获取攻略？

A: 可以在 `data/` 目录下执行：
```bash
git clone --depth=1 https://github.com/MskTmi/ElysianRealm-Data.git
```

### Q: 触发词不生效？

A: 请检查：
- 触发词是否完全匹配（包括空格）
- 配置文件是否正确保存
- 尝试重启AstrBot或重新加载插件

### Q: 图片发送失败？

A: 请确保：
- 图片文件存在于 `data/ElysianRealm-Data/` 目录
- 图片格式受支持（png, jpg, jpeg, gif）
- AstrBot 有读取图片文件的权限

## 效果展示

在群聊中发送触发词后，机器人会自动回复对应的攻略图片：

```
用户: 猫猫乐土
机器人: [发送帕朵菲利丝攻略图片]
```

## 从Mirai版本迁移

如果你之前使用的是Mirai-Console版本的插件：

1. 攻略图片可以直接复用：将 `Mirai/data/ElysianRealm-Data/` 复制到 AstrBot 的 `data/ElysianRealm-Data/`
2. 触发词配置需要转换：参考原配置文件，使用 `/乐土指令 添加` 命令重新配置
3. 命令基本保持一致，只是执行环境从Mirai改为AstrBot

## 技术说明

### 插件结构

```
elysian_realm_strategy/
├── main.py              # 插件主文件
├── metadata.yaml        # 插件元数据
├── requirements.txt     # Python依赖
└── README.md           # 说明文档
```

### 依赖项

- Python 3.8+
- PyYAML >= 6.0
- Git（系统依赖）

### API支持

插件使用AstrBot的以下API：
- `Star` 基类
- `AstrMessageEvent` 消息事件
- `MessageChain` 消息链
- `Plain` 纯文本组件
- `Image` 图片组件

## 其他

- 兼容 AstrBot 最新版本
- 乐土攻略图源：崩坏3通讯中心（月光中心）
- 图片素材来源于网络，仅供交流学习使用
- 碰到问题可以提Issue或联系作者
- 如果觉得有用，请给个 Star ⭐

## 开源协议

本项目基于原 [Bh3-ElysianRealm-Strategy](https://github.com/MskTmi/Bh3-ElysianRealm-Strategy) 项目重构，遵循相同的开源协议。

## 致谢

- 感谢 [AstrBot](https://github.com/AstrBotDevs/AstrBot) 提供优秀的机器人框架
- 感谢原作者 MskTim 开发的Mirai版本插件
- 感谢崩坏3通讯中心提供的攻略图片资源

## 联系方式

- GitHub Issues: [提交问题](https://github.com/YourUsername/astrbot-elysian-realm-strategy/issues)
- QQ: 1226594277

## 更新日志

### v2.1.0 (2024-xx-xx)

- 🆕 **新增数据结构**：支持攻略更新时间追踪
- 🔥 **主唤醒词功能**：添加"最新攻略"关键词，自动返回最近更新的攻略
- 📊 **智能更新检测**：`/更新乐土攻略` 现在会自动检测哪些文件发生了变化
- 📅 **时间戳显示**：`/乐土指令 列表` 现在会显示每个攻略的最后更新时间
- 🔄 **向后兼容**：自动迁移旧格式配置文件到新格式

### v2.0.0 (2024-xx-xx)

- 🎉 首个AstrBot版本发布
- ✨ 从Mirai-Console插件重构为AstrBot插件
- 🔄 保持原有功能，适配AstrBot API
- 📝 更新文档和使用说明
