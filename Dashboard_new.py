import cv2
import numpy as np 
import sqlite3
import os
from PIL import ImageTk
from tkinter import *
from matplotlib import pyplot as plt
from tkinter import filedialog
import PIL.Image, PIL.ImageTk


import mysql.connector as con
import tkinter.messagebox
global var

from tkinter import messagebox
global screen
import Image_capturing as ic

def main_screen():
    
    
    global screen3
    screen3=Tk()
    #screen3=Toplevel(screen)
   # var = StringVar()
    C = Canvas(screen3, bg="blue", height=250, width=300)
    filename = PhotoImage(file = "186040.gif")
    background_label = Label(screen3, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    C.pack()
    screen3.configure(background='white')
    screen3.title("DASHBOARD")
    screen3.geometry('1280x720')
    Label(screen3, text="Sign Language Prediction", bg="Grey", height=1, width=250,font=("Arial Bold", 20)).pack()
    Label(screen3, text="", bg="white").pack()
    Label(screen3, text="", bg="white").pack()

    Label(screen3, text="", bg="white").pack()
    b1 =  Button(screen3,text="Add Training Dataset",height=2,width=30,bg="black",fg="white",font=("Arial Bold", 13),command=train_images)
    
    b1.pack()
    
    Label(screen3, text="", bg="white").pack()
    b2=Button(screen3,text="Preprocess Dataset",height=2,width=30,bg="black",fg="white",font=("Arial Bold", 13),command=preprocessing)
    b2.pack()

    Label(screen3, text="", bg="white").pack()
    b3=Button(screen3,text="Build Model",height=2,width=30,bg="black",fg="white",font=("Arial Bold", 13),command=build_model)
    b3.pack()
    
    Label(screen3, text="", bg="white").pack()
    b5=Button(screen3,text="Predict Sign",height=2,width=30,bg="black",fg="white",font=("Arial Bold", 13),command=predict)
    b5.pack()
   
    Label(screen3, text="", bg="white").pack()
    b6 = Button(screen3, text="Voice Input", height=2, width=30, bg="black", fg="white", font=("Arial Bold", 13),
                command=voice)
    b6.pack()


    
    screen3.mainloop()
def predict():
    import Gesture_Recognize_sign

def train_images():
    global screen3
    global name1_
    
    screen3=Toplevel(screen3)
    screen3.configure(background='white')
    screen3.geometry('1280x720')
    Label(screen3, text="Sign Language Prediction", font=("Arial Bold", 25),bg="grey",width=250,height=2).pack()
    Label(screen3, text="", bg="white").pack()
    Label(screen3, text="", bg="white").pack()
    name = Label(screen3, text="Letter", height=2, bg="white",font=("Arial Bold", 11))
    name.pack()
    name1_ = Entry(screen3, width=60)
    name1_.pack()
   
   

    Label(screen3, text="", bg="white").pack()
    Label(screen3, text="", bg="white").pack()
    login = Button(screen3, text="Capture Images", height=2, width=30,command=capture,bg="black",fg="white",font=("Arial Bold", 13))
    login.pack()
    Label(screen3, text="", bg="white").pack()
    b6 = Button(screen3, text="Exit", height=2, width=30, bg="black", fg="white", font=("Arial Bold", 13),
                command=screen3.destroy)
    b6.pack()
    
def capture():
    a=name1_.get()
    ic.train(a)

def voice():
    import speetch as ss
    ss.call()
    img = cv2.imread('test.jpg',0)
    cv2.imshow('test',img)
    
    
def preprocessing():
    import Image_preprocessing

def build_model():
    import model
main_screen()


    







