        !!! CALCULATOR with GRAFICAL USER INTERFACE!!!
        ----------------------------------------------
      
      
  # PROJECT DESCRIPTION and FEATURES

1-
This project created based on Pyhton3 
Tkinter used as grafical user interface tool
Unreasizeble windows
Contains most of operetions (AC, +, -, *, /, %, ., =, del, 00, √)
Operates as real world standart calculator
To solve float numbers precion problem, 8th digit after decimal point rounded
Any number start as '0' cause "Invalid Syntax" error.

2-
SOME BUTTONS EXPLANATIONS:
del button can be used  as "<--" button, to delete last written character from screen
AC button can be used to set zero all operation
. button can be used to create float digits
% button can be used as modulus operator, returns remainder from division of numbers
√ button can be used as squared root operation
the rest of buttons are well known digits and math operations

3-
SOURCE CODE EXPLANATIONS:
App created on tkinter predefined class called Frame
Even if eval function used to make calculations, with input control system, program security ensured
Created individual class methods for operations which eval function doesn't cover 


  # HOW to INSTALL 
  
1-
Before utulizing this app, be sure python3 and tkinter are pre-installed
Normally tkinter should have downnloaded automatically besides of python3, but if doesn't, type from terminal;

to import tkinter-linux
$ sudo apt-get install python3-tk

to import tkinter-windows
C:\> pip install tk

2-
To install python file to local machine;
a- Script can copy-pastes to local python file, save it than run python script from terminal as it shown above or from a IDE
b- On github project directory, click on green highlighted CODE button and donwload as ZIP file, extract files than run terminal codes
c- Cloning project wiht HTTPS protocol; from terminal; $ git clone https://github.com/metetrkn/calculator_console.git

  # HOW to UTILISE

1-
To run the program, open terminal/console from file located directory;
for linux;
$ python3 calculator-gui.py

for windows;
C:\> python calculator-gui.py

2-
After running program, buttons can be clicked or related equation can be written directly result screen to operate
Click "=" button to get result


  # PLANNED UPGRADE

Inputing any number starts with '0' raises "Invalid Intax" error! This bug will be fixed

   # CREADITS

mete turkan
linkedIn : mete turkan 
Inst : m_trkn46
