from Project import *


class class1(object):
    """description of class"""
    def __init__(self, *args, **kwargs):
        self.frmQLNV = ManageMenu()
        self.frmQLNV.display("Tính")
    def setupForm(self):
        self.FormQuanLy = tk.Tk()
        self.FormQuanLy.title('Form Quan Ly')
        self.FormQuanLy.geometry("600x300")
        self.FormQuanLy.configure(bg = 'White')
        self.FormQuanLy.minsize(600,300)
        self.FormQuanLy.maxsize(600,300)
        self.QLNV_Button()
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
            command = self.frmQLNV.root.mainloop)
        self.dt_Button.place(x = 6, y = 0)


        
