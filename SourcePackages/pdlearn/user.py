import os
import re
import time
import pickle
import base64
import requests
from requests.cookies import RequestsCookieJar
from sys import argv
from pdlearn import score
from pdlearn import file
from pdlearn import color
from pdlearn.mydriver        import Mydriver

def get_userId(cookies):
    userId, total, scores = score.get_score(cookies)
    return userId

def get_fullname(userId):
    fullname = ""
    status = get_user_status()
    for i in status["userId_mapping"]:
        nickname = status["userId_mapping"][i]
        if(str(userId) == i):
            fullname = i + '_' + nickname
            break
    if(fullname == ""):
        print("查找 userId: " + str(userId) + " 失败...")
        pattern = re.compile(u'^[a-zA-Z0-9_\u4e00-\u9fa5]+$')
        while True:
            input_name = input("将为此 userId 添加一个新用户。请输入此用户昵称：")
            if(pattern.search(input_name) != None):
                break
            else:
                print("输入不符合要求，输入内容只能为：英文字母、数字、下划线、中文。")
        save_fullname(str(userId) + '_' + input_name)
        return get_fullname(userId)
    return fullname

def get_nickname(userId):
    return get_fullname(userId).split('_', 1)[1]

def save_fullname(fullname):
    status = get_user_status()
    userId = fullname.split('_', 1)[0]
    nickname = fullname.split('_', 1)[1]
    status["userId_mapping"][userId] = nickname
    save_user_status(status)

def get_user_status():
    template_json_str = '''{\n    "#-说明1":"此文件是保存用户数据及登陆状态的配置文件",'''+\
                        '''\n    "#-说明2":"程序会自动读写该文件。",'''+\
                        '''\n    "#-说明3":"如不熟悉，请勿自行修改内容。错误修改可能导致程序崩溃",'''+\
                        '''\n    "#____________________________________________________________":"",'''+\
                        '''\n    "last_userId":0,\n    "userId_mapping":{\n        "0":"default"\n    }\n}'''
    status = file.get_json_data("user/user_status.json", template_json_str)
    save_user_status(status)
    # print(status)
    return status

def update_last_user(userId):
    status = get_user_status()
    status["last_userId"] = userId
    save_user_status(status)

def save_user_status(status):
    file.save_json_data("user/user_status.json", status)

def get_cookie(userId):
    userId = str(userId)
    template_json_str = '''{}'''
    cookies_json_obj = file.get_json_data("user/cookies.json", template_json_str)
    for i in cookies_json_obj:
        if(i == userId):
            cookies_b64 = cookies_json_obj[i]
            cookies_bytes = base64.b64decode(cookies_b64)
            cookie_list = pickle.loads(cookies_bytes)
            for d in cookie_list: # 检查是否过期
                if 'name' in d and 'value' in d and 'expiry' in d:
                    expiry_timestamp = int(d['expiry'])
                    if expiry_timestamp > (int)(time.time()):
                        pass
                    else:
                        return []
            return cookie_list
    return []

def save_cookies(cookies):
    # print(type(cookies), cookies)
    template_json_str = '''{}'''
    cookies_json_obj = file.get_json_data("user/cookies.json", template_json_str)
    userId = get_userId(cookies)
    cookies_bytes = pickle.dumps(cookies)
    cookies_b64 = base64.b64encode(cookies_bytes)
    cookies_json_obj[str(userId)] = str(cookies_b64, encoding='utf-8')
    # print(type(cookies_json_obj), cookies_json_obj)
    file.save_json_data("user/cookies.json", cookies_json_obj)

def get_article_video_json():
    template_json_str = '''{"#此文件记录用户的视频和文章的浏览进度":"","article_index":{},"video_index":{}}'''
    article_video_json = file.get_json_data("user/article_video_index.json", template_json_str)
    return article_video_json

def get_index(userId, index_type):
    article_video_json = get_article_video_json()
    indexs = article_video_json[index_type]
    if(str(userId) in indexs.keys()):
        index = indexs[str(userId)]
    else:
        index = 0
        article_video_json[index_type][str(userId)] = index
        file.save_json_data("user/article_video_index.json", article_video_json)
    return int(index)

def save_index(userId, index, index_type):
    article_video_json = get_article_video_json()
    article_video_json[index_type][str(userId)] = index
    file.save_json_data("user/article_video_index.json", article_video_json)

def get_article_index(userId):
    return get_index(userId, "article_index")

def save_article_index(userId, index):
    return save_index(userId, index, "article_index")

def get_video_index(userId):
    return get_index(userId, "video_index")

def save_video_index(userId, index):
    return save_index(userId, index, "video_index")

def get_default_userId():
    status = get_user_status()
    default_userId = status['last_userId']
    return default_userId

def get_default_nickname():
    return get_nickname(get_default_userId())

def get_default_fullname():
    return get_fullname(get_default_userId())

def check_default_user_cookie():
    default_userId = get_default_userId()
    default_fullname = get_default_fullname()
    default_nickname = get_default_nickname()
    print_list = [color.blue(str(default_userId)), color.blue(default_nickname)]
    print("=" * 60, "\n默认用户ID：{0[0]}，默认用户昵称：{0[1]}".format(print_list), end=" ")
    cookies = get_cookie(default_userId)
    if not cookies:
        print(color.red("【无有效cookie信息，需要登录】"))
        return []
    else:
        print(color.green("（cookie信息有效）"))
        return cookies

# 保活。执行会花费一定时间，全新cookies的有效时间是12h
def refresh_all_cookies(live_time=8.0):  # cookie有效时间保持在live_time以上
    template_json_str = '''{}'''
    cookies_json_obj = file.get_json_data("user/cookies.json", template_json_str)
    need_check = False
    valid_cookies = []
    for i in cookies_json_obj:
            cookies_b64 = cookies_json_obj[i]
            cookies_bytes = base64.b64decode(cookies_b64)
            cookie_list = pickle.loads(cookies_bytes)
            for d in cookie_list:  # 检查是否过期
                if 'name' in d and 'value' in d and 'expiry' in d and d["name"]=="token":
                    remain_time = (int(d['expiry']) - (int)(time.time()))/3600
                    print(color.green(i+"_"+get_nickname(i)+"，剩余有效时间："+str(int(remain_time*1000)/1000)+" 小时."), end="")
                    if remain_time < 0:
                        print(color.red(" 已过期 需要重新登陆"))
                    else:
                        # print(color.blue(" 有效"), end="")
                        valid_cookies.append(cookie_list)
                        if remain_time <= live_time:  # 全新cookies的有效时间是12h
                            print(color.red(" 需要刷新"))
                            need_check = True
                            # 暂没有证据表明可以用requests来请求，requests请求的响应不带cookies，不确定会不会更新cookies时间
                            # （但是万一服务端自动更新了cookie，可以试试12h之后再访问呢？则剩余时间直接设为12即可。有空的伙计可以做个实验）
                            # jar = RequestsCookieJar()
                            # for cookie in cookie_list:
                            #     jar.set(cookie['name'], cookie['value'])
                            # new_cookies = requests.get("https://pc.xuexi.cn/points/my-points.html", cookies=jar,
                            #                         headers={'Cache-Control': 'no-cache'}).cookies.get_dict()
                            # 浏览器登陆方式更新cookie，速度较慢但可靠
                            driver_login = Mydriver(nohead=False)
                            driver_login.get_url("https://www.xuexi.cn/notFound.html")
                            driver_login.set_cookies(cookie_list)
                            driver_login.get_url('https://pc.xuexi.cn/points/my-points.html')
                            new_cookies = driver_login.get_cookies()
                            driver_login.quit()
                            save_cookies(new_cookies)
                        else:
                            print(color.green(" 无需刷新"))
    if need_check:  # 再执行一遍来检查有效情况
        print("再次检查cookies有效时间...")
        refresh_all_cookies()
    else:
        for cookie in valid_cookies:
            user_id = get_userId(cookie)
            print(color.blue(get_fullname(user_id))+" 的今日得分：")
            score.show_score(cookie)


# 如有多用户，打印各个用户信息
def list_user(printing=True):
    status = get_user_status()
    mapping = status['userId_mapping']
    map_count = len(mapping)
    all_users = []
    for i in mapping:
        if i == "0":
            continue
        else:
            all_users.append([i, mapping[i]])
    if printing:
        if(map_count > 2):
            print("检测到您有多用户：", end="")
            for i in mapping:
                print(color.blue(i + "_" + mapping[i]), end="; ")
            print("")
    return all_users

# 多用户中选择一个用户，半成品
def select_user():
    user_list = list_user(printing=False)
    user_count = len(user_list)
    print("=" * 60)
    if user_count > 1:
        print("检测到多用户：")
        for i in range(user_count):
            print(i, " ", user_list[i][0], " ", user_list[i][1])
        num = int(input("请选择用户序号："))
        if num < 0 or num >= user_count:
            print("输入的范围不对。")
            exit()
        else:
            user_id = user_list[num][0]
            print("默认用户已切换为："+color.blue(get_fullname(user_id)))
            update_last_user(user_id)
    else:
        print("目前你只有一个用户。用户名：", get_default_userId(), "，昵称：", get_default_nickname())


# 仅适用于Windows的关机，有待改进
def shutdown(stime):
    if stime:
        stime = int(stime)
        os.system('shutdown -s -t {}'.format(stime))
        for i in range(stime):
            print("\r{}秒后关机".format(stime - i), end="")
            time.sleep(1)
    else:
        print("无自动关机任务，已释放程序内存，1分钟后窗口将自动关闭")
        # time.sleep(600)
        os.system("timeout 60")
