package com.msktmi.mirai.plugin
import net.mamoe.mirai.console.data.AutoSavePluginConfig
import net.mamoe.mirai.console.data.ValueDescription
import net.mamoe.mirai.console.data.value

object Config : AutoSavePluginConfig("config") {

    @ValueDescription("此处可更改获取乐土攻略使用的 git clone 命令，仅支持 git clone [--depth] [--branch] <远程仓库地址> 格式")
    val repository: MutableMap<String, String> by value(
        mutableMapOf(
            "url" to "git clone --depth=1 --branch legacy https://github.com/MskTmi/ElysianRealm-Data.git"
        )
    )
}
