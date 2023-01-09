package org.example.mirai.plugin

import net.mamoe.mirai.console.plugin.jvm.JvmPluginDescription
import net.mamoe.mirai.console.plugin.jvm.KotlinPlugin
import net.mamoe.mirai.contact.Contact.Companion.sendImage
import net.mamoe.mirai.event.GlobalEventChannel
import net.mamoe.mirai.event.events.BotInvitedJoinGroupRequestEvent
import net.mamoe.mirai.event.events.FriendMessageEvent
import net.mamoe.mirai.event.events.GroupMessageEvent
import net.mamoe.mirai.event.events.NewFriendRequestEvent
import net.mamoe.mirai.utils.ExternalResource.Companion.toExternalResource
import net.mamoe.mirai.utils.info
import java.io.*
import java.nio.charset.Charset


object PluginMain : KotlinPlugin(
    JvmPluginDescription(
        id = "Bh3.ElysianRealm.Strategy",
        name = "ElysianRealm Strategy",
        version = "1.2.0",
    ) {
        author("MskTim")
        info("""崩坏3往世乐土攻略插件""")
    }
) {
    override fun onEnable() {
        logger.info { "乐土攻略已启用！感觉如何？" }
        //配置文件目录 "${dataFolder.absolutePath}/"
        //启用配置文件
        ElysianRealmConfig.reload()
        val eventChannel = GlobalEventChannel.parentScope(this)
        eventChannel.subscribeAlways<GroupMessageEvent>{
            //群消息
            if (ElysianRealmConfig.ElysianRealmConfig.any{it.value.contains(message.contentToString())}){
                //群内发送本地图片
                val filteredMap = ElysianRealmConfig.ElysianRealmConfig.filter { message.contentToString() in it.value }
                File("data/ElysianRealm-Data").walk()
                    .filter { it.isFile }
                    .filter { it.extension in listOf("png","PNG","jpg","jpeg","JPG","gif","GIF") }
                    .filter { it.nameWithoutExtension == filteredMap.keys.elementAt(0) }
                    .forEach {
                        val image = File("data/ElysianRealm-Data/${it.name}").toExternalResource()
                        group.sendImage(image)
                        image.close()
                    }

                //发送网络图片(咕咕咕)
                //var url = URL("")
                //var urlImage = url.openConnection().getInputStream()
                //group.sendImage(urlImage)
                //urlImage.close()
                //不继续处理
                return@subscribeAlways
            }

        }
        eventChannel.subscribeAlways<FriendMessageEvent> {
            //好友信息
            if (message.contentToString() == "#获取乐土攻略") {
                sender.sendMessage("开始获取乐土攻略，可能会需要一段时间，请耐心等待")
                val command = "git clone --depth=1 https://github.com/MskTim/ElysianRealm-Data.git data/ElysianRealm-Data/"
                val pro = Runtime.getRuntime().exec(command)
                if (pro.waitFor() == 0) {
                    sender.sendMessage("乐土攻略获取完成")
                    sender.sendMessage(clearStream(pro.inputStream))
                } else {
                    val errorInfo = clearStream(pro.errorStream)
                    if (errorInfo.indexOf("fatal: destination path") != -1) {
                        sender.sendMessage(errorInfo)
                        sender.sendMessage("data目录下已存在ElysianRealm-Data,请勿重复获取")
                    } else {
                        sender.sendMessage("clone出现异常:")
                        sender.sendMessage(errorInfo)
                    }
                    pro.destroy()
                }

                pro.destroy()
            }
            if (message.contentToString() == "#更新乐土攻略") {
                sender.sendMessage("开始更新乐土攻略，可能会需要一段时间，请耐心等待")
                val command = "git -C ./data/ElysianRealm-Data/ pull --no-rebase"
                val gitPull = Runtime.getRuntime().exec(command)
                if (gitPull.waitFor() == 0) {
                    val inputInfo = clearStream(gitPull.inputStream)
                    if (inputInfo.indexOf("Already up to date") != -1) {
                        sender.sendMessage(inputInfo)
                        sender.sendMessage("已经是最新了")
                    } else {
                        sender.sendMessage("乐土攻略更新完成")
                        sender.sendMessage("[请]在config/Bh3.ElysianRealm.Strategy/ElysianRealmConfig.yml中添加新角色触发词")
                        sender.sendMessage(inputInfo)
                    }
                } else {
                    val errorInfo = clearStream(gitPull.errorStream)
                    if (errorInfo.indexOf("No such file or directo") != -1) {
                        sender.sendMessage(errorInfo)
                        sender.sendMessage("请先输入'#获取乐土攻略'完成初次获取")
                        sender.sendMessage("若仍无法解决可手动删除ElysianRealm-Data文件夹后重试")
                    } else {
                        sender.sendMessage("拉取更新异常:")
                        sender.sendMessage(errorInfo)
                        sender.sendMessage("若无法解决可手动删除ElysianRealm-Data文件夹后输入'#获取乐土攻略'重新获取")
                    }
                }
                gitPull.destroy()
            }
        }
        eventChannel.subscribeAlways<NewFriendRequestEvent>{
            //自动同意好友申请
            //accept()
        }
        eventChannel.subscribeAlways<BotInvitedJoinGroupRequestEvent>{
            //自动加群
            accept()
        }
    }
    override fun onDisable() {
        logger.info { "至此，乐土攻略被关闭了。" }
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