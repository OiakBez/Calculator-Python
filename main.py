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
window.geometry("235x310")
window.config(bg=black)

#Configuração Display (Frames)
frame_window = Frame(window, width=235, height=50, bg=grey)
frame_window.grid(row=0, column=0)

second_frame = Frame(window, width=235, height=268)
second_frame.grid(row=1, column=0)

#global_values
global_values = ''

#Valores na tela
def values_in_window(event):
    global global_values

    global_values = global_values+str(event)
    #result = eval(global_values)

    text_variable.set(global_values)

#Label de resultado
text_variable = StringVar()

label_window = Label(frame_window, textvariable=text_variable, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=grey, fg=white)
label_window.place(x=0,y=0)

#Configuração de botões
clear_button = Button(second_frame, text = "C", width=14, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
clear_button.place(x=0, y=0)
porcentag_button = Button(second_frame, command=lambda:values_in_window('%'), text = "%", width=6, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
porcentag_button.place(x=115, y=0)
divisao_button = Button(second_frame,command=lambda:values_in_window('/'), text = "/", width=7, height=2, font=('Ivy 13 bold'), bg=orange, fg=white, relief=RAISED, overrelief=RIDGE)
divisao_button.place(x=175, y=0)

seven_button = Button(second_frame,command=lambda:values_in_window('9'), text = "9", width=6, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
seven_button.place(x=0, y=52)
eight_button = Button(second_frame,command=lambda:values_in_window('8'), text = "8", width=6, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
eight_button.place(x=57.5, y=52)
nine_button = Button(second_frame,command=lambda:values_in_window('7'), text = "7", width=6, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
nine_button.place(x=115, y=52)
multp_button = Button(second_frame,command=lambda:values_in_window('*'), text = "x", width=7, height=2, font=('Ivy 13 bold'), bg=orange, fg=white, relief=RAISED, overrelief=RIDGE)
multp_button.place(x=175, y=52)

seven_button = Button(second_frame,command=lambda:values_in_window('6'), text = "6", width=6, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
seven_button.place(x=0, y=104)
eight_button = Button(second_frame,command=lambda:values_in_window('5'), text = "5", width=6, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
eight_button.place(x=57.5, y=104)
nine_button = Button(second_frame,command=lambda:values_in_window('4'), text = "4", width=6, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
nine_button.place(x=115, y=104)
multp_button = Button(second_frame,command=lambda:values_in_window('+'), text = "+", width=7, height=2, font=('Ivy 13 bold'), bg=orange, fg=white, relief=RAISED, overrelief=RIDGE)
multp_button.place(x=175, y=104)

seven_button = Button(second_frame,command=lambda:values_in_window('3'), text = "3", width=6, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
seven_button.place(x=0, y=156)
eight_button = Button(second_frame,command=lambda:values_in_window('2'), text = "2", width=6, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
eight_button.place(x=57.5, y=156)
nine_button = Button(second_frame,command=lambda:values_in_window('1'), text = "1", width=6, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
nine_button.place(x=115, y=156)
multp_button = Button(second_frame,command=lambda:values_in_window('-'), text = "-", width=7, height=2, font=('Ivy 13 bold'), bg=orange, fg=white, relief=RAISED, overrelief=RIDGE)
multp_button.place(x=175, y=156)

point_button = Button(second_frame,command=lambda:values_in_window('.'), text = ".", width=6, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
point_button.place(x=0, y=208)
zero_button = Button(second_frame,command=lambda:values_in_window('0'), text = "0", width=6, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
zero_button.place(x=57.5, y=208)
equal_button = Button(second_frame, text = "=", width=12, height=2, font=('Ivy 13 bold'), bg=orange, fg=white, relief=RAISED, overrelief=RIDGE)
equal_button.place(x=120, y=208)

#functions


#mainloop
window.mainloop()