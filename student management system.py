from tkinter import *
from tkinter import ttk
from mysql.connector import connection

class student:
    def __init__(self,root):
        self.root = root
        self.root.title("STUDENT MANAGEMENT SYSTEM")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="STUDENT MANAGEMENT SYSTEM",bd=10,relief=GROOVE,font=("times new roman",40,"normal"),bg="orange",fg="blue")
        title.pack(side=TOP,fill=X)

        #---------ALL VARIABLES-----------

        self.Roll_No_Var=StringVar()
        self.name_Var=StringVar()
        self.email_Var=StringVar()
        self.gender_Var=StringVar()
        self.contact_Var=StringVar()
        self.dob_Var=StringVar()

        #----------MANAGE FRAME-----------

        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=580)

        m_title=Label(Manage_Frame,text="Manage Students",bg="crimson",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)



        lbl_roll=Label(Manage_Frame,text="ROll No.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_Roll=Entry(Manage_Frame,textvariable=self.Roll_No_Var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        

        
        lbl_name=Label(Manage_Frame,text="Name.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_name=Entry(Manage_Frame,textvariable=self.name_Var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        

        lbl_email=Label(Manage_Frame,text="email.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_email=Entry(Manage_Frame,textvariable=self.email_Var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        

        lbl_gender=Label(Manage_Frame,text="Gender",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_Var,font=("times new roman",13,"bold"),state = "readonly")
        combo_gender['values']=("Male","Female","Others")
        combo_gender.grid(row=4,column=1,pady=10,padx=20)
        

        lbl_contact=Label(Manage_Frame,text="Contact",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_contact=Entry(Manage_Frame,textvariable=self.contact_Var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")


        lbl_dob=Label(Manage_Frame,text="D.O.B",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        txt_dob=Entry(Manage_Frame,textvariable=self.dob_Var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")


        
        lbl_adress=Label(Manage_Frame,text="Adress",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_adress.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        self.txt_adress=Text(Manage_Frame,width=30,height=3,font=("bold",10))
        self.txt_adress.grid(row=7,column=1,pady=10,padx=20,sticky="w")

        


         #----------BUTTON FRAME-----------

        btn_Frame = Frame(Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=10,y=510,width=420)

        Addbtn=Button(btn_Frame,text="Add",width=10,command = self.add_students).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(btn_Frame,text="Update",width=10).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(btn_Frame,text="Delete",width=10).grid(row=0,column=2,padx=10,pady=10)
        clearbtn=Button(btn_Frame,text="Clear",width=10).grid(row=0,column=3,padx=10,pady=10)



        
        #----------DETAIL FRAME-----------

        Detail_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=500,y=100,width=800,height=560)

        lbl_search=Label(Detail_Frame,text="Search by:",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,width=10,font=("times new roman",13,"bold"),state = "readonly")
        combo_search['values']=("Roll N0.","Name","Contact")
        combo_search.grid(row=0,column=1,padx=20,pady=10)

        txt_search=Entry(Detail_Frame,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn=Button(Detail_Frame,text="Search",width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame,text="Show All",width=10,pady=5).grid(row=0,column=4,padx=10,pady=10)



        #----------TABLE FRAME--------------

        Table_Frame = Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=70,width=760,height=480)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("roll","name","email","gender","contact","dob","adress"))
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command = self.Student_table.xview)
        scroll_y.config(command = self.Student_table.yview)
        self.Student_table.heading("roll",text="Roll NO.")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="email")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("dob",text="D.O.B")
        self.Student_table.heading("adress",text="Adress")
        self.Student_table['show']='headings'
        self.Student_table.column("roll",width = 100)
        self.Student_table.column("name",width = 100)
        self.Student_table.column("email",width = 100)
        self.Student_table.column("gender",width = 100)
        self.Student_table.column("contact",width = 100)
        self.Student_table.column("dob",width = 100)
        self.Student_table.column("adress",width = 150)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.fetch_data()


    def add_students(self):
        cnx = connection.connect(host = "local host",user = "root",password = "",database = "students",port = "3306")
        cur = connection.cursor()
        cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                        self.name_var.get(),
                                                                        self.email_var.get(),
                                                                        self.gender_var.get(),
                                                                        self.contact_var.get(),
                                                                        self.dob_var.get(),
                                                                        self.txt_Adress.get('1.0',END)
                                                                        ))
        cnx.commit()
        self.fetch_data()
        connection.close()

    def fetch_data(self):
        cnx = connection.connect(host = "local host",user = "root",password = "",database = "students",port = "3306")
        cur = connection.cursor()
        cur.execute("select * from student")
        rows = cur.fetchall()
        if len(rows)!= 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values = row)
            connection.commit()
        cnx.close()

        
  




root = Tk()
ob = student(root)
root.mainloop
