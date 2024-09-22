from tkinter import *
from PIL import Image ,ImageTk
from tkinter import messagebox
from tkinter import ttk 
import sqlite3
import random
from time import strftime
from datetime import datetime 

width = 1305
height = 555

bd = 4
relief = RIDGE
font = "times new roman"
fontSize = 14
bg = "black"
fg = "gold"


class RoomBooking:
    def __init__(self , root):
        self.root = root
        self.root.title("Hotel Management System")
        #   Center The Screen
        screen_width=root.winfo_screenwidth()
        screen_height=root.winfo_screenheight()
        x=int((screen_width - width)/2) 
        y=int((screen_height-height)/2)
        self.root.geometry(f"{width}x{height}+{x+112}+{y+105}")

        #varabiles
        
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()
        ###################### title #####################
        lbl_title = Label(self.root , text="RoomBooking DETAILS" , font=(font , 18 , "bold") , bg=bg , fg=fg, bd=bd, relief=relief)
        lbl_title.place(x=0,y=0,width=width,height=50)
           #      #######3v logo image ////////////////////////
        img2 = Image.open(r"hotel images\logohotel.png")
        # img2 = img2.resize((100, 40),Image.Resampling.LANCZOS)
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbiimg = Label(self.root, image=self.photoimg2 , bd=0 , relief=relief)
        lbiimg.place(x=5,y=2,width=100,height=40)

        #####################labelframe##########################3
        
        labelframeleft=LabelFrame(self.root, bd=2 , relief=relief , text="ROOMBOOKING Details" , font=(font , 12 , "bold") , padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)
        
        
        #################### label and entry #######################
        ###Customer Concat
        lbl_Cust_contact = Label(labelframeleft , text="Customer Contact"  , font=("Arial"  , 12 , "bold") , padx=2 , pady=6)
        lbl_Cust_contact.grid(row=0 , column= 0 , sticky=W) # sticky − What to do if the cell is larger than widget

        entry_contact = ttk.Entry(labelframeleft ,width=27 ,textvariable=self.var_contact ,font=("Arial"  , 13 , "bold"))
        entry_contact.grid(row=0 , column= 1, sticky=W)
        
        #fetch data button 
        btn_fetch= Button(labelframeleft, text="fetch Data",command=self.Fetch_contact ,width=8 , font=("Arial" , 8, "bold") , bg="black" , fg="gold")
        btn_fetch.place(x=347,y=4)
        
        #check in date 
        check_in_date =Label(labelframeleft,font =("arial",12,"bold"),  text ="check in date:",padx=2 , pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,font =("arial",12,"bold"),width=27)
        txtcheck_in_date.grid(row=1,column=1)

        #check out date
        lbl_check_out =Label(labelframeleft,font =("arial",12,"bold"),text ="check out date:",padx=2 , pady=6)
        lbl_check_out.grid(row=2,column=0,sticky=W)
        txt_check_out_date=ttk.Entry(labelframeleft,textvariable=self.var_checkout,font =("arial",12,"bold"),width=27)
        txt_check_out_date.grid(row=2,column=1)

        #room type 
        label_roomtype =Label(labelframeleft,font =("arial",12,"bold"),text ="Room Type:",padx=2 , pady=6)
        label_roomtype.grid(row=3, column=0,sticky=W)

        combo_roomtype=ttk.Combobox(labelframeleft,font =("arial",12,"bold"),textvariable=self.var_roomtype,width =25 , state ="readonly")
        combo_roomtype["value"] = ("Single", "Double", "Luxury")
        combo_roomtype.current(0)
        combo_roomtype.grid(row=3,column=1)

        #avaliable room
        lblroomavaliable=Label(labelframeleft,font =("arial",12,"bold"),text ="Available room:",padx=2 , pady=6)
        lblroomavaliable.grid(row=4,column=0,sticky=W)
        txtroomavaliable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,font =("arial",12,"bold"),width=27)
        txtroomavaliable.grid(row=4 , column=1)


        #meal
        lblmeal =Label(labelframeleft,font =("arial",12,"bold"),text ="Meal:",padx=2 , pady=6)
        lblmeal.grid(row=5,column=0,sticky=W)
        
        combo_meal=ttk.Combobox(labelframeleft,font =("arial",12,"bold"),textvariable=self.var_meal,width =25 , state ="readonly")
        combo_meal["value"] = ("Breakfast", "Launch", "Dinner")
        combo_meal.current(0)
        combo_meal.grid(row=5,column=1)
        # txtmeal=ttk.Entry(labelframeleft,textvariable=self.var_meal,font =("arial",12,"bold"),width=27)
        # txtmeal.grid(row=5,column=1)

        #no of days
        lblnoofdays=Label(labelframeleft,font =("arial",12,"bold"),text ="No of days:",padx=2 , pady=6)
        lblnoofdays.grid(row=6,column=0,sticky=W)
        txtnoofdays =ttk.Entry(labelframeleft,textvariable=self.var_noofdays,font =("arial",12,"bold"),width=27)
        txtnoofdays.grid(row=6,column=1)

        #paid tax 
        lblnoofdays=Label(labelframeleft,font =("arial",12,"bold"),text ="paid tax:",padx=2 , pady=6)
        lblnoofdays.grid(row=7,column=0,sticky=W)
        txtnoofdays =ttk.Entry(labelframeleft,textvariable=self.var_paidtax,font =("arial",12,"bold"),width=27)
        txtnoofdays.grid(row=7,column=1)

        #sub total
        lblnoofdays=Label(labelframeleft,font =("arial",12,"bold"),text ="sub total:",padx=2 , pady=6)
        lblnoofdays.grid(row=8,column=0,sticky=W)
        txtnoofdays =ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,font =("arial",12,"bold"),width=27)
        txtnoofdays.grid(row=8,column=1)

        #total cost
        lblidnumber =Label(labelframeleft,font =("arial",12,"bold"),text ="total cost:",padx=2 , pady=6)
        lblidnumber.grid(row=9,column=0,sticky=W)
        lblidnumber =ttk.Entry(labelframeleft,textvariable=self.var_total,font =("arial",12,"bold"),width=27)
        lblidnumber.grid(row=9,column=1)

        # ==========Bill Button===================================
        
        btnBill = Button(labelframeleft,text="Bill",command=self.total,font=("Arial" , 11, "bold") , bg="black" , fg="gold",width=10)
        btnBill.grid(row=10,column=0,padx =1,sticky=W)
        
        
        ###################btn###################33
        btn_frame = Frame(labelframeleft , bd=2 , relief=relief)
        btn_frame.place(x=0,y=400,width=412,height=40)
        
        btn_add= Button(btn_frame, text="ADD",command=self.add_data,width=10 , font=("Arial" , 11, "bold") , bg="black" , fg="gold")
        btn_add.grid(row=0 , column=0 , padx=1)
        
        btn_update= Button(btn_frame, text="update",command=self.update  , width=10 , font=("Arial" , 11, "bold") , bg="black" , fg="gold")
        btn_update.grid(row=0 , column=1 , padx=1)
        
        btn_del= Button(btn_frame, text="Delete" ,width=10, command=self.Delete , font=("Arial" , 11, "bold") , bg="black" , fg="gold")
        btn_del.grid(row=0 , column=2 , padx=1)
        
        btn_Reset= Button(btn_frame, text="reset",command=self.reset ,width=10 , font=("Arial" , 11, "bold") , bg="black" , fg="gold")
        btn_Reset.grid(row=0 , column=3 , padx=1) 
        
        
        #right side image 
        img3 = Image.open(r"hotel images\bed.jpg")
        img3 = img3.resize((520, 300),Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lbiimg = Label(self.root, image=self.photoimg3 , bd=0 , relief=relief)
        lbiimg.place(x=760,y=55,width=520,height=200)
        
        ################# Tabel frame #################33
        tabel_frame = LabelFrame(self.root , bd=4 , relief=RIDGE ,text="View Details And Search" , font=("Arial" , 12, "bold"))
        tabel_frame.place(x=435,y=280,width=869,height=260)

        lblSearchby = Label(tabel_frame , text="Search by"  , font=("Arial" , 12 , "bold") ,bg="red" , fg="white")
        lblSearchby.grid(row=0 , column= 0 , sticky=W , padx=2) 
    
        self.search_var = StringVar()
        
        combo_search =ttk.Combobox(tabel_frame , textvariable=self.search_var ,font=("Arial" , 12 , "bold") , width=24 , state="readonly")
        combo_search["value"]=("contact" , "room")
        combo_search.current(0)
        combo_search.grid(row=0, column=1 , padx=2)

        self.txt_search = StringVar()
        
        txtSearch=ttk.Entry(tabel_frame ,width=24 ,textvariable=self.txt_search , font=("Arial" , 13 , "bold"))
        txtSearch.grid(row=0 , column= 2 ,padx=2)

        btnSearch= Button(tabel_frame, text="Search", command=self.search , width=10 ,  font=("Arial" , 11, "bold") , bg="black" , fg="gold")
        btnSearch.grid(row=0 , column=3 , padx=1)

        btnShowAll= Button(tabel_frame, text="Show All" , command=self.fetch_data , width=10 , font=("Arial" , 11, "bold") , bg="black" , fg="gold")
        btnShowAll.grid(row=0 , column=4 , padx=1)
        
        
        ################# show data table ##############3
        Detials_table = Frame(tabel_frame ,bd=2 , relief=relief)
        Detials_table.place(x=0,y=50,width=860,height=180)
        scroll_X= ttk.Scrollbar(Detials_table , orient=HORIZONTAL)
        scroll_Y= ttk.Scrollbar(Detials_table , orient=VERTICAL)
        
        columns = ['contact','checkin','checkout','roomtype','roomavailable','meal','NumberOfDays',]
        self.room_table =ttk.Treeview(Detials_table , columns=columns , xscrollcommand=scroll_X.set ,  yscrollcommand=scroll_Y.set )        
        
        scroll_X.pack(side=BOTTOM , fill=X)
        scroll_Y.pack(side=RIGHT , fill=Y)
        
        scroll_X.config(command=self.room_table.xview)
        scroll_Y.config(command=self.room_table.yview)

        self.room_table.heading("contact" , text="Contact")
        self.room_table.heading("checkin" , text="CheckIn")
        self.room_table.heading("checkout" , text="Check Out")
        self.room_table.heading("roomtype" , text="Room Type")
        self.room_table.heading("roomavailable" , text="Room No")
        self.room_table.heading("meal" , text="Meal")
        self.room_table.heading("NumberOfDays" , text="NoOfDays")

        self.room_table["show"]="headings"


        self.room_table.column("contact" ,width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype" ,width=100 )
        self.room_table.column("roomavailable",width=100 )
        self.room_table.column("meal" ,width=100  )
        self.room_table.column("NumberOfDays" ,width=100 )
        self.room_table.pack(fill=BOTH,expand=1)
        
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    #================= All Data Fetch
    
    # =======  Add data
    def add_data(self):
        if self.var_contact.get() == "" or self.var_checkin.get() == "":
            messagebox.showerror("Error","You Have to Fill all the Fields")
        else:
            try:    
                con = sqlite3.connect("room.db")
                cur = con.cursor()
                cur.execute("INSERT INTO room values(?, ?, ?, ?, ?, ?, ?)", (
                                                                      self.var_contact.get(),
                                                                      self.var_checkin.get(),
                                                                      self.var_checkout.get(),
                                                                      self.var_roomtype.get(),
                                                                      self.var_roomavailable.get(),
                                                                      self.var_meal.get(),
                                                                      self.var_noofdays.get()
                                                                                                ))
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo('info',"Room Booked ",parent = self.root)
                # self.reset()
            except EXCEPTION as es :
                messagebox.showwarning('warning',f"Some thing went wrong :{str(es)}",parent = self.root)
    # =========== fetch_data           
    def fetch_data(self):
            con = sqlite3.connect("room.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM room")
            rows = cur.fetchall()
            if len(rows) != 0 :
                self.room_table.delete(*self.room_table.get_children())
                for i in rows:
                    self.room_table.insert("",END,values=i)
                con.commit()
    #get_cursor
    def get_cursor(self,event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row= content["values"]
        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])
    #  update function
    def update(self):
        if self.var_contact.get() == "": 
            messagebox.showerror("Error","Pleas enter Mobile Number",parent = self.root) # ), the parent parameter is used to specify the parent window or widget that the message box should be associated with.
        else:
            con = sqlite3.connect("room.db")
            cur = con.cursor()
            try:
                cur.execute("UPDATE room SET  check_in = ? , check_out = ?  , roomtype = ? , roomavilable = ? , meal = ? , noOfdays = ? WHERE contact = ?",(
                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_roomtype.get(),    
                    self.var_roomavailable.get(),
                    self.var_meal.get(),
                    self.var_noofdays.get(),
                    self.var_contact.get()
                    
                ))
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo('Info', 'room Data has been updated', parent=self.root)
            except Exception as es:
                messagebox.showwarning('Warning', f'Something went wrong: {str(es)}', parent=self.root)
    #  ========== Delete
    def Delete(self):
        Delete = messagebox.askyesno("Hotel Management System","Do you want to Delete This Customer ?")
        if Delete:
            con = sqlite3.connect("room.db")
            cur = con.cursor()
            cur.execute("delete from room where contact = ?",(self.var_contact.get(),))
        else:
            if not Delete:
                return
        con.commit()
        self.fetch_data()
        con.close()
    #   =============== reset
    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        # self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set(""),
        self.var_paidtax.set(""),
        self.var_actualtotal.set(""),
        self.var_total.set("")
    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("error" , "please enter valid contact number",parent =self.root)
        else:
            con = sqlite3.connect("customer.db")
            cur = con.cursor()    
            cur.execute("Select name from customer where mobile = ?",(self.var_contact.get(),))
            row = cur.fetchone()
            if row==None :
                messagebox.showerror("error , this number not found", parent =self.root)
            else:
                con.commit()
                con.close()    
                showdataframe =Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showdataframe.place(x=450,y=55,width =300 , height =180)
                lblname=Label(showdataframe, text="name",font=("arail",12 ,"bold"))
                lblname.place(x=0,y=0)
                lbl=Label(showdataframe, text=row,font=("arail",12 ,"bold"))
                lbl.place(x=90,y=0)
                # =============== Gender
                con = sqlite3.connect("customer.db")
                cur = con.cursor()    
                cur.execute("Select gender from customer where mobile =?",(self.var_contact.get(),))
                row = cur.fetchone()
                lblgender=Label(showdataframe, text="Gender",font=("arail",12 ,"bold"))
                lblgender.place(x=0,y=30)
                lbl2=Label(showdataframe, text=row,font=("arail",12 ,"bold"))
                lbl2.place(x=90,y=30)
                
                # =============== Email
                con = sqlite3.connect("customer.db")
                cur = con.cursor()    
                cur.execute("Select email from customer where mobile = ?",(self.var_contact.get(),))
                row = cur.fetchone()
                
                lblEmail=Label(showdataframe, text="Email",font=("arail",12 ,"bold"))
                lblEmail.place(x=0,y=60)
                lbl3=Label(showdataframe, text=row,font=("arail",12 ,"bold"))
                lbl3.place(x=90,y=60)
                
                # =============== Nationality
                con = sqlite3.connect("customer.db")
                cur = con.cursor()    
                cur.execute("Select nationality from customer where mobile = ?",(self.var_contact.get(),))
                row = cur.fetchone()
                
                lblNat=Label(showdataframe, text="Nationality",font=("arail",12 ,"bold"))
                lblNat.place(x=0,y=90)
                lbl4=Label(showdataframe, text=row,font=("arail",12 ,"bold"))
                lbl4.place(x=90,y=90)
                
                # =============== Address
                con = sqlite3.connect("customer.db")
                cur = con.cursor()    
                cur.execute("Select address from customer where mobile = ?",(self.var_contact.get(),))
                row = cur.fetchone()
                
                lblAddress=Label(showdataframe, text="Address",font=("arail",12 ,"bold"))
                lblAddress.place(x=0,y=120)
                lbl5=Label(showdataframe, text=row,font=("arail",12 ,"bold"))
                lbl5.place(x=90,y=120)
    def total(self):
        indata=self.var_checkin.get()
        outdata=self.var_checkout.get()      
        indata=datetime.strptime(indata, "%d/%m/%Y")
        outdata=datetime.strptime(outdata,"%d/%m/%Y")
        self.var_noofdays.set(abs(outdata - indata).days)
        if(self.var_meal.get()=="BreakFast"and self.var_roomtype.get() =="Luxury" ):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax=str("%.2f"%((q5)*0.1))+"  LE"
            st=str("%.2f"%((q5)))+"  LE"
            tt=str("%.2f"%(q5+(q5)*0.1))+"  LE"
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(st)
            self.var_total.set(tt)


        elif (self.var_meal.get()=="Launch"and self.var_roomtype.get() =="Single" ):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="rs."+str("%.2f"%((q5)*0.09))
            st="rs."+str("%.2f"%((q5)))
            tt="rs."+str("%.2f"%(q5+(q5)*0.09))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(st)
            self.var_total.set(tt)     
    
    # ====== Search
    def search(self):
        con = sqlite3.connect("room.db")
        cur = con.cursor()
        search_column = self.search_var.get()  # Get the selected search column
        search_value = self.txt_search.get()   # Get the search value
        # cur.execute("select * from customer where "+str(search_column)+"LIKE ?"+('%'+str(search_value)+'%',))
        cur.execute("SELECT * FROM room WHERE {} LIKE ?".format(search_column), ('%'+search_value+'%',))
        rows = cur.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows :
                self.room_table.insert("","end",values=i)
            con.commit()
        con.close()
    
if __name__ == "__main__":
    root = Tk()
    obj = RoomBooking(root)
    root.mainloop()