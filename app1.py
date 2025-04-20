import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("提示", "Hello, Tkinter!")

# 创建主窗口
root = tk.Tk()
root.title("工具箱")
root.geometry("600x400")  # 窗口大小

# 添加一个标签
label = tk.Label(root, text="点击按钮试试！")
label.pack(pady=10)  # pady 是上下边距

# 添加一个按钮
button = tk.Button(root, text="click me", command=on_button_click)
button.pack(pady=10)

# 运行主循环
root.mainloop() 
