# 从 Mirai-Console 版本迁移指南

本文档帮助你从原 Mirai-Console 版本的插件迁移到 AstrBot 版本。

## 主要区别

| 项目 | Mirai 版本 | AstrBot 版本 |
|------|-----------|-------------|
| 框架 | Mirai-Console (Kotlin/JVM) | AstrBot (Python) |
| 插件类型 | Mirai Plugin (.jar) | AstrBot Star Plugin |
| 配置位置 | `config/Bh3.ElysianRealm.Strategy/` | `data/plugin_data/elysian_realm_strategy/` |
| 数据位置 | `data/ElysianRealm-Data/` | `data/ElysianRealm-Data/` (相同) |
| 指令格式 | 完全相同 | 完全相同 |

## 迁移步骤

### 1. 备份现有数据

如果你已经在使用 Mirai 版本，请先备份：

```bash
# 备份攻略图片
cp -r Mirai/data/ElysianRealm-Data ~/backup/

# 备份配置文件
cp Mirai/config/Bh3.ElysianRealm.Strategy/ElysianRealmConfig.yml ~/backup/
```

### 2. 安装 AstrBot 版本

按照 README.md 的安装说明安装 AstrBot 插件。

### 3. 迁移攻略图片

如果你已经有攻略图片，可以直接复用：

```bash
# 将 Mirai 的攻略图片复制到 AstrBot 数据目录
cp -r Mirai/data/ElysianRealm-Data /path/to/astrbot/data/
```

或者使用 `/获取乐土攻略` 命令重新获取。

### 4. 迁移配置

#### 方式1: 使用命令添加（推荐）

使用 `/乐土指令 添加` 命令逐个添加触发词。

例如，如果原配置是：
```yaml
菲莉丝:
  - 猫猫乐土
  - 帕朵乐土
```

在 AstrBot 中执行：
```
/乐土指令 添加 Felis 猫猫乐土,帕朵乐土
```

注意：图片名称需要使用英文名（参见下方映射表）。

#### 方式2: 手动编辑配置文件

1. 启动 AstrBot 插件，让它生成默认配置
2. 编辑 `data/plugin_data/elysian_realm_strategy/strategy_config.yaml`
3. 按照 YAML 格式添加你的自定义配置

### 5. 角色名称映射

Mirai 版本中使用的是中文图片名，AstrBot 版本使用英文名（与图床保持一致）：

| 中文名 | 英文名 (AstrBot) | 触发词示例 |
|--------|------------------|-----------|
| 菲莉丝 | Felis | 猫猫乐土, 帕朵乐土 |
| 人律 | Human | 人律乐土, 爱律乐土 |
| 空律 | Void | 空律乐土, 女王乐土 |
| 格蕾修 | Starry | 繁星乐土, 格蕾修乐土 |
| 阿波尼亚 | Disciplinary | 阿波尼亚乐土, 戒律乐土 |
| 伊甸 | Golden | 伊甸乐土, 黄金乐土 |
| ... | ... | ... |

完整映射可以在插件的 `main.py` 中的默认配置找到。

## 功能对比

### 相同功能

✅ 关键词触发攻略图片  
✅ `/获取乐土攻略` 命令  
✅ `/更新乐土攻略` 命令  
✅ `/乐土指令 列表` 查看攻略  
✅ `/乐土指令 添加` 添加触发词  
✅ `/乐土指令 删除` 删除攻略  

### 新增功能

🆕 支持多平台（AstrBot 支持 QQ、Discord、Telegram 等多平台）  
🆕 更简单的配置管理（YAML 格式，更易读）  
🆕 自动配置持久化  

### 差异说明

1. **配置格式**：Mirai 版本使用 Kotlin 对象格式，AstrBot 使用 YAML 格式
2. **图片名称**：AstrBot 版本使用英文名，与 GitHub 图床保持一致
3. **权限管理**：不需要像 Mirai 那样单独配置 chat-command 权限

## 常见问题

### Q: 可以同时运行 Mirai 和 AstrBot 版本吗？

A: 可以，两个版本是完全独立的。但建议只保留一个版本以避免混淆。

### Q: 迁移后原来的触发词还能用吗？

A: 能用！触发词配置是独立的，只要你重新配置了相同的触发词即可。

### Q: 需要重新下载攻略图片吗？

A: 不需要。可以直接复制 Mirai 的 `data/ElysianRealm-Data` 到 AstrBot 的 `data/` 目录。

### Q: 迁移后数据会丢失吗？

A: 不会。只要按照迁移步骤操作，所有数据都会保留。

### Q: 如何回退到 Mirai 版本？

A: 只需停止 AstrBot，继续使用原来的 Mirai 环境即可。两者互不影响。

## 获取帮助

如果在迁移过程中遇到问题：

1. 查看 [README.md](README.md) 的常见问题部分
2. 查看 [AstrBot 官方文档](https://docs.astrbot.app)
3. 提交 [GitHub Issue](https://github.com/YourUsername/astrbot-elysian-realm-strategy/issues)
4. 联系作者 QQ: 1226594277

## 推荐迁移流程

如果你是新用户，建议：
1. 直接使用 AstrBot 版本，无需迁移

如果你是 Mirai 老用户，建议：
1. 在测试环境先试用 AstrBot 版本
2. 确认功能正常后再正式迁移
3. 保留 Mirai 版本的备份，以防万一

祝迁移顺利！🎉
