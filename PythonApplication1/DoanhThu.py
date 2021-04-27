import AddForm as Addform
from EditForm import *
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import sqlite3
from SQLBill import *
from SQLChiTietBill import *
from ChiTietBill import *
from Static import *
class ShowBill():
    def __init__(self):
        pass
    def display(self):
        self.rootShow = tk.Tk()
        self.rootShow.title = 'Doanh Thu'
        self.tree = ttk.Treeview(self.rootShow, column=("c1", "c2", "c3"), show='headings')
        self.tree.pack(side = RIGHT , fill=BOTH,padx= 50,pady = 100)
        self.tree2 = ttk.Treeview(self.rootShow, column=("c1", "c2"), show='headings')
        self.tree2.pack(side = RIGHT , fill=BOTH,padx= 50,pady = 100)
        self.crud = SQLBILL()
        w = 1100
        h = 680
        ws = self.rootShow.winfo_screenwidth()
        hs = self.rootShow.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.rootShow.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.rootShow.configure(bg = '#dff9fb')
        self.crud.ToTalMoney()
        self.labelContent()
        self.labelTotalDoanhThu()
        self.labelTotalMon()
        self.OptionFood()
        self.OptionBill()
        self.buttonStatic()

    def getGridViewData1(self):
        self.tree.column("#1", anchor=tk.CENTER,minwidth=0, width=100, stretch="NO")
        self.tree.heading("#1", text="Thời gian")

        self.tree.column("#2", anchor=tk.CENTER,minwidth=0, width=175, stretch="NO")
        self.tree.heading("#2", text="Số tiền")

        self.tree.column("#3", anchor=tk.CENTER,minwidth=0, width=75, stretch="NO")
        self.tree.heading("#3", text="Mã hóa đơn")
        self.tree.pack()
    def getGridViewData2(self):
        self.tree2.column("#1", anchor=tk.CENTER,minwidth=0, width=100, stretch="NO")
        self.tree2.heading("#1", text="Tên sản phẩm")

        self.tree2.column("#2", anchor=tk.CENTER,minwidth=0, width=175, stretch="NO")
        self.tree2.heading("#2", text="Số Lượng")

        self.tree.pack()
    def MainShow(self):
        self.crud.ShowBill(self.tree,"SELECT * FROM Bill")
        self.crud.ShowBill(self.tree2,"SELECT  ChiTietBill.name , sum(SoLuong) as SoLuong from ChiTietBill GROUP BY Name ")
        self.tree2.bind("<Double-1>",self.OnDoubleClick)
        self.tree.bind("<Double-1>",self.OnDoubleClick2)
        self.getGridViewData1()
        self.getGridViewData2()
        self.rootShow.mainloop()

    def RefreshData(self):
        self.crud.View(self.tree,"SELECT * FROM Bill")

    def OnDoubleClick(self, event = "doubleClick"):
        x = self.tree2.item(self.tree2.selection()[0],"values")
        DSPrice ={"Thạch rau câu": 5000,"Thạch Thủy Tinh": 5000,"Trân châu đen": 5000,"Trân châu trắng": 5000,"Trân châu hoàng kim": 5000,"Plan": 5000,"Nước Ngọt" : 15000,"Trà Sữa Thái Xanh" : 30000,"Chocolate Đá Xay" : 30000,"Trà Ch anh" : 20000,"Cà Phê Đá": 20000,"Cà Phê Sữa" : 25000,"Nước Dừa" :25000, "Nước Cam" : 25000, "Nước Suối" : 10000}
        messagebox.showinfo("Giá trị", str(x[1]) +" " +str(x[0]).strip()+ " có giá là: " +str(float(DSPrice[str(x[0]).strip()]) * int(x[1]))+" VNĐ",parent = self.rootShow)
    def OnDoubleClick2(self, event = "doubleClick"):
        x = self.tree.item(self.tree.selection()[0],"values")
        form1 = ShowChitietBill(x[2])
        form1.display()
#===================Label=========================
    def labelContent(self):
        lb_Content = tk.Label(
            self.rootShow,
            text = 'Doanh Thu',
            font = ('Times', 25, 'bold', 'italic'),
            fg = 'Black',
            bg = '#dff9fb'
            )
        lb_Content.place(x=300,y=20)
    def labelTotalDoanhThu(self):
        lb_Content = tk.Label(
            self.rootShow,
            text = 'Tổng doanh thu: ' + str(self.crud.ToTalMoney())+ " VNĐ ",
            font = ('Times', 12, 'bold', 'italic'),
            fg = 'Black',
            bg = '#dff9fb'
            )
        lb_Content.place(x=20,y=100)
    def labelTotalMon(self):
        lb_Content = tk.Label(
            self.rootShow,
            text = 'Tổng món đã phục vụ: ' + str(self.crud.ToTalFood()) + " Món ",
            font = ('Times', 12, 'bold', 'italic'),
            fg = 'Black',
            bg = '#dff9fb'
            )
        lb_Content.place(x=20,y=150)

    def buttonStatic(self):
        btn_ADD = tk.Button(
            self.rootShow,
            text = 'Xem biểu đồ',
            font = 'Heveltica 10 bold',
            width = 15,
            command = self.ShowStatic
            )
        btn_ADD.place(x=20,y=250)
#====================Button==============
    def OptionFood(self):
        OPTIONS = [
                    "Sort món",
                    "Tên",
                    "Số lượng giảm",
                    "Số lượng tăng",
                    ]
        variable = StringVar(self.rootShow)
        variable.set("Sort món")
        self.et_Sex = OptionMenu(self.rootShow, variable, *OPTIONS,command = self.SortFood)
        #self.et_Sex.configure(background='#dff9fb', foreground='black', activebackground='#dff9fb', activeforeground='#30336b', highlightthickness=0)
        self.et_Sex.place(x=320, y = 70)

    def OptionBill(self):
        OPTIONS = [
                    "Sort Bill",
                    "ID tăng",
                    "ID giảm",
                    "Số tiền tăng",
                    "Số tiền giảm",
                    "Ngày thu tăng",
                    "Ngày thu giảm",
                    ]
        variable = StringVar(self.rootShow)
        variable.set("Sort Bill")
        self.et_Sex = OptionMenu(self.rootShow, variable, *OPTIONS,command = self.SortBill)
        #self.et_Sex.configure(background='#dff9fb', foreground='black', activebackground='#dff9fb', activeforeground='#30336b', highlightthickness=0)
        self.et_Sex.place(x=700, y = 70)
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

#=================function=============
    def close(self):
        self.rootShow.destroy()
    def ShowStatic(self):
        formStatic = ShowSTatic()
        formStatic.display()
#=====================function Sort=============
    def SortBill(self,value):
            OPTIONS = [
                        "ID tăng",
                        "ID giảm",
                        "Số tiền tăng",
                        "Số tiền giảm",
                        "Ngày thu tăng",
                        "Ngày thu giảm",
                        ]
            if(value == OPTIONS[0]):
                self.SortID()
            if(value == OPTIONS[1]):
                self.SortIDReverse()
            if(value == OPTIONS[2]):
                self.SortMoney()
            if(value == OPTIONS[3]):
                self.SortMoneyReverse()
            if(value == OPTIONS[4]):
                self.SortDate()
            if(value == OPTIONS[5]):
                self.SortDateReverse()
    def SortID(self):
        self.crud.View(self.tree,"SELECT * FROM Bill  ORDER BY id ASC")
    def SortIDReverse(self):
        self.crud.View(self.tree,"SELECT * FROM Bill  ORDER BY id DESC")
    def SortMoney(self):
        self.crud.View(self.tree,"SELECT * FROM Bill  ORDER BY CAST(total AS float) ASC")
    def SortMoneyReverse(self):
        self.crud.View(self.tree,"SELECT * FROM Bill  ORDER BY CAST(total AS float) DESC")
    def SortDate(self):
        self.crud.View(self.tree,"SELECT * FROM Bill  ORDER BY Time ASC")
    def SortDateReverse(self):
        self.crud.View(self.tree,"SELECT * FROM Bill  ORDER BY Time DESC")


    def SortFood(self,value):
        OPTIONS = [
                    "Tên",
                    "Số lượng giảm",
                    "Số lượng tăng",
                    ]
        if(value == OPTIONS[0]):
            self.SortName()
        if(value == OPTIONS[1]):
            self.SortValue()
        if(value == OPTIONS[2]):
            self.SortValueReverse()
    def SortName(self):
        self.crud.View(self.tree2,"SELECT  ChiTietBill.name , sum(SoLuong) as SoLuong from ChiTietBill GROUP BY Name  ORDER BY name ASC")
    def SortValue(self):
        self.crud.View(self.tree2,"SELECT  ChiTietBill.name , sum(SoLuong) as SoLuong from ChiTietBill GROUP BY Name ORDER BY SoLuong ASC")
    def SortValueReverse(self):
        self.crud.View(self.tree2,"SELECT  ChiTietBill.name , sum(SoLuong) as SoLuong from ChiTietBill GROUP BY Name ORDER BY SoLuong DESC")
#=========================Function Search====================================
 
#=========================Function Filter====================================
    
#=========================Function Điểm danh====================================
   
#====================================================================

#=========================verif====================================

#====================================================================
