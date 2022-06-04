import tkinter
import tkinter as tk
import webbrowser
from tkinter import messagebox

def result(msg):
    messagebox.showinfo(title='温馨提示', message=msg)

def enter():
    qes = question.get()
    if qes=="":
        result('问题不能为空')
    else:
        webbrowser.open('https://www.baidu.com/s?wd=' + str(qes))

window=tk.Tk()
window.geometry("500x300")
window.configure(background="#f0f0f0")
window.title('万能百事通-[云物缭绕]')

l1 = tk.Label(text="请输入你要提问的问题", fg="black",font=('Label', 13 , "bold")).place(x = 150, y = 50)
window.resizable(width=False, height=False)

question=tk.Entry()
question.place(x=150, y=80)

btn=tk.Button(text='点击获取解答',command=enter).place(x = 150, y = 120)



window.mainloop()