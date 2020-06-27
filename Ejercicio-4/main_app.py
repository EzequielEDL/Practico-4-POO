from tkinter import * 
from tkinter import ttk, font
from functools import partial
from fraction import Fraction


class Application(object):
	__window = None
	__result =  None
	__panel = None
	__operator = None
	__operator_aux = None
	__first_oper = None
	__second_oper = None

	def __init__(self):

		#	colors
		self.color_bg = '#0e172e'
		self.color_bg2 = '#000000'
		self.color_bt1 = '#242f49'
		self.color_bt2 = '#244931'
		self.color_bt3 = '#d81313'
		self.color_lb1 = '#ffffff'

		#	window
		self.__window = Tk()
		self.__window.resizable(0,0)
		self.__window.title('Calculadora')
		self.__window.config(bg = self.color_bg)

		#	font
		font1 = font.Font(family = 'Helvetica', weight = 'bold')
		font2= font.Font(family = 'Courier', weight = 'bold')
		#	image/icon/variable
		self.__result = StringVar()
		self.__panel = StringVar()
		self.__operator = StringVar()
		self.__operator_aux = StringVar()

		#	widgets
		main_frame = Frame(self.__window, borderwidth = 2, bg = self.color_bg)
		main_frame.grid(column = 0, row = 0, padx = 15, pady = 5, sticky = (N, W, E, S))

		second_frame = Frame(main_frame, borderwidth = 2, bg = self.color_bt1)
		second_frame.grid(columnspan = 4, row = 0, padx = 10, pady = 6, sticky = (N, W, E, S))

		opts = {'ipadx': 17, 'ipady': 2, 'padx': 6, 'pady': 6}


		operator_entry = Entry(second_frame, textvariable = self.__operator, font = font2,
			width = 20, state = 'disabled', disabledbackground = self.color_bt1,
			disabledforeground = self.color_lb1, bd = 0)
		operator_entry.grid(columnspan = 4, row = 1, sticky = E, pady = 4, padx = 4)

		panel_entry = Entry(second_frame, textvariable = self.__panel, font = font2,
			width = 20, state = 'disabled', disabledbackground = self.color_bt1,
			disabledforeground = self.color_lb1, bd = 0)
		panel_entry.grid(columnspan = 4, row = 0, sticky = E, pady = 4, padx = 4)

		#		labels
		self.label1 = Label(main_frame, text = 'Casio fx-350MS', font = font1, fg = self.color_lb1,
			bg = self.color_bg).grid(columnspan = 3, row = 1, sticky = W)

		#		buttons
		Button(main_frame, text = '0', activebackground = self.color_bg2, border = 0, 
			activeforeground = self.color_lb1, font = font1, fg = self.color_lb1, bg = self.color_bt1,
			command = partial(self.set_number, '0')).grid(column = 0, row = 5, sticky = W, **opts)
		Button(main_frame, text = '1', activebackground = self.color_bg2, border = 0,
			activeforeground = self.color_lb1, font = font1, fg = self.color_lb1, bg = self.color_bt1,
			command = partial(self.set_number, '1')).grid(column = 0, row = 4, sticky = W, **opts)
		Button(main_frame, text = '2', activebackground = self.color_bg2, border = 0,
			activeforeground = self.color_lb1, font = font1, fg = self.color_lb1, bg = self.color_bt1,
			command = partial(self.set_number, '2')).grid(column = 1, row = 4, sticky = W, **opts)
		Button(main_frame, text = '3', activebackground = self.color_bg2, border = 0,
			activeforeground = self.color_lb1, font = font1, fg = self.color_lb1, bg = self.color_bt1,
			command = partial(self.set_number, '3')).grid(column = 2, row = 4, sticky = W, **opts)
		Button(main_frame, text = '4', activebackground = self.color_bg2, border = 0,
			activeforeground = self.color_lb1, font = font1, fg = self.color_lb1, bg = self.color_bt1,
			command = partial(self.set_number, '4')).grid(column = 0, row = 3, sticky = W, **opts)
		Button(main_frame, text = '5', activebackground = self.color_bg2, border = 0,
			activeforeground = self.color_lb1, font = font1, fg = self.color_lb1, bg = self.color_bt1,
			command = partial(self.set_number, '5')).grid(column = 1, row = 3, sticky = W, **opts)
		Button(main_frame, text = '6', activebackground = self.color_bg2, border = 0,
			activeforeground = self.color_lb1, font = font1, fg = self.color_lb1, bg = self.color_bt1,
			command = partial(self.set_number, '6')).grid(column = 2, row = 3, sticky = W, **opts)
		Button(main_frame, text = '7', activebackground = self.color_bg2, border = 0,
			activeforeground = self.color_lb1, font = font1, fg = self.color_lb1, bg = self.color_bt1,
			command = partial(self.set_number, '7')).grid(column = 0, row = 2, sticky = W, **opts)
		Button(main_frame, text = '8', activebackground = self.color_bg2, border = 0,
			activeforeground = self.color_lb1, font = font1, fg = self.color_lb1, bg = self.color_bt1,
			command = partial(self.set_number, '8')).grid(column = 1, row = 2, sticky = W, **opts)
		Button(main_frame, text = '9', activebackground = self.color_bg2, border = 0,
			activeforeground = self.color_lb1, font = font1, fg = self.color_lb1, bg = self.color_bt1,
			command = partial(self.set_number, '9')).grid(column = 2, row = 2, sticky = W, **opts)

		Button(main_frame, text = '┘', activebackground = self.color_bg2, border = 0,
			activeforeground = self.color_lb1, font = font1, fg = self.color_lb1, bg = self.color_bt2,
			command = partial(self.set_number, '┘')).grid(column = 3, row = 1, sticky = W, **opts)
		Button(main_frame, text = '/  ', activebackground = self.color_bg2, border = 0,
			activeforeground = self.color_lb1, font = font1, fg = self.color_lb1, bg = self.color_bt2,
			command = partial(self.set_operator, '/')).grid(column = 3, row = 2, sticky = W, **opts)
		Button(main_frame, text = '*  ', activebackground = self.color_bg2, border = 0,
			activeforeground = self.color_lb1, font = font1, fg = self.color_lb1, bg = self.color_bt2,
			command = partial(self.set_operator, '*')).grid(column = 3, row = 3, sticky = W, **opts)
		Button(main_frame, text = '-  ', activebackground = self.color_bg2, border = 0,
			activeforeground = self.color_lb1, font = font1, fg = self.color_lb1, bg = self.color_bt2,
			command = partial(self.set_operator, '-')).grid(column = 3, row = 4, sticky = W, **opts)
		Button(main_frame, text = '+ ', activebackground = self.color_bg2, border = 0,
			activeforeground = self.color_lb1, font = font1, fg = self.color_lb1, bg = self.color_bt2,
			command = partial(self.set_operator, '+')).grid(column = 3, row = 5, sticky = W, **opts)

		Button(main_frame, text = '=', activebackground = self.color_bg2, border = 0,
			activeforeground = self.color_lb1, font = font1, fg = self.color_lb1, bg = self.color_bt1,
			command = partial(self.set_operator, '=')).grid(columnspan = 3, row = 5, sticky = E,
			ipadx = 50, ipady = 2, pady = 6, padx = 6)
		Button(main_frame, text = 'C', activebackground = self.color_bg2, border = 0,
			activeforeground = self.color_lb1, font = font1, fg = self.color_lb1, bg = self.color_bt3,
			command = self.clear_panel).grid(column = 2, row = 1, sticky = E,
			ipadx = 15, ipady = 2, pady = 6, padx = 6)		

		panel_entry.focus()
		self.__panel.set('0')

		self.__window.mainloop()
	
	def clear_panel(self):
		self.__panel.set('0')
		self.__operator.set('')

	def set_number(self, number):
		if self.__operator_aux == None:
			value = self.__panel.get()
			self.__panel.set(value + number)

		else:
			self.__operator_aux = None
			value = self.__panel.get()
			self.__first_oper = Fraction(value)
			self.__panel.set(number)

	def resolv_operation(self, operator1 , operation, operator2):
		result = ''

		if operation == '+':
			result = operator1 + operator2
		elif operation == '-':
			result = operator1 - operator2
		elif operation == '*':
			result = operator1 * operator2
		elif operation == '/':
			result = operator1 / operator2

		self.__panel.set(str(result))

	def set_operator(self, op):
		if op == '=':
			operation = self.__operator.get()
			self.__second_oper = Fraction(self.__panel.get())
			self.resolv_operation(self.__first_oper, operation, self.__second_oper)
			self.__operator.set('')
			self.__operator_aux = None

		else:
			if self.__operator.get() == '':
				self.__operator.set(op)
				self.__operator_aux = op

			else:
				operation = self.__operator.get()
				self.__second_oper = Fraction(self.__panel.get())
				self.resolv_operation(self.__first_oper, operation, self.__second_oper)
				self.__operator.set(op)
				self.__operator_aux = op

def app():
	me_app = Application()

if __name__ == '__main__':
	app()