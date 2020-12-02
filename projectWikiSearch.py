import tkinter as tk
import wikipedia
from tkinter import messagebox
root = tk.Tk()
root.geometry('600x650')
root.config(background = 'Grey')
root.title('WikiSearch')
tk.Label(text = "Enter you search ",font = "Times 20 bold",bg = 'Grey').pack(pady = 5)
var = tk.StringVar()
def searchh():
    string = var.get()
    text.delete(1.0,'end')
    try:
        text.insert('insert',wikipedia.summary(string))
    except:
        text.insert('insert','please check your string or internet connection')
    var.set("")

def show():
    tk.messagebox.showinfo('credits','special thanks to the creater')
    root.destroy()



e = tk.Entry(font ="fantasy,25,bold",width = 35,textvariable = var)
e.pack(pady = 5)
b = tk.Button(text = 'Search',font ="fantasy 10 bold",width = 12,command = searchh)
b.pack(pady = 5)
f = tk.Frame(root,bg = 'blue')
f.pack(pady = 5)
scrollbar = tk.Scrollbar(f)
scrollbar.pack(side = 'right',fill = 'y')
text = tk.Text(f,yscrollcommand = scrollbar.set,wrap = 'word',font ="monospace 10 italic",bg = 'White',fg = 'Black')
scrollbar.config(command = text.yview)
text.pack()
button= tk.Button(text = 'Quit',font ="fantasy 10 bold",width = 12,command = show)
button.pack(pady = 5,side = 'left')
root.mainloop()
