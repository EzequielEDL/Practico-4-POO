from tkinter import * 
from tkinter import ttk, font
from PIL import Image, ImageTk

class Application(object):
	__window = None
	__messagebox = None
	__weight = None
	__height = None

	def __init__(self):
		self.__window = Tk()
		#self.__window.geometry('500x200')
		self.__window.resizable(0,0)
		self.__window.title('Calculadora de IMC')
		font1 = font.Font(weight = 'bold')
		self.img = PhotoImage(file = "error.png")

		self.__weight = StringVar()
		self.__height = StringVar()
		self.__message = StringVar()
		self.__message.set('0')
		
		#Widgets
		self.main_frame = ttk.Frame(self.__window, borderwidth = 2,
			relief = 'raised', padding = (10, 10))
		
		self.label1 = ttk.Label(self.main_frame, text = 'Calculadora de IMC',
			font = font1)

		self.label2 = ttk.Label(self.main_frame, text = 'Altura (cm)',)
		self.label3 = ttk.Label(self.main_frame, text = 'Peso (Kg)',)

		self.label4 = ttk.Label(self.main_frame, text = 'Altura',
			font = font1, textvariable = self.__message,
			background = 'green')

		self.c_text1 = ttk.Entry(self.main_frame,
			textvariable = self.__height, width = 30)

		self.c_text2 = ttk.Entry(self.main_frame,
			textvariable = self.__weight, width = 30)
		self.separ1 = ttk.Separator(self.main_frame, orient = HORIZONTAL)
		
		self.button1 = ttk.Button(self.main_frame, text = 'Calcular',
			command = self.calculate)
		self.button2 = ttk.Button(self.main_frame, text = 'Limpiar',
			command = self.clear)

		opts = {'padx': 5, 'pady': 5}

		#Geometry widgets
		self.main_frame.grid(row = 0, column = 0)
		self.label1.grid(row = 0, columnspan = 2)
		self.label2.grid(row = 1, column = 0, **opts)
		self.label3.grid(row = 2, column = 0, **opts)

		self.c_text1.grid(row = 1, column = 1, **opts)
		self.c_text2.grid(row = 2, column = 1, **opts)
		self.separ1.grid(row = 3, columnspan = 2, ipadx=150, **opts)
		self.button1.grid(row = 4, column = 0, **opts)
		self.button2.grid(row = 4, column = 1,  **opts)

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

			text = 'Tu indice de Masa Corporal (IMC) es {:.2f} Kg/m2\n{}'.format(
				imc, type_w)
			self.__message.set(text)

		except ValueError:
			self.messagebox()
			self.__height.set('')
			self.__weight.set('')

	def messagebox(self):
		self.__messagebox = Toplevel()
		self.__messagebox.resizable(0,0)
		self.__messagebox.title('Mensaje de Error')
		font1 = font.Font(weight = 'bold')

		

		#img  = Image.open("error.png") 
		#photo = ImageTk.PhotoImage(img)
		
		label1 = Label(self.__messagebox, image = self.img)
		label2 = Label(self.__messagebox,
			text = 'Error: tipo de dato invalido', font = font1)
		label1.grid(row = 0, column = 0)
		label2.grid(row = 1, column = 0)


	def clear(self):
		self.__height.set('')
		self.__weight.set('')
		self.__message.set('0')


def app():
	me_app = Application()

if __name__ == '__main__':
	app()