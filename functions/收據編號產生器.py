# 收據編號產生器(檢查記錄檔是否存在,新檔案,空檔案存入起始序號,跳過記錄空行)

from datetime import datetime
import os

# 讀最後一筆紀錄收據編號
def lastline(n):
    with open("./database/record.txt", mode="r+", encoding="utf-8-sig") as f:
        d_data = f.readlines()[-n]
        return d_data

#檢查檔案是否存在，不存在,創新檔
path="./database/record.txt"
ifExist=os.path.exists(path)
if ifExist==False:
    open("./database/record.txt", mode="at+")
else:    
    pass

# 判斷是否是空檔,產生起始序號
n = 1
#print(lastline(n))
size = os.path.getsize("./database/record.txt")
#print(str(datetime.today())[1:4])
if size < 10:
    now_year = str(datetime.today())[1:4]
    #now_month = datetime.today().strftime("%m")
    ser_No = "0" + str(now_year)+"00000"

else: #跳過空行,找出最後一行
    while str(lastline(n)) =='\n':
        n += 1
    ser_No = str(lastline(n)[0:8])
    # print("2")
    # print(ser_No)
    # print(type(ser_No))

# 找出今天年與月,產生新序號
def ser_create(ser_No):  
    from datetime import datetime
    # print(str(datetime.today())[1:4])
    now_year = int(str(datetime.today())[1:4])
    ser_year = int(ser_No[1:3])
    # print(f"now_year = {now_year}")
    # print(f"ser_year = {ser_year}")
    if now_year > ser_year:
        ser_No =  "0" +str( now_year)+"00001"
        #print(ser_No)
    # elif now_month > ser_month:
    #     ser_No = int(str(now_year)+str(now_month)+"001")
    else :
        ser_No = "0" + str(int(ser_No) +1)
    return ser_No

new_ser_No = ser_create(ser_No)
#print(f"收據編號 : {new_ser_No}")