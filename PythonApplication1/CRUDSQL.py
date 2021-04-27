import sqlite3
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
class CRUD():
    def __init__(self):
        pass
    # connect to the database
    def connect(self):
        conn = sqlite3.connect("QlNhanVien.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS NhanVien(id INTEGER PRIMARY KEY, TenNhanvVien TEXT, NamSinh INTEGER,GioiTinh TEXT, ChucVu TEXT, LuongCoBan INTEGER, CaLamViec TEXT ,Thuong INTEGER,DiemDanh INTEGER )")
        conn.commit()
        conn.close()
##=====================       GetDatato Grid View ===============================
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

    def ShowStaff(self,tree,sql_Query):
        self.connect() 
        self.View(tree,sql_Query)

##===================================================================================
##=====================Add ===============================(id,name,birthyear,gender,rank,salary,sift,bonus,count)
    def Add(self,id,name,birthyear,gender,rank,salary,sift,bonus,count):
            stringSQL = "INSERT INTO NhanVien values(?,?,?,?,?,?,?,?,?)"
            conn = sqlite3.connect("QlNhanVien.db")
            mydata = (id,name,birthyear,gender,rank,salary,sift,bonus,count)
            cur = conn.cursor()
            cur.execute(stringSQL,mydata)
            conn.commit()
            conn.close()

    def AddStaff(self,id,name,birthyear,gender,rank,salary,sift,bonus,count):
        self.connect() 
        self.Add(id,name,birthyear,gender,rank,salary,sift,bonus,count)
##===================================================================================
##=====================Delete ===============================(id,name,birthyear,gender,rank,salary,sift,bonus,count)
    def Delete(self,id):
        stringSQL = "DELETE FROM NhanVien WHERE IdNhanVien = " + str(id)
        conn = sqlite3.connect("QlNhanVien.db")
        cur = conn.cursor()
        cur.execute(stringSQL)
        conn.commit()
        conn.close()

    # connect to the database

    def DeleteStaff(self,id):
        self.connect() 
        self.Delete(id)

##=====================Update ===============================
    def Update(self,id,name,birthyear,gender,rank,salary,sift,bonus,count):
        stringSQL = "UPDATE NhanVien SET TenNhanVien = '" + name + "', NamSinh = " +str(birthyear)+", GioiTinh = '"+gender+"', ChucVu = '"+rank+"', LuongCoBan = "+str(salary)+", CaLamViec = '"+sift+"', Thuong = "+str(bonus)+", DiemDanh = "+str(count)+" Where IDNhanVien ="+str(id)
        conn = sqlite3.connect("QlNhanVien.db")
        cur = conn.cursor()
        cur.execute(stringSQL)
        conn.commit()
        conn.close()

    # connect to the database

    def UpdateStaff(self,id,name,birthyear,gender,rank,salary,sift,bonus,count):
        self.connect() 
        self.Update(id,name,birthyear,gender,rank,salary,sift,bonus,count)
##===================================================================================
##=====================GetData ===============================
    def getData(self,sql_Query):
        conn = sqlite3.connect("QlNhanVien.db")
        cur = conn.cursor()
        cur.execute(sql_Query)
        rows = cur.fetchall()
        conn.close()
        out = [item for t in rows for item in t]
        return out
##===================================================================================
##=====================GetID NhanVien ===============================
    def getIDNhanVien(self):
        return self.getData("SELECT IDNhanVien from NhanVien")
##===================================================================================
##=====================Cham cong ===============================
    def ChamCong(self,Id,Cong):
        conn = sqlite3.connect("QlNhanVien.db")
        cur = conn.cursor()
        cur.execute("UPDATE NhanVien SET Diemdanh = "+str(Cong)+" WHERE IDnhanvien = "+ str(Id))
        conn.commit()
        conn.close()
##===================================================================================