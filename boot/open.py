import tkinter
from tkinter import messagebox

def result():
    messagebox.showinfo(title='温馨提示', message='您的电脑目前处于开机状态！')

root = tkinter.Tk()
root.iconphoto(True,tkinter.PhotoImage(file="computer.png"))
root.title('一键检测是否开机-[云物缭绕]')
root.geometry("500x300")
root.configure(background="#fff")
root.resizable(width=False, height=False)

# 添加文本内,设置字体的前景色和背景色，和字体类型、大小
text=tkinter.Label(root,text="点击下方按钮，即可智能检测您的电脑是否开机",bg="#fff",font=('thee', 13))
# 将文本内容放置在主窗口内
text.pack(padx=30,pady=30)
# 添加按钮
button=tkinter.Button(root,text="立即检测",bg="#00B42A",fg="#fff",width="30",relief="flat",command=result)
# 这里将按钮放置在主窗口的底部
button.pack(padx=50,pady=50)
root.mainloop()