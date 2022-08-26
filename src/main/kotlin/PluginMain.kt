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
import java.io.File
import java.net.URL

/**
 * 使用 kotlin 版请把
 * `src/main/resources/META-INF.services/net.mamoe.mirai.console.plugin.jvm.JvmPlugin`
 * 文件内容改成 `org.example.mirai.plugin.PluginMain` 也就是当前主类全类名
 *
 * 使用 kotlin 可以把 java 源集删除不会对项目有影响
 *
 * 在 `settings.gradle.kts` 里改构建的插件名称、依赖库和插件版本
 *
 * 在该示例下的 [JvmPluginDescription] 修改插件名称，id和版本，etc
 *
 * 可以使用 `src/test/kotlin/RunMirai.kt` 在 ide 里直接调试，
 * 不用复制到 mirai-console-loader 或其他启动器中调试
 */

object PluginMain : KotlinPlugin(
    JvmPluginDescription(
        id = "Bh3.ElysianRealm.Strategy",
        name = "ElysianRealm Strategy",
        version = "0.1.0",
    ) {
        author("MskTim")
        info("""崩坏3往世乐土攻略插件""")
    }
) {
    override fun onEnable() {
        logger.info { "Plugin loaded" }
        //配置文件目录 "${dataFolder.absolutePath}/"
        val eventChannel = GlobalEventChannel.parentScope(this)
        eventChannel.subscribeAlways<GroupMessageEvent>{
            //群消息
            //复读示例
//            if (message.contentToString().startsWith("复读")) {
//                group.sendMessage(message.contentToString().replace("复读", ""))
//            }
            if (message.contentToString() == "人律乐土") {
                //群内发送
                //发送本地图片
                val image = File("data/人律乐土.jpg").toExternalResource()
                group.sendImage(image)
                image.close()

//                //发送网络图片
//                var url = URL("https://mmbiz.qpic.cn/mmbiz_jpg/63W5YyIWds58otZr3fYHIIXZSyPucZAUOtQF85fZX7YhXR9emtjcwqGibiaBtgc7QXZ9GErhWec3fIOtfpsI5IcQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1")
//                var urlImage = url.openConnection().getInputStream()
//                group.sendImage(urlImage)
//                urlImage.close()


                //向发送者私聊发送消息
                //sender.sendMessage("hi")
                //不继续处理
                return@subscribeAlways
            }
            //分类示例
//            message.forEach {
//                //循环每个元素在消息里
//                if (it is Image) {
//                    //如果消息这一部分是图片
//                    val url = it.queryUrl()
//                    group.sendMessage("图片，下载地址$url")
//                }
//                if (it is PlainText) {
//                    //如果消息这一部分是纯文本
//                    group.sendMessage("纯文本，内容:${it.content}")
//                }
//            }
        }
        eventChannel.subscribeAlways<FriendMessageEvent>{
            //好友信息
            //sender.sendMessage("我活着")
        }
        eventChannel.subscribeAlways<NewFriendRequestEvent>{
            //自动同意好友申请
            //accept()
        }
        eventChannel.subscribeAlways<BotInvitedJoinGroupRequestEvent>{
            //自动同意加群申请
            accept()
        }
    }
}
