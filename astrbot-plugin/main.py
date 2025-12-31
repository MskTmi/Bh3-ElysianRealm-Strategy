"""
崩坏3往世乐土攻略查询插件
基于AstrBot的Honkai Impact 3rd Elysian Realm Strategy Plugin
"""
import os
import subprocess
import yaml
from pathlib import Path
from typing import Dict, Set, List, Optional
from datetime import datetime, timezone

from astrbot.api.star import Star, Context, register
from astrbot.api.event import AstrMessageEvent, MessageChain
from astrbot.api.message.components import Plain, Image

# Constants
SHA1_HASH_LENGTH = 40


@register(
    "elysian_realm_strategy",
    "MskTim",
    "崩坏3往世乐土攻略查询插件，可在聊天中根据关键词触发图片",
    "2.1.0",
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
        # New structure: character_name -> {"keywords": set, "last_updated": timestamp}
        self.strategy_config: Dict[str, Dict] = {}
        
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
                # Migrate old format to new format if needed
                for k, v in loaded.items():
                    if isinstance(v, list):
                        # Old format: character_name: [keywords]
                        self.strategy_config[k] = {
                            "keywords": set(v),
                            "last_updated": None
                        }
                    elif isinstance(v, dict):
                        # New format: character_name: {keywords: [], last_updated: timestamp}
                        keywords = v.get("keywords", [])
                        self.strategy_config[k] = {
                            "keywords": set(keywords) if isinstance(keywords, list) else keywords,
                            "last_updated": v.get("last_updated")
                        }
        else:
            # 默认攻略配置 - migrate to new format
            default_config = {
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
            # Convert to new format
            for char_name, keywords in default_config.items():
                self.strategy_config[char_name] = {
                    "keywords": keywords,
                    "last_updated": None
                }
            self._save_strategy_config()
    
    def _save_strategy_config(self):
        """保存攻略配置"""
        config_path = self.config_dir / self.strategy_config_file
        config_path.parent.mkdir(parents=True, exist_ok=True)
        # Convert to serializable format
        save_data = {}
        for char_name, config in self.strategy_config.items():
            save_data[char_name] = {
                "keywords": list(config["keywords"]),
                "last_updated": config["last_updated"]
            }
        with open(config_path, 'w', encoding='utf-8') as f:
            yaml.dump(save_data, f, allow_unicode=True)
    
    @register.on_message
    async def on_message_create(self, event: AstrMessageEvent):
        """处理消息事件"""
        message_text = event.message_str.strip()
        
        # Check for "latest guide" keyword
        if message_text in ["最新攻略", "最新乐土攻略", "最新乐土"]:
            await self._send_latest_strategy(event)
            return
        
        # 检查是否匹配触发词 - 支持多个图片共享同一关键词
        matching_images = []
        for image_name, config in self.strategy_config.items():
            if message_text in config["keywords"]:
                matching_images.append((image_name, config.get("last_updated")))
        
        if matching_images:
            # 如果有多个匹配，选择最近更新的
            best_match = self._select_latest_image(matching_images)
            await self._send_strategy_image(event, best_match)
            return
        
        # 处理命令
        if message_text.startswith("/获取乐土攻略") or message_text.startswith("/GetStrategy"):
            await self._get_strategy(event)
        elif message_text.startswith("/更新乐土攻略") or message_text.startswith("/UpdateStrategy"):
            await self._update_strategy(event)
        elif message_text.startswith("/乐土指令") or message_text.startswith("/RealmCommand"):
            await self._realm_command(event, message_text)
    
    def _select_latest_image(self, matching_images: List[tuple]) -> str:
        """
        从多个匹配的图片中选择最近更新的
        Args:
            matching_images: List of (image_name, last_updated) tuples
        Returns:
            image_name of the most recently updated image
        """
        # 如果只有一个匹配，直接返回
        if len(matching_images) == 1:
            return matching_images[0][0]
        
        # 找出最近更新的
        best_image = None
        best_time_obj = None
        
        for image_name, last_updated in matching_images:
            if last_updated:
                try:
                    time_obj = datetime.fromisoformat(last_updated)
                    if best_time_obj is None or time_obj > best_time_obj:
                        best_time_obj = time_obj
                        best_image = image_name
                except (ValueError, TypeError) as e:
                    self.logger.error(f"Invalid timestamp for {image_name}: {last_updated}, error: {e}")
                    continue
        
        # 如果所有图片都没有时间戳，返回第一个
        if best_image is None:
            self.logger.warning(f"No valid timestamps found for matching images, returning first match")
            return matching_images[0][0]
        
        return best_image
    
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
    
    async def _send_latest_strategy(self, event: AstrMessageEvent):
        """发送最近更新的攻略"""
        # Find the character with the most recent update
        latest_char = None
        latest_time = None
        latest_time_obj = None
        
        for char_name, config in self.strategy_config.items():
            last_updated = config.get("last_updated")
            if last_updated:
                try:
                    # Parse to datetime for proper comparison
                    time_obj = datetime.fromisoformat(last_updated)
                    if latest_time_obj is None or time_obj > latest_time_obj:
                        latest_time_obj = time_obj
                        latest_time = last_updated
                        latest_char = char_name
                except (ValueError, TypeError) as e:
                    self.logger.error(f"Invalid timestamp for {char_name}: {last_updated}, error: {e}")
                    continue
        
        if latest_char:
            # Get first keyword for display
            latest_config = self.strategy_config[latest_char]
            keywords = list(latest_config["keywords"])
            keyword_display = keywords[0] if keywords else latest_char
            
            # Format timestamp for display
            try:
                update_time_str = latest_time_obj.strftime("%Y-%m-%d")
            except (ValueError, TypeError, AttributeError) as e:
                self.logger.error(f"Error formatting timestamp: {latest_time}, error: {e}")
                update_time_str = "未知日期"
            
            await self.context.send_message(
                event.unified_msg_origin,
                MessageChain([Plain(f"最新更新的攻略：{keyword_display} (更新于 {update_time_str})")])
            )
            await self._send_strategy_image(event, latest_char)
        else:
            await self.context.send_message(
                event.unified_msg_origin,
                MessageChain([Plain("暂无更新记录，请先使用 /更新乐土攻略 更新攻略")])
            )
    
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
        
        # Get list of changed files during update
        try:
            # First, get the current commit hash
            result_hash = subprocess.run(
                ["git", "-C", str(self.data_dir), "rev-parse", "HEAD"],
                capture_output=True,
                text=True,
                timeout=30
            )
            old_commit = result_hash.stdout.strip() if result_hash.returncode == 0 else None
            
            # Validate commit hash format (SHA-1: 40 hex characters)
            if old_commit and not (len(old_commit) == SHA1_HASH_LENGTH and all(c in '0123456789abcdef' for c in old_commit.lower())):
                self.logger.warning(f"Invalid commit hash format: {old_commit}")
                old_commit = None
            
            # Additional validation: verify commit exists in repository
            if old_commit:
                verify_result = subprocess.run(
                    ["git", "-C", str(self.data_dir), "cat-file", "-e", old_commit],
                    capture_output=True,
                    timeout=10
                )
                if verify_result.returncode != 0:
                    self.logger.warning(f"Commit hash does not exist in repository: {old_commit}")
                    old_commit = None
            
            # Pull updates
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
                    # Get list of changed files
                    updated_files = []
                    if old_commit:
                        result_diff = subprocess.run(
                            ["git", "-C", str(self.data_dir), "diff", "--name-only", old_commit, "HEAD"],
                            capture_output=True,
                            text=True,
                            timeout=30
                        )
                        if result_diff.returncode == 0:
                            diff_output = result_diff.stdout.strip()
                            # splitlines() returns empty list for empty string
                            changed_files = diff_output.splitlines()
                            
                            # Filter for image files and extract character names
                            image_extensions = ['.png', '.PNG', '.jpg', '.jpeg', '.JPG', '.gif', '.GIF']
                            current_time = datetime.now(timezone.utc).isoformat()
                            
                            for file_path in changed_files:
                                # Skip empty strings (though splitlines() shouldn't produce them)
                                if not file_path:
                                    continue
                                    file_name = Path(file_path).stem
                                    file_ext = Path(file_path).suffix
                                    if file_ext in image_extensions:
                                        # Update timestamp for this character
                                        if file_name in self.strategy_config:
                                            self.strategy_config[file_name]["last_updated"] = current_time
                                            updated_files.append(file_name)
                            
                            # Save updated config
                            if updated_files:
                                self._save_strategy_config()
                    
                    response_msg = "乐土攻略更新完成\n"
                    if updated_files:
                        response_msg += f"更新的角色: {', '.join(updated_files)}\n"
                    response_msg += "[请]使用'/乐土指令 添加 [imageName] [command]'为新角色添加触发词\n"
                    response_msg += "例：/乐土指令 添加 菲莉丝 猫猫乐土\n"
                    response_msg += "或使用 '最新攻略' 查看最新更新的攻略"
                    
                    await self.context.send_message(
                        event.unified_msg_origin,
                        MessageChain([Plain(response_msg)])
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
        for image_name, config in self.strategy_config.items():
            keywords = config["keywords"]
            last_updated = config.get("last_updated")
            
            result += f"{image_name}: {', '.join(keywords)}"
            if last_updated:
                try:
                    update_time = datetime.fromisoformat(last_updated).strftime("%Y-%m-%d")
                    result += f" (更新于: {update_time})"
                except (ValueError, TypeError) as e:
                    self.logger.error(f"Invalid timestamp for {image_name}: {last_updated}, error: {e}")
            result += "\n"
        
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
            self.strategy_config[image_name]["keywords"].update(keyword_list)
        else:
            self.strategy_config[image_name] = {
                "keywords": set(keyword_list),
                "last_updated": datetime.now(timezone.utc).isoformat()
            }
        
        self._save_strategy_config()
        
        await self.context.send_message(
            event.unified_msg_origin,
            MessageChain([
                Plain(f"添加成功: {image_name} -> {', '.join(self.strategy_config[image_name]['keywords'])}")
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
