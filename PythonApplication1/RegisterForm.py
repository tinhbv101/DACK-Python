from tkinter import *
from tkinter import messagebox, ttk
import os
from tkinter import messagebox
from mydb import *

class RegisterForm(object):
    """description of class"""



#===============REGISTER FORM DESIGN================ 


    def setUpRegisterForm(self):
        self.RegisterForm = Tk()
        self.RegisterForm.title('Register')
        self.RegisterForm.geometry("428x452")
        self.RegisterForm.configure(bg = 'Purple')
        self.RegisterForm.minsize(428,452)
        self.RegisterForm.maxsize(428,452)
        self.Content()
        self.UserName_Textbox()
        self.Password_Textbox()
        self.Confirm_Textbox()
        self.Cancel_Button()
        self.Register_Button()
        self.RegisterForm.mainloop()


    #set up content
    def Content(self):
        Content_Label = Label(
            self.RegisterForm, 
            text = "Account Register", 
            font = ("Comic Sans MS", 25, "bold", "underline"),
            fg='aqua',
            bg = "Purple")
        Content_Label.place(x = 90, y = 44)


    #set up Text Box Username
    def UserName_Textbox(self):
        userName_Label = Label(
            self.RegisterForm, 
            text = "Username:", 
            font = ("Yu Gothic UI", 15),
            fg='white', 
            bg = 'Purple')
        userName_Label.place(x = 40, y = 138)
        self.userName_TextBox = Entry(
            self.RegisterForm,
            font =("Yu Gothic UI", 15))
        self.userName_TextBox.place(x = 149, y = 138)

    #set up Text Box Password
    def Password_Textbox(self):
        passWord_Label = Label(self.RegisterForm, 
                               text = "Password:", 
                               font = ("Yu Gothic UI", 15),
                               fg='white', 
                               bg = 'Purple')
        passWord_Label.place(x = 42, y = 184)
        self.passWord_TextBox = Entry(
            self.RegisterForm,
            font =("Yu Gothic UI", 15), 
            show = "*")
        self.passWord_TextBox.place(x = 149, y = 184)


    #set up Text Box Confirm Password
    def Confirm_Textbox(self):
        conFirm_Label = Label(
            self.RegisterForm, 
            text = "Confirm:", 
            font = ("Yu Gothic UI", 15),
            fg='white', 
            bg = 'Purple')
        conFirm_Label.place(x = 56, y = 231)
        self.conFirm_TextBox = Entry(
            self.RegisterForm,
            font =("Yu Gothic UI", 15),
            show = "*")
        self.conFirm_TextBox.place(x = 149, y = 231)


    #set up Button Cancel
    def Cancel_Button(self):
        self.cancel_Button = Button(
            self.RegisterForm, 
            text = "Cancel", 
            font = "Helvetica 15 bold",
            fg = 'white',
            bg = 'red',
            bd =  10,
            highlightthickness=4, 
            highlightcolor="#37d3ff", 
            highlightbackground="#37d3ff", 
            borderwidth=4,
            width = 11,
            command = self.cancelCommand)
        self.cancel_Button.place(x = 50, y = 307)

    



    #set up Button Register
    def Register_Button(self):
        self.register_Button = Button(self.RegisterForm, text = "Register", font = "Helvetica 15 bold",
                      fg = 'white',
                      bg = 'green3',
                      bd =  10, 
                      highlightthickness=4, 
                      highlightcolor="#37d3ff", 
                      highlightbackground="#37d3ff", 
                      borderwidth=4,
                      width = 11,
                      command = self.registerCommand)
        self.register_Button.place(x = 228, y = 307)




#=================COMMAND==================


    def registerCommand(self):
        mdb = mydb()
        if self.passWord_TextBox.get() != self.conFirm_TextBox.get():
            messagebox.showerror("Register", "Lỗi: Mật khẩu xác nhận không trùng khớp")
        elif not self.verif():
            messagebox.showerror("Register", "Lỗi: Username, Password, Confirm không được bỏ trống")
        else:
            mdb.insert(self.userName_TextBox.get(),self.passWord_TextBox.get())

    def verif(self):
        if self.userName_TextBox.get() == "" or self.passWord_TextBox.get() == "" or self.conFirm_TextBox.get() == "":
            return False
        else:
            return True

        
    def cancelCommand(self):
        self.RegisterForm.destroy()    

