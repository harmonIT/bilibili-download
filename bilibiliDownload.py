import requests
import re
import json
from moviepy.editor import AudioFileClip, VideoFileClip
import tkinter as tk
from tkinter import messagebox

def download_video(url):
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67',
            'Referer':url
    }
    resp = requests.get(url, headers=head)
    if resp.status_code == 200:
        print('>>>请求成功')

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
    print('>>>音频下载完成')
    video_url = json_data['data']['dash']['video'][0]['backupUrl'][0]
    video_data = requests.get(video_url,headers=head)
    with open(title+'.mp4', mode='wb') as f:
        f.write(video_data.content)
    # print('>>>视频下载完成')
    # 读取视频和音频文件  
    video_clip = VideoFileClip(title+'.mp4') 
    audio_clip = AudioFileClip(title+'.mp3')  


    # 合并音频和视频  
    final_clip = video_clip.set_audio(audio_clip)

    # 写入输出文件

    final_clip.write_videofile('%s合并.mp4'%title, codec='libx264', audio_codec='aac') 

    print('>>>视频下载成功')
    print('默认保存位置为当前文件夹')
    # 关闭clip的reader，释放资源  
    # video_clip.reader.close()  
    # audio_clip.reader.close()  
    # final_clip.reader.close_all() 

def on_button_click():
    user_input = entry.get()  # 获取输入框中的内容
    download_video(user_input)  # 调用 bilibiliDownload.py 中的 download 函数下载视频

# 创建主窗口
root = tk.Tk()
root.title("bilibili下载器测试版")
root.geometry("600x400")  # 窗口大小

# 添加一个标签
label = tk.Label(root, text="输入视频地址:")
label.pack(pady=10)  # pady 是上下边距

# 添加一个输入框
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# 添加一个按钮
button = tk.Button(root, text="点击下载视频", command=on_button_click)
button.pack(pady=10)

# 运行主循环
root.mainloop()
