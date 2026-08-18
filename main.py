from tkinter import *
from tkinter import ttk

black = "#080808"
grey = "#2e2b2a"
orange = "#ba3c06"

window = Tk()

window.title("Calculadora")
window.geometry("235x318")
window.config(bg=black)

frame_window = Frame(window, width=235, height=50, bg=grey)
frame_window.grid(row=0, column=0)

second_frame = Frame(window, width=235, height=268, bg=orange)
second_frame.grid(row=1, column=0)
window.mainloop()