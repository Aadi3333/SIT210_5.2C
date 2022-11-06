from tkinter import *
import tkinter.font
from turtle import width
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)


Redled = LED(14)
Blueled = LED(15)
Greenled = LED(18)

window = Tk()
window.title("LED Toggler")
window.geometry("400x400")
myFont = tkinter.font.Font(family="Helvetica", size=12, weight="bold")

def RedLed():
    if Redled.is_lit:
        Redled.off()
        ledButton1["text"] = "Turn RED LED on"
    else:
        Redled.on()
        Blueled.off()
        Greenled.off()
        ledButton1["text"] = "Turn RED Led off"


def BlueLed():
    if Blueled.is_lit:
        Blueled.off()
        ledButton2["text"] = "Turn Blue Led on"
    else:
        Blueled.on()
        Redled.off()
        Greenled.off()
        ledButton2["text"] = "Turn Blue Led off"


def GreenLed():
    if Greenled.is_lit:
        Greenled.off()
        ledButton3["text"] = "Turn Green Led on"
    else:
        Greenled.on()
        Redled.off()
        Blueled.off()
        ledButton3["text"] = "Turn Green Led off"
      

def close():
    RPi.GPIO.cleanup()
    window.destroy()
    exit()
    



ledButton1 = Radiobutton(window,text="RED LED",font=myFont, command= RedLed, bg= 'red', height=3, width=20)
ledButton1.grid(row=1,column=3)

ledButton2 = Radiobutton(window,text="Blue LED", font=myFont, command= BlueLed, bg= 'blue', height=3, width=20)
ledButton2.grid(row=2,column=3)

ledButton3 = Radiobutton(window,text="GREEN LED", font=myFont, command= GreenLed, bg= 'green', height=3, width=20)
ledButton3.grid(row=3,column=3)

exitButton = Radiobutton(window,text ="Exit Button", font=myFont, command= close, bg='white',height=3,width=20)
exitButton.grid(row =4,column=3)

window.protocol("WM_DELETE_WINDOW", close)
window.mainloop()
