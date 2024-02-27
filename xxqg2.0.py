
# 导入requests和BeautifulSoup模块
import requests
from bs4 import BeautifulSoup
from pickle import FALSE
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys,re
import sqlite3,random




video_url_list = [
    # 视频  重要活动  重要会议 重要讲话 出国访问 指示批示 函电贺词 重要活动视频专辑 学习专题报道 新闻联播 文艺频道 科技频道
    "https://www.xuexi.cn/lgdata/525pi8vcj24p.json?_st=28424280&js_v=",
    "https://www.xuexi.cn/lgdata/1jpuhp6fn73.json?_st=28427295&js_v=",
    "https://www.xuexi.cn/lgdata/19vhj0omh73.json?_st=28427297&js_v=",
    "https://www.xuexi.cn/lgdata/1je1objnh73.json?_st=28427508&js_v=",
    "https://www.xuexi.cn/lgdata/35il6fpn0ohq.json?_st=28427509&js_v=",
    "https://www.xuexi.cn/lgdata/35il6fpn0ohq.json?_st=28427512&js_v=",
    "https://www.xuexi.cn/lgdata/35il6fpn0ohq.json?_st=28427512&js_v=",
    "https://www.xuexi.cn/lgdata/1oajo2vt47l.json?_st=28427529&js_v=",
    "https://www.xuexi.cn/lgdata/1bfcj7u3pnl.json?_st=28427532&js_v=",
    "https://www.xuexi.cn/lgdata/ueg1f0a0nl.json?_st=28427534&js_v=", 
    "https://www.xuexi.cn/lgdata/2qfjjjrprmdh.json?_st=28427534&js_v="
    "https://www.xuexi.cn/lgdata/4sg3vhk2csq6.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/41gt3rsjd6l8.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/54tjo9frmhm7.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/4akevmg39ve0.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/15cbvf54onl.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/56ao086isdu2.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/3pmpl2p3nshf.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/4p8ukmanart0.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/38sfhpqcktn3.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/4fm13avfpbau.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/2sgo9h2rpc6t.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/5atk41jfgid9.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/533m3s0sj1nh.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/4shpa7t6lsuc.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/3vgbcdm1uifo.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/55dke6hh8s88.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/5d5p7nu9pfk6.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/584m77j0cd3d.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/4482vukq9ocv.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/3qf506ordq2n.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/3fdnb631h5q8.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/3415vllh4uao.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/3h85bk43dm8o.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/32g0f3710h2p.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/591ht3bc22pi.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/1lth3moi9nl.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/1l936o60vnl.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/1oj66esmr7l.json?_st=28427534&js_v=",
    "https://pc-api.xuexi.cn/open/api/auth/check?t=0.7605514646220785",
    "https://www.xuexi.cn/lgdata/11hqahk157l.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/1g48a4279nl.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/4tiagbqngp0n.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/5bb94gbrsvcd.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/16421k8267l.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/16cqa8jnh7l.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/16e0lo2fg7l.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/u1cia4cg7l.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/11otarnmh7l.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/eta8vnluqmd.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/3o3ufqgl8rsn.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/3nm8if67c913.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/31t4ilb2dj0v.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/574qghjkouko.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/4e2nfgd90jvk.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/4daoj5702n8r.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/36up4sad3crf.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/3pnauk0r03ta.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/3u1gkneeb2gv.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/5as0fe8pj73h.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/4uku6c5k9pkk.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/2q52dgs89i1e.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/4t9trhn5p829.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/58dp34sd0o0c.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/5e6l8l3a29fg.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/39dbk7r4mnt3.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/51bijiln7jnq.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/43far0vuo1t3.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/3u7v0chcjh22.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/4eumaom7o63n.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/s1a1ron32o2i.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/1n65t296p3dfp.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/1gaq3mgmboc6j.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/1jss89qtctluc.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/12s9gh9jn31ob.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/1a774joi40tgl.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/16bt7qi7rbk1b.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/13r67480jpf1b.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/1i7keqgh7cnt8.json?_st=28427534&js_v=",
    "https://www.xuexi.cn/lgdata/v3klp6fr7l.json?_st=28427541&js_v=",
    "https://www.xuexi.cn/lgdata/14s4462g9nl.json?_st=28427540&js_v="
]


# pushplus Token  http://www.pushplus.plus/send?token={token}&content=pushplus消息内容
pushPlus_token_url = "http://www.pushplus.plus/send?token=36f63c3fee6b4f2aaf1c705df2afc071&content="

# 积分查询
Query_Score_url = "https://pc-proxy-api.xuexi.cn/delegate/score/days/listScoreProgress?sence=score&deviceType=2"

# 总的session id 
headers_xxqg = {
  "name": "your_cookie_name",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
  "Accept": "application/json",
  "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
  "Cookie":"__UID__=834a0a60-b4d7-11ee-9c1b-e1e4fc791328; aliyungf_tc=0fd24f2cf7a88bf4303b28f8553c5a15b275054879d557cefce23cf01c75eeec; csrf_token=94949962211756071705890330079; tmzw=1705976529820; zwfigprt=5bb0e860ec0dda75689097a42186cea0; token=c5565950268d42d7b2fe1928319d99df; acw_tc=ac11000117059765296278003e6c46e5b615d113afa8ef84bd69029404333f"
}

# 定义要添加的 cookie
cookie_video = {
    'name': 'token',
    'value': 'c5565950268d42d7b2fe1928319d99df',
    'path': '/',
    "Domain": ".xuexi.cn",
    'secure': False,  # 是否是安全连接
    'httpOnly': False,  # 是否是 HttpOnly
    'SameSite': 'None'
}




# 读取xxqg_study docker拷贝出的sqlite3  user.db
async def read_user_table(driver):
    try:
        # 连接到 SQLite 数据库"/etc/alist/user.db"  /root/wujiajia/xxqgPy/  /root/wujiajia/xxqgPy/user.db
        connection = sqlite3.connect("/root/wujiajia/xxqgPy/user.db") 
        # 创建游标对象
        cursor = connection.cursor()
        # 执行查询语句
        cursor.execute("SELECT token FROM user")
        # 获取查询结果
        token_data = cursor.fetchall()
        # 打印用户数据
        for token in token_data:
            print(f'token是：{token[0]}')
            
            # 1-更新看视频中的token
            cookie_video["value"] = token[0]

            # 2-更新 Cookie 中的 token 这个token值是查看分数的
            # headers_xxqg = "token=c5565950268d42d7b2fe1928319d99df;"
            # 从cookie中提取token的值
            cookie_value = headers_xxqg.get('Cookie', '')
            token_match = re.search(r'token=([a-fA-F0-9]+)', cookie_value)
            if token_match:
                # 获取匹配到的token值
                current_token = token_match.group(1)
                # 替换token的值为1
                modified_cookie = re.sub(r'token=[a-fA-F0-9]+', 'token='+str(token[0]), cookie_value)
                # 更新请求头字典
                headers_xxqg['Cookie'] = modified_cookie
                # 输出结果
                print(headers_xxqg)
            else:
                print(" read_user_table ：Token not found in the cookie.")
                return
            

            # 3-查询video分数是否大于12分，
            ThisPersonIsContinue = await QueryScore(headers_xxqg)
            if ThisPersonIsContinue:
                print("视频学习已经满12分，跳过学习")
                continue
            else:
                print("视频学习已经未满12分，开始学习")
                await get_Video_url(driver)

    except sqlite3.Error as e:
        print(f"SQLite 错误: {e}")
    finally:
        # 关闭连接
        if connection:
            connection.close()




#获取当前时间戳
def getCurrentTime():
        # 获取当前时间的毫秒级时间戳
    milliseconds_timestamp = int(time.time() * 1000)
    return milliseconds_timestamp


async def open_video_url(driver,url):
    driver.get(url)
    driver.add_cookie(cookie_video)
    driver.refresh()
    await asyncio.sleep(8)
        # 播放视频    //*[@id='aliplayer-*-component_*']
    img_Course = driver.find_element(By.XPATH, '//*[contains(@id, "aliplayer-") and contains(@id, "_component_")]')
    img_Course.click()
    print("点击了")
    await asyncio.sleep(70)
    
#***************************************主程序逻辑********************************
# 随机取出api接口18条数据 用来看视频
async def QueryScore(modified_headers):
    
    response = requests.get(Query_Score_url, headers=modified_headers)
    if response.status_code == 200:
        datas = response.json()
        video_current_score = datas.get("data").get("taskProgress")[1].get("currentScore")
        if int(video_current_score) >=12:
            return True
        else:
            False
    else:
        print("QueryScore 请求出错")

# 随机取出api接口18条数据 用来看视频
async def get_Video_url(driver):
    try:
        count = 1 
        # 随机选择一个值
        random_value_video_url = random.choice(video_url_list)
        print(f"选取的url是：{random_value_video_url}")

        response = requests.get(random_value_video_url+str(getCurrentTime()), headers=headers_xxqg)
        
        if response.status_code == 200:
            print('get_Video_url 请求视频数据成功')
            data = response.json()
            # 遍历数据，判断每条 item 是否是 kPureVideo 类型  data[0:60]
            # 使用 random.sample 随机取出18条记录
            random_sample = random.sample(data, 18)
            print(f"视频数据随机条数：{random_sample}")
            for item in random_sample:
                if item.get("itemType") != "kReading":
                    # 如果是 kPureVideo 类型，打印对应的 url 值
                    print("正在播放视频的URL:", item.get("url"))
                    # await open_video_url(driver,item.get("url"))  看视频函数
                    # 正在打开看视频
                    driver.get(item.get("url"))
                    driver.add_cookie(cookie_video)
                    driver.refresh()
                    await asyncio.sleep(8)
                    # 查找播放视频按钮 //*[@id='aliplayer-*-component_*']
                    try:
                        video_player_btn = driver.find_element(By.XPATH, '//*[contains(@id, "aliplayer-") and contains(@id, "_component_")]')
                        if video_player_btn:
                            video_player_btn.click()
                            print("开始播放视频了")
                            await asyncio.sleep(70)
                            count += 1
                        else:
                            continue
                    except NoSuchElementException:
                        # 如果元素不存在，打印消息并退出循环
                        print("元素不存在，退出循环")
                        continue

                else:
                    continue

                if count >= 24:
                    break

                    

        else:
            print("get_Video_url 请求视频数据失败:",response.status_code)
            sys.exit(0)
    except requests.exceptions.RequestException as e:
        print(f"POST_HeartBeat 异常Request failed: {e}")

async def main():
    # 启动Chrome浏览器
    # options = webdriver.EdgeOptions()
    # options.add_experimental_option("detach" , True)

    # 设置Chrome浏览器的无头模式
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--remote-debugging-port=9222')
    options.add_argument('--single-process')



    # 创建Chrome WebDriver的新实例
    driver = webdriver.Chrome(options=options)
    

    await read_user_table(driver)
    #await get_Video_url(driver)
    
    
    await asyncio.sleep(10)

# 运行主程序

asyncio.run(main())