from sqlite3 import PARSE_DECLTYPES
from tkinter import *
from functools import partial

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

#window
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Regigster it')

img_frame=Frame(tkWindow,bd=2,relief=RIDGE,bg='pink') #bd means border, relief is for border style
img_frame.place(x=0,y=0,width=1530,height=780) #to show frame

#username label and text entry box
usernameLabel = Label(img_frame, text="User Name",font=('arial',11,'bold'),bg='pink').grid(row=0, column=0, sticky=W)
username = StringVar()
usernameEntry = Entry(img_frame, textvariable=username,width=22,font=('arial',11,"bold")).grid(row=0, column=1)  

#Gmail label and text entry box
usernameLabel = Label(img_frame, text="Gmail",font=('arial',11,'bold'),bg='pink').grid(row=1, column=0, sticky=W)
username = StringVar()
usernameEntry = Entry(img_frame, textvariable=username,width=22,font=('arial',11,"bold")).grid(row=1, column=1)  

#password label and password entry box
passwordLabel = Label(img_frame,text="Password",font=('arial',11,'bold'),bg='pink').grid(row=2, column=0, sticky=W)  
password = StringVar()
passwordEntry = Entry(img_frame, textvariable=password, show='*',width=22,font=('arial',11,"bold")).grid(row=2, column=1)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(img_frame, text="Sign Up", command=validateLogin,width=18,font=('arial',11,"bold"),bg="blue").grid(row=5,column=0,pady=5)

tkWindow.mainloop()