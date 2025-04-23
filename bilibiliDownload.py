import requests
import re
import json
from moviepy.editor import AudioFileClip, VideoFileClip
import tkinter as tk

def download_video(url):
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67',
        'Referer':url
    }
    resp = requests.get(url, headers=head)
    if resp.status_code == 200:
        print('>>>正在下载视频......')

    #step2 提取标题
    title = re.findall('<h1.*>(.*?)</h1>',resp.text)[0]

    #step3 获取音频和视频
    json_data = re.findall('<script>window.__playinfo__=(.*?)</script>', resp.text)[0]
    json_data = json.loads(json_data)

    audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
    audio_data = requests.get(audio_url,headers=head)
    with open('音频.mp3', mode='wb') as f:
        f.write(audio_data.content)
    video_url = json_data['data']['dash']['video'][0]['baseUrl']
    video_data = requests.get(video_url,headers=head)
    with open('无声视频.mp4', mode='wb') as f:
        f.write(video_data.content)
    # 读取视频和音频文件  
    video_clip = VideoFileClip('无声视频.mp4') 
    audio_clip = AudioFileClip('音频.mp3')  

    # 合并音频和视频  
    final_clip = video_clip.set_audio(audio_clip)

    # 写入输出文件
    final_clip.write_videofile('%s.mp4'%title, codec='libx264', audio_codec='aac') 

    print('>>>视频下载成功\n默认保存位置为：当前文件夹（包含三个文件：音频、无声视频、有声视频）')

def on_button_click():
    user_input = entry.get() 
    download_video(user_input)
    entry.delete(0, tk.END)

# 创建主窗口
root = tk.Tk()
root.title("bilibili下载器测试版")
root.geometry("600x400")

# 添加一个标签
label = tk.Label(root, text="输入视频地址:")
label.pack(pady=10)

# 添加一个输入框
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# 添加一个按钮
button = tk.Button(root, text="点击下载视频", command=on_button_click)
button.pack(pady=10)

# 运行主循环
root.mainloop()
