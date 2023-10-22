# from http import server
from tkinter import* #give all data which is requirement from tkinter
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import date

class Employee:
    def __init__(self, root):
        self.root=root ## declarartion
        self.root.geometry("1535x790+0+0") ##0 and 0 are starting x,y
        self.root.title('Employe Management System')

        # variables for talking the data from entry fields and combobox
        self.var_dep=StringVar() #global variable
        self.var_name=StringVar()
        self.var_designition=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_married=StringVar()
        self.var_dob=StringVar()
        self.var_idproofcomb=StringVar()
        self.var_idproof=StringVar()
        self.var_gender=StringVar()
        self.var_doj=StringVar()
        self.var_phone=StringVar()
        self.var_country=StringVar()
        self.var_city=StringVar()
        self.var_salary=StringVar()



        #making Label of Titile
        lbl_title=Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM',font=('times new roman',37,'bold'),fg='darkblue',bg='white') #title is made on the root, 38 is font_size
        lbl_title.place(x=0,y=0,width=1530,height=50) #to show tile on the screen

        # img_logo=Image.open('college_images/emplogo.png')
        img_logo=Image.open('index1.png') #opening the logo
        img_logo=img_logo.resize((50,50),Image.ANTIALIAS) #ANTIALIAS converts image in low level
        self.photo_logo=ImageTk.PhotoImage(img_logo) #self is due to the variable in the class can be used inside class

        #show logo with title by button or Label
        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=270,y=0,width=50,height=50) #stXpoint,stYpoint,

        #making the frame for appending images
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white') #bd means border, relief is for border style
        img_frame.place(x=0,y=50,width=1530,height=160) #to show frame

        #1st Image
        img1=Image.open('college_images/e1.png')
        img1=img1.resize((540,160),Image.ANTIALIAS) #Antilise converts image in low level
        self.photo1=ImageTk.PhotoImage(img1) #self is due to the variable can be used with class

        #show image1 by button or Label
        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=540,height=160)

        #2nd Image
        img2=Image.open('college_images/e2.png')
        img2=img2.resize((540,160),Image.ANTIALIAS) #Antilise converts image in low level
        self.photo2=ImageTk.PhotoImage(img2) #self is due to the variable can be used with class

        #show image2 by button or Label
        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=540,y=0,width=540,height=160)

        #3rd Image
        img3=Image.open('college_images/e3.jpg')
        img3=img3.resize((540,160),Image.ANTIALIAS) #Antilise converts image in low level
        self.photo3=ImageTk.PhotoImage(img3) #self is due to the variable can be used with class

        #show logo in title by button or Labelimg_frame
        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=1000,y=0,width=540,height=160)

        #Main Frame
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=220,width=1500,height=575)
        
        # Upper Frame
        upper_frame=LabelFrame(Main_frame,bd=2,bg='white',relief=RIDGE,text="Employee Information",font=('times new roman',11,'bold'),fg='red')
        upper_frame.place(x=10,y=10,width=1480,height=270)

        #place is used when we don't know where we need to place.
        #grid is used when we know where we need to place
        # Labels and Entry fields for Department
        lbl_dep=Label(upper_frame,text='Department',font=('arial',11,'bold'),bg='white')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W) #sticky is used to stick at West

        #combo Box For Department
        combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep,font=('arial',11,'bold'),width=17,state='readonly') #readonly because we can't edit
        combo_dep['value']=('Select Department','HR','Software Engineer','Manager',) #giving values in combobox
        combo_dep.current(0) #starting potion 0
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Name
        lbl_Name=Label(upper_frame,font=('arial',11,'bold'),text="Name:",bg='white')
        lbl_Name.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=('arial',11,"bold"))
        txt_name.grid(row=0,column=3,padx=2,pady=7)

        # lbl_Designition
        lbl_Designition=Label(upper_frame,font=('areal',12,'bold'),text='Designition:',bg='white');
        lbl_Designition.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_Designition=ttk.Entry(upper_frame,textvariable=self.var_designition,width=22,font=('areal',11,'bold'))
        txt_Designition.grid(row=1,column=1,sticky=W,padx=2,pady=7)

        # Address
        lbl_Address=Label(upper_frame,font=('areal',12,'bold'),text='Address:',bg='white');
        lbl_Address.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=('areal',11,'bold'))
        txt_address.grid(row=2,column=1,sticky=W,padx=2,pady=7)

        # Date of Birth
        lbl_DateOfBirth=Label(upper_frame,font=('areal',12,'bold'),text='Date of Birth:',bg='white')
        lbl_DateOfBirth.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        # txt_designi=ttk.Entry(upper_frame,textvariable=self.var_dob,width=22,font=('areal',11,'bold'))
        # txt_designi.grid(row=3,column=1,sticky=W,padx=2,pady=7)
        txt_designi=DateEntry(upper_frame,selectmode='day',textvariable=self.var_dob,width=20,font=('areal',11,'bold'))
        txt_designi.grid(row=3,column=1,sticky=W,padx=2,pady=7)
        dt=date(2022,10,8)
        txt_designi.set_date(dt)

        #Id Proof
        #combobox for ID Proof
        combo_IdP=ttk.Combobox(upper_frame,textvariable=self.var_idproofcomb,font=('arial',12,"bold"),width=17,state='readonly') #readonly because we can't edit
        combo_IdP['value']=('Select Id Proof','Aadhar Card','Voter Id','Pan Card','Passport','Bank Passbook') #giving values in combobo
        combo_IdP.current(0) #starting position 0\
        combo_IdP.grid(row=4,column=0,sticky=W,padx=2,pady=7)

        txt_idproof=ttk.Entry(upper_frame,textvariable=self.var_idproof,width=22,font=('areal',11,'bold'))
        txt_idproof.grid(row=4,column=1,sticky=W,padx=2,pady=7)

        # Email
        lbl_Email=Label(upper_frame,font=('areal',12,'bold'),text='Email:',bg='white')
        lbl_Email.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_email=ttk.Entry(upper_frame,textvariable=self.var_email,width=22,font=('areal',11,'bold'))
        txt_email.grid(row=1,column=3,sticky=W,padx=2,pady=7)
        
        # Marital Status
        lbl_Marital=Label(upper_frame,font=('areal',12,'bold'),text='Marital Status:',bg='white')
        lbl_Marital.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        #combo Box for Maretial Status
        combo_mar=ttk.Combobox(upper_frame,textvariable=self.var_married,font=('arial',11,'bold'),width=17,state='readonly') #readonly because we can't edit
        combo_mar['value']=('Select Gender', 'Single/Unmarried', 'married', 'Widow', 'Divorced', 'Separated', 'Others') #giving values in combobox
        combo_mar.current(0) #starting position 0
        combo_mar.grid(row=2,column=3,padx=2,pady=10,sticky=W)

        # gender
        lbl_Gender=Label(upper_frame,font=('areal',12,'bold'),text='Gender:',bg='white')
        lbl_Gender.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_gender=ttk.Entry(upper_frame,textvariable=self.var_gender,width=22,font=('areal',11,'bold'))
        txt_gender.grid(row=3,column=3,sticky=W,padx=2,pady=7)

        # Date of Joining Proof
        lbl_DOJ=Label(upper_frame,font=('areal',12,'bold'),text='Date of Joining:',bg='white')
        lbl_DOJ.grid(row=4,column=2,sticky=W,padx=2,pady=7)

        # txt_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,width=22,font=('areal',11,'bold'))
        # txt_doj.grid(row=4,column=3,sticky=W,padx=2,pady=7)
        txt_doj=DateEntry(upper_frame,selectmode='day',textvariable=self.var_dob,width=20,font=('areal',11,'bold'))
        txt_doj.grid(row=4,column=3,sticky=W,padx=2,pady=7)
        dt=date(2022,10,8)
        txt_doj.set_date(dt)

        # Phone
        lbl_Phone=Label(upper_frame,font=('areal',12,'bold'),text='phone:',bg='white')
        lbl_Phone.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_phone=ttk.Entry(upper_frame,textvariable=self.var_phone,width=22,font=('areal',11,'bold'))
        txt_phone.grid(row=0,column=5,sticky=W,padx=2,pady=7)

        # Country
        lbl_Country=Label(upper_frame,font=('areal',12,'bold'),text='Country:',bg='white')
        lbl_Country.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_country=ttk.Entry(upper_frame,textvariable=self.var_country,width=22,font=('areal',11,'bold'))
        txt_country.grid(row=1,column=5,sticky=W,padx=2,pady=7)

        #City
        lbl_City=Label(upper_frame,font=('areal',12,'bold'),text='City:',bg='white')
        lbl_City.grid(row=2,column=4,sticky=W,padx=2,pady=7)

        txt_city=ttk.Entry(upper_frame,textvariable=self.var_city,width=22,font=('areal',11,'bold'))
        txt_city.grid(row=2,column=5,sticky=W,padx=2,pady=7)

        # CTC
        lbl_CTC=Label(upper_frame,font=('areal',12,'bold'),text='CTC:',bg='white');
        lbl_CTC.grid(row=3,column=4,sticky=W,padx=2,pady=7)

        txt_ctc=ttk.Entry(upper_frame,textvariable=self.var_salary,width=22,font=('areal',11,'bold'))
        txt_ctc.grid(row=3,column=5,sticky=W,padx=2,pady=7)

        # mask Image
        img_mask=Image.open('college_images/maskface.webp')
        img_mask=img_mask.resize((220,220),Image.ANTIALIAS)
        self.photomask=ImageTk.PhotoImage(img_mask)

        self.img_mask=Label(upper_frame,image=self.photomask)
        self.img_mask.place(x=1000,y=0,width=220,height=220)


        #Button Frame
        Button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        Button_frame.place(x=1290,y=20,width=170,height=210)

        # save button
        btn_add=Button(Button_frame,text="Save",command=self.add_data,font=('arial',15,'bold'),width=13,bg="blue",fg='white') # add_data is function name for saving the data
        btn_add.grid(row=0,column=0,padx=1,pady=5)

        # save button
        btn_update=Button(Button_frame,text="Update",command=self.update_data,font=('arial',15,'bold'),width=13,bg="blue",fg='white')
        btn_update.grid(row=1,column=0,padx=1,pady=5)

        # save button
        btn_delete=Button(Button_frame,text="Delete",command=self.delete_data,font=('arial',15,'bold'),width=13,bg="blue",fg='white')
        btn_delete.grid(row=2,column=0,padx=1,pady=5)

        # save button
        btn_clear=Button(Button_frame,text="Clear",command=self.reset_data,font=('arial',15,'bold'),width=13,bg="blue",fg='white')
        btn_clear.grid(row=3,column=0,padx=1,pady=5)


        # Down Frame
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text="Employee Information",font=('times new roman',11,'bold'),fg='red')
        down_frame.place(x=10,y=280,width=1480,height=285)

        # Search Frame
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white',text="Search Employee Information",font=('times new roman',11,'bold'),fg='red')
        search_frame.place(x=0,y=0,width=1470,height=70)

        # Search By Label
        lbl_search=Label(search_frame,font=('arial',11,'bold'),text='Search By',fg='white',bg='red')
        lbl_search.grid(row=0,column=0,sticky=W,padx=5)

        # Search By Type :Combobox
        self.var_com_search=StringVar()
        comb_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,state='readonly',font=('arial',11,"bold"),width=15)
        comb_search['value']=('Select to search','Phone','ID_Proof_No')
        comb_search.current(0) #starting place 0
        comb_search.grid(row=0,column=1,sticky=W,padx=5)

        # Search By number
        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,font=('arial',11,'bold'))
        txt_search.grid(row=0,column=2,sticky=W,padx=5)

        # Search Button
        btn_search=Button(search_frame,command=self.search_data,font=('arial',15,'bold'),text='Search',fg='white',bg='blue',width=14)
        btn_search.grid(row=0,column=3,sticky=W,padx=5)

        # Show All button
        btn_ShowAll=Button(search_frame,command=self.fetch_data,font=('arial',15,'bold'),text='Show All',fg='white',bg='blue',width=14)
        btn_ShowAll.grid(row=0,column=4,sticky=W,padx=5)

        # stau at Home
        lbl_stayhome=Label(search_frame,text='Wear a mask',font=('times new roman',30,'bold'),bg='white') #title is made on the root, 38 is font_size
        lbl_stayhome.place(x=790,y=0,width=600,height=30)

        # # inserting masked picture
        img_logo_mask=Image.open("college_images/maskface.webp")
        img_logo_mask=img_logo_mask.resize((50,50),Image.ANTIALIAS)
        self.photoimg_logo_mask=ImageTk.PhotoImage(img_logo_mask) #t this variable can be used in any where

        self.logo=Label(search_frame,image=self.photoimg_logo_mask)
        self.logo.place(x=900,y=0,width=50,height=50)

        # ================ Employee Table ==============================
        # Table Frame for Employee details
        table_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text="Details of Employee",font=('times new roman',11,'bold'),fg='red')
        table_frame.place(x=0,y=72,width=1470,height=185)

        # making scroll bars
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL) # Horizontal
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL) # Vertical 

        # make dummy variables for table
        self.employee_table=ttk.Treeview(table_frame,column=('dep','name','degi','email','address','married','dob','doj','idproofcomb','idproof','gender','phone','country','city','salary',),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)  #dummy name

        scroll_x.pack(side=BOTTOM,fill=X) # it fills the text in x diection
        scroll_y.pack(side=RIGHT,fill=Y)  # it fills text in the y diection

        scroll_x.config(command=self.employee_table.xview) #used for seeing the x view
        scroll_y.config(command=self.employee_table.yview) #used for seeing the y view

        #column names(headings) for Employee table
        self.employee_table.heading('dep',text='Department')
        self.employee_table.heading('name',text='Name')
        self.employee_table.heading('degi',text='Degination')
        self.employee_table.heading('email',text='Email')
        self.employee_table.heading('address',text='Address')
        self.employee_table.heading('married',text='Marital Status')
        self.employee_table.heading('dob',text='DOB')
        self.employee_table.heading('doj',text='DOJ')
        self.employee_table.heading('idproofcomb',text='ID Type')
        self.employee_table.heading('idproof',text='ID Proof No')
        self.employee_table.heading('gender',text='Gender')
        self.employee_table.heading('phone',text='phone')
        self.employee_table.heading('country',text='Country')
        self.employee_table.heading('city',text='City')
        self.employee_table.heading('salary',text='CTC')

        # Show the employee table
        self.employee_table['show']='headings'

        # seeting the colmns and removing the blank space
        self.employee_table.column('dep',width=100)
        self.employee_table.column('name',width=100)
        self.employee_table.column('degi',width=100)
        self.employee_table.column('email',width=100)
        self.employee_table.column('address',width=100)
        self.employee_table.column('married',width=100)
        self.employee_table.column('dob',width=100)
        self.employee_table.column('doj',width=100)
        self.employee_table.column('idproofcomb',width=100)
        self.employee_table.column('idproof',width=100)
        self.employee_table.column('gender',width=100)
        self.employee_table.column('phone',width=100)
        self.employee_table.column('country',width=100)
        self.employee_table.column('city',width=100)
        self.employee_table.column('salary',width=100)

        #setting the table columns in both sides
        self.employee_table.pack(fill=BOTH,expand=1)
        #bind the table i.e. getting the data into input field by clicking on data row
        self.employee_table.bind("<ButtonRelease>",self.get_curosor)

        # call function for fetching the data from data base
        self.fetch_data()

        ######################################## Designing Part completed ############################
    ######################################## Action Part Below ###################################
    # Function declaration
    def add_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="": #get for getting the data
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                # conn=mysql.connector.connect(host='localhost',username='root',password='Password@123',database='new_projectdbemp')
                conn=mysql.connector.connect(host='localhost',username='root',password='Password@123',database='mydata') #connecting python to database
                my_cursor=conn.cursor() #making cursor for data adding
                my_cursor.execute('insert into temp values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                    self.var_dep.get(),
                    self.var_name.get(),
                    self.var_designition.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_married.get(),
                    self.var_dob.get(),
                    self.var_doj.get(),
                    self.var_idproofcomb.get(),
                    self.var_idproof.get(),
                    self.var_gender.get(),
                    self.var_phone.get(),
                    self.var_country.get(),
                    self.var_city.get(),
                    self.var_salary.get(),
                )) #executing the sql qwery
                conn.commit()
                conn.close()
                self.fetch_data() #for immidiate getting data in employee_table
                messagebox.showinfo('Success','Employee has been added!',parent=self.root)
            except Exception as er:
                messagebox.showerror('Error',f'Due to: {str(er)}',parent=self.root)
    
    #fetch data from database
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Password@123',database='mydata')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from temp')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i)
            conn.commit() #commit means update
        conn.close()

    # Get cursor
    def get_curosor(self,event=""):#event is variable it can be anything
        cursor_row=self.employee_table.focus() #focus to table
        content=self.employee_table.item(cursor_row)
        data=content['values']
        #variables to bind
        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_designition.set(data[2])
        self.var_email.set(data[3])
        self.var_address.set(data[4])
        self.var_married.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7])
        self.var_idproofcomb.set(data[8])
        self.var_idproof.set(data[9])
        self.var_gender.set(data[10])
        self.var_phone.set(data[11])
        self.var_country.set(data[12])
        self.var_city.set(data[13])
        self.var_salary.set(data[14])
    
    #update data
    def update_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="": #get for getting the data
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                update=messagebox.askyesno('Update','Are you sure to update this employee data')
                if update>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='Password@123',database='mydata') #connecting python to database
                    my_cursor=conn.cursor() #making cursor for data adding
                    my_cursor.execute('update temp set Department=%s,Name=%s,Designition=%s,Email=%s,Address=%s,Marital_Status=%s,DOB=%s,DOJ=%s,ID_Type=%s,Gender=%s,Phone=%s,Country=%s,City=%s,Salary=%s where ID_Proof_No=%s',(
                        self.var_dep.get(),
                        self.var_name.get(),
                        self.var_designition.get(),
                        self.var_email.get(),
                        self.var_address.get(),
                        self.var_married.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_idproofcomb.get(),
                        self.var_gender.get(),
                        self.var_phone.get(),
                        self.var_country.get(),
                        self.var_city.get(),
                        self.var_salary.get(),
                        self.var_idproof.get(),
                    ))
                else:
                    if not update:
                        return
                conn.commit() #update
                self.fetch_data()
                conn.close()
                messagebox.showinfo('success','Employee Successfully updated',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f"Due To:{str(es)}",parent=self.root)
        
    #delete
    def delete_data(self):
        if self.var_idproof.get()=="":
            messagebox.showerror('Error',"All fields are required")
        else:
            try:
                Delete=messagebox.askyesno('Delete','Are you sure delete this employeee',parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='Password@123',database='mydata') #connecting python to database
                    my_cursor=conn.cursor() #making cursor for data adding
                    sql='delete from temp where Id_Proof_No=%s'
                    value=(self.var_idproof.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Delete','Employee Successfully Deleted',parent=self.root)
                self.reset_data()
            except Exception as es:
                messagebox.showerror('Error',f"Due To:{str(es)}",parent=self.root)
            
    #reset
    def reset_data(self):      
        Clear=messagebox.askyesno('Clear','Are you sure to clear this employee data')      
        self.var_dep.set("Select Department")
        self.var_name.set("")
        self.var_designition.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_married.set("Married")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_idproofcomb.set("Select Id Proof")
        self.var_idproof.set("")
        self.var_gender.set("")
        self.var_phone.set("")
        self.var_country.set("")
        self.var_city.set("")
        self.var_salary.set("")

    #search function for search the data
    def search_data(self):
        if self.var_com_search.get()=='' or self.var_search.get()=='':
            messagebox.showerror('Error','Please select option')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Password@123',database='mydata') #connecting python to database
                my_cursor=conn.cursor() #making cursor for data adding
                # my_cursor.execute('select * from temp where ' +  str(self.var_com_search.get()) + '=' + str(self.var_search.get())) #if unique value
                my_cursor.execute('select * from temp where ' + str(self.var_com_search.get()) +" LIKE'%"+ str(self.var_search.get() +"%'")) #mysql qwery
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("",END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error',f"Due To:{str(es)}",parent=self.root)


        
        



    
        
        

        





## close the window
if __name__=="__main__":
    root=Tk()
    obj=Employee(root) ## object of class type
    root.mainloop()
