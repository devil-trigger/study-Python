import requests
import json
import os

my_headers = {  # 请求头（无脑复制）
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63",
    "Cookie": "_ga=GA1.2.1083049585.1590317697; _gid=GA1.2.2053211683.1598526974; _gat=1; "
              "Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1597491567,1598094297,1598096480,1598526974; "
              "Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1598526974; kw_token=HYZQI4KPK3P",
    "Referer": "http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6",
    "csrf": "HYZQI4KPK3P",
}


def getMusicUrl(musicName, model):  # 0：input输入，默认/其他：函数传参输入
    # 参数list
    params = {
        # 'key': kw,
        'key': musicName,
        'pn': 1,  # 页数
        'rn': '10',  # 音乐数
        'httpsStatus': '1',
        'reqId': 'ea151d7194e68f1a82bb43c97531e874'
        # 'reqId': 'cc337fa0-e856-11ea-8e2d-ab61b365fb50'
    }
    if model == 0:
        kw = input('输入需要下载的音乐名称：')
        params['key'] = kw
    else:
        params['key'] = musicName
    # api_res = requests.get(url = )
    # print(params)
    music_list = []
    url = 'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?'
    res = requests.get(url=url, headers=my_headers, params=params)
    res.encoding = 'utf-8'
    text = res.text
    json_list = json.loads(text)
    datapack = json_list['data']['list']
    # print(datapack)

    for i in datapack:
        music_name = i['name']  # 歌名
        # print(music_name)
        music_single = i['artist']  # 演唱者
        # print(music_single)
        api_music = "http://www.kuwo.cn/url?format=mp3&rid={}&response=url&type=convert_url3" \
                    "&br=128kmp3&from=web&t=1598528574799&httpsStatus=1" \
                    "&reqId=9a4d4081-28d2-11ec-b683-b127a9098d73".format(i['rid'])
        # 其他参数为标准格式，只有传入的参数需要变动
        api_res = requests.get(url=api_music)
        music_url = json.loads(api_res.text)['url']
        # print(music_url)
        music_list.append({
            'rid': i['rid'],
            'musicName': music_name,
            'musicSingle': music_single,
            'url': music_url
        })

    # print(music_list)
    return music_list


music_list = getMusicUrl('', 0)


def download_music(my_list):
    url_list = []  # 存放所有url
    rid_list = []  # 存放rid
    music_info = []  # 存放信息
    for s in my_list:
        url_list.append(s['url'])
        rid_list.append(str(s['rid']))
        list_info = {
            'rid': s['rid'],
            'Name': s['musicName'],
            'Single': s['musicSingle']
        }
        music_info.append(list_info)
        print(list_info)
    input_Explain = input('是否全部下载(YES/NO)：')
    download_root = 'D://downMusic//'  # 下载路径
    confirm_list = ['yes', 'YES', 'Yes', 'YeS', 'YEs', 'yEs']  # 确认的输入列表

    if input_Explain in confirm_list:  # 若确认YES,则全部下载
        for i, val in enumerate(my_list):
            sing_title = val['musicName'] + '-' + val['musicSingle']
            print('正在下载:  ' + sing_title)
            if not os.path.exists(download_root):  # 若不在该目录下，则创建目录
                os.mkdir(download_root)
            open(download_root + '{}.mp3'.format(sing_title), 'wb')
            if i == len(my_list) - 1:
                print('歌曲已全部下载完成')

    else:
        download_single = input('输入下载的歌曲rid：')
        if download_single in rid_list:
            if not os.path.exists(download_root):  # 若不在该目录下，则创建目录
                os.mkdir(download_root)
            rid_num = rid_list.index(download_single)
            # print(rid_num)
            my_url = requests.get(url=url_list[rid_num]).content
            with open(
                    download_root + '{}.mp3'.format(music_info[rid_num]['Name'] + '-' + music_info[rid_num]['Single']),
                    'wb') as f:
                f.write(my_url)
                print(music_info[rid_num]['Name'] + '下载成功')
        else:
            print('输入rid错误，退出程序')


download_music(music_list)
# 输入歌曲>列出搜索到的歌曲列表>是否全部下载