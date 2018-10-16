# BJFUhelper

## 介绍

BJFUhelper是一个Telegram bot, 用于实现一些便捷的查询工作.

现已将原有功能迁移至微信平台.

主要功能信息来源: 

- [北林教务系统](http://newjwxt.bjfu.edu.cn/)
- [青桥网](http://qq.bjfu.edu.cn/)

Telegram id: `@bjfuhelper_bot`

## Telegram bot 功能及用法:

- 获取帮助: `/help`
- 登录教务系统: `/regist` `学号` `密码`
- 获取当日课表: `/class`
- 获取明日课表: `/tomorrow`
- 查询本周周数: `/week`
- 获取本周课表: `/thisweek`
- 获取下周课表: `/nextweek`
- 退出登录: `/del`
- 查看二课堂活动 (测试功能): `/qqact`
- 查看实验实习安排: `/extracourse`
- 一键评教: `/evaluate`

## Wechat bot 功能及用法:

- 获取帮助: `help`
- 登录教务系统: `login` `学号` `密码`<br>
- 获取当日课表: `class`<br>
- 获取明日课表: `tomorrow`<br>
- 查询本周周数: `weeknum`<br>
- 获取本周课表: `thisweek`<br>
- 获取下周课表: `nextweek`<br>
- 退出登录: `del`<br>
- 查询快递: `kd` `单号`<br>
- 查询天气: `today` `城市` | `later` `城市`<br>
- 查询wca选手信息: `wca` `姓名|WCAID`<br>

> 微信封号频繁, 暂停更新Wechat bot

## 账号密码保存方式:

- 所有登录信息存储在内存中, 结束进程将会自动销毁, 故重启后需要重新登录.
- 为保护隐私, 请在发送登录信息后 **DELETE MESSAGE(Telegram)** 或 **撤回信息(Wechat)**