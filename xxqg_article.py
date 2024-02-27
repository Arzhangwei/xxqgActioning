import requests
import json
import re
import os,sys
# 设置接口的URL
url = "https://www.xuexi.cn/lgdata/1jscb6pu1n2.json?_st=26095725"  # 替换为你要访问的接口URL

goTo_url = 'dtxuexi://appclient/page/study_feeds?url=https://article.xuexi.cn/articles/index.html?'
i = 0

try:
    # 获取第一个参数
    first_arg = sys.argv[1]
    if first_arg is None or first_arg == '':
        file_path = "/www/wwwroot/vip.bankwjj.cloudns.org/v2ray/xxqg_article.txt"
    else:
        file_path = str(first_arg)
    
    # 检查文件是否存在
    if os.path.exists(file_path):
        # 删除文件
        os.remove(file_path)
        print(f"{file_path} 文件已成功删除。")
    else:
        print(f"{file_path} 文件不存在。")
    
    # 发送GET请求并获取响应
    response = requests.get(url)

    # 检查响应状态码
    if response.status_code == 200:
        # 使用json.loads()方法解析JSON数据
        data = json.loads(response.text)
        
        # 处理JSON数据
        # 你可以通过data字典来访问JSON数据的不同字段
        for item in data:
            #判断文章类型，筛选掉视频类型
            Article_type = str(item['type'])
            if Article_type == 'shipin':
                continue
            
            urls = str(item['url'])
            item_Id = str(item['itemId'])
            matchs = re.search(r'\?id=(\d+)', urls)
            if matchs:
            # 获取匹配到的ID值
                art_Id = matchs.group(1)
                # /www/wwwroot/bankwjj.cf/v2ray/
                with open(file_path, 'a') as file:
                    file.write(goTo_url+'art_id='+art_Id+'&item_id='+item_Id+'\n')
                print("url:", art_Id)
                
            else:
                print("未找到匹配的ID字段")
            
            #保存500个数据就够了，不然太大了也不好处理
            i = i+1
            if i > 500:
                break

    else:
        print("请求失败，状态码:", response.status_code)

except requests.exceptions.RequestException as e:
    print("请求发生异常:", e)
except json.JSONDecodeError as e:
    print("JSON解析错误:", e)