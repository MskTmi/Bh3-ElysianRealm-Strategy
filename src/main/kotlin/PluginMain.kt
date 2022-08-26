package org.example.mirai.plugin

import io.ktor.util.*
import net.mamoe.mirai.console.data.AutoSavePluginConfig
import net.mamoe.mirai.console.data.ValueDescription
import net.mamoe.mirai.console.data.value
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
        version = "1.0.0",
    ) {
        author("MskTim")
        info("""崩坏3往世乐土攻略插件""")
    }
) {
    override fun onEnable() {
        logger.info { "Plugin loaded" }
        //配置文件目录 "${dataFolder.absolutePath}/"
        //启用配置文件
        ElysianRealmConfig.reload()
        val eventChannel = GlobalEventChannel.parentScope(this)
        eventChannel.subscribeAlways<GroupMessageEvent>{
            //群消息
//            if (message.contentToString() == "hi") {
////                //发送网络图片
////                var url = URL("https://mmbiz.qpic.cn/mmbiz_jpg/63W5YyIWds58otZr3fYHIIXZSyPucZAUOtQF85fZX7YhXR9emtjcwqGibiaBtgc7QXZ9GErhWec3fIOtfpsI5IcQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1")
////                var urlImage = url.openConnection().getInputStream()
////                group.sendImage(urlImage)
////                urlImage.close()

//                //向发送者私聊发送消息
//                //sender.sendMessage("hi")
//                //不继续处理
//                return@subscribeAlways
//            }

            if (ElysianRealmConfig.ElysianRealmConfig.any{it.value.contains(message.contentToString())}){
                //群内发送本地图片
                val filteredMap = ElysianRealmConfig.ElysianRealmConfig.filter { message.contentToString() in it.value }
                val image = File("data/ElysianRealm-Data/${filteredMap.keys.elementAt(0)}.JPG").toExternalResource()
                group.sendImage(image)
                image.close()

                //不继续处理
                return@subscribeAlways
            }

//
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
            accept()
        }
    }
}
object ElysianRealmConfig : AutoSavePluginConfig("ElysianRealmConfig") {

    @ValueDescription("新加入角色可自行添加")
    val ElysianRealmConfig: Map<String, Set<String>> by value(

        mapOf(
            "人之律者" to setOf(
                "人律乐土",
                "爱律乐土"
            ),
            "空之律者" to setOf(
                "空律乐土",
                "女王乐土"
            ),
            "格蕾修" to setOf(
                "繁星乐土",
                "格蕾修乐土",
                "绘世乐土"
            ),
            "阿波尼亚" to setOf(
                "阿波尼亚乐土",
                "戒律乐土"
            ),
            "伊甸" to setOf(
                "伊甸乐土",
                "黄金乐土"
            ),
            "帕朵菲莉丝" to setOf(
                "帕朵乐土",
                "猫猫乐土",
                "菲利丝乐土"
            ),
            "伊甸" to setOf(
                "伊甸乐土",
                "黄金乐土"
            ),
            "缭乱星棘" to setOf(
                "火塔乐土",
                "烤箱乐土",
                "星棘乐土",
                "星塔乐土"
            ),
            "天元骑英" to setOf(
                "天元乐土",
                "泥头鹅乐土"
            ),
            "次生银翼" to setOf(
                "大鸭鸭乐土",
                "次生银翼乐土"
            ),
            "卡萝尔" to setOf(
                "卡萝尔乐土"
            ),
            "伊甸" to setOf(
                "伊甸乐土",
                "黄金乐土"
            ),
            "梅比乌斯" to setOf(
                "梅比乌斯乐土",
                "蛇蛇乐土"
            ),
            "渡鸦" to setOf(
                "渡鸦乐土"
            ),
            "雷之律者" to setOf(
                "雷律乐土"
            ),
            "雷律平A流" to setOf(
                "雷律平A流"
            ),
            "雷律天罚流" to setOf(
                "雷律天罚流"
            ),
            "失落迷迭" to setOf(
                "迷迭乐土"
            ),
            "狂热蓝调Δ" to setOf(
                "萝莎莉娅乐土",
                "粉毛乐土",
                "德尔塔乐土"
            ),
            "不灭星锚" to setOf(
                "星锚乐土",
                "星猫乐土"
            ),
            "爱莉希雅" to setOf(
                "爱莉乐土",
                "爱莉希雅乐土"
            ),
            "薪炎之律者" to setOf(
                "炎律乐土",
                "薪炎乐土"
            ),
            "识之律者" to setOf(
                "识律乐土",
                "识宝乐土"
            ),
            "魇夜星渊" to setOf(
                "奶希乐土",
                "冰希乐土"
            ),
            "菲谢尔" to setOf(
                "皇女乐土",
                "菲谢尔乐土"
            ),
            "彼岸双生" to setOf(
                "双生乐土",
                "黑希乐土"
            ),
            "辉骑士 · 月魄" to setOf(
                "幽兰戴尔乐土",
                "月魄乐土",
                "呆鹅乐土"
            ),
            "暮光骑士 · 月煌" to setOf(
                "月煌乐土",
                "紫苑乐土"
            ),
            "圣仪装 · 今样" to setOf(
                "今样乐土",
                "卡莲乐土"
            ),
            "御神装 · 勿忘" to setOf(
                "勿忘乐土",
                "机八乐土",
                "八重樱乐土"
            ),
            "苍骑士 · 月魂" to setOf(
                "月魂乐土",
                "冰箱乐土",
                "冰塔乐土"
            ),
            "破晓强袭" to setOf(
                "强袭乐土"
            ),
            "月下初拥" to setOf(
                "月下乐土"
            ),
            "理之律者" to setOf(
                "理律乐土",
                "摩托鸭乐土",
                "车车乐土"
            ),
            "女武神 · 荣光" to setOf(
                "荣光乐土"
            )
        )
    )
}

