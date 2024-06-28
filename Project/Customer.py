from tkinter import *
from PIL import Image ,ImageTk
from tkinter import messagebox
from tkinter import ttk 
import sqlite3
import random
import re  

width = 1305
height = 555

bd = 4
relief = RIDGE
font = "times new roman"
fontSize = 14
bg = "black"
fg = "gold"

class Cust_Win:
    def __init__(self , root):
        self.root = root
        self.root.title("Hotel Management System")
        #   Center The Screen
        screen_width=root.winfo_screenwidth()
        screen_height=root.winfo_screenheight()
        x=int((screen_width - width)/2) 
        y=int((screen_height-height)/2)
        self.root.geometry(f"{width}x{height}+{x+112}+{y+105}")
        ###################### Variables #####################
        self.var_ref = StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
        
        self.var_cusName = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_idProof = StringVar()
        self.var_idNumber = StringVar()
        
        ###################### title #####################
        lbl_title = Label(self.root , text="ADD CUSTOMER DETAILS" , font=(font , 18 , "bold") , bg=bg , fg=fg, bd=bd, relief=relief)
        lbl_title.place(x=0,y=0,width=width,height=50)
           #      #######3v logo image ////////////////////////
        img2 = Image.open(r"hotel images\logohotel.png")
        img2 = img2.resize((100, 40),Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbiimg = Label(self.root, image=self.photoimg2 , bd=0 , relief=relief)
        lbiimg.place(x=5,y=2,width=100,height=40)
        
        #####################labelframe##########################3
        labelframe=LabelFrame(self.root, bd=2 , relief=relief , text="customer Details" , font=(font , 12 , "bold") , padx=2)
        labelframe.place(x=5,y=50,width=425,height=490)
        
        #################### label and entry #######################
        ###custREf
        lbl_Cust_ref = Label(labelframe , text="Customer Ref"  , font=("Arial"  , 12 , "bold") , padx=2 , pady=6)
        lbl_Cust_ref.grid(row=0 , column= 0 , sticky=W) # sticky − What to do if the cell is larger than widget
        entry_ref = ttk.Entry(labelframe ,width=29  ,textvariable=self.var_ref,font=("Arial"  , 13 , "bold"),state="readonly")
        entry_ref.grid(row=0 , column= 1)
        ###cust name    
        custname = Label(labelframe , text="Customer name"  , font=("Arial" , 12 , "bold") , padx=2 , pady=6)
        custname.grid(row=1, column= 0 , sticky=W)

        txtnam = ttk.Entry(labelframe ,width=29  , textvariable=self.var_cusName , font=("Arial" , 13 , "bold"))
        txtnam.grid(row=1 , column= 1)
        ###Mother name
        lblfname = Label(labelframe , text="Mother name"  , font=("Arial" , 12 , "bold") , padx=2 , pady=6)
        lblfname.grid(row=2 , column= 0 , sticky=W)

        txtfnam = ttk.Entry(labelframe ,width=29  , textvariable=self.var_mother , font=("Arial" , 13 , "bold"))
        txtfnam.grid(row=2 , column= 1)
        ###gender combox
        lblGender = Label(labelframe , text="Gender"  , font=("Arial" , 12 , "bold") , padx=2 , pady=6)
        lblGender.grid(row=3 , column= 0 , sticky=W)

        combo_gender =ttk.Combobox(labelframe , textvariable=self.var_gender , font=("Arial" , 12 , "bold") , width=27 , state="readonly")
        combo_gender["value"]=("Male" , "Female")
        combo_gender.current(0)
        combo_gender.grid(row=3 , column=1)

        ### postcode
        lblpostcode= Label(labelframe , text="Post Code"  , font=("Arial" , 12 , "bold") , padx=2 , pady=6)
        lblpostcode.grid(row=4 , column= 0 , sticky=W)

        txtpostcode=ttk.Entry(labelframe ,width=29,  textvariable=self.var_post  , font=("Arial" , 13 , "bold"))
        txtpostcode.grid(row=4 , column= 1)
        ###mobild number
        lblmobilelabel = Label(labelframe , text="Mobile Number"  , font=("Arial" , 12 , "bold") , padx=2 , pady=6)
        lblmobilelabel.grid(row=5 , column= 0 , sticky=W)

        txtmobile=ttk.Entry(labelframe ,width=29 , textvariable=self.var_mobile , font=("Arial" , 13 , "bold"))
        txtmobile.grid(row=5 , column= 1)

        ###email
        lblemail = Label(labelframe , text="Email"  , font=("Arial" , 12 , "bold") , padx=2 , pady=6)
        lblemail.grid(row=6 , column= 0 , sticky=W)

        txtemail=ttk.Entry(labelframe ,width=29  , textvariable=self.var_email ,font=("Arial" , 13 , "bold"))
        txtemail.grid(row=6 , column= 1)

        ###nationality
        lblnationality = Label(labelframe , text="Nationality"  , font=("Arial" , 12 , "bold") , padx=2 , pady=6)
        lblnationality.grid(row=7 , column= 0 , sticky=W)

        combo_nationality =ttk.Combobox(labelframe , textvariable=self.var_nationality , font=("Arial" , 12 , "bold") , width=27 , state="readonly")
        combo_nationality["value"]=("Egypt" , "USA"  , "UK","UAE")
        combo_nationality.current(0)
        combo_nationality.grid(row=7 , column=1)


        ### idproof type combobox   
        lblidproof = Label(labelframe , text="id proof Type "  , font=("Arial" , 12 , "bold") , padx=2 , pady=6)
        lblidproof.grid(row=8 , column= 0 , sticky=W)

        combo_id =ttk.Combobox(labelframe , textvariable=self.var_idProof, font=("Arial" , 12 , "bold") , width=27 , state="readonly")
        combo_id["value"]=("National ID Card","Passport","Driving Licence")
        combo_id.current(0)
        combo_id.grid(row=8 , column=1)

        ###id number
        lbleNumber = Label(labelframe , text="id number"  , font=("Arial" , 12 , "bold") , padx=2 , pady=6)
        lbleNumber.grid(row=9 , column= 0 , sticky=W)

        txtidNumber=ttk.Entry(labelframe ,width=29 , textvariable=self.var_idNumber , font=("Arial" , 13 , "bold"))
        txtidNumber.grid(row=9 , column= 1)

        ### address
        lblAddres = Label(labelframe , text="address"  , font=("Arial" , 12 , "bold") , padx=2 , pady=6)
        lblAddres.grid(row=10 , column= 0 , sticky=W)

        txtAddress=ttk.Entry(labelframe ,width=29  , textvariable=self.var_address, font=("Arial" , 13 , "bold"))
        txtAddress.grid(row=10, column= 1)
        ###################btn###################33
        btn_frame = Frame(labelframe , bd=bd , relief=relief)
        btn_frame.place(x=0,y=400,width=412,height=40)
        
        btn_add= Button(btn_frame, text="ADD"  , command=self.add_data ,width=10 , font=("Arial" , 11, "bold") , bg="black" , fg="gold")
        btn_add.grid(row=0 , column=0 , padx=1)
        
        btn_update= Button(btn_frame, text="update" ,command=self.update , width=10 , font=("Arial" , 11, "bold") , bg="black" , fg="gold")
        btn_update.grid(row=0 , column=1 , padx=1)
        
        btn_del= Button(btn_frame, text="Delete" , command=self.Delete  , width=10 , font=("Arial" , 11, "bold") , bg="black" , fg="gold")
        btn_del.grid(row=0 , column=2 , padx=1)
        
        btn_Reset= Button(btn_frame, text="reset" ,command=self.reset , width=10 , font=("Arial" , 11, "bold") , bg="black" , fg="gold")
        btn_Reset.grid(row=0 , column=3 , padx=1)    
        
        ################## Tabel frame #################33
        tabel_frame = LabelFrame(self.root , bd=4 , relief=RIDGE ,text="View Details And Search" , font=("Arial" , 12, "bold"))
        tabel_frame.place(x=435,y=50,width=869,height=490)

        lblSearchby = Label(tabel_frame , text="Search by"  , font=("Arial" , 12 , "bold") ,bg="red" , fg="white")
        lblSearchby.grid(row=0 , column= 0 , sticky=W , padx=2) 
    
        self.search_var = StringVar()
        
        combo_search =ttk.Combobox(tabel_frame , textvariable=self.search_var ,font=("Arial" , 12 , "bold") , width=24 , state="readonly")
        combo_search["value"]=("Mobile" , "ref")
        combo_search.current(0)
        combo_search.grid(row=0, column=1 , padx=2)

        self.txt_search = StringVar()
        
        txtSearch=ttk.Entry(tabel_frame ,width=24 ,textvariable=self.txt_search , font=("Arial" , 13 , "bold"))
        txtSearch.grid(row=0 , column= 2 ,padx=2)

        btnSearch= Button(tabel_frame, text="Search" ,command=self.search , width=10 ,  font=("Arial" , 11, "bold") , bg="black" , fg="gold")
        btnSearch.grid(row=0 , column=3 , padx=1)

        btnShowAll= Button(tabel_frame, text="Show All",command=self.fetch_data  , width=10 , font=("Arial" , 11, "bold") , bg="black" , fg="gold")
        btnShowAll.grid(row=0 , column=4 , padx=1)
        
        ################# show data table ##############3
        Detials_table = LabelFrame(tabel_frame ,bd=2 , relief=relief)
        Detials_table.place(x=0,y=50,width=860,height=350)
        scroll_X= ttk.Scrollbar(Detials_table , orient=HORIZONTAL)
        scroll_Y= ttk.Scrollbar(Detials_table , orient=VERTICAL)
        
        columns = ['ref','name','mother','gender','post','mobile','email','nationality','idproof','idnumber','address']
        self.cust_details_Table =ttk.Treeview(Detials_table , columns=columns , xscrollcommand=scroll_X.set ,  yscrollcommand=scroll_Y.set )        
        
        scroll_X.pack(side=BOTTOM , fill=X)
        scroll_Y.pack(side=RIGHT , fill=Y)
        scroll_X.config(command=self.cust_details_Table.xview)
        scroll_Y.config(command=self.cust_details_Table.yview)

        self.cust_details_Table.heading("ref" , text="ref")
        self.cust_details_Table.heading("name" , text="name")
        self.cust_details_Table.heading("mother" , text="mother")
        self.cust_details_Table.heading("gender" , text="gender")
        self.cust_details_Table.heading("post" , text="post")
        self.cust_details_Table.heading("mobile" , text="mobile")
        self.cust_details_Table.heading("email" , text="email")
        self.cust_details_Table.heading("nationality" , text="nationality")
        self.cust_details_Table.heading("idproof" , text="id proof")
        self.cust_details_Table.heading("idnumber" , text="id number")
        self.cust_details_Table.heading("address" , text="address")

        self.cust_details_Table["show"]="headings"


        self.cust_details_Table.column("ref" ,width=100)
        self.cust_details_Table.column("name",width=100)
        self.cust_details_Table.column("mother",width=100)
        self.cust_details_Table.column("gender" ,width=100 )
        self.cust_details_Table.column("post",width=100 )
        self.cust_details_Table.column("mobile" ,width=100  )
        self.cust_details_Table.column("email" ,width=100 )
        self.cust_details_Table.column("nationality" ,width=100  )
        self.cust_details_Table.column("idproof" ,width=100 )
        self.cust_details_Table.column("idnumber" ,width=100 )
        self.cust_details_Table.column("address" ,width=100 )

        self.cust_details_Table.pack(fill=BOTH,expand=1) 
        self.cust_details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
    # def validate_email(self,em):  
    #     if re.match(r"[^@]+@[^@]+\.[^@]+",em):  
    #         return True  
    #     return False  
        
    def validate_data(self,dt,typ):
        idx=0
        for i in dt:
            if(type(dt[i]) == typ[idx] or typ[idx] == ""):
                pass
            else:
                messagebox.showerror(f"error","The data must be {typ[idx]}",parent = self.root)
            idx=idx+1
            
    
    def add_data(self):
        if self.var_mobile.get() == "" or self.var_mother.get() == "":
            messagebox.showerror("Error","You Have to Fill all the Fields")
        else:
            try:    
                con = sqlite3.connect("customer.db")
                cur = con.cursor()
                vRef = self.var_ref.get()
                vName = self.var_cusName.get()
                vMother =  self.var_mother.get()
                vGend = self.var_gender.get()
                vPost = self.var_post.get()
                vMob = self.var_mobile.get()
                vEmail = self.var_email.get()
                vNato = self.var_nationality.get()
                vIdP =self.var_idProof.get()
                vIdN= self.var_idNumber.get()
                vAdd = self.var_address.get()
                valuesLst = [vRef,vName,vMother,vGend,vPost,vMob,vEmail,vNato,vIdP,vIdN,vAdd]
                typesLst = [int,str,str,"",int,int,str,"","",int,str]
                self.validate_data(valuesLst,typesLst)
                cur.execute("INSERT INTO customer values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", valuesLst)
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo('info',"Customer Data has been added",parent = self.root)
                self.reset()
            except EXCEPTION as es :
                messagebox.showwarning('warning',f"Some thing went wrong :{str(es)}",parent = self.root)
            
    def fetch_data(self):
        con = sqlite3.connect("customer.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM customer")
        rows = cur.fetchall()
        if len(rows) != 0 :
            self.cust_details_Table.delete(*self.cust_details_Table.get_children())
            for i in rows:
                self.cust_details_Table.insert("",END,values=i)
            con.commit()
        con.close()
            
    
    def get_cursor(self,event=""):
        cursor_row = self.cust_details_Table.focus()
        content = self.cust_details_Table.item(cursor_row)
        row = content["values"]
        
        self.var_ref.set(row[0]),
        self.var_cusName.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_idProof.set(row[8]),
        self.var_idNumber.set(row[9]),
        self.var_address.set(row[10])
        
    def update(self):
        if self.var_mobile.get() == "": 
            messagebox.showerror("Error","Pleas enter Mobile Number",parent = self.root) # ), the parent parameter is used to specify the parent window or widget that the message box should be associated with.
        else:
            con = sqlite3.connect("customer.db")
            cur = con.cursor()
            try:
                cur.execute("UPDATE customer SET name = ? , mother = ? , gender = ?  , post = ? , mobile = ? , email = ? , nationality = ? , idproof = ? , idnumber = ? , address = ? WHERE ref = ?",(
                    self.var_cusName.get(),
                    self.var_mother.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_idProof.get(),
                    self.var_idNumber.get(),
                    self.var_address.get(),
                    self.var_ref.get()
                ))
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo('Info', 'Customer Data has been updated', parent=self.root)
            except Exception as es:
                messagebox.showwarning('Warning', f'Something went wrong: {str(es)}', parent=self.root)
            
            
    def Delete(self):
        Delete = messagebox.askyesno("Hotel Management System","Do you want to Delete This Customer ?")
        if Delete:
            con = sqlite3.connect("customer.db")
            cur = con.cursor()
            cur.execute("delete from customer where ref = ?",(self.var_ref.get(),))
        else:
            if not Delete:
                return
        con.commit()
        self.fetch_data()
        con.close()
    
    
    def reset(self):
        x=random.randint(1000,9999)
        self.var_ref.set(x),
        self.var_cusName.set(""),
        self.var_mother.set(""),
        # self.var_gender.set(),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        # self.var_nationality.set(""),
        # self.var_idProof.set(""),
        self.var_idNumber.set(""),
        self.var_address.set("")

    
    def search(self):
        con = sqlite3.connect("customer.db")
        cur = con.cursor()
        search_column = self.search_var.get()  # Get the selected search column
        search_value = self.txt_search.get()   # Get the search value
        # cur.execute("select * from customer where "+str(search_column)+"LIKE ?"+('%'+str(search_value)+'%',))
        cur.execute("SELECT * FROM customer WHERE {} LIKE ?".format(search_column), ('%'+search_value+'%',))
        rows = cur.fetchall()
        if len(rows) != 0:
            self.cust_details_Table.delete(*self.cust_details_Table.get_children())
            for i in rows :
                self.cust_details_Table.insert("","end",values=i)
            con.commit()
        con.close()


if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()