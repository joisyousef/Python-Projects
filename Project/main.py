from tkinter import *
from PIL import Image ,ImageTk
from Customer import Cust_Win
from room import RoomBooking

width = 1550
height = 800
x=0
y=0
bd = 4
relief = RIDGE
font = "times new roman"
fontSize = 14
bg = "black"
fg = "gold"
class HotelManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management System")
        #   Center The Screen
        screen_width=root.winfo_screenwidth()
        screen_height=root.winfo_screenheight()
        x=int((screen_width - width)/2)     
        y=int((screen_height-height)/2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
            
            
        img1 = Image.open(r"hotel images\hotel1.png")
        img1 = img1.resize((1550,140),Image.Resampling.LANCZOS) # Antialiasing is a technique used to mitigate lose of details  and sharpness
        self.photoImg1 = ImageTk.PhotoImage(img1)
        
        lblImg = Label(self.root,image=self.photoImg1,bd=4,relief=relief)
        lblImg.place(x=0,y=0,width=width,height=140)
        
        #   logo
        img2 = Image.open(r"hotel images\logohotel.png")
        img2 = img2.resize((230,140),Image.Resampling.LANCZOS) # Antialiasing is a technique used to mitigate lose of details  and sharpness
        self.photoImg2 = ImageTk.PhotoImage(img2)
        
        lblImg = Label(self.root,image=self.photoImg2,bd=bd,relief=relief)
        lblImg.place(x=0,y=0,width=230,height=140)
        
        #   title
        lbl_title = Label(self.root , text="HOTEL MANAGEMENT SYSTEM " , font=(font , 40 , "bold") , bg=bg , fg=fg, bd=bd, relief=relief)
        lbl_title.place(x=0,y=140,width=1550,height=50)
        
        #################### main frame ###############33
        main_frame = Frame(self.root , bd=bd , relief=relief)
        main_frame.place(x=0,y=190,width=width,height=620)
        
        ###################### menu #####################
        lbl_menu = Label(main_frame , text="MENUE " , font=(font , 20 , "bold") , bg=bg , fg=fg, bd=bd, relief=relief)
        lbl_menu.place(x=0,y=0,width=230)
        
        #################### btn frame ###############33
        btn_frame = Frame(main_frame , bd=bd , relief=relief)
        btn_frame.place(x=0,y=35,width=228,height=190)
        
        cust_btn= Button(btn_frame, text="CUSTOMER"  ,command=self.cus_details, width=22 , font=(font, fontSize, "bold") , bg=bg , fg=fg , bd=0 ,cursor="hand1")
        cust_btn.grid(row=0 , column=0,pady=1)
        
        room_btn= Button(btn_frame, text="ROOM" , command=self.roomBooking,width=22 , font=(font , fontSize, "bold") , bg=bg , fg=fg, bd=0 ,cursor="hand1")
        room_btn.grid(row=1 , column=0,pady=1)
        
        details_btn= Button(btn_frame, text="DETAils" , width=22 , font=(font , fontSize, "bold") , bg=bg , fg=fg, bd=0 ,cursor="hand1")
        details_btn.grid(row=2 , column=0,pady=1)
        
        report_btn= Button(btn_frame, text="REPORT" , width=22 , font=(font , fontSize, "bold") , bg=bg , fg=fg , bd=0 ,cursor="hand1")
        report_btn.grid(row=3 , column=0,pady=1)
        
        logout_btn= Button(btn_frame, text="LOGOUT" , width=22 , font=(font, fontSize, "bold") , bg=bg, fg=fg , bd=0 ,cursor="hand1")
        logout_btn.grid(row=4 , column=0,pady=1)
        
        # right slid image 
        img3 = Image.open(r"hotel images\slide3.jpg")
        img3 = img3.resize((1310, 590),Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lbiimg = Label(main_frame, image=self.photoimg3 , bd=bd , relief=relief)
        lbiimg.place(x=225,y=0,width=1310,height=590)
        
        # down image 
        img4 = Image.open(r"hotel images\myh.jpg")
        img4 = img4.resize((230, 210),Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lbiimg = Label(main_frame, image=self.photoimg4 , bd=bd , relief=relief)
        lbiimg.place(x=0,y=225,width=230,height=210)
        
        img5 = Image.open(r"hotel images\khana.jpg")
        img5 = img5.resize((230, 190),Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        lbiimg = Label(main_frame, image=self.photoimg5 , bd=bd , relief=relief)
        lbiimg.place(x=0,y=420,width=230,height=190)
    def cus_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)
                
    def roomBooking(self):
        self.new_window = Toplevel(self.root)
        self.app = RoomBooking(self.new_window)        

if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()