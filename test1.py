
import requests
import re
import json
from moviepy.editor import AudioFileClip, VideoFileClip, CompositeVideoClip

#step1 获取源码
url = 'https://www.bilibili.com/video/BV155oGY3Ect/?spm_id_from=333.1007.tianma.1-1-1.click'
head = {
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67',
              'Referer':url } # 这两个参数缺一不可
resp = requests.get(url, headers=head)
print(resp.status_code)

#step2 提取标题
title = re.findall('<h1.*>(.*?)</h1>',resp.text)[0]
print('>>>标题:',title)

#step3 获取音频和视频
json_data = re.findall('<script>window.__playinfo__=(.*?)</script>', resp.text)[0]
json_data = json.loads(json_data)

audio_url = json_data['data']['dash']['audio'][0]['backupUrl'][0]
audio_data = requests.get(audio_url,headers=head)
with open(title+'.mp3', mode='wb') as f:
     f.write(audio_data.content)
video_url = json_data['data']['dash']['video'][0]['backupUrl'][0]
video_data = requests.get(video_url,headers=head)
with open(title+'.mp4', mode='wb') as f:
    f.write(video_data.content)
print('>>>视频下载完成')

# 读取视频和音频文件  
video_clip = VideoFileClip(title+'.mp4') 
audio_clip = AudioFileClip(title+'.mp3')  


# 合并音频和视频  
final_clip = video_clip.set_audio(audio_clip)

# 写入输出文件

final_clip.write_videofile('output_file.mp4', codec='libx264', audio_codec='aac') 

print('>>>合并完成')
# 关闭clip的reader，释放资源  
video_clip.reader.close()  
audio_clip.reader.close()  
final_clip.reader.close_all() 

