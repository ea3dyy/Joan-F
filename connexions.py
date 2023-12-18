#! /usr/bin/env python

import tkinter as Tkinter
from tkinter import Canvas
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()
# el pin 7 activa Raspberry 1. Inici desconnectat
GPIO.setup(7, GPIO.OUT, initial =0)
# el pin 11 activa Raspberry 2. Inici desconnectat
GPIO.setup(11, GPIO.OUT, initial =0)
# el pin 12 activa Raspberry 3. Inici desconnectat
GPIO.setup(12, GPIO.OUT, initial =0)
# el pin 13 activa Raspberry 4. Inici desconnectat
GPIO.setup(13, GPIO.OUT, initial =0)
# el pin 15 activa Disp 1 (220V). Inici desconnectat
GPIO.setup(15, GPIO.OUT, initial =0)
# el pin 16 activa Disp 2 (220V). Inici desconnectat
GPIO.setup(16, GPIO.OUT, initial =0)
# el pin 18 activa Disp 3 (220V). Inici desconnectat
GPIO.setup(18, GPIO.OUT, initial =0)
# el pin 18 activa Disp 4 (220V). Inici desconnectat
GPIO.setup(22, GPIO.OUT, initial =0)

# variables inicials dels pins
# pin7 = 7
# pin11 = 11

# el pin 7 activa Raspberry 1. Inici desconnectat
# GPIO.output(7, GPIO.LOW)
# el pin 11 activa Raspberry 1. Inici desconnectat
# GPIO.output(11, GPIO.LOW)

finestra=Tkinter.Tk()
finestra.title("Connexions")
finestra.geometry("1280x760")
finestra.configure(bg='#00FF00')

# Els collons de Canvas

# canvas=Canvas(finestra)
canvas=Canvas(finestra, width=1280, heigh=720, bg='#00FF00')
canvas.create_rectangle(10,0, 1270,50, fill="blue")
canvas.create_rectangle(10,330, 1270,380, fill="blue")
canvas.pack()
# sha acabat la importacio del  canvas 
# primera linia amb canvas
canvas.create_line(10, 50, 1270, 50, fill="green", width=3)
# segona linia
canvas.create_line(10, 330, 1270, 330, fill="green", width=3)
# tercera linia
canvas.create_line(10, 380, 1270, 380, fill="green", width=3)

# Valors inicials desconnectats 
estat01 = Tkinter.Label(finestra, text = "    Desconnectat 1   ", font=("Arial", 15), bg="green", fg="white").place(x=88,y=64)
canvas.create_rectangle(87,58, 273,99, fill="green")
estat02 = Tkinter.Label(finestra, text = "    Desconnectat 2  ", font=("Arial", 15), bg="green", fg="white").place(x=392,y=64)
canvas.create_rectangle(391,58, 572,99, fill="green")
estat03 = Tkinter.Label(finestra, text = " Desconnectat 3   ", font=("Arial", 15), bg="green", fg="white").place(x=707,y=64)
canvas.create_rectangle(690,58, 874,99, fill="green")
estat04 = Tkinter.Label(finestra, text = "Desconnectat 4  ", font=("Arial", 15), bg="green", fg="white").place(x=1018,y=64)
canvas.create_rectangle(990,58, 1174,99, fill="green")
estat05 = Tkinter.Label(finestra, text = "  Desconnectat 5   ", font=("Arial", 15), bg="green", fg="white").place(x=100,y=392)
canvas.create_rectangle(90,388, 273,424, fill="green")
estat06 = Tkinter.Label(finestra, text = " Desconnectat 6   ", font=("Arial", 15), bg="green", fg="white").place(x=405,y=392)
canvas.create_rectangle(390,388, 573,424, fill="green")
estat07 = Tkinter.Label(finestra, text = " Desconnectat 7", font=("Arial", 15), bg="green", fg="white").place(x=710,y=392)
canvas.create_rectangle(690,388, 872,424, fill="green")
estat08 = Tkinter.Label(finestra, text = "  Desconnectat 8   ", font=("Arial", 15), bg="green", fg="white").place(x=1000,y=392)
canvas.create_rectangle(990,388, 1174,424, fill="green")




# Funcions d operacions de cada boto
# Funcions de la Raspberry 1

def onr01():
    estat01 = Tkinter.Label(finestra, text = "       Connectat 1     ", font=("Arial", 15), bg="red", fg="white").place(x=89,y=64)
    canvas.create_rectangle(87,58, 273,99, fill="red")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7, GPIO.LOW)


def offr01(): 
    estat01 = Tkinter.Label(finestra, text = "    Desconnectat 1   ", font=("Arial", 15), bg="green", fg="white").place(x=88,y=64)
    canvas.create_rectangle(87,58, 273,99, fill="green")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7, GPIO.HIGH)

# Funcions de la Raspberry 2
def onr02():
    estat02 = Tkinter.Label(finestra, text = "      Connectat 2     ", font=("Arial", 15), bg="red", fg="white").place(x=393,y=64)
    canvas.create_rectangle(391,58, 572,99, fill="red")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT) 
    GPIO.output(11, GPIO.LOW)
def offr02():
    estat02 = Tkinter.Label(finestra, text = "    Desconnectat 2  ", font=("Arial", 15), bg="green", fg="white").place(x=392,y=64)
    canvas.create_rectangle(391,58, 572,99, fill="green")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    GPIO.output(11, GPIO.HIGH)

# Funcions de la Raspberry 3
def onr03():
    estat03 = Tkinter.Label(finestra, text = "    Connectat 3     ", font=("Arial", 15), bg="red", fg="white").place(x=707,y=64)
    canvas.create_rectangle(690,58, 874,99, fill="red")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT) 
    GPIO.output(12, GPIO.LOW)
def offr03():
    estat03 = Tkinter.Label(finestra, text = " Desconnectat 3   ", font=("Arial", 15), bg="green", fg="white").place(x=707,y=64)
    canvas.create_rectangle(690,58, 874,99, fill="green")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT) 
    GPIO.output(12, GPIO.HIGH)

# Funcions de la Raspberry 4
def onr04():
    estat04 = Tkinter.Label(finestra, text = "  Connectat 4     ", font=("Arial", 15), fg="white", bg="red").place(x=1018,y=64)
    canvas.create_rectangle(990,58, 1174,99, fill="red")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(13, GPIO.OUT) 
    GPIO.output(13, GPIO.LOW)
def offr04():
    estat04 = Tkinter.Label(finestra, text = "Desconnectat 4  ", font=("Arial", 15), bg="green", fg="white").place(x=1018,y=64)
    canvas.create_rectangle(990,58, 1174,99, fill="green")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(13, GPIO.OUT) 
    GPIO.output(13, GPIO.HIGH)

# Funcions del Dispositiu 1 220V
def disp01_on():
    estat01 = Tkinter.Label(finestra, text = "     Connectat 5     ", font=("Arial", 15), bg="red", fg="white").place(x=100,y=392)
    canvas.create_rectangle(90,388, 273,424, fill="red")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(15, GPIO.OUT) 
    GPIO.output(15, GPIO.LOW)
def disp01_off():
    estat01 = Tkinter.Label(finestra, text = "  Desconnectat 5   ", font=("Arial", 15), bg="green", fg="white").place(x=100,y=392)
    canvas.create_rectangle(90,388, 273,424, fill="green")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(15, GPIO.OUT) 
    GPIO.output(15, GPIO.HIGH)

# Funcions del Dispositiu 2 220V
def disp02_on():
    estat01 = Tkinter.Label(finestra, text = "    Connectat 6     ", font=("Arial", 15), bg="red", fg="white").place(x=405,y=392)
    canvas.create_rectangle(390,388, 573,424, fill="red")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16, GPIO.OUT) 
    GPIO.output(16, GPIO.LOW)
def disp02_off():
    estat01 = Tkinter.Label(finestra, text = " Desconnectat 6   ", font=("Arial", 15), bg="green", fg="white").place(x=405,y=392)
    canvas.create_rectangle(390,388, 573,424, fill="green")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16, GPIO.OUT) 
    GPIO.output(16, GPIO.HIGH)

# Funcions del Dispositiu 3 220V
def disp03_on():
    estat01 = Tkinter.Label(finestra, text = "    Connectat 7    ", font=("Arial", 15), bg="red", fg="white").place(x=710,y=392)
    canvas.create_rectangle(690,388, 872,424, fill="red")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(18, GPIO.OUT) 
    GPIO.output(18, GPIO.LOW)
def disp03_off():
    estat01 = Tkinter.Label(finestra, text = " Desconnectat 7  ", font=("Arial", 15), bg="green", fg="white").place(x=710,y=392)
    canvas.create_rectangle(690,388, 872,424, fill="green")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(18, GPIO.OUT) 
    GPIO.output(18, GPIO.HIGH)

# Funcions del Dispositiu 4 220V
def disp04_on():
    estat01 = Tkinter.Label(finestra, text = "    Connectat 8      ", font=("Arial", 15), bg="red", fg="white").place(x=1000,y=392)
    canvas.create_rectangle(990,388, 1174,424, fill="red")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(22, GPIO.OUT) 
    GPIO.output(22, GPIO.LOW)
def disp04_off():
    estat01 = Tkinter.Label(finestra, text = "  Desconnectat 8   ", font=("Arial", 15), bg="green", fg="white").place(x=1000,y=392)
    canvas.create_rectangle(990,388, 1174,424, fill="green")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(22, GPIO.OUT) 
    GPIO.output(22, GPIO.HIGH)

# titols de cada dispositiu

titol1 = Tkinter.Label(finestra, text="Rasberry 1", font=("Arial Black",20), bg="blue", fg="white").place(x=110,y=10)
titol2 = Tkinter.Label(finestra, text="Rasberry 2", font=("Arial Black",20), bg="blue", fg="white").place(x=410,y=10)
titol3 = Tkinter.Label(finestra, text="Rasberry 3", font=("Arial Black",20), bg="blue", fg="white").place(x=710,y=10)
titol4 = Tkinter.Label(finestra, text="Rasberry 4", font=("Arial Black",20), bg="blue", fg="white").place(x=1010,y=10)
titol5 = Tkinter.Label(finestra, text="Disp.1 (220V)", font=("Arial Black",20),bg="blue", fg="white").place(x=90,y=340)
titol6 = Tkinter.Label(finestra, text="Disp.2 (220V)", font=("Arial Black",20), bg="blue", fg="white").place(x=390,y=340)
titol7 = Tkinter.Label(finestra, text="Disp.3 (220V)", font=("Arial Black",20), bg="blue", fg="white").place(x=690,y=340)
titol8 = Tkinter.Label(finestra, text="Disp.4 (220V)", font=("Arial Black",20), bg="blue", fg="white").place(x=990,y=340)

# Tots els botons

# Botons de Raspberry 1
raspberry1on=Tkinter.Button(finestra, text="On", font=("Verdana",15), width=12, height=3, command = onr01).place(x=90,y=112)
rasbberry1off=Tkinter.Button(finestra, text="Off", font=("Verdana",15), width=12, height=3, command = offr01).place(x=90,y=213)

# Botons de Raspberry 2

raspberry2on=Tkinter.Button(finestra, text="On", font=("Verdana",15), width=12, height=3, command = onr02).place(x=390,y=112)
raspberry2off=Tkinter.Button(finestra, text="Off", font=("Verdana",15), width=12, height=3, command = offr02).place(x=390,y=213)

# Botons de Raspberry 3
raspberry3on=Tkinter.Button(finestra, text="On", font=("Verdana",15), width=12, height=3, command = onr03).place(x=690,y=112)
raspberry3off=Tkinter.Button(finestra, text="Off", font=("Verdana",15), width=12, height=3, command = offr03).place(x=690,y=213)

# Botons de Raspberry 4
raspberry4on=Tkinter.Button(finestra, text="On", font=("Verdana",15), width=12, height=3, command = onr04).place(x=990,y=112)
raspberry4off=Tkinter.Button(finestra, text="Off", font=("Verdana",15), width=12, height=3, command = offr04).place(x=990,y=213)

# Botons de Disp 1
button9=Tkinter.Button(finestra, text="On", font=("Verdana",15), width=12, height=3, command = disp01_on).place(x=90,y=437)
button10=Tkinter.Button(finestra, text="Off", font=("Verdana",15), width=12, height=3, command = disp01_off).place(x=90,y=539)

# Botons de Disp 2
button11=Tkinter.Button(finestra, text="On", font=("Verdana",15), width=12, height=3, command = disp02_on).place(x=390,y=437)
button12=Tkinter.Button(finestra, text="Off", font=("Verdana",15), width=12, height=3, command = disp02_off).place(x=390,y=539)

# Botons de Disp 3
button13=Tkinter.Button(finestra, text="On", font=("Verdana",15), width=12, height=3, command = disp03_on).place(x=690,y=437)
button14=Tkinter.Button(finestra, text="Off", font=("Verdana",15), width=12, height=3, command = disp03_off).place(x=690,y=539)

# Botons de Disp 4
button15=Tkinter.Button(finestra, text="On", font=("Verdana",15), width=12, height=3, command = disp04_on).place(x=990,y=437)
button16=Tkinter.Button(finestra, text="Off", font=("Verdana",15), width=12, height=3, command = disp04_off).place(x=990,y=539)



GPIO.cleanup()
finestra.mainloop()


