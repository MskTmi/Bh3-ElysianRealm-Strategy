# 基于Mirai-Console的崩坏3 往世乐土攻略查询插件

可在QQ群内根据关键词触发图片，快速获取往世乐土攻略

> 本插件基于mirai-console 2.12.0

## 食用方法

1. 运行 [Mirai Console](https://github.com/mamoe/mirai) 生成plugins文件夹;

2. 下载 [ElysianRealm](https://github.com/MskTim/Bh3-ElysianRealm-Strategy/releases) 将 `ElysianRealm-1.4.0.mirai2.jar` 放置在plugins文件夹;

3. 初次使用私聊机器人输入 `#获取乐土攻略` 自动获取攻略图片;

> 后续乐土更新也可使用 `#更新乐土攻略` 获取新版攻略(因为是手动上传图床,在不弃坑的情况下可能会有一到两天延迟);  
> 更新后「请」在config/Bh3.ElysianRealm.Strategy/ElysianRealmConfig.yml中添加新角色触发词;

## 效果

![IMG_6327](https://user-images.githubusercontent.com/87525977/187026836-b4310fe8-b213-4249-91f3-e0864f8c4d84.PNG)


## 手动添加角色


1. 在Mirai/config/Bh3.ElysianRealm.Strategy/ElysianRealmConfig.yml 中添加角色名称（图片文件名）以及触发词;
2. 下载 [ElysianRealm-Data.zip](https://github.com/MskTim/ElysianRealm-Data/releases) 或去 [图床地址](https://github.com/MskTim/ElysianRealm-Data) 下载图片;
3. 将图片放置在 Mirai/data/ElysianRealm-Data下;

> 图片名为ElysianRealmConfig.yml 中添加的角色名称 + jpg  
  支持主流图片后缀名(jpeg,png,gif)

> 插件功能为根据关键词触发图片，可自定其他内容;
## 常见问题
1. 获取乐土攻略功能仅支持群聊，私聊机器人无效;
2.  `#获取乐土攻略` 与 `#更新乐土攻略` 功能依赖Github,请确保网络通畅;
3. 无法使用`#获取乐土攻略`也可在Mirai/data目录下打开Shell输入 `git clone https://github.com/MskTim/ElysianRealm-Data.git` 手动获取;
4. 自 `1.4.0` 版本起将攻略文件名更改为英文(解决部分Linux下的中文文件名编码的问题),旧版本在更新后需删除Mirai/config/Bh3.ElysianRealm.Strategy目录下的ElysianRealmConfig.yml文件后重启mirai (初次使用无视)

## 其他
- 兼容mirai-console 2.13.2
- 图片素材来源于网络，仅供交流学习使用
- 乐土攻略图源：崩坏3通讯中心
- 碰到奇怪bug可以联系我：1226594277(qq)
- 最后「请」点个 stars⭐吧~
