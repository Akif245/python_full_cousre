from tkinter import *
window=Tk()
window.title("Tkinter window")
window.minsize(width=500,height=500)


l1=Label(text="This is a lable",font=("Arial ",20 ,"bold"))
l1.pack()

l1["text"]="New text"
l1.config(text="New text ")

def button():
    print("I got clicked")
    l1.config(text=input.get())
btn=Button(text="Click me",command=button)
btn.pack()
input=Entry(width="20")
input.pack()












window.mainloop()


