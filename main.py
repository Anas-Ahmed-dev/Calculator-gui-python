from tkinter import Label # A tool used to display text on a window, such as numbers on the screen
from tkinter import StringVar # A tool used to store the text displayed from the label
from tkinter import Tk # A tool used to provide a title and size for an application (Calculator)
from tkinter import Button # A tool used to create a button on the screen
from tkinter import Frame # A tool used to create a frame (organise other functions, like buttons) on the screen

def button_press(num): # Function used to allow the user to press the buttons on the calculator

  global calculator_text # Allows the variable calculator_text to be used in the program through the global variable

  calculator_text = calculator_text + str(num) # Allows the user input to be displayed on the screen by assigning the value of the user input to the variable calculator_text

  calculator_label.set(calculator_text) # Allows the calculator_text to be displayed on the screen

def equals(): # Function used to calculate the answer
  global calculator_text # Allows the variable calculator_text to be used in the program through the global variable

  total = str(eval(calculator_text)) # Allows the calculator_text to be calculated and displayed on the screen. The eval() is used to take any user input from the calculator and essentially return the answer. An example is ("2 + 2") which would return 4.)

  calculator_label.set(total) # Allows the total calculated from eval() to be stored in the 'calculator_label' variable 

  calculator_text = total # Sets the total to calculator_text and allows the total to be displayed on the screen

def clear(): # Function used to clear the user input

  global calculator_text # Allows the variable calculator_text to be used in the program through the global variable

  calculator_label.set("") # Allows the calculator_text to be cleared from the screen. The use of ("") is used to clear the calculator_text variable. This is because ("") usually means 'empty' and this function is used to clear the calculator_text variable. Essentially, it makes the user input 'empty'

  calculator_text = ""


window = Tk() # Allows the title and size (height and width) of the calculator to be displayed on the screen
window.title("Calculator Project:") # Name of the project
window.geometry("500x500") # Size of the project (height and width)


calculator_text = ""

calculator_label = StringVar() # Holds the values of the user input which are going to be executed/calculated

Label = Label(window, textvariable = calculator_label, font = ('Calibri', 20), bg = "white" , width = 20 , height = 2)
Label.pack() # The 'Label' function is used to display text on the screen. The 'textvariable' is used to assign the value of the calculator_label variable to the calculator_text variable. The 'font' is used to change the font of the text. The 'bg' is used to change the background colour of the text. The 'width' and 'height' are used to change the size of the text. The pack() tool essentially organises the text to the top of the screen.

frame = Frame(window) # The 'Frame' function is used to organise  functions, (like buttons) on the screen
frame.pack() # This pack() function neatly organises the buttons into readable sections

button1 = Button(frame, text = 1, height = 3, width = 5, font = 30, command = lambda: button_press(1))
button1.grid(row = 0, column = 0) # The 'Button' function is used to create a button on the screen. The 'text' is used to display the text on the button. The 'height' and 'width' are used to change the size of the button. The 'font' is used to change the font of the text. The 'command' is used to execute the function when the button is pressed. The 'lambda' is used to allow the function to be executed when the button is pressed. 

button2 = Button(frame, text = 2, height = 3, width = 5, font = 30, command = lambda: button_press(2))
button2.grid(row = 0, column = 1)

button3 = Button(frame, text = 3, height = 3, width = 5, font = 30, command = lambda: button_press(3))
button3.grid(row = 0, column = 2)

button4 = Button(frame, text = 4, height = 3, width = 5, font = 30, command = lambda: button_press(4))
button4.grid(row = 1, column = 0)

button5 = Button(frame, text = 5, height = 3, width = 5, font = 30, command = lambda: button_press(5))
button5.grid(row = 1, column = 1)

button6 = Button(frame, text = 6, height = 3, width = 5, font = 30, command = lambda: button_press(6))
button6.grid(row = 1, column = 2)

button7 = Button(frame, text = 7, height = 3, width = 5, font = 30, command = lambda: button_press(7))
button7.grid(row = 2, column = 0)

button8 = Button(frame, text = 8, height = 3, width = 5, font = 30, command = lambda: button_press(8))
button8.grid(row = 2, column = 1)

button9 = Button(frame, text = 9, height = 3, width = 5, font = 30, command = lambda: button_press(9))
button9.grid(row = 2, column = 2)

button0 = Button(frame, text = 0, height = 3, width = 5, font = 30, command = lambda: button_press(0))
button0.grid(row = 3, column = 1)

button_plus = Button(frame, text = "+", height = 3, width = 5, font = 30, command = lambda: button_press("+"))
button_plus.grid(row = 0, column = 3)

button_minus = Button(frame, text = "-", height = 3, width = 5, font = 30, command = lambda: button_press("-"))
button_minus.grid(row = 1, column = 3)

button_multiply = Button(frame, text = "*", height = 3, width = 5, font = 30, command = lambda: button_press("*"))
button_multiply.grid(row = 2, column = 3)

button_divide = Button(frame, text = "/", height = 3, width = 5, font = 30, command = lambda: button_press("/"))
button_divide.grid(row = 3, column = 3)

equal = Button(frame, text = '=', height = 3, width = 5, font = 30, command = equals)
equal.grid(row = 3, column = 2)

decimal = Button(frame, text = ".", height = 3, width = 5, font = 30, command = lambda: button_press("."))
decimal.grid(row = 3, column = 0)

square = Button(frame, text = 'x^2', height = 3, width = 5, font = 30, command = lambda: button_press('**2'))
square.grid(row = 0, column = 4)

cube = Button(frame, text = 'x^3', height = 3, width = 5, font = 30, command = lambda: button_press('**3'))
cube.grid(row = 1, column = 4)

square_root = Button(frame, text = 'x^0.5', height = 3, width = 5, font = 30, command = lambda: button_press('**0.5'))
square_root.grid(row = 2, column = 4)

a = 1/3 # Assigning the value 1/3 to a for cube root

cube_root = Button(frame, text = 'x^1/3', height = 3, width = 5, font = 30, command = lambda: button_press('**a'))
cube_root.grid(row = 3, column = 4)

clear = Button(window, text = 'Clear', height = 3, width = 20, font = 40, command = clear)
clear.pack() # The pack() tool is used to adjust the sizes of buttons to an appropriate scale. However, you can see there is no row or column placed. This is so we can place the clear button in a unique space


window.mainloop() # This tool is used to basically allow the user to input data on the screen. The program responds to buttons clicked by the user to provide an output. This tool also repeats endlessly, which means the user can continue to use the calculator until the program is stopped/closed