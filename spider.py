import requests
import ffmpeg

url = "https://www.bilibili.com" 
headers = {
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
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
print(response.status_code)


