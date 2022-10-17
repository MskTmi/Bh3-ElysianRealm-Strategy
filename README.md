# 基于Mirai-Console的崩坏3 往世乐土攻略查询插件

可在QQ群内根据关键词触发图片，快速获取往世乐土攻略

> 本插件基于mirai-console 2.12.0

## 食用方法

1. 运行 [Mirai Console](https://github.com/mamoe/mirai) 生成plugins文件夹;

2. 下载 [ElysianRealm](https://github.com/MskTim/Bh3-ElysianRealm-Strategy/releases) 将`ElysianRealm-1.1.0.mirai2.jar`放置在plugins文件夹;

3. 将`ElysianRealm-Data.zip`解压至data目录下;

## 效果

![IMG_6327](https://user-images.githubusercontent.com/87525977/187026836-b4310fe8-b213-4249-91f3-e0864f8c4d84.PNG)


## 手动添加角色

后续角色更新可手动添加：
1. 在Mirai/config/Bh3.ElysianRealm.Strategy/ElysianRealmConfig.yml 中添加角色名称（图片文件名）以及触发词;

2. 将图片放置在 Mirai/data/ElysianRealm-Data下;

> 图片名为ElysianRealmConfig.yml 中添加的角色名称 + jpg 
> 支持主流图片后缀名(jpeg,png,gif)

> 插件功能为根据关键词触发图片，可自定其他内容

## 其他
- 图片素材来源于网络，仅供交流学习使用
- 乐土攻略图源：崩坏3通讯中心
