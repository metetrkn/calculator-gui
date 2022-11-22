from tkinter import *
from math import sqrt

# app
class Application(Frame):
    def __init__(self, master): 
        super(Application, self).__init__(master)
        # the result on screen
        self.task = ""
        
        self.UserIn = StringVar()
        
        self.grid()
        
        # creates widgets
        self.create_widgets()


    # function to create widgets
    def create_widgets(self):

        # calculation screen
        self.user_input = Entry(self, bg="#5BC8AC", bd=29,
        insertwidth=4, width=24, textvariable=self.UserIn,
        font=("Vardana", 20, "bold"), justify=RIGHT)

        self.user_input.grid(columnspan=4)

        # default value on screen
        self.user_input.insert(0, "0")

        # button 7
        self.button1 = Button(self, bg="#beb9db", bd=12, text="7",
        padx=37, pady=25, font=("Helvetica", 20, "bold"), width=1,
        command= lambda:self.buttonClick(7)) 
        self.button1.grid(row=2, column=0, sticky=W)

        # button 8
        self.button2 = Button(self, bg="#beb9db", bd=12, text="8",
        padx=37, pady=25, font=("Helvetica", 20, "bold"), width=1,
        command= lambda:self.buttonClick(8)) 
        self.button2.grid(row=2, column=1, sticky=W)

        # button 9
        self.button3 = Button(self, bg="#beb9db", bd=12, text="9",
        padx=37, pady=25, font=("Helvetica", 20, "bold"), width=1,
        command= lambda:self.buttonClick(9)) 
        self.button3.grid(row=2, column=2, sticky=W)

        # button 4
        self.button4 = Button(self, bg="#beb9db", bd=12, text="4",
        padx=37, pady=25, font=("Helvetica", 20, "bold"), width=1,
        command= lambda:self.buttonClick(4)) 
        self.button4.grid(row=3, column=0, sticky=W)

        # button 5
        self.button5 = Button(self, bg="#beb9db", bd=12, text="5",
        padx=37, pady=25, font=("Helvetica", 20, "bold"), width=1,
        command= lambda:self.buttonClick(5)) 
        self.button5.grid(row=3, column=1, sticky=W)

        # button 6
        self.button6 = Button(self, bg="#beb9db", bd=12, text="6",
        padx=37, pady=25, font=("Helvetica", 20, "bold"), width=1,
        command= lambda:self.buttonClick(6)) 
        self.button6.grid(row=3, column=2, sticky=W)

        # button 1
        self.button7 = Button(self, bg="#beb9db", bd=12, text="1",
        padx=37, pady=25, font=("Helvetica", 20, "bold"), width=1,
        command= lambda:self.buttonClick(1)) 
        self.button7.grid(row=4, column=0, sticky=W)

        # button 2
        self.button8 = Button(self, bg="#beb9db", bd=12, text="2",
        padx=37, pady=25, font=("Helvetica", 20, "bold"), width=1,
        command= lambda:self.buttonClick(2)) 
        self.button8.grid(row=4, column=1, sticky=W)

        # button 3
        self.button9 = Button(self, bg="#beb9db", bd=12, text="3",
        padx=37, pady=25, font=("Helvetica", 20, "bold"), width=1,
        command= lambda:self.buttonClick(3)) 
        self.button9.grid(row=4, column=2, sticky=W)

        # button 0
        self.button9 = Button(self, bg="#beb9db", bd=12, text="0",
        padx=37, pady=25, font=("Helvetica", 20, "bold"), width=1,
        command= lambda:self.buttonClick(0)) 
        self.button9.grid(row=5, column=0, sticky=W)

        # button +
        self.Addbutton = Button(self, bg="#fdcce5", bd=12, text = "+",
        padx=37, pady=25, font=("Helvetica", 20, "bold"), width=1,
        command=lambda:self.buttonClick("+"))
        self.Addbutton.grid(row=2, column=3, sticky=W)

        # button -
        self.Subbutton = Button(self, bg="#fdcce5", bd=12, text = "-",
        padx=37, pady=25, font=("Helvetica", 20, "bold"), width=1,
        command=lambda:self.buttonClick("-"))
        self.Subbutton.grid(row=3, column=3, sticky=W)

        # button *
        self.Multbutton = Button(self, bg="#fdcce5", bd=12, text = "*",
        padx=37, pady=25, font=("Helvetica", 20, "bold"), width=1,
        command=lambda:self.buttonClick("*"))
        self.Multbutton.grid(row=4, column=3, sticky=W)   

        # button /
        self.Divbutton = Button(self, bg="#fdcce5", bd=12, text = "/",
        padx=37, pady=25, font=("Helvetica", 20, "bold"), width=1,
        command=lambda:self.buttonClick("/"))
        self.Divbutton.grid(row=5, column=3, sticky=W)

        # button =
        self.EqualsButton = Button(self, bg="#E6D72A", bd=12, text = "=",
        padx=37, pady=25, width=1,
        command=self.CalculateTask, font=("Helvetica", 20, "bold"))
        self.EqualsButton.grid(row=5, column=1, sticky=W, columnspan=2)

        # button %
        self.ModulusButton = Button(self, bg="#8bd3c7", bd=12, text = "%",
        padx=37, pady=25, width=1,
        command=lambda:self.buttonClick("%"), font=("Helvetica", 20, "bold"))
        self.ModulusButton.grid(row=5, column=2, sticky=W, columnspan=2)

        # button AC
        self.ClearButton = Button(self, bg="#E6D72A", bd=12, text = "AC",
        padx=200, pady=25,command=self.ClearDisplay,
        font=("Helvetica", 20, "bold"))
        self.ClearButton.grid(row=1, columnspan=4, sticky=W)

        # button del
        self.DelButton = Button(self, bg="#E6D72A", bd=12, text = "del",
        padx=37, pady=25, font=("Helvetica", 20, "bold"), width=1,
        command=self.deleter)
        self.DelButton.grid(row=6, column=1, sticky=W)     

        # button √
        self.SquaRootButton = Button(self, bg="#fdcce5", bd=12, text = "√",
        padx=37, pady=25, font=("Helvetica", 20, "bold"),  width=1,
        command=lambda:self.buttonClick("√"))
        self.SquaRootButton.grid(row=6, column=3, sticky=W) 

        # button .
        self.DotButton = Button(self, bg="#8bd3c7", bd=12, text = ".",
        padx=37, pady=25, font=("Helvetica", 20, "bold"), width=1,
        command=lambda:self.buttonClick("."))
        self.DotButton.grid(row=6, column=2, sticky=W) 

        # button 00 
        self.DubZeroButton = Button(self, bg="#beb9db", bd=12, text = "00",
        padx=37, pady=25, font=("Helvetica", 20, "bold"), width=1,
        command=lambda:self.buttonClick("00"))
        self.DubZeroButton.grid(row=6, column=0, sticky=W) 


    def buttonClick(self, number):                    
        self.task = str(self.task) + str(number)
        self.UserIn.set(self.task)
        
    def deleter(self):
        # deleting last character on result screen
        self.data = self.user_input.get()[:-1]
        # updating user input as deleted one
        self.UserIn.set(self.data)
        # getting new task as deleted one
        self.task = self.UserIn.get()


    def CalculateTask(self):
        self.data = self.user_input.get()
        try:
            # precaution for eval
            self.allowed = "r.0123456789+-*/√%"
            for i in self.data:
                if i not in self.allowed:
                    raise SyntaxError
            
            # square root calculation
            if "√" in self.data:
                self.data = self.data.replace("√", "")
                self.answer = round(sqrt(float(self.data)), 8)
                self.displayText(self.answer)
                self.task=self.answer

            # rest of math operions
            else:
                self.answer = round(eval(self.data), 8)
                self.displayText(self.answer)
                self.task=self.answer

        # excepition handling
        except ZeroDivisionError as zer:
            self.displayText(zer)
            self.task = ""

        except SyntaxError as e:
            self.displayText("Invalid Syntax!")
            self.task = ""

    def displayText(self, value):
        self.user_input.delete(0, END)
        self.user_input.insert(0, value)
    
    def ClearDisplay(self):
        self.task = ""
        self.user_input.delete(0, END)
        self.user_input.insert(0, "0")


# tk class
calculator = Tk()

# title in the main window
calculator.title("Calculator 1.01")

# unresiazable window
calculator.resizable(width=False, height=False)

# instance
app = Application(calculator)

# keep running calculator
mainloop()
