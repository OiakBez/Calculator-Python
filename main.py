from tkinter import *
from tkinter import ttk

class Calculadora():
    def __init__(self):
        
        #cores
        self.black = "#080808"
        self.grey = "#2e2b2a"
        self.orange = "#ba3c06"
        self.white = "#fafafa"

        #Configuração da janela (window)
        self.window = Tk()

        self.window.title("Calculadora")
        self.window.geometry("235x310")
        self.window.config(bg=self.black)

        #Configuração Display (Frames)
        self.frame_window = Frame(self.window, width=235, height=50, bg=self.grey)
        self.frame_window.grid(row=0, column=0)

        self.second_frame = Frame(self.window, width=235, height=268)
        self.second_frame.grid(row=1, column=0)

        #global_values
        self.global_values = ''

        #Valores na tela
        def values_in_window(event):
            self.global_values = self.global_values+str(event)
            text_variable.set(self.global_values)

        #functions
        def clear():
            self.global_values = ''
            text_variable.set('')
        
        def calculate():
            try:
                result = eval(self.global_values)
                self.global_values = str(result)
                text_variable.set(self.global_values)
            except:
                text_variable.set('Error')
                self.global_values = ''

        #Label de resultado
        text_variable = StringVar()

        label_window = Label(self.frame_window, textvariable=text_variable, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=self.grey, fg=self.white)
        label_window.place(x=0,y=0)

        #Configuração de botões
        clear_button = Button(self.second_frame,command=lambda:clear(), text = "C", width=14, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
        clear_button.place(x=0, y=0)
        porcentag_button = Button(self.second_frame, command=lambda:values_in_window('%'), text = "%", width=6, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
        porcentag_button.place(x=115, y=0)
        divisao_button = Button(self.second_frame,command=lambda:values_in_window('/'), text = "/", width=7, height=2, font=('Ivy 13 bold'), bg=self.orange, fg=self.white, relief=RAISED, overrelief=RIDGE)
        divisao_button.place(x=175, y=0)

        seven_button = Button(self.second_frame,command=lambda:values_in_window('9'), text = "9", width=6, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
        seven_button.place(x=0, y=52)
        eight_button = Button(self.second_frame,command=lambda:values_in_window('8'), text = "8", width=6, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
        eight_button.place(x=57.5, y=52)
        nine_button = Button(self.second_frame,command=lambda:values_in_window('7'), text = "7", width=6, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
        nine_button.place(x=115, y=52)
        multp_button = Button(self.second_frame,command=lambda:values_in_window('*'), text = "x", width=7, height=2, font=('Ivy 13 bold'), bg=self.orange, fg=self.white, relief=RAISED, overrelief=RIDGE)
        multp_button.place(x=175, y=52)

        six_button = Button(self.second_frame,command=lambda:values_in_window('6'), text = "6", width=6, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
        six_button.place(x=0, y=104)
        five_button = Button(self.second_frame,command=lambda:values_in_window('5'), text = "5", width=6, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
        five_button.place(x=57.5, y=104)
        four_button = Button(self.second_frame,command=lambda:values_in_window('4'), text = "4", width=6, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
        four_button.place(x=115, y=104)
        add_button = Button(self.second_frame,command=lambda:values_in_window('+'), text = "+", width=7, height=2, font=('Ivy 13 bold'), bg=self.orange, fg=self.white, relief=RAISED, overrelief=RIDGE)
        add_button.place(x=175, y=104)

        three_button = Button(self.second_frame,command=lambda:values_in_window('3'), text = "3", width=6, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
        three_button.place(x=0, y=156)
        two_button = Button(self.second_frame,command=lambda:values_in_window('2'), text = "2", width=6, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
        two_button.place(x=57.5, y=156)
        one_button = Button(self.second_frame,command=lambda:values_in_window('1'), text = "1", width=6, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
        one_button.place(x=115, y=156)
        sub_button = Button(self.second_frame,command=lambda:values_in_window('-'), text = "-", width=7, height=2, font=('Ivy 13 bold'), bg=self.orange, fg=self.white, relief=RAISED, overrelief=RIDGE)
        sub_button.place(x=175, y=156)

        point_button = Button(self.second_frame,command=lambda:values_in_window('.'), text = ".", width=6, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
        point_button.place(x=0, y=208)
        zero_button = Button(self.second_frame,command=lambda:values_in_window('0'), text = "0", width=6, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
        zero_button.place(x=57.5, y=208)
        equal_button = Button(self.second_frame,command=lambda:calculate(), text = "=", width=12, height=2, font=('Ivy 13 bold'), bg=self.orange, fg=self.white, relief=RAISED, overrelief=RIDGE)
        equal_button.place(x=120, y=208)

#mainloop
if __name__=="__main__":
    app = Calculadora()
    app.window.mainloop()
