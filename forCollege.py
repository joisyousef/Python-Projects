from tkinter import *
window = Tk()
window.title('Hello World!')
window.geometry('800x500+150+200')
#window.geometry('%dx%d+0+0' %(800,500))
window.minsize(200,200)
#window.resizable(False,True)
window.maxsize(700,700)
window.config(background='white')
window.lift()
#window.iconify()
window.state('normal')





window.mainloop()