'''import requests
import hashlib, json
url = 'https://api.bilibili.com/pgc/player/web/v2/playurl?avid=114357732118511&bvid=BV1eS5rzcESM&cid=29479208871&qn=127&fnver=0&fnval=4048&fourk=1&support_multi_audio=true&from_client=BROWSER'


head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67',
        'Referer':url,
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language":"zh-CN,zh;q=0.9,en;q=0.8",
        "cache-control":"no-cache",
        "cookie":"buvid3=5887617F-5DEB-8788-355B-F87EFBCE0A8C70306infoc; b_nut=1744944970; b_lsid=852D946F_19646D33B7D; _uuid=87E997C1-3C44-63DD-10B13-9924D2E42510E70658infoc; buvid4=65FE7BDC-DCC2-E6DD-5BB0-BA712846D12371317-025041810-dblaZrqqMDHoq34oAMuObAWO1464cM+tJT+xbuLQHZPFAIaRR4w1X6ySxL0B4l/V; buvid_fp=7ce9859060da520355a096c875ae61d5",
        "pragma":"no-cache",
        "priority":"u=0, i",
        "sec-ch-ua":"\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
        "sec-ch-ua-mobile":"?0",
        "sec-ch-ua-platform":"\"Windows\"",
        "sec-fetch-dest":"document",
        "sec-fetch-mode":"navigate",
        "sec-fetch-site":"none",
        "sec-fetch-user":"?1",
        "upgrade-insecure-requests":"1",
    }
resp = requests.get(url, headers=head)
resp.encoding = 'utf-8'
print(resp.status_code,resp.text)'''
'''def get_play_list(start_url, cid, quality):
    entropy = 'rbMCKn@KuamXWlPMoJGsKcbiJKUfkPF_8dABscJntvqhRSETg'
    appkey, sec = ''.join([chr(ord(i) + 2) for i in entropy[::-1]]).split(':')
    params = 'appkey=%s&cid=%s&otype=json&qn=%s&quality=%s&type=' % (appkey, cid, quality, quality)
    chksum = hashlib.md5(bytes(params + sec, 'utf8')).hexdigest()
    url_api = 'https://interface.bilibili.com/v2/playurl?%s&sign=%s' % (params, chksum)
    print(url_api)
    headers = {
        'Referer': start_url,  # 注意加上referer
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language":"zh-CN,zh;q=0.9,en;q=0.8",
        "cache-control":"no-cache",
        "cookie":"buvid3=5887617F-5DEB-8788-355B-F87EFBCE0A8C70306infoc; b_nut=1744944970; b_lsid=852D946F_19646D33B7D; _uuid=87E997C1-3C44-63DD-10B13-9924D2E42510E70658infoc; buvid4=65FE7BDC-DCC2-E6DD-5BB0-BA712846D12371317-025041810-dblaZrqqMDHoq34oAMuObAWO1464cM+tJT+xbuLQHZPFAIaRR4w1X6ySxL0B4l/V; buvid_fp=7ce9859060da520355a096c875ae61d5",
        "pragma":"no-cache",
        "priority":"u=0, i",
        "sec-ch-ua":"\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
        "sec-ch-ua-mobile":"?0",
        "sec-ch-ua-platform":"\"Windows\"",
        "sec-fetch-dest":"document",
        "sec-fetch-mode":"navigate",
        "sec-fetch-site":"none",
        "sec-fetch-user":"?1",
        "upgrade-insecure-requests":"1",
        }
    # print(url_api)
    html = requests.get(url_api, headers=headers)
    html.encoding = 'utf-8'
    print(html.text)
    # print(json.dumps(html))
    # video_list = []
    # for i in html['durl']:
    #     video_list.append(i['url'])
    # print(video_list)
    # return video_list
get_play_list(url,'29066594658','80')
# data =resp.content
# with open('test.mp4', mode='wb') as f:
#     f.write(data)
'''

from bilibili_api import interactive_video
import asyncio

async def main():
    ivideo = interactive_video.up_get_ivideo_pages("BV1UE411y7Wy")
    downloader = interactive_video.get_edge_infor(ivideo, "test.ivi")
    downloader.ignore_event("DOWNLOAD_PART")
    @downloader.on("__ALL__")
    async def on_event(data: dict):
        print(data)
    await downloader.start()

asyncio.run(main())