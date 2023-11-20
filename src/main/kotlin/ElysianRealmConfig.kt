package com.msktmi.mirai.plugin

import net.mamoe.mirai.console.data.AutoSavePluginConfig
import net.mamoe.mirai.console.data.ValueDescription
import net.mamoe.mirai.console.data.value

object ElysianRealmConfig : AutoSavePluginConfig("ElysianRealmConfig") {

    @ValueDescription("新加入角色可自行添加")
    val ElysianRealmConfig: MutableMap<String, Set<String>> by value(

        mutableMapOf(
            "Human" to setOf(
                "人律乐土",
                "爱律乐土"
            ),
            "Void" to setOf(
                "空律乐土",
                "女王乐土"
            ),
            "Starry" to setOf(
                "繁星乐土",
                "格蕾修乐土",
                "绘世乐土"
            ),
            "Disciplinary" to setOf(
                "阿波尼亚乐土",
                "戒律乐土"
            ),
            "Golden" to setOf(
                "伊甸乐土",
                "黄金乐土"
            ),
            "Felis" to setOf(
                "帕朵乐土",
                "猫猫乐土",
                "帕朵菲利丝乐土",
                "菲利丝乐土"
            ),
            "Oven" to setOf(
                "火塔乐土",
                "烤箱乐土",
                "星棘乐土",
                "星塔乐土"
            ),
            "Palatinus" to setOf(
                "天元乐土",
                "天鹅乐土",
                "泥头鹅乐土"
            ),
            "Silverwing" to setOf(
                "大鸭鸭乐土",
                "次生银翼乐土"
            ),
            "Carol" to setOf(
                "卡萝尔乐土"
            ),
            "Lnfinite" to setOf(
                "梅比乌斯乐土",
                "蛇蛇乐土"
            ),
            "Raven" to setOf(
                "渡鸦乐土"
            ),
            "Thunder" to setOf(
                "雷律乐土"
            ),
            "Thunder_Attack" to setOf(
                "雷律乐土3",
                "雷律平A流"
            ),
            "Thunder_Punishment" to setOf(
                "雷律乐土2",
                "雷律天罚流"
            ),
            "Rosemary" to setOf(
                "迷迭乐土"
            ),
            "Delta" to setOf(
                "萝莎莉娅乐土",
                "粉毛乐土",
                "德尔塔乐土"
            ),
            "Anchora" to setOf(
                "星锚乐土",
                "星猫乐土"
            ),
            "Elysia" to setOf(
                "爱莉乐土",
                "爱莉希雅乐土"
            ),
            "Flamescion" to setOf(
                "炎律乐土",
                "薪炎乐土"
            ),
            "Sentience" to setOf(
                "识律乐土",
                "识宝乐土"
            ),
            "Starchasm" to setOf(
                "奶希乐土",
                "冰希乐土"
            ),
            "Fischl" to setOf(
                "皇女乐土",
                "菲谢尔乐土"
            ),
            "TwinSeele" to setOf(
                "双生乐土",
                "黑希乐土"
            ),
            "Excelsis" to setOf(
                "幽兰戴尔乐土",
                "月魄乐土",
                "呆鹅乐土"
            ),
            "Twilight" to setOf(
                "月煌乐土",
                "紫苑乐土"
            ),
            "Kallen" to setOf(
                "今样乐土",
                "卡莲乐土"
            ),
            "Moment" to setOf(
                "勿忘乐土",
                "机八乐土",
                "冰八乐土",
                "八重樱乐土"
            ),
            "Refrigerator" to setOf(
                "月魂乐土",
                "冰箱乐土",
                "冰塔乐土"
            ),
            "Bladestrike" to setOf(
                "强袭乐土"
            ),
            "LunaKindred" to setOf(
                "月下乐土"
            ),
            "Reason" to setOf(
                "理律乐土",
                "摩托鸭乐土",
                "车车乐土"
            ),
            "Gloria" to setOf(
                "荣光乐土"
            ),
            "Human_Branch" to setOf(
                "人律乐土2",
                "人律蓄力流",
                "人律纯蓄流",
                "人律蓄力"
            ),
            "Susang" to setOf(
                "李素裳乐土",
                "月痕乐土"
            ),
            "Helical" to setOf(
                "维尔薇乐土",
                "维尔微乐土",
                "v2v乐土"
            ),
            "Void_Skill" to setOf(
                "女王乐土2",
                "女王大招流",
                "空律大招流"
            ),
            "Eclipse" to setOf(
                "姬子乐土",
                "真红乐土",
                "月蚀乐土"
            ),
            "Cabbage" to setOf(
                "包菜乐土",
                "爱酱乐土",
                "爱衣乐土"
            ),
            "Truth" to setOf(
                "真理乐土",
                "真律乐土",
                "真鸭乐土",
                "真理之律者乐土"
            ),
            "Serenade" to setOf(
                "冰卡乐土",
                "s卡乐土",
                "S卡乐土",
                "怪盗乐土",
                "舞卡乐土"
            ),
            "Truth_Weapon" to setOf(
                "真理乐土2",
                "真理武器流",
                "真律武器流",
                "真鸭武器流",
                "真理之律者武器流"
            ),
            "Eclipse_Branch" to setOf(
                "真红乐土2",
                "姬子蓄力流",
                "真红蓄力流",
                "月蚀蓄力流"
            ),
            "First" to setOf(
                "始源乐土",
                "始源大招流",
                "始源大招流乐土"
            ),
            "First_Branch" to setOf(
                "始源乐土2",
                "始源之律者乐土",
                "始源分支流",
                "始源蓄力流",
                "始源分支流乐土"
            ),
            "Finally" to setOf(
                "终焉乐土",
                "终焉之律者乐土"
            ),
            "Finally_Branch" to setOf(
                "终焉乐土2",
                "终焉分支流",
                "终焉蓄力流",
                "终焉分支流乐土"
            ),
            "ShadowKnight" to setOf(
                "月轮乐土"
            ),
            "Susana" to setOf(
                "苏莎娜乐土",
                "苏珊娜乐土",
                "热砂乐土"
            ),
            "Dreamweaver" to setOf(
                "羽兔乐土2",
                "羽兔投矛流",
                "羽兔大招流"
            ),
            "Dreamweaver_Weapon" to setOf(
                "羽兔乐土",
                "羽兔摇旗流",
                "羽兔武器流"
            ),
            "TerminalAide0017" to setOf(
                "0017乐土",
                "终末乐土",
                "终末协理乐土",
                "普罗米修斯乐土",
                "普鸭乐土"
            ),
            "ShigureKira" to setOf(
                "时雨绮罗乐土",
                "时雨绮罗大招流",
                "时雨乐土",
                "绮罗乐土"
            ),
            "ShigureKira_Branch" to setOf(
                "绮罗乐土2",
                "时雨绮罗乐土2",
                "时雨绮罗蓄力流",
                "时雨绮罗分支流",
                "绮罗分支流"
            ),
            "Rebirth_Life" to setOf(
                "死律乐土3",
                "死律塑灵流",
                "死律塑灵流乐土",
                "塑灵流乐土",
                "死生之律者乐土"
            ),
            "Rebirth_Death" to setOf(
                "死律乐土2",
                "死生之律者乐土2",
                "死律结命流",
                "死律结命流乐土",
                "结命流乐土"
            ),
            "Rebirth_Swap" to setOf(
                "死律乐土",
                "死律凋换流",
                "死律凋换流乐土",
                "凋换流乐土"
            ),
            "Sirin_Attack" to setOf(
                "西琳乐土2",
                "河豚乐土2",
                "西琳普攻流"
            ),
            "Sirin_Branch" to setOf(
                "西琳乐土",
                "河豚乐土",
                "西琳蓄力流",
                "西琳分支流"
            ),
            "TheresaLuna_Weapon" to setOf(
                "月下誓约乐土",
                "大月下乐土2",
                "月下誓约武器流",
                "大月下武器流"
            ),
            "TheresaLuna_Attack" to setOf(
                "月下誓约普攻流",
                "大月下普攻流",
                "大月下乐土"
            ),
            "Sentience_brick" to setOf(
                "识律板砖流",
                "识律乐土2"
            ),
            "CosmicExpression_Parry" to setOf(
                "大格蕾修乐土",
                "大格蕾修弹反流"
            ),
            "TheresaLuna_Attack" to setOf(
                "大格蕾修普攻流",
                "大格蕾修乐土2"
            )
        )
    )
}