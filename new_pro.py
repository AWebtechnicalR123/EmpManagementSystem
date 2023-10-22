from cProfile import label
import tkinter as tk
import mysql.connector
from tkinter import *

class Employee:
    def __init__(self, root):
        self.root=root ## declarartion
        self.root.geometry("1535x790+0+0") ##0 and 0 are starting x,y
        self.root.title('Employe Management System')

        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='pink') #bd means border, relief is for border style
        img_frame.place(x=0,y=0,width=1530,height=780) #to show frame

        #HOME button
        login_id=Button(img_frame, text="HOME",width=18,font=('arial',11,"bold"),bg="blue").grid(row=0,column=0,pady=5)

        #sign up button
        Button(img_frame, text="Sign Up",width=18,font=('arial',11,"bold"),bg="blue").grid(row=0,column=1,pady=5)

        #login button
        Button(img_frame, text="Login",width=18,font=('arial',11,"bold"),bg="blue").grid(row=0,column=2,pady=5)







## close the window
if __name__=="__main__":
    root=Tk()
    obj=Employee(root) ## object of class type
    root.mainloop()