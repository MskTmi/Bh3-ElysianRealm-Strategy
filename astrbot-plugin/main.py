"""
崩坏3往世乐土攻略查询插件
基于AstrBot的Honkai Impact 3rd Elysian Realm Strategy Plugin
"""
import os
import subprocess
import yaml
from pathlib import Path
from typing import Dict, Set, List

from astrbot.api.star import Star, Context, register
from astrbot.api.event import AstrMessageEvent, MessageChain
from astrbot.api.message.components import Plain, Image


@register(
    "elysian_realm_strategy",
    "MskTim",
    "崩坏3往世乐土攻略查询插件，可在聊天中根据关键词触发图片",
    "2.0.0",
    "https://github.com/MskTmi/Bh3-ElysianRealm-Strategy"
)
class ElysianRealmStrategy(Star):
    """崩坏3往世乐土攻略插件"""
    
    def __init__(self, context: Context):
        super().__init__(context)
        self.config_file = "config.yaml"
        self.strategy_config_file = "strategy_config.yaml"
        # Use AstrBot's data directory for the plugin
        plugin_data_dir = Path(context.get_data_dir())
        self.config_dir = plugin_data_dir
        self.data_dir = Path("data/ElysianRealm-Data")  # Shared data directory for images
        self.config: Dict[str, str] = {}
        self.strategy_config: Dict[str, Set[str]] = {}
        
        # Load configurations
        self._load_config()
        self._load_strategy_config()
        
    def _load_config(self):
        """加载插件配置"""
        config_path = self.config_dir / self.config_file
        config_path.parent.mkdir(parents=True, exist_ok=True)
        
        if config_path.exists():
            with open(config_path, 'r', encoding='utf-8') as f:
                self.config = yaml.safe_load(f) or {}
        else:
            # 默认配置
            self.config = {
                "repository_url": "https://github.com/MskTmi/ElysianRealm-Data.git"
            }
            self._save_config()
            
    def _save_config(self):
        """保存插件配置"""
        config_path = self.config_dir / self.config_file
        config_path.parent.mkdir(parents=True, exist_ok=True)
        with open(config_path, 'w', encoding='utf-8') as f:
            yaml.dump(self.config, f, allow_unicode=True)
    
    def _load_strategy_config(self):
        """加载攻略配置（角色名称和触发词映射）"""
        config_path = self.config_dir / self.strategy_config_file
        
        if config_path.exists():
            with open(config_path, 'r', encoding='utf-8') as f:
                loaded = yaml.safe_load(f) or {}
                # Convert list to set for each entry
                self.strategy_config = {k: set(v) if isinstance(v, list) else v for k, v in loaded.items()}
        else:
            # 默认攻略配置
            self.strategy_config = {
                "Human": {"人律乐土", "爱律乐土"},
                "Void": {"空律乐土", "女王乐土"},
                "Starry": {"繁星乐土", "格蕾修乐土", "绘世乐土"},
                "Disciplinary": {"阿波尼亚乐土", "戒律乐土"},
                "Golden": {"伊甸乐土", "黄金乐土"},
                "Felis": {"帕朵乐土", "猫猫乐土", "帕朵菲利丝乐土", "菲利丝乐土"},
                "Oven": {"火塔乐土", "烤箱乐土", "星棘乐土", "星塔乐土"},
                "Palatinus": {"天元乐土", "天鹅乐土", "泥头鹅乐土"},
                "Silverwing": {"大鸭鸭乐土", "次生银翼乐土"},
                "Carol": {"卡萝尔乐土"},
                "Lnfinite": {"梅比乌斯乐土", "蛇蛇乐土"},
                "Raven": {"渡鸦乐土"},
                "Thunder": {"雷律乐土"},
                "Thunder_Attack": {"雷律乐土3", "雷律平A流"},
                "Thunder_Punishment": {"雷律乐土2", "雷律天罚流"},
                "Rosemary": {"迷迭乐土"},
                "Delta": {"萝莎莉娅乐土", "粉毛乐土", "德尔塔乐土"},
                "Anchora": {"星锚乐土", "星猫乐土"},
                "Elysia": {"爱莉乐土", "爱莉希雅乐土"},
                "Flamescion": {"炎律乐土", "薪炎乐土"},
                "Sentience": {"识律乐土", "识宝乐土"},
                "Starchasm": {"奶希乐土", "冰希乐土"},
                "Fischl": {"皇女乐土", "菲谢尔乐土"},
                "TwinSeele": {"双生乐土", "黑希乐土"},
                "Excelsis": {"幽兰戴尔乐土", "月魄乐土", "呆鹅乐土"},
                "Twilight": {"月煌乐土", "紫苑乐土"},
                "Kallen": {"今样乐土", "卡莲乐土"},
                "Moment": {"勿忘乐土", "机八乐土", "冰八乐土", "八重樱乐土"},
                "Refrigerator": {"月魂乐土", "冰箱乐土", "冰塔乐土"},
                "Bladestrike": {"强袭乐土"},
                "LunaKindred": {"月下乐土"},
                "Reason": {"理律乐土", "摩托鸭乐土", "车车乐土"},
                "Gloria": {"荣光乐土"},
                "Human_Branch": {"人律乐土2", "人律蓄力流", "人律纯蓄流", "人律蓄力"},
                "Susang": {"李素裳乐土", "月痕乐土"},
                "Helical": {"维尔薇乐土", "维尔微乐土", "v2v乐土"},
                "Void_Skill": {"女王乐土2", "女王大招流", "空律大招流"},
                "Eclipse": {"姬子乐土", "真红乐土", "月蚀乐土"},
                "Cabbage": {"包菜乐土", "爱酱乐土", "爱衣乐土"},
                "Truth": {"真理乐土", "真律乐土", "真鸭乐土", "真理之律者乐土"},
                "Serenade": {"冰卡乐土", "s卡乐土", "S卡乐土", "怪盗乐土", "舞卡乐土"},
                "Truth_Weapon": {"真理乐土2", "真理武器流", "真律武器流", "真鸭武器流", "真理之律者武器流"},
                "Eclipse_Branch": {"真红乐土2", "姬子蓄力流", "真红蓄力流", "月蚀蓄力流"},
                "First": {"始源乐土", "始源大招流", "始源大招流乐土"},
                "First_Branch": {"始源乐土2", "始源之律者乐土", "始源分支流", "始源蓄力流", "始源分支流乐土"},
                "Finally": {"终焉乐土", "终焉之律者乐土"},
                "Finally_Branch": {"终焉乐土2", "终焉分支流", "终焉蓄力流", "终焉分支流乐土"},
                "ShadowKnight": {"月轮乐土"},
                "Susana": {"苏莎娜乐土", "苏珊娜乐土", "热砂乐土"},
                "Dreamweaver": {"羽兔乐土2", "羽兔投矛流", "羽兔大招流"},
                "Dreamweaver_Weapon": {"羽兔乐土", "羽兔摇旗流", "羽兔武器流"},
                "TerminalAide0017": {"0017乐土", "终末乐土", "终末协理乐土", "普罗米修斯乐土", "普鸭乐土"},
                "ShigureKira": {"时雨绮罗乐土", "时雨绮罗大招流", "时雨乐土", "绮罗乐土"},
                "ShigureKira_Branch": {"绮罗乐土2", "时雨绮罗乐土2", "时雨绮罗蓄力流", "时雨绮罗分支流", "绮罗分支流"},
                "Rebirth_Life": {"死律乐土3", "死律塑灵流", "死律塑灵流乐土", "塑灵流乐土", "死生之律者乐土"},
                "Rebirth_Death": {"死律乐土2", "死生之律者乐土2", "死律结命流", "死律结命流乐土", "结命流乐土"},
                "Rebirth_Swap": {"死律乐土", "死律凋换流", "死律凋换流乐土", "凋换流乐土"},
                "Sirin_Attack": {"西琳乐土2", "河豚乐土2", "西琳普攻流"},
                "Sirin_Branch": {"西琳乐土", "河豚乐土", "西琳蓄力流", "西琳分支流"},
                "TheresaLuna_Weapon": {"月下誓约乐土", "大月下乐土2", "月下誓约武器流", "大月下武器流"},
                "TheresaLuna_Attack": {"月下誓约普攻流", "大月下普攻流", "大月下乐土"},
                "Sentience_brick": {"识律板砖流", "识律乐土2"},
                "CosmicExpression_Parry": {"大格蕾修乐土", "大格蕾修弹反流"},
                "CosmicExpression_Attack": {"大格蕾修普攻流", "大格蕾修乐土2"}
            }
            self._save_strategy_config()
    
    def _save_strategy_config(self):
        """保存攻略配置"""
        config_path = self.config_dir / self.strategy_config_file
        config_path.parent.mkdir(parents=True, exist_ok=True)
        # Convert sets to lists for YAML serialization
        save_data = {k: list(v) for k, v in self.strategy_config.items()}
        with open(config_path, 'w', encoding='utf-8') as f:
            yaml.dump(save_data, f, allow_unicode=True)
    
    @register.on_message
    async def on_message_create(self, event: AstrMessageEvent):
        """处理消息事件"""
        message_text = event.message_str.strip()
        
        # 检查是否匹配触发词
        for image_name, keywords in self.strategy_config.items():
            if message_text in keywords:
                await self._send_strategy_image(event, image_name)
                return
        
        # 处理命令
        if message_text.startswith("/获取乐土攻略") or message_text.startswith("/GetStrategy"):
            await self._get_strategy(event)
        elif message_text.startswith("/更新乐土攻略") or message_text.startswith("/UpdateStrategy"):
            await self._update_strategy(event)
        elif message_text.startswith("/乐土指令") or message_text.startswith("/RealmCommand"):
            await self._realm_command(event, message_text)
    
    async def _send_strategy_image(self, event: AstrMessageEvent, image_name: str):
        """发送攻略图片"""
        # 查找图片文件
        image_extensions = ['.png', '.PNG', '.jpg', '.jpeg', '.JPG', '.gif', '.GIF']
        
        for ext in image_extensions:
            image_path = self.data_dir / f"{image_name}{ext}"
            if image_path.exists():
                try:
                    # 使用AstrBot的Image组件发送图片
                    await self.context.send_message(
                        event.unified_msg_origin,
                        MessageChain([Image.fromFileSystem(str(image_path))])
                    )
                    return
                except Exception as e:
                    self.logger.error(f"发送图片失败: {e}")
                    await self.context.send_message(
                        event.unified_msg_origin,
                        MessageChain([Plain(f"发送图片失败: {str(e)}")])
                    )
                    return
        
        # 未找到图片
        self.logger.warning(f"未找到图片: {image_name}")
    
    async def _get_strategy(self, event: AstrMessageEvent):
        """获取乐土攻略（首次克隆仓库）"""
        await self.context.send_message(
            event.unified_msg_origin,
            MessageChain([Plain("开始获取乐土攻略，可能会需要一段时间，请耐心等待")])
        )
        
        # 确保数据目录存在
        self.data_dir.parent.mkdir(parents=True, exist_ok=True)
        
        # 检查目录是否已存在
        if self.data_dir.exists():
            await self.context.send_message(
                event.unified_msg_origin,
                MessageChain([
                    Plain("data目录下已存在ElysianRealm-Data，请勿重复获取\n"),
                    Plain("如需更新请使用 /更新乐土攻略 命令")
                ])
            )
            return
        
        # 克隆仓库
        repository_url = self.config.get("repository_url", "https://github.com/MskTmi/ElysianRealm-Data.git")
        try:
            result = subprocess.run(
                ["git", "clone", "--depth=1", repository_url, str(self.data_dir)],
                capture_output=True,
                text=True,
                timeout=300
            )
            
            if result.returncode == 0:
                await self.context.send_message(
                    event.unified_msg_origin,
                    MessageChain([Plain("乐土攻略获取完成")])
                )
            else:
                error_msg = result.stderr or result.stdout
                await self.context.send_message(
                    event.unified_msg_origin,
                    MessageChain([
                        Plain("获取失败:\n"),
                        Plain(error_msg)
                    ])
                )
        except subprocess.TimeoutExpired:
            await self.context.send_message(
                event.unified_msg_origin,
                MessageChain([Plain("获取超时，请检查网络连接")])
            )
        except FileNotFoundError:
            await self.context.send_message(
                event.unified_msg_origin,
                MessageChain([
                    Plain("未找到git命令，请确保已安装git并添加到环境变量")
                ])
            )
        except Exception as e:
            await self.context.send_message(
                event.unified_msg_origin,
                MessageChain([Plain(f"获取失败: {str(e)}")])
            )
    
    async def _update_strategy(self, event: AstrMessageEvent):
        """更新乐土攻略（拉取最新版本）"""
        await self.context.send_message(
            event.unified_msg_origin,
            MessageChain([Plain("开始更新乐土攻略，可能会需要一段时间，请耐心等待")])
        )
        
        # 检查目录是否存在
        if not self.data_dir.exists():
            await self.context.send_message(
                event.unified_msg_origin,
                MessageChain([
                    Plain("未找到ElysianRealm-Data目录\n"),
                    Plain("请先使用 /获取乐土攻略 完成初次获取")
                ])
            )
            return
        
        # 拉取更新
        try:
            result = subprocess.run(
                ["git", "-C", str(self.data_dir), "pull", "--no-rebase"],
                capture_output=True,
                text=True,
                timeout=300
            )
            
            if result.returncode == 0:
                output = result.stdout
                if "Already up to date" in output or "已经是最新" in output:
                    await self.context.send_message(
                        event.unified_msg_origin,
                        MessageChain([Plain("已经是最新版本了")])
                    )
                else:
                    await self.context.send_message(
                        event.unified_msg_origin,
                        MessageChain([
                            Plain("乐土攻略更新完成\n"),
                            Plain("[请]使用'/乐土指令 添加 [imageName] [command]'添加新角色触发词\n"),
                            Plain("例：/乐土指令 添加 菲莉丝 猫猫乐土")
                        ])
                    )
            else:
                error_msg = result.stderr or result.stdout
                await self.context.send_message(
                    event.unified_msg_origin,
                    MessageChain([
                        Plain("更新失败:\n"),
                        Plain(error_msg)
                    ])
                )
        except subprocess.TimeoutExpired:
            await self.context.send_message(
                event.unified_msg_origin,
                MessageChain([Plain("更新超时，请检查网络连接")])
            )
        except Exception as e:
            await self.context.send_message(
                event.unified_msg_origin,
                MessageChain([Plain(f"更新失败: {str(e)}")])
            )
    
    async def _realm_command(self, event: AstrMessageEvent, message_text: str):
        """处理乐土指令"""
        parts = message_text.split()
        
        if len(parts) < 2:
            await self.context.send_message(
                event.unified_msg_origin,
                MessageChain([
                    Plain("用法:\n"),
                    Plain("/乐土指令 列表 - 查看所有攻略\n"),
                    Plain("/乐土指令 添加 [图片名] [触发词1,触发词2,...] - 添加触发词\n"),
                    Plain("/乐土指令 删除 [图片名] - 删除攻略")
                ])
            )
            return
        
        subcommand = parts[1]
        
        if subcommand in ["列表", "list"]:
            await self._list_strategies(event)
        elif subcommand in ["添加", "add"]:
            if len(parts) < 4:
                await self.context.send_message(
                    event.unified_msg_origin,
                    MessageChain([Plain("用法: /乐土指令 添加 [图片名] [触发词1,触发词2,...]")])
                )
                return
            image_name = parts[2]
            keywords = parts[3]
            await self._add_strategy(event, image_name, keywords)
        elif subcommand in ["删除", "remove", "del"]:
            if len(parts) < 3:
                await self.context.send_message(
                    event.unified_msg_origin,
                    MessageChain([Plain("用法: /乐土指令 删除 [图片名]")])
                )
                return
            image_name = parts[2]
            await self._remove_strategy(event, image_name)
        else:
            await self.context.send_message(
                event.unified_msg_origin,
                MessageChain([Plain(f"未知子命令: {subcommand}")])
            )
    
    async def _list_strategies(self, event: AstrMessageEvent):
        """列出所有攻略"""
        if not self.strategy_config:
            await self.context.send_message(
                event.unified_msg_origin,
                MessageChain([Plain("暂无攻略配置")])
            )
            return
        
        result = "攻略列表:\n\n"
        for image_name, keywords in self.strategy_config.items():
            result += f"{image_name}: {', '.join(keywords)}\n"
        
        await self.context.send_message(
            event.unified_msg_origin,
            MessageChain([Plain(result)])
        )
    
    async def _add_strategy(self, event: AstrMessageEvent, image_name: str, keywords: str):
        """添加或更新攻略触发词"""
        # 分割触发词
        keyword_list = [k.strip() for k in keywords.replace('，', ',').split(',') if k.strip()]
        
        if not keyword_list:
            await self.context.send_message(
                event.unified_msg_origin,
                MessageChain([Plain("请提供至少一个触发词")])
            )
            return
        
        # 添加或更新
        if image_name in self.strategy_config:
            self.strategy_config[image_name].update(keyword_list)
        else:
            self.strategy_config[image_name] = set(keyword_list)
        
        self._save_strategy_config()
        
        await self.context.send_message(
            event.unified_msg_origin,
            MessageChain([
                Plain(f"添加成功: {image_name} -> {', '.join(self.strategy_config[image_name])}")
            ])
        )
    
    async def _remove_strategy(self, event: AstrMessageEvent, image_name: str):
        """删除攻略"""
        if image_name in self.strategy_config:
            del self.strategy_config[image_name]
            self._save_strategy_config()
            await self.context.send_message(
                event.unified_msg_origin,
                MessageChain([Plain(f"删除'{image_name}'成功")])
            )
        else:
            await self.context.send_message(
                event.unified_msg_origin,
                MessageChain([Plain(f"没有找到名称为'{image_name}'的攻略")])
            )
