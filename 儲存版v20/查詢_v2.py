#if __name__ == "__main__":
def inq_module():
    import tkinter as tk
    from openpyxl import load_workbook
    import functions.收據編號產生器 as 收據編號產生器
    from datetime import datetime
    import 數字轉換器 as converter
    from 輸出列表機 import printing
    from tkinter import messagebox
    from tkinter import DISABLED
    from tkinter import NORMAL
    from 收據系統 import menu
    window = tk.Tk()
    window.title("中 研 福 德 宮")
    window.geometry("650x450+300+150")
    window.iconbitmap("Puyma32x32.ico")
    window.resizable(0,0) #限制視窗縮放 0= true ,1 = fals 
    window.config(bg="skyblue")
    window.attributes("-topmost",1) #置頂 0= true ,1 = fals
    label_head = tk.Label(window,text="查  詢  記  錄",font=("標楷體",24,'bold'),
                    fg='#000',bg="#FFFFCC" ,relief="ridge",pady=2,padx=5)      
    inq_lab1 = tk.Label(window,text="  收據編號  ",font=("Arial",14,'bold'),
                    fg='#fff',bg='#f50',relief="raised",pady=2,padx=5,)      
    inq_lab2 = tk.Label(window, text="  捐款日期  ",font=("Arial",14,'bold'),
                    fg='#fff',bg='#f50', relief="raised",pady=2,padx=5)               
    inq_lab2_1 = tk.Label(window,font=("Arial",14,'bold'),relief="raised",
                    width=9,pady=2, padx=5,bg="gray72",fg="blue")            
    inq_lab3 = tk.Label(window,text="  付  款  人  ",font=("Arial",14,'bold'),
                    fg='#fff',bg='#f50',relief="raised", pady=2, padx=5)                       
    inq_lab3_1 = tk.Label(window,font=("Arial",14,'bold'),relief="sunken",
                    width=32,pady=2,padx=5,bg="gray72",fg="blue")    
    inq_lab4 = tk.Label(window,text="  地        址  ",font=("Arial",14,'bold'),
                    fg='#fff',bg='#f50',relief="raised", pady=2, padx=5)     
    inq_lab4_1 = tk.Label(window,font=("Arial",14,'bold'),relief="sunken",
                    width=32,pady=2,padx=5,bg="gray72",fg="blue")    
    inq_lab5 = tk.Label(window,text="  收款性質  ",font=("Arial",14,'bold'),
                    fg='#fff',bg='#f50',relief="raised", pady=2, padx=5)  
    inq_lab5_1 = tk.Label(window,font=("Arial",14,'bold'),relief="sunken",
                    width=15,pady=2,padx=5,bg="gray72",fg="blue")                      
    inq_lab6 = tk.Label(window,text="  付款金額  ",font=("Arial",14,'bold'),
                    fg='#fff',bg='#f50',relief="raised", pady=2, padx=5)
    inq_lab6_1 = tk.Label(window,font=("Arial",14,'bold'),relief="sunken",
                    width=9,pady=2,padx=5,bg="gray72",fg="blue")    
    inq_lab7 = tk.Label(window,text="  經  手  人  ",font=("Arial",14,'bold'),
                    fg='#fff',bg='#f50',relief="raised", pady=2, padx=5) 
    inq_lab7_1 = tk.Label(window,font=("Arial",14,'bold'),relief="raised",
                    width=9,pady=2,padx=5,bg="gray72",fg="blue")                  
    inq_lab8 = tk.Label(window,text="    負責人    ",font=("Arial",14,'bold'),
                    fg='#fff', bg='#f50', relief="raised",pady=2,padx=5)   
    inq_lab8_1 = tk.Label(window,font=("Arial",14,'bold'),
                    width=9,relief="raised",pady=2, padx=5,bg="gray72",fg="blue") 
    inq_lab9 = tk.Label(window,text="  會        計  ",font=("Arial",14,'bold'),
                    fg='#fff', bg='#f50', relief="raised",pady=2,padx=5)   
    inq_lab9_1 = tk.Label(window,font=("Arial",14,'bold'),
                    width=9,relief="raised",pady=2, padx=5,bg="gray72",fg="blue") 
    inq_lab10 = tk.Label(window,text="  註 記  ",font=("Arial",14,'bold'),
                    fg='#fff', bg='#f50', relief="raised",pady=2,padx=5) 
    inq_lab10_1 = tk.Label(window,font=("Arial",14,'bold'),
                    width=5,relief="raised",pady=2, padx=5,bg="gray72",fg="red")                                                              
    label_copyright = tk.Label(window,text="Copyright © 2022 Puyuma Workshop ",font=("Arial",8,'bold'),
                    bg="skyblue" ,padx=1,pady=1) 

    def inq(event):     
        with open("捐款記錄.txt", mode="r+",encoding="UTF-8") as f:
            for line in f.readlines():
                if entry1.get() == line.split(',')[0]:
                    inq_lab2_1.config(text=line.split(',')[1])
                    inq_lab3_1.config(text=(line.split(',')[2]))
                    inq_lab4_1.config(text=(line.split(',')[3]))
                    inq_lab5_1.config(text=(line.split(',')[4]))
                    inq_lab6_1.config(text=(line.split(',')[5]))
                    inq_lab7_1.config(text=(line.split(',')[6]))
                    inq_lab8_1.config(text=(line.split(',')[7]))
                    inq_lab9_1.config(text=(line.split(',')[8]))
                    inq_lab10_1.config(text=line.split(',')[9])
                    inq_btn['state'] = NORMAL #<Return>按下後、開啟<查詢另一筆>功能
                    break
            else: 
                tk.messagebox.showerror('錯誤訊息', '單據編號不存在')
                entry1.delete(0,'end')
                inq_lab2_1.config(text="")
                inq_lab3_1.config(text="")
                inq_lab4_1.config(text="")
                inq_lab5_1.config(text="")
                inq_lab6_1.config(text="")
                inq_lab7_1.config(text="")
                inq_lab8_1.config(text="")
                inq_lab9_1.config(text="")
                inq_lab10_1.config(text="")

    a1 = tk.StringVar()
    a1.set("")   
    def up(event):
        a1.set("0"+str(int(entry1.get())+1))
        inq(event)
    def down(event):
        a1.set("0"+str(int(entry1.get())-1))
        inq(event)              
    def clickbton():
        entry1.delete(0,'end')
        inq_lab2_1.config(text="")
        inq_lab3_1.config(text="")
        inq_lab4_1.config(text="")
        inq_lab5_1.config(text="")
        inq_lab6_1.config(text="")
        inq_lab7_1.config(text="")
        inq_lab8_1.config(text="")
        inq_lab9_1.config(text="")
        inq_lab10_1.config(text="")
        inq_btn['state'] = DISABLED #暫時關閉<查詢另一筆>功能，避免與<Return>衝突
    def ending():
        window.destroy()
        menu()

    entry1=tk.Entry(textvariable=a1,font=('Arial',14,'bold'),width=10,border=1,bd=5)
    entry1.bind('<Return>',inq)
    entry1.bind('<Up>',up)
    entry1.bind('<Down>',down)

    inq_btn = tk.Button(window,text="查詢另一筆",font=('Arial',14,'bold'),
                    padx=2,pady=2,activeforeground='#f00', command=clickbton)  
                  
    inq_btn['state'] = DISABLED #暫時關閉<查詢另一筆>功能，避免與<Return>衝突                

    ending_btn = tk.Button(window,text="離  開",font=('Arial',12,'bold'),
                    fg="white",bg="blue",activeforeground='#f00',command=ending)
    label_head.place(x=200,y=5)
    inq_lab1.place(x=340, y=65)
    entry1.place(x=472, y=62)
    inq_lab2.place(x=70, y=65)
    inq_lab2_1.place(x=200, y=65)
    inq_lab3.place(x=70, y=110)
    inq_lab3_1.place(x=200, y=110)
    inq_lab4.place(x=70, y=150)
    inq_lab4_1.place(x=200, y=150)
    inq_lab5.place(x=70, y=190)
    inq_lab5_1.place(x=200, y=190)
    inq_lab6.place(x=70, y=230)
    inq_lab6_1.place(x=200, y=230)
    inq_lab7.place(x=70, y=270)
    inq_lab7_1.place(x=200, y=270)
    inq_lab8.place(x=345, y=270)
    inq_lab8_1.place(x=475, y=270)
    inq_lab9.place(x=345, y=230)
    inq_lab9_1.place(x=475, y=230)
    inq_lab10.place(x=430, y=190)
    inq_lab10_1.place(x=524, y=190)
    inq_btn.place(x=260, y=350)
    ending_btn.place(x=40, y=400)
    label_copyright.place(x=430, y=430)
    window.mainloop()

if __name__ == "__main__":
    inq_module()
