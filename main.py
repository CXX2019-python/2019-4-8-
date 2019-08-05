import requests

count = 0

url = 'https://www.ximalaya.com/revision/play/album?albumId=9742774&pageNum=1&sort=1&pageSize=30'

header= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',

    'xm-sign': input('请上网访问https://www.ximalaya.com/yinyue/19349717/,按下f12，找到network,点击XHR,找到getCurrentUser，点击headers,往下翻到xm-sign,复制后面的一串粘贴到这里。\nxm-sign值：')
}

# text 提取字符串数据 content得到二进制     json

response = requests.get(url, headers=header).json()

print('原生数据：',response)

audio_data = response['data']['tracksAudioPlay']

print('音频数据列表：',audio_data)

# 依次获取每个元素
for audio in audio_data:
    count += 1
    print('音频信息：', audio)
    music_url = audio['src']
    print('音频网址',music_url)
    music_name = audio['trackName']+'.m4a'
    print('音频名称',music_name)

    with open('music/'+music_name, "wb") as f:
        f.write(requests.get(music_url,headers=header).content)
