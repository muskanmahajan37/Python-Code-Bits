from tkinter import *
root= Tk()
root.title("calculator")
root.geometry("300x300")
label1 = Label(root, text="Write Here")
label1.grid(row=0, column=0)
label2 = Label(root, text="Write Again")
label2.grid(row =1, column=0)
entry1= Entry(root)
entry2=Entry(root)
entry1.grid(row=0, column=0)
entry2.grid(row=1, column=0)
button=Button(root, text = "Click Here")
button.grid(row =2, column=0)
check = Checkbutton(root, text="Mark a tick Here")
check.grid(row=2, column=1)
radio = Radiobutton(root, text= "Press Here")
radio.grid(row=3, column=0)
root.mainloop()