#importing the figlet module
from tkinter import font
from turtle import filling, width
import pyfiglet as pfg

#pfg.figlet_format('inputText', font='typeoffont')

#taking the input text for the default font
#res = pfg.figlet_format("Happy Birthday Daisy", font="slant", width=50)

#taking the input text for 3-D format
#res = pfg.figlet_format("Welcome",font="3-d")

#taking the input text foralphabet format
#res = pfg.figlet_format("Welcome",font="alphabet")


#taking the input text for the doh format   
res = pfg.figlet_format("Happy Birthday Daisy",font="doh", width=250)

#Printing the output
print("The input text printed in the default format will look as follows")
print(res)

#using the 