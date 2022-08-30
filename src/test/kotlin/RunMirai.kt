package org.example.mirai.plugin

import net.mamoe.mirai.alsoLogin
import net.mamoe.mirai.console.MiraiConsole
import net.mamoe.mirai.console.plugin.PluginManager.INSTANCE.enable
import net.mamoe.mirai.console.plugin.PluginManager.INSTANCE.load
import net.mamoe.mirai.console.terminal.MiraiConsoleTerminalLoader

suspend fun main() {
    MiraiConsoleTerminalLoader.startAsDaemon()

    //Kotlin
    PluginMain.load()
    PluginMain.enable()

    //测试
    val bot = MiraiConsole.addBot(2651250485, "2020abcd") {
        fileBasedDeviceInfo()
    }.alsoLogin()

    MiraiConsole.job.join()
}