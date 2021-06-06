from tkinter import *
from tkinter import messagebox
import os
from elevate import elevate
from selenium import webdriver

from control_browser import cb

import sys

elevate() 
#함수파트

#주요 변수
path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
block_list = "C:\\Users\\user\\Desktop\\opensc\\block_list.txt"
origin_list = "C:\\Users\\user\\Desktop\\opensc\\hosts_origin.txt"
first_1 = True

global python_site_list #파이썬 내부에서 관리할 코드
python_site_list = []
global origin_host
origin_host = []

# browser=webdriver.Chrome('../chromedriver')

# print(browser.title)

def start():
    print("실행")
    with open(path, 'r+') as file: 
            content = file.read() 
            for site in python_site_list: 
                if site in content: 
                    pass
                else:
                    file.write(redirect + " " + site + "\n")
def end():
    print("중지")
    with open(path, 'w+') as file:
        file.writelines(origin_host) 
        

def add():
    try:
        ia = input_address.get()
        if ia != '':
            listbox.insert(END,ia)
            with open(block_list,'a') as banlist:
                banlist.write(ia+"\n")
            print("추가")
            input_address.delete(0,END)
    except:
        pass
    else:
        pass
def delete():
    try:
        seleted_one = listbox.get(listbox.curselection())
        print(seleted_one)
        listbox.delete(listbox.curselection())
        python_site_list.remove(seleted_one)
        print(python_site_list)
        with open(block_list,'w') as banlist:
            banlist.writelines(python_site_list)
            print("삭제")
    except:    
        pass
    else:
        pass
def on_closing():
    if messagebox.askokcancel("종료", "종료 하시겠습니까?"):
        root.destroy()


#tkinter 스펙
root = Tk()
root.title("Block website")
root.geometry("460x380+100+200")
root.resizable(False, False)
#차단할 주소 입력
label_address = Label(root,text="차단할 주소 :")
label_address.place(x=10, y=45)
input_address = Entry(root,width=38)
input_address.place(x=90, y=45)

#추가,삭제 버튼
b_add = Button(root, text="추가",command=add)
b_add.pack()
b_add.place(x=380, y=20,width=70, height=70)

b_delete = Button(root, text="삭제",command=delete)
b_delete.pack()
b_delete.place(x=380, y=120,width=70, height=170)

#스크롤바 리스트박스 프레임
frame = Frame(root, width=40,height=13)
frame.pack()
frame.place(x=8,y=100)

#스크롤바
scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

#리스트박스
listbox = Listbox(frame, selectmode='single', width=45, height=13,yscrollcommand=scrollbar.set)
listbox.pack()
listbox.place()

scrollbar.config(command=listbox.yview)

if first_1 == True:
    #차단리스트 불러와서 초기 모습 설정하기
    f=open("block_list.txt",'r')
    while True:
        line = f.readline()
        if not line: 
            break
        python_site_list.append(line)
        listbox.insert(END,line)  
    f.close()
    first_1 = False
    print(python_site_list) 
    with open(origin_list, 'r+') as origin:
        origin_host = origin.readlines()

#실행중지 버튼
b_go = Button(root, text="실행",command=start)
b_go.pack()
b_go.place(x=150,y=320,width=70,height=50)
b_stop = Button(root, text="중지",command=end) #실행함수와 중지함수 만들 것
b_stop.pack()
b_stop.place(x=250,y=320,width=70,height=50)


root.protocol("WM_DELETE_WINDOW", on_closing)#이게 중요함
root.mainloop()
