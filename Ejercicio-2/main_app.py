from tkinter import * 
from tkinter import ttk, font
from PIL import Image, ImageTk
import requests

class Application(object):
	__window = None
	__coin_in = None
	__coin_out = None
	__message = None
	
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
		self.__window.title('Conversor de moneda')
		self.__window.config(bg = self.color_bg)

		#	font
		font1 = font.Font(family = 'Helvetica', weight='bold')
		font2 = font.Font(family = 'Helvetica')

		#	image/icon/variable
		self.icon1 = PhotoImage(file = "icon/cancel.png")
		self.__coin_in = StringVar()
		self.__coin_out = StringVar()
		self.__coin_out.set('0')
		self.__message = StringVar()

		#	widgets
		self.main_frame = Frame(self.__window, borderwidth = 2,
			 bg = self.color_bg)

		#		labels
		self.label1 = Label(self.main_frame, text = 'Dolares (US)',
			font = font1, fg = self.color_lb1, bg = self.color_bg)
		self.label2 = Label(self.main_frame, text = 'Pesos (ARS)',
			font = font1, fg = self.color_lb1, bg = self.color_bg)
		self.label3 = Label(self.main_frame, text = 'Es equivalente a:',
			font = font2, fg = self.color_lb1, bg = self.color_bg)
		self.label4 = Label(self.main_frame, font = font1,
			textvariable = self.__coin_out, fg = self.color_bt,
			bg = self.color_bg)
		self.label5 = Label(self.main_frame, font = font1,
			textvariable = self.__message, fg = '#ff0000',
			bg = self.color_bg)

		#		text box
		self.text_box1 = Entry(self.main_frame,
			textvariable = self.__coin_in, font = font2,
			bg = self.color_bg, fg = self.color_lb1, bd = 4)

		#		separator
		self.separ1 = ttk.Separator(self.main_frame, orient = HORIZONTAL)
		
		#		buttons
		self.button1 = Button(self.main_frame, compound = LEFT,
			image = self.icon1, text = " Salir", fg = self.color_lb1,
			command = self.__window.destroy, bg = self.color_bt,
			font = font1, border = 0, activebackground = self.color_lb2,
			activeforeground = self.color_lb1)

		#		keyboard
		self.__window.bind('<Return>', self.calculate)
		
		#	Geometry widgets
		opts = {'padx': 5, 'pady': 5}

		self.main_frame.grid(row = 0, column = 0, padx = 15, pady = 15)
		self.label1.grid(row = 0, column = 2)
		self.label2.grid(row = 1, column = 2, **opts)
		self.label3.grid(row = 1, column = 0, **opts)
		self.label4.grid(row = 1, column = 1, **opts)
		self.label5.grid(row = 0, column = 0, **opts)
		self.text_box1.grid(row = 0, column = 1, **opts)
		self.separ1.grid(row = 2, columnspan = 3, ipadx = 220, **opts)
		self.button1.grid(row = 4, columnspan = 3, ipadx = 15, ipady = 4, **opts)
		
		self.text_box1.focus()

		self.__window.mainloop()

	def calculate(self, event):
		try:
			coin_in = float(self.text_box1.get())
			self.__message.set('')
			
			coin_out = self.convertor() * coin_in

			self.__coin_out.set(coin_out)

		except ValueError:
			self.__message.set('Error')
			self.__coin_out.set('')

	def convertor(self):
		url = 'https://www.dolarsi.com/api/api.php?type=dolar'
		r = requests.get(url)
		x = r.json()
		i = 0
		while i < len(x) and x[i]['casa']['nombre'] != 'Oficial':
			i += 1

		if i < len(x):
			dollar_sell = float(x[i]['casa']['venta'].replace(',', '.'))

		return dollar_sell

def app():
	me_app = Application()

if __name__ == '__main__':
	app()