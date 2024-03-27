
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
import sqlite3,random,json






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


async def getRandomUrl_func():
    # 从 config.json 文件中读取数据
    with open("config.json", "r") as json_file:
        data = json.load(json_file)

    # 从数据中随机选择一条
    random_data = random.choice(data["video_url_list"])

    print("随机选择的数据是：", random_data)
    return random_data

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
        #random_value_video_url = random.choice(video_url_list)
        random_value_video_url = await getRandomUrl_func()
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