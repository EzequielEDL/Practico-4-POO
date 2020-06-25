from tkinter import * 
from tkinter import ttk, font
from PIL import Image, ImageTk

class Application(object):
	__window = None
	__messagebox = None
	__weight = None
	__height = None

	def __init__(self):

		#	colors
		self.color_bg = '#0e172e'
		self.color_bt = '#18e758'
		self.color_lb1 = '#ffffff'
		self.color_lb2 = '#000000'

		#	window
		self.__window = Tk()
		#self.__window.geometry('500x200')
		self.__window.resizable(0,0)
		self.__window.title('Calculadora de IMC')
		self.__window.config(bg = self.color_bg)

		#	font
		font1 = font.Font(family = 'Helvetica', weight='bold')
		font2 = font.Font(family = 'Helvetica')

		#	image/icon/variable
		self.icon1 = PhotoImage(file = "icon/reload.png")
		self.icon2 = PhotoImage(file = "icon/garbage.png")
		self.__weight = StringVar()
		self.__height = StringVar()
		self.__message = StringVar()
		self.__message.set('0')

		#	widgets
		self.main_frame = Frame(self.__window, borderwidth = 2,
			 bg = self.color_bg)

		#		labels
		self.label1 = Label(self.main_frame, text = 'Calculadora de IMC',
			font = font1, fg = self.color_lb1, bg = self.color_bg)
		self.label2 = Label(self.main_frame, text = 'Altura (cm)',
			font = font2, fg = self.color_lb1, bg = self.color_bg)
		self.label3 = Label(self.main_frame, text = 'Peso (Kg)',
			font = font2, fg = self.color_lb1, bg = self.color_bg)
		self.label4 = Label(self.main_frame, font = font1,
			textvariable = self.__message, fg = self.color_lb1,
			bg = self.color_bg)

		#		text box
		self.c_text1 = Entry(self.main_frame,
			textvariable = self.__height, font = font2, bg = self.color_bg,
			fg = self.color_lb1, bd = 4)
		self.c_text2 = Entry(self.main_frame,
			textvariable = self.__weight, font = font2, bg = self.color_bg,
			fg = self.color_lb1, bd = 4)

		#		separator
		self.separ1 = ttk.Separator(self.main_frame, orient = HORIZONTAL)
		
		#		buttons
		self.button1 = Button(self.main_frame, compound = LEFT,
			image = self.icon1, text = " Calcular", fg = self.color_lb1,
			command = self.calculate, bg = self.color_bt, font = font1,
			border = 0, activebackground = self.color_lb2,
			activeforeground = self.color_lb1)
		self.button2 = Button(self.main_frame, compound = LEFT,
			image = self.icon2, text = " Limpiar", fg = self.color_lb1,
			command = self.clear, bg = self.color_bt, font = font1,
			border = 0, activebackground = self.color_lb2,
			activeforeground = self.color_lb1)

		#	Geometry widgets
		opts = {'padx': 5, 'pady': 5}

		self.main_frame.grid(row = 0, column = 0, padx = 15, pady = 15)
		self.label1.grid(row = 0, columnspan = 2)
		self.label2.grid(row = 1, column = 0, **opts)
		self.label3.grid(row = 2, column = 0, **opts)
		self.c_text1.grid(row = 1, column = 1, **opts)
		self.c_text2.grid(row = 2, column = 1, **opts)
		self.separ1.grid(row = 3, columnspan = 2, ipadx = 150, **opts)
		self.button1.grid(row = 4, column = 0, ipadx = 7, ipady = 4, **opts)
		self.button2.grid(row = 4, column = 1, ipadx = 7, ipady = 4, **opts)
		self.label4.grid(row = 5, columnspan = 2, **opts)

		self.__window.mainloop()

	def calculate(self):
		try:
			height = float(self.c_text1.get()) / 100
			weight = float(self.c_text2.get())

			imc = weight / (height ** 2)
			print('{} / {}^2 = {}'.format(weight, height, imc))

			if imc < 18.5:
				type_w = 'Peso inferior al normal'
			elif imc < 24.9:
				type_w = 'Peso Normal'
			elif imc < 29.9:
				type_w = 'Peso superior al normal'
			else:
				type_w = 'Peso obesidad'

			text = '(IMC) : {:.2f} Kg/m2\n{}'.format(
				imc, type_w)
			self.label4.config(fg = self.color_bt)
			self.__message.set(text)

		except ValueError:
			self.label4.config(fg = '#f30808')
			self.__message.set('Error: Datos invalidos')
			self.__height.set('')
			self.__weight.set('')

	def clear(self):
		self.__height.set('')
		self.__weight.set('')
		self.__message.set('0')


def app():
	me_app = Application()

if __name__ == '__main__':
	app()