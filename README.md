


在原本的xxqg dodocker的基础上增加了完成视频任务；
使用前先拉xxqg项目，正常登录配置
我懒不想重写，所以用户管理沿用xxqg docker

建议使用3.0，config.json可以自己配置含有视频的url接口。


一、新增crontab定时任务
1.拷贝xxqg docker用户token，
0 */4 * * * docker cp 16a008105d3a:/opt/config/user.db /root/wujiajia/xxqgPy/user.db > /dev/null 2>&1

2.运行xxq3.0.py，补偿视频学习
30 06,07,08 * * * python3 /root/wujiajia/xxqgPy/xxqg3.0.py > /dev/null 2>&1


