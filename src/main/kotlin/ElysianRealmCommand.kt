package org.example.mirai.plugin

import net.mamoe.mirai.console.command.*
import java.io.BufferedReader
import java.io.InputStream
import java.io.InputStreamReader
import java.nio.charset.Charset

object GetImageCommand : SimpleCommand(PluginMain, "获取乐土攻略", "GetImageCommand") {
    @Handler
    suspend fun handle(context: CommandSender) {
        context.sendMessage("开始获取乐土攻略，可能会需要一段时间，请耐心等待")
        val command = "git clone --depth=1 https://github.com/MskTim/ElysianRealm-Data.git data/ElysianRealm-Data/"
        val pro = Runtime.getRuntime().exec(command)
        if (pro.waitFor() == 0) {
            context.sendMessage("乐土攻略获取完成")
            context.sendMessage(clearStream(pro.inputStream))
        } else {
            val errorInfo = clearStream(pro.errorStream)
            if (errorInfo.indexOf("fatal: destination path") != -1) {
                context.sendMessage(errorInfo)
                context.sendMessage("data目录下已存在ElysianRealm-Data,请勿重复获取")
            } else {
                context.sendMessage("clone出现异常:")
                context.sendMessage(errorInfo)
            }
            pro.destroy()
        }
        pro.destroy()
    }
}

object UpdateImageCommand : SimpleCommand(PluginMain, "更新乐土攻略", "UpdateImageCommand") {
    @Handler
    suspend fun handle(context: CommandSender) {
        context.sendMessage("开始更新乐土攻略，可能会需要一段时间，请耐心等待")
        val command = "git -C ./data/ElysianRealm-Data/ pull --no-rebase"
        val gitPull = Runtime.getRuntime().exec(command)
        if (gitPull.waitFor() == 0) {
            val inputInfo = clearStream(gitPull.inputStream)
            if (inputInfo.indexOf("Already up to date") != -1) {
                context.sendMessage(inputInfo)
                context.sendMessage("已经是最新了")
            } else {
                context.sendMessage("乐土攻略更新完成")
                context.sendMessage("[请]在config/Bh3.ElysianRealm.Strategy/ElysianRealmConfig.yml中添加新角色触发词")
                context.sendMessage(inputInfo)
            }
        } else {
            val errorInfo = clearStream(gitPull.errorStream)
            if (errorInfo.indexOf("No such file or directo") != -1) {
                context.sendMessage(errorInfo)
                context.sendMessage("请先输入'#获取乐土攻略'完成初次获取")
                context.sendMessage("若仍无法解决可手动删除ElysianRealm-Data文件夹后重试")
            } else {
                context.sendMessage("拉取更新异常:")
                context.sendMessage(errorInfo)
                context.sendMessage("若无法解决可手动删除ElysianRealm-Data文件夹后输入'#获取乐土攻略'重新获取")
            }
        }
        gitPull.destroy()
    }
}

object AddConfigCommand : CompositeCommand(PluginMain, "RealmCommand", "realmcommand", "乐土指令") {
    @SubCommand("新建", "新增", "new", "re")
    suspend fun reConfig(context: CommandSender, imageName: String, command: String) {
        val list = command.split(",", "，")
        var switch = true
        list.forEach {
            if (switch) {
                ElysianRealmConfig.ElysianRealmConfig[imageName] = setOf(
                    it
                )
                switch = false
            } else {
                ElysianRealmConfig.ElysianRealmConfig[imageName] =
                    ElysianRealmConfig.ElysianRealmConfig[imageName]!! + setOf(
                        it
                    )
            }
        }
        context.sendMessage("新建成功：" + ElysianRealmConfig.ElysianRealmConfig.filter { it.key == imageName }
            .toString())
    }

    @SubCommand("添加", "追加", "add")
    suspend fun addConfig(context: CommandSender, imageName: String, command: String) {
        try {
            val list = command.split(",", "，")
            list.forEach {
                ElysianRealmConfig.ElysianRealmConfig[imageName] =
                    ElysianRealmConfig.ElysianRealmConfig[imageName]!! + setOf(
                        it
                    )
            }
            context.sendMessage("添加成功：" + ElysianRealmConfig.ElysianRealmConfig.filter { it.key == imageName }
                .toString())
        } catch (e: Exception) {
            context.sendMessage("$e\n添加失败，请检查追加指令是否存在\n找到的集合：" + ElysianRealmConfig.ElysianRealmConfig.filter { it.key == imageName }
                .toString())
        }
    }

    @SubCommand("list", "列表")
    suspend fun configList(context: CommandSender) {
        var list = ""
        ElysianRealmConfig.ElysianRealmConfig.forEach {
            list += "$it\n\n"
        }
        context.sendMessage(list)
    }
}

fun clearStream(inputStream: InputStream?): String {
    val isr = InputStreamReader(inputStream, Charset.forName("GBK"))
    val br = BufferedReader(isr)
    var line: String?
    var info = ""

    while (br.readLine().also { line = it } != null) {
        info += line
    }
    return info
}