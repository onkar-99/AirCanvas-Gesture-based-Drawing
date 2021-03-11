from tkinter import *
import tkinter as tk
import track
import cv2
import numpy as np
import draw
import people_count
import start_gui
import ctypes 
global low
low=(0,0,0,0)
def adjustWindow(window):
    w = 1000
    h = 750
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w,h,x,y))
    window.resizable(False,False)
 
def instructions():
    ins = Tk() 
    ins.title("Welcome")
    adjustWindow(ins)
    Label(ins, text="Instructions", width='50', height="3", font=("Calibri", 30,'bold'), fg='white', bg='purple', anchor = CENTER).place(x=-80, y=-40)
    Label(ins, text="", bg='light blue', width='400', height='500').place(x=0, y=100)
    Label(ins, text="Marker", font=("Calibri", 20,'bold'), fg='black', bg='light blue', anchor = CENTER).place(x=100, y=200)
    Label(ins, text="Press: s-save | Esc-Quit", font=("Calibri", 15,'bold'), fg='black', bg='light blue', anchor = CENTER).place(x=100, y=250)
    
    Label(ins, text="Draw", font=("Calibri", 20,'bold'), fg='black', bg='light blue', anchor = CENTER).place(x=100, y=400)
    Label(ins, text="b-stop | space-start | c-clear", font=("Calibri", 15,'bold'), fg='black', bg='light blue', anchor = CENTER).place(x=100, y=450)
    Label(ins, text="d-done | n-new object", font=("Calibri", 15,'bold'), fg='black', bg='light blue', anchor = CENTER).place(x=100, y=500)

    Button(ins, text='Back', width=20, font=("Open Sans", 15, 'bold'), bg='purple', fg='white',command=ins.destroy).place(x=400, y=600)
    ins.mainloop()
    
def tracker():
    global low,high
    low=(0,0,0,0)
    low,high=track.hsv()
    
def draw_doodle(low):
    if len(low)==3:
        start_gui.menu(low,high)
    else:
        r=ctypes.windll.user32.MessageBoxW(0, "Please select marker first", "Dialogue Box", 0)

    #draw.draw_img()


screen = Tk() 
screen.title("Welcome")
adjustWindow(screen)
Label(screen, text="Lets Play DOODLE !!!", width='50', height="3", font=("Calibri", 30,'bold'), fg='white', bg='purple', anchor = CENTER).place(x=-80, y=-40)
Label(screen, text="", bg='light blue', width='400', height='500').place(x=0, y=100)
Button(screen, text='Start your game', width=20, font=("Open Sans", 20, 'bold'), bg='pink', fg='black', command=lambda: draw_doodle(low)).place(x=300, y=200)
Button(screen, text='Instructions', width=20, font=("Open Sans", 20, 'bold'), bg='pink', fg='black',  command = instructions).place(x=300, y=300)
Button(screen, text='Change Marker', width=20, font=("Open Sans", 20, 'bold'), bg='pink', fg='black',  command = tracker).place(x=300, y=400)

screen.mainloop() 
