
def readlastnline(frame,n):
    with open("./database/record.txt", mode="r", encoding="utf-8-sig") as f:
        for line in (f.readlines()[-n:]):
            print(line)
            return line
data = readlastnline("捐款記錄.txt",1)
print(data[0:7])