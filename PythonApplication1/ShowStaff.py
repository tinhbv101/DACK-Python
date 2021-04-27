import AddForm as Addform
from EditForm import *
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import sqlite3
from CRUDSQL import *



class ShowForm():
    def __init__(self):
        pass
    def display(self):
        self.rootShow = tk.Tk()
        self.rootShow.title = 'Quản lý nhân viên'
        self.tree = ttk.Treeview(self.rootShow, column=("c1", "c2", "c3","c4","c5", "c6", "c7","c8","c9"), show='headings')
        self.tree.pack(side = RIGHT , fill=BOTH,padx= 50,pady = 100)
        w = 1380
        h = 680
        ws = self.rootShow.winfo_screenwidth()
        hs = self.rootShow.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.rootShow.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.rootShow.configure(bg = '#dff9fb')
        #self.rootShow.resizable(FALSE, FALSE)
        #self.rootShow.geometry("1380x680+50+20")
        self.crud = CRUD()
        self.SearchTxt = StringVar(self.rootShow)
        self.labelContent()
        self.buttonRemove()
        self.buttonRefresh()
        self.OptionSort()
        self.entrySearch()
        self.buttonSearch()
        self.OptionGender()
        self.OptionRank()
        self.buttonChamcong()
        self.buttonADD()
        #self.btn_Remove.bind('<Enter>', self.btnRemove_Hover)

    def getGridViewData(self):
        self.tree.column("#1", anchor=tk.CENTER,minwidth=0, width=100, stretch="NO")
        self.tree.heading("#1", text="ID")

        self.tree.column("#2", anchor=tk.CENTER,minwidth=0, width=175, stretch="NO")
        self.tree.heading("#2", text="Tên nhân viên")

        self.tree.column("#3", anchor=tk.CENTER,minwidth=0, width=75, stretch="NO")
        self.tree.heading("#3", text="Năm sinh")

        self.tree.column("#4", anchor=tk.CENTER,minwidth=0, width=75, stretch="NO")
        self.tree.heading("#4", text="Giới tính")

        self.tree.column("#5", anchor=tk.CENTER,minwidth=0, width=175, stretch="NO")
        self.tree.heading("#5", text="Chức vụ")

        self.tree.column("#6", anchor=tk.CENTER,minwidth=0, width=125, stretch="NO")
        self.tree.heading("#6", text="Lương cơ bản")

        self.tree.column("#7", anchor=tk.CENTER,minwidth=0, width=125, stretch="NO")
        self.tree.heading("#7", text="Ca làm việc")

        self.tree.column("#8", anchor=tk.CENTER,minwidth=0, width=125, stretch="NO")
        self.tree.heading("#8", text="Thưởng")

        self.tree.column("#9", anchor=tk.CENTER,minwidth=0, width=75, stretch="NO")
        self.tree.heading("#9", text="Điểm danh")

        self.tree.pack()

    def MainShow(self):
        self.crud.ShowStaff(self.tree,"SELECT * FROM NhanVien")
        self.tree.bind("<Double-1>",self.OnDoubleClick)
        self.getGridViewData()
        self.rootShow.mainloop()

    def RefreshData(self):
        self.crud.View(self.tree,"SELECT * FROM NhanVien")

    def OnDoubleClick(self, event = "doubleClick"):
        x = self.tree.item(self.tree.selection()[0],"values")
        editform = EditForm(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8])
        editform.guiForm()
#====================Button==============

    def labelContent(self):
        lb_Content = tk.Label(
            self.rootShow,
            text = 'Quản lý nhân viên',
            font = ('Times', 25, 'bold', 'italic'),
            fg = 'Black',
            bg = '#dff9fb'
            )
        lb_Content.place(x=100,y=10)
    #Button ADD
    def buttonADD(self):
        btn_ADD = tk.Button(
            self.rootShow,
            text = 'Thêm Nhân Viên',
            font = 'Heveltica 10 bold',
            width = 15,
            command = self.Add
            )
        btn_ADD.place(x=800, y = 600)
    #End tk.Button ADD

    def buttonRemove(self):
        self.btn_Remove = tk.Button(
            self.rootShow,
            text = 'Xóa Nhân viên đã chọn',
            font = 'Heveltica 10 bold',
            #height = 2,
            width = 20,
            command = self.Delete
            )
        self.btn_Remove.place(x=1050, y = 600)


    def buttonRefresh(self):
        button1 = tk.Button(self.rootShow,
                            text = "Lọc lại dữ liệu",
                            font = 'Heveltica 13',
                            width = 15,
                            command = self.RefreshData
                            )
        button1.place(x=20, y = 100)
        print(self.tree.item)
    
    
    def OptionSort(self):
        OPTIONS = [
                    "Chọn cách sắp xếp",
                    "ID",
                    "ID reverse",
                    "Name",
                    "Name reverse",
                    "Gender",
                    "Gender reverse",
                    "Birth Year",
                    "Birth Year reverse",
                    "Salary",
                    "Salary reverse",
                    ]
        variable = StringVar(self.rootShow)
        variable.set("Chọn cách sắp xếp")
        self.optionSort = OptionMenu(self.rootShow, variable, *OPTIONS,command = self.SortType)
        #self.optionSort.configure(background='#dff9fb', foreground='black', activebackground='#dff9fb', activeforeground='#30336b', highlightthickness=0)
        self.optionSort.place(x=20, y = 180)

    def OptionGender(self):
        OPTIONS = [
                    "Chọn giới tính",
                    "Tất cả",
                    "Nữ",
                    "Nam"
                    ]
        variable = StringVar(self.rootShow)
        variable.set("Chọn giới tính")
        self.et_Sex = OptionMenu(self.rootShow, variable, *OPTIONS,command = self.FilterGender)
        #self.et_Sex.configure(background='#dff9fb', foreground='black', activebackground='#dff9fb', activeforeground='#30336b', highlightthickness=0)
        self.et_Sex.place(x=20, y = 260)

    def OptionRank(self):
        OPTIONS = [
                    "Chọn chức vụ",
                    "Tất cả",
                    "Quản Lý",
                    "Tổ trưởng",
                    "Pha chế",
                    "Quét dọn",
                    "Rửa Ly",
                    "Bảo vệ",
                    "Xuât nhập kho",
                    "Thu ngân",
                    ]
        variable = StringVar(self.rootShow)
        variable.set("Chọn chức vụ")
        self.optionRank = OptionMenu(self.rootShow, variable, *OPTIONS,command = self.FilterRank)
        #self.optionRank.configure(background='#dff9fb', foreground='black', activebackground='#dff9fb', activeforeground='#30336b', highlightthickness=0)
        self.optionRank.place(x=20, y = 340)
    def buttonChamcong(self):
        button1 = Button(self.rootShow, width = 15,text="Chấm công",command = self.ChamCong)
        button1.place(x=20, y = 440)
        print(self.tree.item)
#=============================Search Entry============================
    def labelID(self):
        lb_ID = Label(
            self.rootShow,
            text = 'Search by name ',
            font = 'Heveltica 15 bold',
            bg = '#dff9fb')
        lb_ID.place(x=60,y=110)
    #Entry Search
    def entrySearch(self):
        self.et_Search = tk.Entry(
            self.rootShow,
            font = 'Times 15',
            bg = '#aaa69d',
            width = 30,
            textvariable = self.SearchTxt)
        self.et_Search.place(x=720,y = 34)
    def buttonSearch(self):
        button1 = tk.Button(self.rootShow,text="TÌm kiếm NV", font = 'Times 11', width = 20, command = self.SreachByName)
        button1.place(x=1100, y = 32)
        print(self.tree.item)
#=================function=============
    def Delete(self):
        if(self.tree.item(self.tree.focus(),"values") != ""):
            idDel = self.tree.item(self.tree.focus(),"values")[0]
            if(self.checkIDNhanVien(idDel) == False):
                 MsgBox = messagebox.askquestion ('Xóa nhân viên','Bạn có chắc muốn xóa nhân viên: '+str(idDel),icon = 'warning')
                 if MsgBox == 'yes':
                     self.crud.DeleteStaff(idDel)
                     messagebox.showinfo("Xóa Nhân Viên", "Xoa Nhan Vien Thanh Cong",parent=self.rootShow)
                 else:
                     messagebox.showinfo("Xóa Nhân Viên", "Đã hủy xóa nhân viên",parent=self.rootShow)
            else:
                messagebox.showerror("Xóa Nhân Viên", "Lỗi: ID nhân viên không tồn tại",parent=self.rootShow)
        else:
            messagebox.showerror("Xóa Nhân Viên", "Lỗi: Không Nhân Viên nào được chọn",parent=self.rootShow)
    
            
    def Add(self):
        form2 = Addform.AddForm()
        form2.guiForm()

    def close(self):
        self.rootShow.destroy()
#=====================function Sort=============
    def SortType(self,value):
        OPTIONS = [
                    "Choose Sort",
                    "ID",
                    "ID reverse",
                    "Name",
                    "Name reverse",
                    "Gender",
                    "Gender reverse",
                    "Birth Year",
                    "Birth Year reverse",
                    "Salary",
                    "Salary reverse",
                    ]
        if(value == OPTIONS[1]):
            self.SortID()
        if(value == OPTIONS[2]):
            self.SortIDReverse()
        if(value == OPTIONS[3]):
            self.SortName()
        if(value == OPTIONS[4]):
            self.SortNameReverse()
        if(value == OPTIONS[5]):
            self.SortGender()
        if(value == OPTIONS[6]):
            self.SortGenderReverse()
        if(value == OPTIONS[7]):
            self.SortBirthYear()
        if(value == OPTIONS[8]):
            self.SortBirthYearReverse()
        if(value == OPTIONS[9]):
            self.SortSalary()
        if(value == OPTIONS[10]):
            self.SortSalaryReverse()



    def SortID(self):
        self.crud.View(self.tree,"SELECT * FROM NhanVien ORDER BY IDnhanvien ASC")
    def SortIDReverse(self):
        self.crud.View(self.tree,"SELECT * FROM NhanVien ORDER BY IDnhanvien DESC")
    def SortName(self):
        self.crud.View(self.tree,"SELECT * FROM NhanVien ORDER BY tennhanvien ASC")
    def SortNameReverse(self):
        self.crud.View(self.tree,"SELECT * FROM NhanVien ORDER BY tennhanvien DESC")
    def SortNameReverse(self):
        self.crud.View(self.tree,"SELECT * FROM NhanVien ORDER BY tennhanvien DESC")
    def SortGender(self):
        self.crud.View(self.tree,"SELECT * FROM NhanVien ORDER BY Gioitinh ASC")
    def SortGenderReverse(self):
        self.crud.View(self.tree,"SELECT * FROM NhanVien ORDER BY Gioitinh DESC")
    def SortBirthYear(self):
        self.crud.View(self.tree,"SELECT * FROM NhanVien ORDER BY Namsinh ASC")
    def SortBirthYearReverse(self):
        self.crud.View(self.tree,"SELECT * FROM NhanVien ORDER BY Namsinh DESC")
    def SortSalary(self):
        self.crud.View(self.tree,"SELECT * FROM NhanVien ORDER BY Luongcoban ASC")
    def SortSalaryReverse(self):
        self.crud.View(self.tree,"SELECT * FROM NhanVien ORDER BY Luongcoban DESC")
#=========================Function Search====================================
    def SreachByName(self):
        self.crud.View(self.tree,"SELECT * FROM NhanVien Where Tennhanvien LIKE '%" +self.SearchTxt.get()+"%'"+" OR IDnhanvien LIKE '%" +self.SearchTxt.get()+"%'"+" OR namsinh LIKE '%" +self.SearchTxt.get()+"%'")
#=========================Function Filter====================================
    def FilterGender(self,value):
        if(value == "Tất cả"):
            self.RefreshData()
        else:
            self.crud.View(self.tree,"SELECT * FROM NhanVien WHERE Gioitinh = '"+ value +"'")
    def FilterRank(self,value):
         if(value == "Tất cả"):
            self.RefreshData()
         else:
            self.crud.View(self.tree,"SELECT * FROM NhanVien WHERE Chucvu = '"+ value +"'")

#=========================Function Điểm danh====================================
    def ChamCong(self):
        if(self.tree.item(self.tree.focus(),"values") != ""):
            idDel = int(self.tree.item(self.tree.focus(),"values")[0])
            Cong = int(self.tree.item(self.tree.focus(),"values")[8]) + 1
            self.crud.ChamCong(idDel,Cong)
            self.RefreshData()
            messagebox.showinfo("Delete Nhân Viên", "Chấm công nhân viên thành công",parent=self.rootShow)
        else:
            messagebox.showerror("Delete Nhân Viên", "Lỗi: Không Nhân Viên nào được chọn",parent=self.rootShow)
#====================================================================

#=========================verif====================================
    def checkIDNhanVien(self,idDel):
        listID = self.crud.getIDNhanVien()
        if(int(idDel) in listID):
            return False
        else:
            return True
#====================================================================
