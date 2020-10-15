import requests, json
import time
def main():
    session = requests.Session()
    ckurl = "https://ejw.glmc.edu.cn/login/GetValidateCode?id=0.07966794016126882"
    url1 = "https://ejw.glmc.edu.cn/Login/SubmitLogin"

    valcode = session.get(ckurl)

    f = open('valcode.png', 'wb')
    f.write(valcode.content)
    f.close()

    codekey = input("请输入验证码：")
    print('ok')

    headers ={
        'Accept': '*/*',
        'Accept-Language': 'zh-Hans-CN, zh-Hans;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Host': 'ejw.glmc.edu.cn',
        'Referer': 'https://ejw.glmc.edu.cn/',
        'User-Agent': 'Mozilla/5.0(WindowsNT10.0;WOW64;Trident/7.0;rv: 11.0) likeGeckoCore/1.70.3741.400QQBrowser/10.5.3863.400',
        'X-Requested-With': 'XMLHttpRequest'
    }
    ius=input("请输入学号：")
    ipwd=input("请输入密码：")

    data = {
        'ck': '',
        'pwd': '',
        'us': ''
    }

    data['ck'] = str(codekey)
    data['pwd']= str(ipwd)
    data['us'] = str(ius)
    test = session.post(url1, data=data, headers=headers)
    # print(test.status_code)
    # print(test.text)

    t = str(int(time.time()*1000))
    # print(t)

    params = {
        '_dc': t,
        'term': '',
        'page': 1,
        'start': 0,
        'limit': 25,
        'sort': json.dumps([{"property":"stid","direction":"ASC"},{"property":"term","direction":"ASC"}])
    }

    getcj = session.get('https://ejw.glmc.edu.cn/Student/GetStuScore', headers=headers, params=params)

    # print(getcj.status_code)
    # print(getcj.text)

    try:
        r = json.loads(getcj.text.replace("'true'",'"true"').replace("success:",'"success":').replace("data:",'"data":'))
        getthing = r['data']
        # print(getthing)
        for item in getthing:
            print(item["cname"],':',item["zpxs"])
    except Exception as e:
        print(e)
        pass

    # print(getthing)
    return
if __name__== '__main__':
    main()