import requests
import os

name = input('需要下载的歌曲：')
print('正在下载  '+name)
url = 'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn=1&rn=30&httpsStatus=1&reqId=e8a9bff0-0e30-11eb-97cc-db48132c64cd'.format(name)

headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'Cookie': 'ga=GA1.2.1225086306.1602678311; _gid=GA1.2.1019722193.1602678311; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1602678313,1602678619,1602678641,1602679041; _gat=1; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1602681276; kw_token=408BSULIVI',
        'csrf': '408BSULIVI',
        'Referer': 'http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6'
    }

response = requests.get(url,headers=headers).json()
rid = response['data']['list'][0]['rid']
artist = response['data']['list'][0]['artist']

music_url = f'http://www.kuwo.cn/url?format=mp3&rid={rid}&response=url&type=convert_url3&br=128kmp3&from=web&t=1602688878965&httpsStatus=1&reqId=e8aad160-0e30-11eb-97cc-db48132c64cd'
result = requests.get(music_url,headers=headers).json()
mp3 = requests.get(result['url'],headers=headers)
name = name.split(' ')[0]

if not os.path.exists(f"酷我音乐/{artist}"):
    os.mkdir(f"酷我音乐/{artist}") # Create folder

with open("酷我音乐/{}/{} {}.mp3".format(artist, name, artist),"wb") as f:
    f.write(mp3.content)
    print('下载完毕')