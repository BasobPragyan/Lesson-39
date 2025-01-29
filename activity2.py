from tkinter import*
root=Tk()
root.title("Login App")
root.geometry("400x400")
frame=Frame(master=root,height=200,width=360,bg="#d0efff")
lab1=Label(frame,text="Full Name",bg="#3895D3",fg="white",width=12)
lab2=Label(frame,text="Email Id",bg="#3895D3",fg="white",width=12)
lab3=Label(frame,text="Email Password",bg="#3895D3",fg="white",width=12)
name_entry=Entry(frame)
email_entry=Entry(frame)
pass_entry=Entry(frame,show="*")
def display():
    name=name_entry.get()
    greet="Hey!"+name
    message="\nCongrats for your new account!"
    textbox.insert(END,greet)
    textbox.insert(END,message)

textbox=Text(bg="#BEBEBE",fg="black")
button=Button(text="Create account",command=display,bg="red")
frame.place(x=20,y=0)
lab1.place(x=20,y=20)
name_entry.place(x=150,y=20)
lab2.place(x=20,y=80)
email_entry.place(x=150,y=80)
lab3.place(x=20,y=140)
pass_entry.place(x=150,y=140)
button.place(x=130,y=210)
textbox.place(y=250)

root.mainloop()