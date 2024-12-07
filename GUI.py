from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
from googletrans import Translator
from tkinter import message box

root = tk.Tk()
root.title("Language Translator")
root.geomentry("530x330")
root.maxsize(530,330)
root.minsize(530,330)
img = ImageTk.PhotoImage(Image.open("translator.png"))
label = label(image = img
              )
