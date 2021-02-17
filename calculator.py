from tkinter import *
from math import sqrt
import time

root = Tk()
root.title("Calculator")

numberfield = Entry(root, width = 50, borderwidth=10)
numberfield.get()
numberfield.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

#Define number buttons
def click_button(number):
	if numberfield.get() == 'Error - CLEAR':
		numberfield.delete(0, END)
	numberfield.insert(END, number)

#Define operators
def click_add():
	global num_1 
	global operation
	num_1 = float(numberfield.get())
	numberfield.delete(0, END)
	operation = 'addition'

def click_subtract():
	global num_1
	global operation
	num_1 = float(numberfield.get())
	numberfield.delete(0, END)
	operation = 'subtraction'

def click_multiply():
	global num_1
	global operation
	num_1 = float(numberfield.get())
	numberfield.delete(0, END)
	operation = 'multiplication'

def click_divide():
	global num_1 
	global operation
	num_1 = float(numberfield.get())
	numberfield.delete(0, END)
	operation = 'division'

def click_sqrt():
	if numberfield.get() == '':
		numberfield.insert(0, '√')
		global operation
		operation = 'sqrt'
	else:
		num_1 = float(numberfield.get())
		new_num = sqrt(num_1)
		numberfield.delete(0, END)
		numberfield.insert(0, new_num)

def click_carrot():
	global num_1
	global operation
	num_1 = float(numberfield.get())
	numberfield.delete(0, END)
	operation = 'carrot'

#Define Calculation
def click_equal():
	if operation == 'addition':
		num_2 = float(numberfield.get())
		numberfield.delete(0, END)
		new_num = num_1 + num_2
		numberfield.insert(0, new_num)

	elif operation == 'subtraction':
		num_2 = float(numberfield.get())
		numberfield.delete(0, END)
		new_num = num_1 - num_2
		numberfield.insert(0, new_num)

	elif operation == 'multiplication':
		num_2 = float(numberfield.get())
		numberfield.delete(0, END)
		new_num = num_1 * num_2
		numberfield.insert(0, new_num)

	elif operation == 'division':
		num_2 = float(numberfield.get())
		numberfield.delete(0, END)
		try:
			new_num = num_1 / num_2
			numberfield.insert(0, new_num)
		except ZeroDivisionError:
			numberfield.insert(0, 'Error - CLEAR')

	elif operation == 'sqrt':
		num_2 = float(numberfield.get()[1:])
		numberfield.delete(0, END)
		new_num = sqrt(num_2)
		numberfield.insert(0, new_num)

	elif operation == 'carrot':
		num_2 = float(numberfield.get())
		numberfield.delete(0, END)
		try:
			new_num = num_1 ** num_2
			numberfield.insert(0, new_num)
		except OverflowError:
			numberfield.insert(0, 'Error - CLEAR')

	else:
		pass

#Define Clear
def click_clear():
	numberfield.delete(0, END)

# Create and Display Buttons 0-9
one_button = Button(text = '1', padx = 30, pady = 20, command = lambda: click_button('1'))
two_button = Button(text = '2', padx = 30, pady = 20, command = lambda: click_button('2'))
three_button = Button(text = '3', padx = 30, pady = 20, command = lambda: click_button('3'))
four_button = Button(text = '4', padx = 30, pady = 20, command = lambda: click_button('4'))
five_button = Button(text = '5', padx = 30, pady = 20, command = lambda: click_button('5'))
six_button = Button(text = '6', padx = 30, pady = 20, command = lambda: click_button('6'))
seven_button = Button(text = '7', padx = 30, pady = 20, command = lambda: click_button('7'))
eight_button = Button(text = '8', padx = 30, pady = 20, command = lambda: click_button('8'))
nine_button = Button(text = '9', padx = 30, pady = 20, command = lambda: click_button('9'))

one_button.grid(row = 3, column = 0)
two_button.grid(row = 3, column = 1)
three_button.grid(row = 3, column = 2)
four_button.grid(row = 2, column = 0)
five_button.grid(row = 2, column = 1)
six_button.grid(row = 2, column = 2)
seven_button.grid(row = 1, column = 0)
eight_button.grid(row = 1, column = 1)
nine_button.grid(row = 1, column = 2)


#Create and Display Other Buttons
zero_button = Button(text = '0', padx = 30, pady = 20, command = lambda: click_button('0'))
operator_add = Button(text = '+', padx = 30, pady = 20, command = click_add)
operator_subtract = Button(text = '-', padx = 30, pady = 20, command = click_subtract)
operator_multiply = Button(text = '*', padx = 30, pady = 20, command = click_multiply)
operator_divide = Button(text = '/', padx = 30, pady = 20, command = click_divide)
button_clear = Button(text = 'CLEAR', padx = 55, pady = 20, command = click_clear)
button_equal = Button(text = '=', padx = 69, pady = 20, command = click_equal)
button_squareroot = Button(text = '√', padx = 29, pady = 20, command = click_sqrt)
button_carrot = Button(text = '^', padx = 29, pady = 20, command = click_carrot)

zero_button.grid(row = 4, column = 0)
button_squareroot.grid(row = 4, column = 2)
operator_add.grid(row = 2, column = 3)
operator_subtract.grid(row = 3, column = 3)
operator_multiply.grid(row = 2, column = 4)
operator_divide.grid(row = 3, column = 4)
button_clear.grid(row = 1, column = 3, columnspan = 2)
button_equal.grid(row = 4, column = 3, columnspan = 2)
button_squareroot.grid(row = 4, column = 1)
button_carrot.grid(row = 4, column = 2)



root.mainloop()

# for num in range(1,10):
#use global?
# 	if num > 0 and num <= 3:
# 		num_button.grid(row = 3, column = num - 1)

# 	elif num > 3 and num <= 6:
# 		num_button.grid(row = 2, column = num - 4)

# 	else:
# 		num_button.grid(row = 1, column = num - 7)


#Dangerous solution!
	# if number == '=':
	# 	try:
	# 		new_num = eval(numberfield.get())
	# 		numberfield.delete(0, END)
	# 		numberfield.insert(0, new_num)
	# 	except ZeroDivisionError:
	# 		numberfield.delete(0, END)
	# 		numberfield.insert(0, 'Divide By Zero Error')

	# elif number == 'CLEAR':
	# 	numberfield.delete(0, END)

	# else:
	# 	numberfield.insert(END, number)


