import sqlite3
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
class SQLBILL():
    def __init__(self):
        pass
    # connect to the database
    def connect(self):
        conn = sqlite3.connect("QlNhanVien.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Bill(Time TEXT , Total TEXT, id TEXT PRIMARY KEY)")
        conn.commit()
        conn.close()
##=====================Add ===============================
    def Add(self,time, total, id):
            stringSQL = "INSERT INTO Bill values(?,?,?)"
            conn = sqlite3.connect("QlNhanVien.db")
            mydata = (time,total,id)
            cur = conn.cursor()
            cur.execute(stringSQL,mydata)
            conn.commit()
            conn.close()

    def AddBill(self,time,total,id):
        self.connect() 
        self.Add(time,total,id)
##===================================================================================
##=====================Show Bill===============================
    def View(self,tree,sql_Query):
        for row in tree.get_children():
            tree.delete(row)
        conn = sqlite3.connect("QlNhanVien.db")
        cur = conn.cursor()
        cur.execute(sql_Query)
        rows = cur.fetchall()    
        for row in rows:
            print(row) 
            tree.insert("", tk.END, values=row)        
        conn.close()

    def ShowBill(self,tree,sql_Query):
        self.connect() 
        self.View(tree,sql_Query)
##======================function===============================================
    def ToTalMoney(self):
        stringSQL = "SELECT sum(total) from Bill"
        conn = sqlite3.connect("QlNhanVien.db")
        cur = conn.cursor()
        cur.execute(stringSQL)
        rows = cur.fetchall()
        conn.close()
        return rows[0][0]

    def FoodForBill(self,ID):
        stringSQL = "SELECT name, SoLuong FROM ChiTietBill  Where ChiTietBill.id = '"+ID+"'"
        conn = sqlite3.connect("QlNhanVien.db")
        cur = conn.cursor()
        cur.execute(stringSQL)
        rows = cur.fetchall()
        conn.close()
        return rows

    def ToTalFood(self):
        stringSQL = "SELECT  sum(SoLuong) from ChiTietBill"
        conn = sqlite3.connect("QlNhanVien.db")
        cur = conn.cursor()
        cur.execute(stringSQL)
        rows = cur.fetchall()
        conn.close()
        return rows[0][0]

    def SoLuongMonTrongNgay(self):
        stringSQL = "SELECT Time,Name, Sum(SoLuong) FROM Bill INNER JOIN ChiTietBill on Bill.id = ChiTietBill.ID GROUP by Time,Name"
        conn = sqlite3.connect("QlNhanVien.db")
        cur = conn.cursor()
        cur.execute(stringSQL)
        rows = cur.fetchall()
        conn.close()
        return rows
    def LaytenMonAn(self):
        stringSQL = "SELECT DISTINCT Name FROM ChiTietBill"
        conn = sqlite3.connect("QlNhanVien.db")
        cur = conn.cursor()
        cur.execute(stringSQL)
        rows = cur.fetchall()
        conn.close()
        return rows