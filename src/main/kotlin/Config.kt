package com.msktmi.mirai.plugin
import net.mamoe.mirai.console.data.AutoSavePluginConfig
import net.mamoe.mirai.console.data.ValueDescription
import net.mamoe.mirai.console.data.value

object Config : AutoSavePluginConfig("config") {

    @ValueDescription("此处可更改乐土攻略存储库地址")
    val repository: MutableMap<String, String> by value(
        mutableMapOf(
            "url" to "https://github.com/MskTmi/ElysianRealm-Data.git"
        )
    )
}