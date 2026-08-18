from tkinter import *
from tkinter import ttk

#cores
black = "#080808"
grey = "#2e2b2a"
orange = "#ba3c06"
white = "#fafafa"

#Configuração da janela (window)
window = Tk()

window.title("Calculadora")
window.geometry("235x318")
window.config(bg=black)

#Configuração Display (Frames)
frame_window = Frame(window, width=235, height=50, bg=grey)
frame_window.grid(row=0, column=0)

second_frame = Frame(window, width=235, height=268)
second_frame.grid(row=1, column=0)

#Configuração de botões
clear_button = Button(second_frame, text = "C", width=17, height=2)
clear_button.place(x=0, y=0)

porcentag_button = Button(second_frame, text = "%", width=6, height=2)
porcentag_button.place(x=125, y=0)

divisao_button = Button(second_frame, text = "/", width=7, height=2, bg=orange, fg=white)
divisao_button.place(x=175, y=0)
window.mainloop()