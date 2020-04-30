
import tkinter as tk
password='123456'
user='admin'
def func():    
    if en1.get()=='123456':
       btn1.config(bg='green')
    if en2.get()=='admin':
        btn1.config(bg='red')
 
win = tk.Tk()
lb1=tk.Label(win,text='User name:')
lb2=tk.Label(win,text='Password:')
btn1=tk.Button(win,text='login')
en1=tk.Entry(win)
en2=tk.Entry(win)
lb1.pack()
en1.pack()
lb2.pack()
en2.pack()
btn1.pack()
s1=tkinter.StringVar()
s1=tkinter.StringVar()

btn1.pack()
if btn1.config(enable):
    func()

