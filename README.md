2个方法,都只有24分。


一、docker填补视频无法获取12分
在原本的xxqg dodocker的基础上增加了完成视频任务；
使用前先拉xxqg项目，正常登录配置
用户管理沿用xxqg docker
建议使用xxqg3.0，config.json可以自己配置含有视频的url接口。

服务器新增crontab定时任务：
1.拷贝xxqg docker 里面的user.db，使用该db的token去补满视频
0 */4 * * * docker cp 16a008105d3a:/opt/config/user.db /root/wujiajia/xxqgPy/user.db > /dev/null 2>&1

2.运行xxq3.0.py，补偿视频学习：
30 06,07,08 * * * python3 /root/wujiajia/xxqgPy/xxqg3.0.py > /dev/null 2>&1


二、IOS快捷指令

文章:IOS_xxqg_acticle.txt
视频：xxqg_static_video_IOS.txt
自行编写快捷指令，这个不难，稍微看下就可以。
