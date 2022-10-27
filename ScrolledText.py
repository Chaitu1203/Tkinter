from textwrap import wrap
import tkinter
from tkinter import ttk
from tkinter import scrolledtext
from turtle import width
window=tkinter.Tk()
window.geometry("600x600")


ttk.Label(window,text="scrolled text",background="blue",foreground="white",font=("Times new Roman",15)).grid(column=1,row=0)

#Scrolled Text
text1=scrolledtext.ScrolledText(window,wrap=tkinter.WORD,width=20,height=10)
text1.grid(column=0,pady=10,padx=10)
text1.focus()
window.mainloop()