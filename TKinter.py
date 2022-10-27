#GUI def:
"""GUI ,is a type of user interfae that allows to intract with electronic devices throughgraphical icons and visual indicators"""

#Tkinter :
"""def :tkinter in python GUI programming is standard python GUI library it gives us an object-orinted interface to the Tkinter GUI toolkit
tel:tkinter is a inbulit python module used to create simply gui AppSearch"""

import tkinter
from tkinter import *
from tkinter import messagebox 

window = tkinter.Tk()
window.geometry("600x600")


#label
#label=tkinter.Label(window,text="chaitnya").pack()


#button
b = Button(window,text="subscribe",fg="red",bg="white")
b.grid(column=1,row=0)

#radio button
r=Radiobutton(window,text="python",value=1)
r.grid(column=2,row=1)
r1=Radiobutton(window,text="django",value=2)
r1.grid(column=2,row=2)
r2=Radiobutton(window,text="mysql",value=3)
r2.grid(column=2,row=3)

#Entry
e=Entry(window,width=60)
e.grid(column=3,row=0)


#meaasgebox
def Button1():
    messagebox.showinfo("status","do subscribe")

b=Button(window,text="python life",command=Button1).pack()
window.mainloop()

#CheckButton
c=StringVar()
c = Checkbutton(window,text='select',var=c)
c.grid(column=0,row=0)
window.mainloop()


#spinBox
s=Spinbox(window,from_=0,to=100,width=50)
s.grid(column=0,row=0)
window.mainloop()
