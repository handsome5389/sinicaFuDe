
def set_module():
    import tkinter as tk
    from datetime import datetime
    from tkinter import messagebox
    from tkinter import DISABLED
    from tkinter import NORMAL
    import 編碼器
    from 收據系統 import menu
    window = tk.Tk()
    window.title("中 研 福 德 宮")
    window.geometry("500x350+400+150")
    window.iconbitmap("Puyma32x32.ico")
    window.resizable(0,0) #限制視窗縮放 0= true ,1 = fals 
    window.config(bg="skyblue")
    window.attributes("-topmost",1) #置頂 0= true ,1 = fals
    label_head = tk.Label(window,text="設 定 使 用 者",font=("標楷體",30,'bold'),
                    fg='#000',bg="skyblue" ,pady=2,padx=5)      
    set_lab1 = tk.Label(window,bg='#f50', relief='raised',pady=2,padx=5, text="  建檔日期  ",font=("Arial",14,'bold'),fg='#fff')   
    set_lab1_1 = tk.Label(window, text=str(datetime.today())[0:10],font=("Arial",14,'bold'),
                        bg="gray72",relief='raised',pady=2, padx=7)   
    set_lab2 = tk.Label(window,text="    使用者    ",font=("Arial",14,'bold'),
                    fg='#fff',bg='#f50',relief='raised',pady=2,padx=5) 
    # limits = tk.Label(window,text="操作員",font=("Arial",14,'bold'),
                    #   width=5,fg='#fff',bg='gray72',relief='raised',pady=4,padx=3)                                                
    set_lab3 = tk.Label(window,text="   密碼(一)   ",
                    font=("Arial",14,'bold'),fg='#fff',bg='#f50',
                    relief='raised', pady=2, padx=5)       
    set_lab4 = tk.Label(window,text="   密碼(二)   ",font=("Arial",14,'bold'),
                    fg='#fff', bg='#f50', relief='groove',pady=2,padx=5)                 
    set_lab5 = tk.Label(window,text="操作修改與刪除、先輸入使用者再按<Enter>鍵 !",
                    font=("Arial",12,'bold'),fg='#f00',relief='raised', padx=5,pady=2)               
    label_copyright = tk.Label(window,text="Copyright © 2022 Puyuma Workshop ",
                    font=("Arial",8,'bold'),bg="skyblue" ,padx=1,pady=1)
    a = tk.StringVar()
    b = tk.StringVar()
    c = tk.StringVar()
    a.set("操作員")    
    b.set("")
    c.set("")
    user_name=tk.Entry(window, font=('Arial',14,'bold'),width=8,border=1,bd =5)
    limits = tk.Entry(window, textvariable=a,font=('Arial',14,'bold'),width=6,border=1,bd =5)
    password1=tk.Entry(window, textvariable=b,font=('Arial',14,'bold'),width=15,border=1,bd =5)
    password2=tk.Entry(window, textvariable=c,font=('Arial',14,'bold'),width=15,border=1,bd =5)

    def add_btn():
        check = 0
        with open("password.txt", mode="r",encoding="UTF-8") as f:
                for line in f.readlines():
                    if  user_name.get() == (line.split(','))[2]:
                        check =1
                        tk.messagebox.showerror('錯誤訊息', '使用者已存在')
                        user_name.delete(0,'end')
                        print(check)
                        break
        while check ==0:              
            if user_name.get() =="":
                tk.messagebox.showerror('錯誤訊息', '使用者不可空白')
                break
            if password1.get() =="" or password2.get() =="":
                print(check)
                tk.messagebox.showerror('錯誤訊息', '密碼不可空白')
                break
            if password1.get() != password2.get() :
                tk.messagebox.showerror('錯誤訊息', '兩次密碼輸入不同')
                password1.delete(0,'end')
                password2.delete(0,'end')
                break
            else:
                with open("password.txt", mode="a",encoding="UTF-8") as f:
                        f.write(str(datetime.today())[0:10] + "," + limits.get() +"," + user_name.get() + "," + 編碼器.encode(password1.get()) +"," + str(datetime.today())+",\n") 
                        tk.messagebox.showinfo('提醒訊息', '新增使用者成功')
                        user_name.delete(0,'end')
                        password1.delete(0,'end')
                        password2.delete(0,'end')                
            break               
                    
    def mod_btn():
        check = 0
        if  password1.get() =="" or password2.get() =="":
            tk.messagebox.showerror('錯誤訊息', '密碼不可空白')
            check = 1
        elif user_name.get() ==""and check == 0:
            tk.messagebox.showerror('錯誤訊息', '使用者不可空白')   
        elif  password1.get() != password2.get() and check == 0:
            tk.messagebox.showerror('錯誤訊息', '兩次密碼輸入不同')
            password1.delete(0,'end')
            password2.delete(0,'end')
        
        else:
            file_data = "" 
            with open("password.txt", mode="r",encoding="UTF-8") as f:
                for line in f:
                    print(password1.get())
                    if user_name.get() == line.split(",")[2]:
                        line = line.split(",")[0]+","+line.split(",")[1]+","+line.split(",")[2]+","+編碼器.encode(password1.get())+"," + str(datetime.today())+",\n"
                        file_data += line
                        print("1")
                    else:    
                        file_data += line
                        print("2")
            print(file_data)
            with open("password.txt", mode="w",encoding="UTF-8") as f:
                f.write(file_data)
            tk.messagebox.showinfo('提醒訊息', '密碼修改成功')
            user_name.delete(0,'end')
            password1.delete(0,'end')
            password2.delete(0,'end')
            set_add_btn['state'] = NORMAL

    def del_btn():
        file_data = "" 
        with open("password.txt", mode="r",encoding="UTF-8") as f:
            for line in f:
                if user_name.get() == line.split(",")[2]:
                    result = tk.messagebox.askokcancel('提醒訊息', '是否確定刪除使用者')
                else:    
                    file_data += line
            if result:           
                with open("password.txt", mode="w",encoding="UTF-8") as f:
                    f.write(file_data)
                    tk.messagebox.showinfo('提醒訊息', '使用者刪除成功')
        
            user_name.delete(0,'end')
            password1.delete(0,'end')
            password2.delete(0,'end')
            set_add_btn['state'] = NORMAL

    def set_modify(event):     
        set_add_btn['state'] = DISABLED    
        #set_add_btn(state=DISABLED)
        with open("password.txt", mode="r+",encoding="UTF-8") as f:
            for line in f.readlines():
                mod_line = line.split(',')
                if user_name.get() == mod_line[2]:
                    set_lab1_1.config(text=(mod_line[0]))
                    a.set(mod_line[1])
                    b.set(編碼器.decode(mod_line[3]))
                    c.set(編碼器.decode(mod_line[3]))
                    break
            else: 
                tk.messagebox.showerror('錯誤訊息', '使用者不存在')
                user_name.delete(0,'end')
                password1.delete(0,'end')
                password2.delete(0,'end')   
                set_add_btn['state'] = NORMAL

    def ending():
        window.destroy()
        menu()

    user_name.bind('<Return>',set_modify)

    set_add_btn = tk.Button(window,text="新 增",font=('Arial',14,'bold'),
                    padx=2,pady=2,activeforeground='#f00',command=add_btn) 
    set_mod_btn = tk.Button(window,text="修 改",font=('Arial',14,'bold'),
                    padx=2,pady=2,activeforeground='#f00', command=mod_btn)      
    set_del_btn = tk.Button(window,text="刪 除",font=('Arial',14,'bold'),
                    padx=2,pady=2,activeforeground='#f00', command=del_btn)
    ending_btn = tk.Button(window,text="離  開",font=('Arial',12,'bold'),
                    fg="white",bg="blue",activeforeground='#f00',command=ending) 

    label_head.place(x=100,y=5)
    set_lab1.place(x=100, y=70)
    set_lab1_1.place(x=233, y=70)
    set_lab2.place(x=100, y=110)
    user_name.place(x=230, y=110)
    limits.place(x=330, y=111)
    set_lab3.place(x=100, y=150)
    password1.place(x=230, y=150)
    set_lab4.place(x=100, y=190)
    password2.place(x=230, y=190)
    set_lab5.place(x=70, y=240)
    set_add_btn.place(x=140, y=280)
    set_mod_btn.place(x=220, y=280)
    set_del_btn.place(x=300, y=280)
    ending_btn.place(x=40, y=300)
    label_copyright.place(x=295, y=332)
    window.mainloop()

if __name__ == "__main__":
    set_module()