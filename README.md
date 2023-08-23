# 基于Mirai-Console的崩坏3 往世乐土攻略查询插件

> 可在QQ群内根据关键词触发图片，快速获取往世乐土攻略

## 食用方法

1. 运行 [Mirai Console](https://github.com/mamoe/mirai) 生成plugins文件夹;

2. 下载 [ElysianRealm](https://github.com/MskTim/Bh3-ElysianRealm-Strategy/releases) 将 `ElysianRealm-1.5.1.mirai2.jar` 放置在plugins文件夹;

3. 初次使用私聊机器人输入 `/获取乐土攻略` 自动获取攻略图片;

## 攻略更新

- 后续乐土更新可使用 `/更新乐土攻略` 获取新版攻略（推荐），或去 [图床](https://github.com/MskTim/ElysianRealm-Data) 手动更新  

> 手动上传图床,在不弃坑的情况下可能会有一到两天延迟  

 - 使用`/更新乐土攻略`更新后「请」使用[指令](#指令)为新获取的攻略添加触发词   
> 也可在config/Bh3.ElysianRealm.Strategy/ElysianRealmConfig.yml中手动添加
## 效果

![IMG_6327](https://user-images.githubusercontent.com/87525977/187026836-b4310fe8-b213-4249-91f3-e0864f8c4d84.PNG)

## 指令
| 指令                                                       | 描述              |
|:---------------------------------------------------------|:----------------|
| `/<GetStrategy 获取乐土攻略>`                                  | 获取乐土攻略          |
| `/<UpdateStrategy 更新乐土攻略>`                               | 更新乐土攻略          |
| `/<RealmCommand 乐土指令> <list 列表>`                         | 查看攻略列表          |
| `/<RealmCommand 乐土指令> <add 添加> [imageName] [command]`    | 为攻略添加触发词        |
| `/<RealmCommand 乐土指令> <remove 删除> [imageName]`           | 删除一个攻略          |

- `/获取乐土攻略` or `/GetStrategy`获取乐土攻略
- `/RealmCommand add 菲莉丝 帕朵乐土,菲莉丝乐土` 为一个攻略并添加一个或多个触发词（使用`,`分割）


### 注意：  
1. 在聊天环境执行指令需先安装 [chat-command](https://github.com/project-mirai/chat-command) 并添加权限（攻略获取不受影响）  
   - 安装chat-command后私聊机器人输入`/perm permit u123456 *:*` 添加权限，允许用户 123456 执行任意指令
   
2. `[imageName]` 为ElysianRealm-Data下添加的图片名，`[command]` 为触发词，在群聊内输入触发词可以发送对应的图片
   - 例 `/RealmCommand add 菲莉丝 猫猫乐土` 指令为Mirai/data/ElysianRealm-Data文件夹下的 `菲莉丝.jpg` 添加"猫猫乐土"为触发词

## 手动添加角色（不推荐）

手动去图床下载压缩包解压安装，虽不影响功能但后续更新无法使用部分指令比较麻烦  
使用指令获取与更新攻略均使用GitHub图床，保持网络畅通即可  
实在无法使用git可继续 ↓

1. 在Mirai/config/Bh3.ElysianRealm.Strategy/ElysianRealmConfig.yml 中添加角色名称（图片文件名）以及触发词;
2. 去 [图床地址](https://github.com/MskTim/ElysianRealm-Data) 下载 [ElysianRealm-Data.zip](https://github.com/MskTim/ElysianRealm-Data/releases) ;
3. 将图片放置在 Mirai/data/ElysianRealm-Data下;

> 图片名为ElysianRealmConfig.yml 中添加的角色名称 + jpg  
  支持主流图片后缀名(jpeg,png,gif)

> 插件功能为根据关键词触发图片，可自定其他内容

## 常见问题
1. 获取乐土攻略功能仅支持群聊，私聊机器人无效
2. 使用指令需要先添加自己QQ号为管理员
3.  `/获取乐土攻略` 与 `/更新乐土攻略` 功能依赖Github,请确保网络通畅
4.  `/获取乐土攻略` 与 `/更新乐土攻略` 失败与成功均会返回提示信息，请勿反复请求
5. 无法使用 `/获取乐土攻略` 也可在Mirai/data目录下打开Shell输入 `git clone https://github.com/MskTim/ElysianRealm-Data.git` 获取（不影响后续使用指令更新）
6. 自 `1.4.0` 版本起将攻略文件名更改为英文(解决部分Linux下的中文文件名编码的问题),旧版本在更新后需删除Mirai/config/Bh3.ElysianRealm.Strategy目录下的ElysianRealmConfig.yml文件后重启mirai (初次使用无视)

## 其他
- 兼容mirai-console 2.15.0
- 乐土攻略图源：崩坏3通讯中心（月光中心）
- 图片素材来源于网络，仅供交流学习使用
- 碰到奇怪bug可以发issues或是联系我：1226594277(qq)
- 最后「请」点个 stars⭐吧~
