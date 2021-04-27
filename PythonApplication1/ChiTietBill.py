import AddForm as Addform
from EditForm import *
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import sqlite3
from SQLBill import *
from SQLChiTietBill import *

class ShowChitietBill():
    def __init__(self,IDBill):
        self.IDBill = IDBill
    def display(self):
        self.rootShow = tk.Tk()
        self.rootShow.title = 'Doanh Thu'
     
        self.crud = SQLBILL()
        w = 300
        h = 700
        ws = self.rootShow.winfo_screenwidth()
        hs = self.rootShow.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.rootShow.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.rootShow.configure(bg = '#dff9fb')
        self.labelContent()
        self.labelBill()
#===============Label====================
    def labelContent(self):
        lb_Content = tk.Label(
            self.rootShow,
            text = 'Chi tiết Bill: '+ str(self.IDBill),
            font = ('Times', 15, 'italic'),
            fg = 'Black',
            bg = '#dff9fb'
            )
        lb_Content.pack(pady=30)

    def labelBill(self):
        DSPrice ={"Thạch rau câu": 5000,"Thạch Thủy Tinh": 5000,"Trân châu đen": 5000,"Trân châu trắng": 5000,"Trân châu hoàng kim": 5000,"Plan": 5000,"Nước Ngọt" : 15000,"Trà Sữa Thái Xanh" : 30000,"Chocolate Đá Xay" : 30000,"Trà Chanh" : 20000,"Cà Phê Đá": 20000,"Cà Phê Sữa" : 25000,"Nước Dừa" :25000, "Nước Cam" : 25000, "Nước Suối" : 10000}
        listfood = self.crud.FoodForBill(self.IDBill)
        tt = 0
        lb_Content = tk.Label(
            self.rootShow,
            text = 'Các món đã gọi ',
            font = ('Times', 15, 'italic'),
            fg = 'Black',
            bg = '#dff9fb'
            )
        lb_Content.pack(pady=20)
        for index,item in enumerate(listfood):
            Label(self.rootShow,text="Tên : "+ item[0] +"  SL: "+ item[1]+ "  Giá:  "+ str(DSPrice[str(item[0]).strip()] *int(item[1])) + "VNĐ").pack(anchor = "w" ,padx =10,pady=10)
            tt = tt +DSPrice[str(item[0]).strip()] *int(item[1])
        lb_Total = tk.Label(
            self.rootShow,
            text = 'Tổng tiền '+ str(tt)+ " VNĐ ",
            font = ('Times', 15, 'italic'),
            fg = 'Black',
            bg = '#dff9fb'
            )
        lb_Total.pack(pady=20)
#===============Funtion====================
    
    