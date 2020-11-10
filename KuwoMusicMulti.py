import requests
import os

def get_music(rid):
    url_music = f'http://www.kuwo.cn/url?format=mp3&rid={rid}&response=url&type=convert_url3&br=128kmp3&from=web&t=1602680864921&httpsStatus=1&reqId=3fecbfa0-0e1e-11eb-b34f-d9db5112dda7'
    result = requests.get(url_music,headers=headers).json()
    music_url = result["url"]
    music = requests.get(music_url,headers=headers)

    if not os.path.exists(f"酷我音乐/{singer}"):
        os.mkdir(f"酷我音乐/{singer}")

    with open(f"酷我音乐/{singer}/{song}.mp3","wb") as f:
        print("正在下载： {}".format(song))
        f.write(music.content)


if __name__ == '__main__':
    singer = input('输入想爬取的歌手名： ')
    page = int(input('想要爬取的页数： '))

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'Cookie': 'ga=GA1.2.1225086306.1602678311; _gid=GA1.2.1019722193.1602678311; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1602678313,1602678619,1602678641,1602679041; _gat=1; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1602681276; kw_token=408BSULIVI',
        'csrf': '408BSULIVI',
        'Referer': 'http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6'
    }

    for i in range(1, page + 1):
        url = f'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={singer}&pn={i}&rn=30&httpsStatus=1&reqId=1e01ea80-0e1b-11eb-b7bf-b1c888e7d2fa'

        response = requests.get(url,headers=headers).json()
        data = response['data']['list']

        for content in data:
            rid = content['rid']
            song = content['name']
            get_music(rid)
