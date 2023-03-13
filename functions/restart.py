
def restart():
    rst=str(input("需要繼續作業嗎? Y/N: "))
    if rst == "Y":
        main()
    elif rst == "N":
        exit()
    else:
        print("Invaild Input")
        restart()

def restart_all():
   
   exec('香油錢練習.py')

restart_all()