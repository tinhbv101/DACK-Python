from tkinter import *
from ShowStaff import *
from DoanhThu import *
import os
from tkinter import messagebox
from mydb import *
from Project import *
class FormQuanLy(object):
    """description of class"""


#=================FromQuanLy Design=================
    def setupForm(self):
        self.FormQuanLy = Tk()
        self.FormQuanLy.title('Form Quan Ly')
        self.FormQuanLy.geometry("600x300")
        self.FormQuanLy.configure(bg = 'White')
        self.FormQuanLy.minsize(600,300)
        self.FormQuanLy.maxsize(600,300)
        self.QLNV_Button()
        self.DT_Button()
        self.FormQuanLy.mainloop()



    def QLNV_Button(self):
        self.dt_Button = tk.Button(
            self.FormQuanLy, 
            text = "Quản lý nhân viên", 
            font = "Helvetica 15 bold",
            fg = 'white',
            bg = 'red',
            bd =  10,
            highlightthickness=4, 
            highlightcolor="#37d3ff", 
            highlightbackground="#37d3ff", 
            borderwidth=4,
            width = 22,
            height = 11,
            command = self.qlnvCommand)
        self.dt_Button.place(x = 6, y = 0)
    
        
        
        
        
    def DT_Button(self):
        self.qlk_Button = tk.Button(
            self.FormQuanLy, 
            text = "Doanh thu", 
            font = "Helvetica 15 bold",
            fg = 'white',
            bg = 'red',
            bd =  10,
            highlightthickness=4, 
            highlightcolor="#37d3ff", 
            highlightbackground="#37d3ff", 
            borderwidth=4,
            width = 22,
            height = 11,
            command = self.dtCommand)
        self.qlk_Button.place(x = 305, y = 0)

#=================Command=================
    def qlnvCommand(self):
        frmQLNV = ShowForm()
        frmQLNV.display()
        frmQLNV.MainShow()

    def dtCommand(self):
        frm = ManageMenu()
        frm.display()

