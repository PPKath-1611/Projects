from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import pymysql

class ConnectorDB:
    def __init__(self, root):
        self.con = pymysql.connect(host='localhost', 
                                     port=3306,
                                     user='root', 
                                     password='pranesh@2001',
                                     database='inventory')
        self.root = root
        titlespace = "  "
        self.root.title(55 * titlespace + "Inventory Control Management System")
        self.root.geometry("980x700+30+0")
        self.root.resizable(width=False, height=False)

        MainFrame = Frame(self.root, bd = 10, width = 950, height = 700, relief = RIDGE, bg = "yellow")
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd = 7, width = 950, height = 100, relief = RIDGE, bg = "gold")
        TitleFrame.grid(row = 0, column = 0)

        TopFrame3 = Frame(MainFrame, bd = 6, width = 950, height = 500, relief = RIDGE)
        TopFrame3.grid(row = 1, column = 0)

        LeftFrame = Frame(TopFrame3, bd = 6, width = 950, height = 400, padx = 2, bg="gold", relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame, bd = 6, width = 500, height = 150, padx = 12, pady = 5, relief = FLAT)
        LeftFrame1.pack(side=TOP)

        RightFrame1 = Frame(TopFrame3, bd = 6, width = 100, height = 400, padx = 2, bg = "gold", relief = RIDGE)
        RightFrame1.pack(side = RIGHT)
        RightFrame2 = Frame(RightFrame1, bd = 6, width = 180, height = 300, padx = 2, pady = 2, relief = RIDGE)
        RightFrame2.pack(side = TOP)
        #-----------------------------------------------------------------------------------------------------------#

        CustomerName = StringVar()
        Username = StringVar()
        Password = StringVar()
        Mobileno = StringVar()
        Address = StringVar()
        Signedin = StringVar()
        Cust_ID = StringVar()

        #-----------------------------------------------------------------------------------------------------------#
        
        def iExit():
                iExit = tkinter.messagebox.askyesno("ICMS", "Confirm you want to exit ??")
                if iExit > 0:
                        root.destroy()
                return
        
        def Reset():
                self.entCustomerName.delete(0, END)
                self.entUsername.delete(0, END)
                self.entPassword.delete(0, END)
                self.entMobile.delete(0, END)
                self.entAddress.delete(0, END)
       
        def Insert():
                if CustomerName.get() == "" or Username.get() == "" or Password.get() == "":
                        tkinter.messagebox.askyesno("Insertion Error", "Enter Required Details Please")
                else:
                        cur = self.con.cursor()
                        cur.execute("insert into Customer(Cust_name, username, user_password, mobile, address, signedin) values(%s, %s, %s, %s, %s, now())",(
                                CustomerName.get(),
                                Username.get(),
                                Password.get(),
                                Mobileno.get(),
                                Address.get()
                        )) # Creating a cursor object
                        self.con.commit()
                        print("Customer Data saved to Database")
                Reset()

        def Display():
                cur = self.con.cursor()
                cur.execute("select * from Customer");
                result = cur.fetchall()
                if len(result) != 0:
                        self.student_records.delete(*self.student_records.get_children())
                        for row in result:
                                self.student_records.insert('', END, values = row)
                self.con.commit()

        def Tap_View(ev):
                viewinfo = self.student_records.focus()
                usedata = self.student_records.item(viewinfo)
                row = usedata['values']
                CustomerName.set(row[1]),
                Username.set(row[2]),
                Password.set(row[3]),
                Mobileno.set(row[4]),
                Address.set(row[5]),

        def Update():
                cur = self.con.cursor()
                cur.execute("update Customer set Cust_name=%s, username=%s, user_password=%s, address=%s where mobile = %s",(
                CustomerName.get(),
                Username.get(),
                Password.get(),
                Address.get(),
                Mobileno.get(),  
                ))
                self.con.commit()
                Display()
                tkinter.messagebox.showinfo("ICMS", "Record Updated Succesfully")
                Reset()

        def Delete():
                cur = self.con.cursor()
                cur.execute("delete from customer where Cust_Name=%s", CustomerName.get())
                self.con.commit()
                Display()
                tkinter.messagebox.showinfo("ICMS", "Record Successfully Deleted")
                Reset()

        def Search():
                try:
                        cur = self.con.cursor()
                        cur.execute("select * from Customer where username=%s and user_password=%s", (Username.get(), Password.get()))
                        result = cur.fetchall()
                        if len(result) != 0:
                            self.student_records.delete(*self.student_records.get_children())
                        for row in result:
                                self.student_records.insert('', END, values = row)
                        self.con.commit()
                except:
                        tkinter.messagebox.showinfo("ICMS", "No results found !!")
                        Reset()
        #-----------------------------------------------------------------------------------------------------------#

        self.lbltitle = Label(TitleFrame, font=('arial', 34, 'bold'), text="Inventory Control Management", bd = 7, bg="gold")
        self.lbltitle.grid(row = 0, column = 0, padx = 132)

        self.lblCustomerName = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Cust Name :", bd = 7)
        self.lblCustomerName.grid(row = 1, column = 0, sticky=W, padx=5)
        self.entCustomerName = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd = 5, width = 44, justify='left', textvariable=CustomerName)
        self.entCustomerName.grid(row = 1, column = 1, sticky=W, padx=5)

        self.lblUsername = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Username :", bd = 7)
        self.lblUsername.grid(row = 2, column = 0, sticky=W, padx=5)
        self.entUsername = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd = 5, width = 44, justify='left', textvariable=Username)
        self.entUsername.grid(row = 2, column = 1, sticky=W, padx=5)

        self.lblPassword = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Password :", bd = 7)
        self.lblPassword.grid(row = 3, column = 0, sticky=W, padx=5)
        self.entPassword = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd = 5, width = 44, justify='left', textvariable=Password, show="*")
        self.entPassword.grid(row = 3, column = 1, sticky=W, padx=5)

        self.lblMobile = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Mobile no :", bd = 7)
        self.lblMobile.grid(row = 4, column = 0, sticky=W, padx=5)
        self.entMobile = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd = 5, width = 44, justify='left',  textvariable=Mobileno)
        self.entMobile.grid(row = 4, column = 1, sticky=W, padx=5)
        
        self.lblAddress = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Address :", bd = 7)
        self.lblAddress.grid(row = 5, column = 0, sticky=W, padx=5)
        self.entAddress = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd = 5, width = 44, justify='left', textvariable=Address)
        self.entAddress.grid(row = 5, column = 1, sticky=W, padx=5)

# ------------------------------------TABLE TREEVIEW------------------------------------------------------   #

        self.student_records = ttk.Treeview(LeftFrame, height = 15, columns=("Cust_ID", "Cust_Name", "Username", "Password", "Mobile", 
        "Address", "LoginTime"))

        scroll_y = ttk.Scrollbar(LeftFrame, orient=VERTICAL, command = self.student_records.yview)
        scroll_y.pack(side=RIGHT, fill="y")

        scroll_x = ttk.Scrollbar(LeftFrame, orient=HORIZONTAL, command = self.student_records.xview)
        scroll_x.pack(side=BOTTOM, fill="x")

        self.student_records.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

        self.student_records.heading("Cust_ID", text="Cust_ID") 
        self.student_records.heading("Cust_Name", text="Customer Name")
        self.student_records.heading("Username", text="Username")
        self.student_records.heading("Password", text="Password")
        self.student_records.heading("Mobile", text="Mobile")
        self.student_records.heading("Address", text="Address")
        self.student_records.heading("LoginTime", text="SignedIn")

        self.student_records['show'] = 'headings'
        
        self.student_records.column("Cust_ID", width=70, minwidth = 150)
        self.student_records.column("Cust_Name", width = 100, minwidth = 150)
        self.student_records.column("Username", width = 80, minwidth = 150)
        self.student_records.column("Password", width = 80, minwidth = 150)
        self.student_records.column("Mobile", width = 80, minwidth = 150)
        self.student_records.column("Address", width = 100, minwidth = 150)
        self.student_records.column("LoginTime", width = 100, minwidth = 150)

        self.student_records.pack(fill = BOTH, expand = 1)
        self.student_records.bind("<ButtonRelease-1>",Tap_View)
        #Display()

# ------------------------------------  BUTTONS -----------------------------------------------------#

        self.InsertBtn = Button(RightFrame2, font=('arial', 16, 'bold'), text="Insert", bd = 4, pady = 1, padx = 24, 
        width=8, height = 2, command = Insert).grid(row=0, column=0, padx=1)

        self.DisplayBtn = Button(RightFrame2, font=('arial', 16, 'bold'), text="Display", bd = 4, pady = 1, padx = 24, 
        width=8, height = 2, command = Display).grid(row=1, column=0, padx=1)

        self.UpdateBtn = Button(RightFrame2, font=('arial', 16, 'bold'), text="Update", bd = 4, pady = 1, padx = 24, 
        width=8, height = 2, command = Update).grid(row=2, column=0, padx=1)

        self.DeleteBtn = Button(RightFrame2, font=('arial', 16, 'bold'), text="Delete", bd = 4, pady = 1, padx = 24, 
        width=8, height = 2, command = Delete).grid(row=3, column=0, padx=1)

        self.SearchBtn = Button(RightFrame2, font=('arial', 16, 'bold'), text="Search", bd = 4, pady = 1, padx = 24, 
        width=8, height = 2, command = Search).grid(row=4, column=0, padx=1)

        self.ResetBtn = Button(RightFrame2, font=('arial', 16, 'bold'), text="Reset", bd = 4, pady = 1, padx = 24, 
        width=8, height = 2, command = Reset).grid(row=5, column=0, padx=1)

        self.ExitBtn = Button(RightFrame2, font=('arial', 16, 'bold'), text="EXIT", bd = 4, pady = 1, padx = 24, 
        width=8, height = 2, command = iExit).grid(row=6, column=0, padx=1)



if __name__ == '__main__':
    root = Tk()
    application = ConnectorDB(root)
    root.mainloop()