import sqlite3
from tkinter import messagebox
class mydb(object):
    """description of class"""
    def connect(self):
        conn = sqlite3.connect("QlNhanVien.db")
        cur = conn.cursor()
        conn.commit()
        conn.close()


    def insert(self,username, password):
        conn = sqlite3.connect("QlNhanVien.db")
        cur = conn.cursor()
        query = "SELECT * FROM login WHERE username = '" + username + "'"
        if len(self.getData(query)) != 0:
            messagebox.showerror("Register", "Lỗi: Username đã tồn tại")
        else:
            cur.execute("INSERT INTO login VALUES(NULL,?,?)",(username,password))
            messagebox.showinfo("Register", "Tạo tài khoản thành công")
            conn.commit()
        conn.close()





    def getData(self,sql_Query):
        conn = sqlite3.connect("QlNhanVien.db")
        cur = conn.cursor()
        cur.execute(sql_Query)
        rows = cur.fetchall()
        conn.close()
        return rows
