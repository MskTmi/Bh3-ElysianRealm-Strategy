package org.example.mirai.plugin

import net.mamoe.mirai.console.command.CommandManager
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
        //注册指令
        CommandManager.registerCommand(GetImageCommand)
        CommandManager.registerCommand(UpdateImageCommand)
        CommandManager.registerCommand(AddConfigCommand)
        //启用配置文件
        ElysianRealmConfig.reload()
        val eventChannel = GlobalEventChannel.parentScope(this)
        eventChannel.subscribeAlways<GroupMessageEvent> {
            //群消息
            if (ElysianRealmConfig.ElysianRealmConfig.any { it.value.contains(message.contentToString()) }) {
                //群内发送本地图片
                val filteredMap = ElysianRealmConfig.ElysianRealmConfig.filter { message.contentToString() in it.value }
                File("data/ElysianRealm-Data").walk()
                    .filter { it.isFile }
                    .filter { it.extension in listOf("png", "PNG", "jpg", "jpeg", "JPG", "gif", "GIF") }
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

        }
        eventChannel.subscribeAlways<NewFriendRequestEvent> {
            //自动同意好友申请
            //accept()
        }
        eventChannel.subscribeAlways<BotInvitedJoinGroupRequestEvent> {
            //自动加群
            //accept()
        }
    }

    override fun onDisable() {
        logger.info { "至此，乐土攻略被关闭了。" }
    }
}
