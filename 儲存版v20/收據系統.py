def menu():
    import shutil
    from datetime import datetime
    import tkinter as tk
    from tkinter import messagebox
    from tkinter import DISABLED
    import 編碼器 
    from 新增_v2 import add_module
    from 查詢_v2 import inq_module
    from 修改_v2 import mod_module
    from 設定 import set_module
    window = tk.Tk()
    window.title("Puyuma Workshop")
    window.geometry("500x350+400+150")
    window.iconbitmap("image\Puyma32x32.ico")
    window.resizable(0,0) #限制視窗縮放 0= true ,1 = fals 
    window.config(bg="skyblue")
    window.attributes("-topmost",1) #置頂 0= true ,1 = fals
    def add():
        window.destroy()
        add_module()
    def inq():
        window.destroy()
        inq_module()
    def mod():
        window.destroy()
        mod_module()
    def setup():
        window.destroy()
        set_module()
    def ending():
        try:
            shutil.copy('./database/捐款記錄.txt','e:./record_backup')
        except:
            pass
        m_lab_head.destroy()
        m_btn1.destroy()
        m_btn2.destroy()
        m_btn3.destroy()
        m_btn4.destroy()
        m_btn5.destroy()
        label1= tk.Label(window,text="謝謝使用收據管理統",font=("標楷體",22,'bold'),
                relief="ridge",fg='#000',bg="#FFFFCC" ,pady=2,padx=5) 
        label1.place(x=100,y=80) 
        label2= tk.Label(window,text="Puyuma workshop全體員工敬呈 中研福德宮",font=("標楷體",16,'bold'),
                relief="ridge",fg='#000',bg="#FFFFCC" ,pady=2,padx=5) 
        label2.place(x=20,y=200) 
        window.after(3000, window.destroy)
    
    def now_user(): #找出目前使用者
        time2 = ""
        adm =""
        with open("./database/password.txt", mode="r",encoding="UTF-8") as f:
                    for line in f.readlines():
                        time1 = (line.split(','))[4]
                        if time2 < time1:
                            time2 = time1
                            last_user = (line.split(','))[2]  
                            adm =   (line.split(','))[1]                
        return last_user,adm

    m_lab_head = tk.Label(window,text="中研福德宮收款管理系統",font=("標楷體",26,'bold'),
                    fg='#000',bg="skyblue" ,pady=2,padx=5)
    label_copyright = tk.Label(window,text="Copyright © 2023 Puyuma Workshop ",
                    font=("Arial",8,'bold'),bg="skyblue" ,padx=1,pady=1)
    m_btn1 = tk.Button(window,text="新              增",font=('Arial',16,'bold'),
                    padx=25,pady=0,bg='#f50',activeforeground='#f00',command=add)
    m_btn2 = tk.Button(window,text="查              詢",font=('Arial',16,'bold'),
                    padx=25,pady=0,bg='#f50',activeforeground='#f00',command=inq)
    m_btn3 = tk.Button(window,text="修              改",font=('Arial',16,'bold'),
                    padx=25,pady=0,bg='#f50',activeforeground='#f00',command=mod)
    m_btn4 = tk.Button(window,text="設              定",font=('Arial',16,'bold'),
                    padx=25,pady=0,bg='#f50',activeforeground='#f00',command=setup)  
    m_btn5 = tk.Button(window,text="離              開",font=('Arial',16,'bold'),
                    padx=25,pady=0,bg='#f50',activeforeground='#f00',command=ending) 
 
    
    if super_adm != "admin":
        if now_user()[1] == "負責人":
            #m_btn1['state'] = DISABLED
            m_btn3['state'] = DISABLED
            m_btn4['state'] = DISABLED
        elif now_user()[1] == "操作員":
            m_btn2['state'] = DISABLED
            m_btn3['state'] = DISABLED
            m_btn4['state'] = DISABLED

    m_lab_head.place(x=35,y=5)
    m_btn1.place(x=145, y=60)
    m_btn2.place(x=145, y=110)
    m_btn3.place(x=145, y=160)
    m_btn4.place(x=145, y=210)
    m_btn5.place(x=145, y=260)
    label_copyright.place(x=295, y=332)
    window.mainloop()

super_adm = ""

if __name__ == "__main__":
    import os
    from datetime import datetime
    import tkinter as tk
    from tkinter import messagebox
    import 編碼器
  
    def end():
        window.destroy()

    def verify():
        global super_adm
        if log_user_name.get() =="handsome" and log_password.get() =="emily540120":
            super_adm = "admin"
        #if log_user_name.get() =="handsome5389" and log_password.get() =="emily540120":
            lab_head.destroy()
            log_lab1.destroy()
            log_lab2.destroy()
            log_user_name.destroy()
            log_password.destroy()
            log_btn.destroy()
            window.destroy()
            menu()
        else:   
            file_data = ""
            check = 0
            if log_user_name.get() =="" or log_password.get() =="":
                tk.messagebox.showerror('錯誤訊息', '使用者與密碼不可空白')
                log_user_name.delete(0,'end')
                log_password.delete(0,'end')
                check =1
            with open("./database/password.txt", mode="r+",encoding="UTF-8") as f:
                for line in f.readlines():
                    if  log_user_name.get() == (line.split(','))[2] and 編碼器.encode(log_password.get()) == (line.split(','))[3] :
                        check =1
                        with open("./database/password.txt", mode="r",encoding="UTF-8") as f:
                            for line in f:
                                if log_user_name.get() == line.split(",")[2]:              
                                    line = line.split(",")[0]+","+line.split(",")[1]+","+line.split(",")[2]+","+line.split(",")[3]+","+str(datetime.today())+",\n"
                                    file_data += line
                                else:     
                                    file_data += line
                        with open("./database/password.txt", mode="w",encoding="UTF-8") as f:
                            f.write(file_data)
                        # lab_head.destroy()
                        # log_lab1.destroy()
                        # log_lab2.destroy()
                        # log_user_name.destroy()
                        # log_password.destroy()
                        # log_btn.destroy()
                        window.destroy()
                        menu()
                        break  
            if check == 0:           
                tk.messagebox.showerror('錯誤訊息', '使用者或密碼錯誤')
                log_user_name.delete(0,'end')
                log_password.delete(0,'end')
        return  
    window = tk.Tk()
    window.title("Puyuma Workshop")
    window.geometry("500x350+400+150")
    window.iconbitmap("image\Puyma32x32.ico")
    window.resizable(0,0) #限制視窗縮放 0= true ,1 = fals 
    window.config(bg="skyblue")
    window.attributes("-topmost",1) #置頂 0= true ,1 = fals


    lab_head = tk.Label(window,text="收 據 系 統 登 入",font=("標楷體",30,'bold'),
                    fg='#000',bg="skyblue" ,pady=2,padx=5)
    label_copyright = tk.Label(window,text="Copyright © 2023 Puyuma Workshop ",
                    font=("Arial",8,'bold'),bg="skyblue" ,padx=1,pady=1)
    log_lab1 = tk.Label(window,text="    使 用 者    ", font=("Arial",16,'bold'),
    fg='#fff',bg='#f50',relief='raised', pady=5, padx=5)                              
    log_lab2 = tk.Label(window,text="    密     碼     ", font=("Arial",16,'bold'),
    fg='#fff',bg='#f50',relief='raised', pady=5, padx=5)                   
    log_user_name=tk.Entry(window,font=('Arial',16,'bold'),width=15,relief="sunken",border=1,bd =5)
    log_password=tk.Entry(window,show="*",font=('Arial',16,'bold'),width=15,relief="sunken",border=1,bd =5)
    log_btn = tk.Button(window,text="登  入",font=('Arial',16,'bold'),
                    padx=2,pady=0,activeforeground='#f00',command=verify)
    end_btn = tk.Button(window,text="離  開",font=('Arial',16,'bold'),
                padx=2,pady=0,activeforeground='#f00',command=end)             

    lab_head.place(x=70,y=5)
    log_lab1.place(x=70, y=100)
    log_user_name.place(x=240, y=100)
    log_lab2.place(x=70, y=160)
    log_password.place(x=240, y=160)
    log_btn.place(x=300, y=250)
    end_btn.place(x=120, y=250)
    label_copyright.place(x=295, y=332)
    window.mainloop()


