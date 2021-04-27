import numpy as np
import matplotlib as mpl 
import matplotlib.pyplot as plt
from AddForm import *
from ShowStaff import *
from EditForm import *
from DoanhThu import *
from Static import *
from LoginForm import *
from class1 import *



id = 19110344
name="Nguyen Le Hoang Ha"
birthyear = 2999
gender ="Nam"
rank = "Xuât nhập kho"
salary = 10000
sift = "sang"
bonus = 0
count = 0

crud = CRUD()
#form = ShowForm("SELECT * FROM NhanVien")
#crud.addstaff(id,name,birthyear,gender,rank,salary,sift,bonus,count)
#crud.deletestaff(19110345)
#crud.UpdateStaff(id,name,birthyear,gender,rank,salary,sift,bonus,count)
#form.MainShow()
#form = EditForm(id,name,birthyear,gender,rank,salary,sift,bonus,count)
#form.guiForm()
#print(crud.getData("SELECT IDNhanVien from NhanVien"))
#form2 = AddForm()
#form2.guiForm()


#=======Form Nhan Vien
frm = ManageMenu()
#frm.display()



#======QLNV====
#form1 = ShowForm()
#form1.display()
#form1.MainShow()



#====Doanh thu===
#form3 = ShowBill()
#form3.display()
#form3.MainShow()




#formStatic = ShowSTatic()
#formStatic.display()


frmLogin = LoginForm()
frmLogin.setupLoginForm()


#cls = class1()
#cls.setupForm()

