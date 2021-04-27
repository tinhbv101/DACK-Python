from os import environ
import calendar
import numpy as np
import matplotlib as mpl 
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import sqlite3
from SQLBill import *
from matplotlib import colors as mcolors

class ShowSTatic():
    def __init__(self):
        self.crud = SQLBILL()
        self.suppress_qt_warnings()
        
    def display(self):
        DS = self.LayCacMonGiongNhau()
        #DSTemp = []
        #DSTemp.append(DS[0])
        self.DrawStatic(DS)

    def suppress_qt_warnings(self):
        environ["QT_DEVICE_PIXEL_RATIO"] = "0"
        environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
        environ["QT_SCREEN_SCALE_FACTORS"] = "1"
        environ["QT_SCALE_FACTOR"] = "1"

    def LayCacMonGiongNhau(self):
        DS = self.crud.SoLuongMonTrongNgay()
        Listtemp = self.crud.LaytenMonAn()
        ListName = []
        DSBD =[]
        ResultArr= []
        for item in Listtemp:
            ListName.append(item[0].strip())
        for item in ListName:
            TempArrDate = []
            TempArrSL = []
            for item2 in DS:
                if(item == item2[1].strip()) :
                    TempArrDate.append(int(item2[0][0])*10 +int(item2[0][1]))
                    TempArrSL.append(item2[2])
            TempArr =[TempArrDate,TempArrSL,item]
            DSBD.append(TempArr)
        for item in DSBD:
            TempArrDate = []
            TempArrSL = []
            for i in range(31):
                TempArrDate.append(i+1)
                TempArrSL.append(0)
            for j in range(len(item[0])):
                TempArrSL[item[0][j]] = item[1][j]
            TempArr =[TempArrDate,TempArrSL,item[2]]
            ResultArr.append(TempArr)
        return ResultArr



    def DrawStatic(self,DS):
        self.fig, ax = plt.subplots()
        lines = []
        ax.set_title('Biểu đồ số lượng các món đã bán trong tháng của quán')
        for item in DS:
            line, = ax.plot(item[0], item[1], lw=2, label=item[2])
            lines.append(line)
        leg = ax.legend(fancybox=True, shadow=True)
        self.lined = {}  
        for legline, origline in zip(leg.get_lines(), lines):
            legline.set_picker(True)  
            self.lined[legline] = origline
        self.fig.canvas.mpl_connect('pick_event', self.on_pick)
        plt.show()
    def on_pick(self,event):
        legline = event.artist
        origline = self.lined[legline]
        visible = not origline.get_visible()
        origline.set_visible(visible)
        legline.set_alpha(1.0 if visible else 0.2)
        self.fig.canvas.draw()
