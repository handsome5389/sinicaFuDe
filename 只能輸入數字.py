# def f( x ):
#   print( "pressed" )
# element.bind( "<Return>", f )



import tkinter as tk

def validate(P):
    #print(P)
    if str.isdigit(P) or P == '':
        return True
    else:
        return False
        
root = tk.Tk()
root.title('my window')

mylabel = tk.Label(root, text='input:')
mylabel.pack(side=tk.LEFT)

vcmd = (root.register(validate), '%P')
myentry = tk.Entry(root, validate='key', validatecommand=vcmd)
myentry.pack(side=tk.LEFT)

root.mainloop()