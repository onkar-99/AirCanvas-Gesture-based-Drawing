import draw
from matplotlib import pyplot as plt
#from keras.models import load_model
from tkinter import *
import random
def count(names,low,high):
    n=len(names)
    scores=[]
    for i in range(0,n):
        s=draw.draw_img(names[i],low,high)
        scores.append(s)
    print('pc-------------')
    print(scores)
    def adjustWindow(window):
        w = 1000
        h = 750
        ws = window.winfo_screenwidth()
        hs = window.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        window.geometry('%dx%d+%d+%d' % (w,h,x,y))
        window.resizable(False,False)
    screen = Tk() 
    screen.title("Results!!!")
    adjustWindow(screen)
    Label(screen, text="RESULTS !!!", width='50', height="3", font=("Calibri", 30,'bold'), fg='white', bg='purple', anchor = CENTER).place(x=-80, y=-40)
    Label(screen, text="", bg='light blue', width='400', height='500').place(x=0, y=100)
    for i in range(0,n):
        Label(screen, text="{}'s Score -> {}".format(names[i],scores[i]), font=("Calibri", 20,'bold'), fg='black', bg='light blue', anchor = CENTER).place(x=150, y=200+i*50)
    screen.mainloop() 

