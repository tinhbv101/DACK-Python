from ShowStaff import *
import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import sqlite3
from CRUDSQL import *


class EditForm(object):
    def __init__(self,id,name,birthyear,gender,rank,salary,sift,bonus,count):
        self.Editroot = Tk()
        self.Editroot.title = 'Edit'
        w = 1000
        h = 550
        ws = self.Editroot.winfo_screenwidth()
        hs = self.Editroot.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.Editroot.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.Editroot.configure(bg = '#dff9fb')
        self.Editroot.resizable(FALSE, FALSE)
        self.display()
        #self.guiForm()

        self.id.set(id)
        self.name.set(name)
        self.birthyear.set(birthyear)
        self.gender.set(gender)
        self.rank.set(rank)
        self.salary.set(salary)
        self.sift.set(sift)
        self.bonus.set(bonus)
        self.count.set(count)
    def display(self):
        self.id = IntVar(self.Editroot)
        self.name = StringVar(self.Editroot)
        self.birthyear = IntVar(self.Editroot)
        self.gender = StringVar(self.Editroot)
        self.rank = StringVar(self.Editroot)
        self.salary = IntVar(self.Editroot)
        self.sift = StringVar(self.Editroot)
        self.bonus = IntVar(self.Editroot)
        self.count = IntVar(self.Editroot)
        self.crud = CRUD()
        
#========================Gui form===============================

    def guiForm(self):
        self.labelContent()
        self.labelID()
        self.labelNVname()
        self.labelnamSinh()
        self.labelSex()
        self.labelchucVu()
        self.labelluongCoBan()
        self.labelcaLamViec()
        self.labelThuong()
        self.labeldiemDanh()
        self.entryID()
        self.entryNVname()
        self.labelnamSinh()
        self.entrynamSinh()
        self.entrySex(self.gender.get())
        self.entrychucVu(self.rank.get())
        self.entryluongCoBan()
        self.entrycaLamViec()
        self.entryThuong()
        self.entrydiemDanh()
        self.buttonEdit()
        #self.buttonRemove()
        #self.buttonADD()
        self.Editroot.mainloop()
#==================================================================================

#===============================Lable Form==============================================
    def labelContent(self):
        lb_Content = tk.Label(
            self.Editroot,
            text = 'Chỉnh sửa nhân viên',
            font = ('Times', 25, 'bold', 'italic'),
            fg = 'Black',
            bg = '#dff9fb'
            )
        lb_Content.place(x=300,y=20)
#=================================================================

#=============================label ID============================
    def labelID(self):
        lb_ID = tk.Label(
            self.Editroot,
            text = 'ID Nhân Viên: ',
            font = 'Times 15 bold',
            bg = '#dff9fb')
        lb_ID.place(x=60,y=110)
#==============================================================

#===================================label NVname===============
    def labelNVname(self):
        lb_NVname = tk.Label(
            self.Editroot,
            text = 'Tên nhân viên: ',
            font = 'Times 15 bold',
            bg = '#dff9fb')
        lb_NVname.place(x=60,y=180)
#===========================End label NVname=========================

    #label năm sinh
    def labelnamSinh(self):
        lb_namSinh = tk.Label(
            self.Editroot,
            text = 'Năm sinh: ',
            font = 'Times 15 bold',
            bg = '#dff9fb')
        lb_namSinh.place(x=60,y=250)
    #End label giới tính

    #label giới tính
    def labelSex(self):
        lb_Sex = tk.Label(
            self.Editroot,
            text = 'Giới tính: ',
            font = 'Times 15 bold',
            bg = '#dff9fb')
        lb_Sex.place(x=60,y=320)
    #End label giới tính

    #label chức vụ
    def labelchucVu(self):
        lb_chucVu = tk.Label(
            self.Editroot,
            text = 'Chức vụ: ',
            font = 'Times 15 bold',
            bg = '#dff9fb')
        lb_chucVu.place(x=60,y=390)
    #End label giới tính

    #label lương cơ bản
    def labelluongCoBan(self):
        lb_luongCoBan = tk.Label(
            self.Editroot,
            text = 'Lương cơ bản: ',
            font = 'Times 15 bold',
            bg = '#dff9fb')
        lb_luongCoBan.place(x=550,y=125)
    #End label lương cơ bản

    #label ca làm việc
    def labelcaLamViec(self):
        lb_caLamViec = tk.Label(
            self.Editroot,
            text = 'Ca làm việc: ',
            font = 'Times 15 bold',
            bg = '#dff9fb')
        lb_caLamViec.place(x=550,y=205)
    #End label ca làm việc

    #label thưởng
    def labelThuong(self):
        lb_Thuong = tk.Label(
            self.Editroot,
            text = 'Thưởng: ',
            font = 'Times 15 bold',
            bg = '#dff9fb')
        lb_Thuong.place(x=550,y=285)
    #End label thưởng

    #label điểm danh
    def labeldiemDanh(self):
        lb_diemDanh = tk.Label(
            self.Editroot,
            text = 'Điểm danh: ',
            font = 'Times 15 bold',
            bg = '#dff9fb')
        lb_diemDanh.place(x=550,y=365)
    #End label điểm danh

    #tk.Entry ID
    def entryID(self):
        self.et_ID = tk.Entry(
            self.Editroot,
            font = 'Times 15',
            bg = '#aaa69d',
            textvariable = self.id)
        self.et_ID.place(x=220,y = 110)
    #End tk.Entry ID

    #tk.Entry NVname
    def entryNVname(self):
        self.et_NVname = tk.Entry(
            self.Editroot,
            font = 'Times 15',
            bg = '#aaa69d',
            textvariable = self.name)
        self.et_NVname.place(x=220,y = 180)
    #End tk.Entry NVname

    #tk.Entry năm sinh
    def entrynamSinh(self):
        self.et_namSinh = tk.Entry(
            self.Editroot,
            font = 'Times 15',
            bg = '#aaa69d',
            textvariable = self.birthyear)
        self.et_namSinh.place(x=220,y = 250)
    #End tk.Entry năm sinh

    #tk.Entry sex
    def entrySex(self,value):
        OPTIONS = [
                    value,
                    "Nữ",
                    "Nam"
                    ]
        variable = StringVar(self.Editroot)
        variable.set(value)
        self.et_Sex = OptionMenu(self.Editroot, variable, *OPTIONS,command = self.SetGender)
        self.et_Sex.place(x=220,y = 320)
    #End tk.Entry sex

    #tk.Entry chức vụ
    def entrychucVu(self,value):
        OPTIONS= [
                    value,
                    "Quản Lý",
                    "Tổ trưởng",
                    "Pha chế",
                    "Quét dọn",
                    "Rửa Ly",
                    "Bảo vệ",
                    "Xuât nhập kho",
                    "Thu ngân",
                    ]
        variable = StringVar(self.Editroot)
        variable.set("Choose Sort")
        self.et_chucVu = OptionMenu(self.Editroot, variable, *OPTIONS,command = self.SetRank)
        self.et_chucVu.place(x=220,y = 390)
    #End tk.Entry chức vụ

    #tk.Entry lương cơ bản
    def entryluongCoBan(self):
        self.et_luongCoBan = tk.Entry(
            self.Editroot,
            font = 'Times 15',
            bg = '#aaa69d',
            textvariable = self.salary)
        self.et_luongCoBan.place(x=710,y = 125)
    #End tk.Entry lương cơ bản

    #tk.Entry ca làm việc
    def entrycaLamViec(self):
        self.et_caLamViec = tk.Entry(
            self.Editroot,
            font = 'Times 15',
            bg = '#aaa69d',
            textvariable = self.sift)
        self.et_caLamViec.place(x=710,y = 205)
    #End tk.Entry ca làm việc

    #Entry thưởng
    def entryThuong(self):
        self.et_Thuong = tk.Entry(
            self.Editroot,
            font = 'Times 15',
            bg = '#aaa69d',
            textvariable = self.bonus)
        self.et_Thuong.place(x=710,y = 285)
    #End tk.Entry thưởng

    #tk.Entry điểm danh
    def entrydiemDanh(self):
        self.et_diemDanh = tk.Entry(
            self.Editroot,
            font = 'Times 15',
            bg = '#aaa69d',
            textvariable = self.count)
        self.et_diemDanh.place(x=710,y = 365)
    #End tk.Entry điểm danh

    #Button ADD
    def buttonADD(self):
        btn_ADD = tk.Button(
            self.Editroot,
            text = 'Thêm nhân viên',
            font = 'Heveltica 15 bold',
            width = 10,
            command = self.Add
            )
        btn_ADD.place(x=200, y = 450)
    #End tk.Button ADD

    #tk.Button Edit
    def buttonEdit(self):
        btn_Edit = tk.Button(
            self.Editroot,
            text = 'Lưu thay đổi',
            font = 'Heveltica 10 bold',
            width = 15,
            bg = '#c7ecee',
            command = self.Update
            )
        btn_Edit.place(x=650, y = 450)
    #End Button Edit

    #Button Remove
    def buttonRemove(self):
        btn_Remove = tk.Button(
            self.Editroot,
            text = 'Xóa Nhân Viên',
            font = 'Heveltica 15 bold',
            command = self.Delete
            )
        btn_Remove.place(x=620, y = 450)
    #End Button Remove
    #Button SHOW
    #End Button Show
    #Command
    def Delete(self):
        if(self.checkIDNhanVien() == False):
            self.crud.DeleteStaff(self.id.get())
            messagebox.showinfo("Add Nhân Viên", "Xoa Nhan Vien Thanh Cong")
        else:
            messagebox.showerror("Add Nhân Viên", "Lỗi: ID nhân viên không tồn tại")

    def Add(self):
        if (self.checkTT() == True):
            if(self.checkGioiTinh() == True):
                if(self.checkIDNhanVien() == True):
                    self.crud.AddStaff(self.id.get(),self.name.get(),self.birthyear.get(),self.gender.get(),self.rank.get(),self.salary.get(),self.sift.get(),self.bonus.get(),self.count.get())
                    messagebox.showinfo("Add Nhân Viên", "Thêm nhân viên thành công")
                else:
                     messagebox.showerror("Add Nhân Viên", "Lỗi: ID nhân viên đã tồn tại")
            else:
                messagebox.showerror("Add Nhân Viên", "Lỗi: Giới tính chỉ chấp nhận 'Nam' hoac 'Nữ' ")
        else:
            messagebox.showerror("Add Nhân Viên", "Không được để trông các mục")

    def Update(self):
        if (self.checkTT() == True):
            if(self.checkGioiTinh() == True):
                if(self.checkIDNhanVien() == False):
                    self.crud.UpdateStaff(self.id.get(),self.name.get(),self.birthyear.get(),self.gender.get(),self.rank.get(),self.salary.get(),self.sift.get(),self.bonus.get(),self.count.get())
                    messagebox.showinfo("Add Nhân Viên", "Sửa Nhân viên thành công")
                else:
                     messagebox.showerror("Add Nhân Viên", "Lỗi: Không tìm thấy nhân viên để sửa")
            else:
                messagebox.showerror("Add Nhân Viên", "Lỗi: Giới tính chỉ chấp nhận 'Nam' hoac 'Nữ' ")
        else:
            messagebox.showerror("Add Nhân Viên", "Không được để trông các mục")

    #command
#=========================verif====================================
    def checkIDNhanVien(self):
        listID = self.crud.getIDNhanVien()
        if(self.id.get() in listID):
            return False
        else:
            return True

    def checkTT(self):
        if(self.id.get() == 0 or self.name.get() == "" or self.birthyear.get() == 0 or self.rank.get() == "" or self.salary.get() == 0 or self.sift.get() == ""):
            return False
        else:
            return True

    def checkGioiTinh(self):
        if(self.gender.get() != "Nam" and self.gender.get() != "Nữ"):
            return False
        else:
            return True
#=======================function===========================================
    def SetGender(self,value):
        print(value)
        self.gender.set(value) 
    def SetRank(self,value):
        print(value)
        self.rank.set(value) 
   
#==================================================================
