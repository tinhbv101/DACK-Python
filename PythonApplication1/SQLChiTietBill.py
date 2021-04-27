
import sqlite3
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
class SQLChiTietBill():
    def __init__(CTbill):
        pass
    # connect to the database
    def connect(CTbill):
        conn = sqlite3.connect("QlNhanVien.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS ChiTietBill(ID TEXT, Name TEXT , SoLuong TEXT, PRIMARY KEY(ID,Name))")
        conn.commit()
        conn.close()
##=====================Add ===============================
    def Add(CTbill,id, name, sl):
            stringSQL = "INSERT INTO ChiTietBill values(?,?,?)"
            conn = sqlite3.connect("QlNhanVien.db")
            mydata = (id,name,sl)
            cur = conn.cursor()
            cur.execute(stringSQL,mydata)
            conn.commit()
            conn.close()

    def AddCTBill(CTbill,id,name,sl):
        CTbill.connect() 
        CTbill.Add(id,name,sl)
##===================================================================================

