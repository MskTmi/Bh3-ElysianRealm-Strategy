package net.msktmi.mirai.plugin

import net.mamoe.mirai.console.command.*
import net.mamoe.mirai.message.data.*
import java.io.BufferedReader
import java.io.InputStream
import java.io.InputStreamReader
import java.nio.charset.Charset

object GetImageCommand : SimpleCommand(PluginMain, "获取乐土攻略", "GetStrategy") {
    @Handler
    suspend fun handle(context: CommandSender) {
        context.sendMessage("开始获取乐土攻略，可能会需要一段时间，请耐心等待")
        val repository = Config.repository["url"]
        val command = "git clone --depth=1 $repository data/ElysianRealm-Data/"
        val pro = Runtime.getRuntime().exec(command)
        if (pro.waitFor() == 0) {
            context.sendMessage("乐土攻略获取完成")
            if (clearStream(pro.inputStream).isNullOrEmpty()) {
                context.sendMessage(clearStream(pro.inputStream))
            }
        } else {
            val errorInfo = clearStream(pro.errorStream)
            if (errorInfo.indexOf("fatal: destination path") != -1) {
                val forward: ForwardMessage = buildForwardMessage(context.subject!!) {
                    add(context.bot!!, PlainText(errorInfo))
                    add(context.bot!!, PlainText("data目录下已存在ElysianRealm-Data,请勿重复获取"))
                }
                context.sendMessage(forward)
            } else {
                val forward: ForwardMessage = buildForwardMessage(context.subject!!) {
                    add(context.bot!!, PlainText("clone出现异常:"))
                    add(context.bot!!, PlainText(errorInfo))
                }
                context.sendMessage(forward)
            }
            pro.destroy()
        }
        pro.destroy()
    }
}

object UpdateImageCommand : SimpleCommand(PluginMain, "更新乐土攻略", "UpdateStrategy") {
    @Handler
    suspend fun handle(context: CommandSender) {
        //开始更新
        context.sendMessage("开始更新乐土攻略，可能会需要一段时间，请耐心等待")
        val command = "git -C ./data/ElysianRealm-Data/ pull --no-rebase"
        val gitPull = Runtime.getRuntime().exec(command)
        if (gitPull.waitFor() == 0) {
            val inputInfo = clearStream(gitPull.inputStream)
            //不需要更新
            if (inputInfo.indexOf("Already up to date") != -1) {
                val forward: ForwardMessage = buildForwardMessage(context.subject!!) {
                    add(context.bot!!, PlainText(inputInfo))
                    add(context.bot!!, PlainText("已经是最新了"))
                }
                context.sendMessage(forward)
            } else {
                //更新成功
                val forward: ForwardMessage = buildForwardMessage(context.subject!!) {
                    add(context.bot!!, PlainText("乐土攻略更新完成"))
                    add(context.bot!!, PlainText("[请]使用'/RealmCommand add [imageName] [command]'添加新角色触发词"))
                    add(context.bot!!, PlainText("例 `/RealmCommand add 菲莉丝 猫猫乐土` 指令为Mirai/data/ElysianRealm-Data文件夹下的 `菲莉丝.jpg` 添加\"猫猫乐土\"为触发词"))
                    add(context.bot!!, PlainText("或关闭机器人后在'config/Bh3.ElysianRealm.Strategy/ElysianRealmConfig.yml'中手动添加"))
                    add(context.bot!!, PlainText(inputInfo))
                }
                context.sendMessage(forward)
            }
        } else {
            val errorInfo = clearStream(gitPull.errorStream)
            if (errorInfo.indexOf("No such file or directo") != -1) {
                //未找到git路径
                val forward: ForwardMessage = buildForwardMessage(context.subject!!) {
                    add(context.bot!!, PlainText(errorInfo))
                    add(context.bot!!, PlainText("请先输入'/获取乐土攻略'完成初次获取"))
                    add(context.bot!!, PlainText("若仍无法解决可手动删除ElysianRealm-Data文件夹后重试"))
                }
                context.sendMessage(forward)
            } else {
                //拉取异常
                val forward: ForwardMessage = buildForwardMessage(context.subject!!) {
                    add(context.bot!!, PlainText("拉取更新异常:"))
                    add(context.bot!!, PlainText(errorInfo))
                    add(context.bot!!, PlainText("若无法解决可手动删ElysianRealm-Data文件夹后输入'/获取乐土攻略'重新获取"))
                }
                context.sendMessage(forward)
            }
        }
        gitPull.destroy()
    }
}

object AddConfigCommand : CompositeCommand(PluginMain, "RealmCommand", "realmcommand", "乐土指令") {

    @SubCommand("添加", "add")
    suspend fun addConfig(context: CommandSender, imageName: String, command: String) {
        val list = command.split(",", "，")
        try {
            list.forEach {
                ElysianRealmConfig.ElysianRealmConfig[imageName] =
                    ElysianRealmConfig.ElysianRealmConfig[imageName]!! + setOf(
                        it
                    )
            }
            context.sendMessage("添加成功：" + ElysianRealmConfig.ElysianRealmConfig.filter { it.key == imageName }
                .toString())
        } catch (e: Exception) {
            if (ElysianRealmConfig.ElysianRealmConfig.filter { it.key == imageName }.isEmpty()) {
                //没有则新建后添加
                newStrategy(list, imageName)
                context.sendMessage("已新建后添加：" + ElysianRealmConfig.ElysianRealmConfig.filter { it.key == imageName }
                    .toString())
            }
        }
    }

    @SubCommand("删除", "remove", "del")
    suspend fun reConfig(context: CommandSender, imageName: String) {
        if (ElysianRealmConfig.ElysianRealmConfig.filter { it.key == imageName }.isNotEmpty()) {
            ElysianRealmConfig.ElysianRealmConfig.remove(imageName)
            context.sendMessage("删除'${imageName}'成功")
        } else {
            context.sendMessage("没有找到名称为'${imageName}'的集合")
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

//新增一个攻略
fun newStrategy(list: List<String>, imageName: String) {
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
}
