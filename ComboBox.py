import tkinter
from tkinter import ttk
from tkinter.font import names
window=tkinter.Tk()
window.geometry("600x600")


ttk.Label(window,text="python life",background="blue",foreground="white",font=("Times new Roman",15)).grid(column=1,row=0)


##combobox
c=tkinter.StringVar()
names=ttk.Combobox(window,width=27,textvariable=c)
names['values']=("chaitanya",
                    "luke",
                    "someone")
names.grid(column=2,row=3)
names.current()
window.mainloop()