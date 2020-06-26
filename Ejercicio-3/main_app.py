from tkinter import * 
from tkinter import ttk, font
from PIL import Image, ImageTk
from datetime import datetime
import requests
import re


#	7 labels
#	2 buttons
#	3 list box
#	4 separator
#	1 textbox

class Application(object):
	__window = None
	__coin_in =  None
	__message = None
	__update = None

	def __init__(self):

		#	colors
		self.color_bg = '#0e172e'
		self.color_bt = '#18e758'
		self.color_lb1 = '#ffffff'
		self.color_lb2 = '#000000'

		#	window
		self.__window = Tk()
		#self.__window.geometry('335x385')
		self.__window.resizable(0,0)
		self.__window.title('Cotizaciones del Dolar')
		self.__window.config(bg = self.color_bg)

		#	font
		font1 = font.Font(family = 'Helvetica', weight='bold')
		font2 = font.Font(family = 'Helvetica')

		#	image/icon/variable
		self.icon1 = PhotoImage(file = "icon/upload-1.png")
		self.icon2 = PhotoImage(file = "icon/cancel.png")
		self.__coin_in = StringVar()
		self.__message = StringVar()
		self.__update = StringVar()
		self.__coin_in.set('1')

		#	widgets
		self.main_frame = Frame(self.__window, borderwidth = 2,
			 bg = self.color_bg)

		#		labels
		self.label1 = Label(self.main_frame, text = 'Cotizaciones del Dolar',
			font = font1, fg = self.color_lb1, bg = self.color_bg)
		self.label2 = Label(self.main_frame, text = 'Cantidad de Dolares: $',
			font = font2, fg = self.color_lb1, bg = self.color_bg)
		self.label3 = Label(self.main_frame, textvariable = self.__message,
			font = font1, fg = '#ff0000', bg = self.color_bg)
		self.label4 = Label(self.main_frame, text = 'Tipo de Dolar',
			font = font1, fg = self.color_lb1, bg = self.color_bg)
		self.label5 = Label(self.main_frame, text = 'Compra (ARS)',
			font = font1, fg = self.color_lb1, bg = self.color_bg)
		self.label6 = Label(self.main_frame, text = 'Venta (ARS)',
			font = font1, fg = self.color_lb1, bg = self.color_bg)
		self.label7 = Label(self.main_frame, textvariable = self.__update,
			font = font2, fg = self.color_lb1, bg = self.color_bg)

		#		text box
		self.text_box1 = Entry(self.main_frame,
			textvariable = self.__coin_in, font = font2,
			bg = self.color_bg, fg = self.color_lb1, bd = 4, width = 10)

		#		separator
		self.separ1 = ttk.Separator(self.main_frame, orient = HORIZONTAL)
		self.separ2 = ttk.Separator(self.main_frame, orient = HORIZONTAL)
		self.separ3 = ttk.Separator(self.main_frame, orient = HORIZONTAL)
		self.separ4 = ttk.Separator(self.main_frame, orient = HORIZONTAL)

		#		buttons
		self.button1 = Button(self.main_frame, compound = LEFT,
			image = self.icon1, text = " Actualizar", fg = self.color_lb1,
			command = self.load_listbox, bg = self.color_bt,
			font = font1, border = 0, activebackground = self.color_lb2,
			activeforeground = self.color_lb1)
		self.button2 = Button(self.main_frame, compound = LEFT,
			image = self.icon2, text = " Salir", fg = self.color_lb1,
			command = self.__window.destroy, bg = self.color_bt,
			font = font1, border = 0, activebackground = self.color_lb2,
			activeforeground = self.color_lb1)
		
		#	listbox
		self.listbox1 = Listbox(self.main_frame, font = font1,
			bg = self.color_bg, bd = 0, fg = self.color_lb1,
			activestyle = 'none', selectbackground = self.color_bg,
			width = 25, highlightthickness = 0, height = 6, takefocus = 0)
		self.listbox2 = Listbox(self.main_frame, font = font1,
			bg = self.color_bg, bd = 0, fg = self.color_lb1,
			activestyle = 'none', selectbackground = self.color_bt,
			width = 12, highlightthickness = 0, height = 6)
		self.listbox3 = Listbox(self.main_frame, font = font1,
			bg = self.color_bg, bd = 0, fg = self.color_lb1,
			activestyle = 'none', selectbackground = self.color_bt,
			width = 12, highlightthickness = 0, height = 6)

		#		keyboard
		self.__window.bind('<Return>', self.validate)
		
		#	Geometry widgets
		opts = {'padx': 5, 'pady': 5}

		self.main_frame.grid(row = 0, column = 0, padx = 15, pady = 5)
		self.label1.grid(row = 0, columnspan = 3, **opts)
		
		self.separ1.grid(row = 1, columnspan = 3, ipadx = 220, **opts)
		
		self.label2.grid(row = 2, column = 0, sticky = 'e', **opts)
		self.text_box1.grid(row = 2, column = 1, **opts)
		self.label3.grid(row = 2, column = 2, sticky = 'w', **opts)
		
		self.separ2.grid(row = 3, columnspan = 3, ipadx = 220, **opts)

		self.label4.grid(row = 4, column = 0, sticky = 'w', **opts)
		self.label5.grid(row = 4, column = 1, sticky = 'w', **opts)
		self.label6.grid(row = 4, column = 2, sticky = 'w', **opts)

		self.separ3.grid(row = 5, columnspan = 3, ipadx = 220, **opts)

		self.listbox1.grid(row = 6, column = 0, pady = 5)
		self.listbox2.grid(row = 6, column = 1, pady = 5)
		self.listbox3.grid(row = 6, column = 2, pady = 5)

		self.separ4.grid(row = 7, columnspan = 3, ipadx = 220, **opts)

		self.label7.grid(row = 8, columnspan = 3, sticky = 'w', **opts)

		self.button1.grid(row = 9, columnspan = 3, sticky = 'w', 
			ipadx = 15, ipady = 4, **opts)
		self.button2.grid(row = 9, columnspan = 3, sticky = 'e',
			ipadx = 15, ipady = 4, **opts)

		self.text_box1.focus()
		self.load_listbox()

		self.__window.mainloop()

	def load_listbox(self):
		if isfloat(self.__coin_in.get()):
			self.__message.set('')
			list_coins = self.list_coins()
			coin = float(self.__coin_in.get())

			for i in range(len(list_coins)):
				print(i)
				self.listbox1.delete(i)
				self.listbox2.delete(i)
				self.listbox3.delete(i)

				self.listbox1.insert(i, list_coins[i].get('name'))
				self.listbox2.insert(i, list_coins[i].get('buy') * coin)
				self.listbox3.insert(i, list_coins[i].get('sell') * coin)

			date = 'Ultima actualizacion: '
			date += str(datetime.now().time().replace(microsecond = 0))
			date += ' - ' + str(datetime.now().date()).replace('-','/')
			self.__update.set(date)
		

	def validate(self, event):
		try:
			coin_in = float(self.text_box1.get())
			self.__message.set('')
			self.load_listbox()

		except ValueError:
			self.__message.set('Error')
			self.__coin_in.set('')

	def list_coins(self):
		url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
		request = requests.get(url)
		list_json = request.json()
		list_coins = []

		for i in list_json:
			if i['casa']['nombre'] is not None:
				name = i['casa']['nombre']
				if re.search('dolar', name.lower()) is not None:
					if isfloat(i['casa']['compra']):
						buy = float(i['casa']['compra'].replace(',', '.'))
						sell = float(i['casa']['venta'].replace(',', '.'))
						list_coins.append({'name': name, 'buy': buy,
							'sell': sell})
		return list_coins

def isfloat(value):
	try:
		float(value.replace(',', '.'))
		return True

	except ValueError:
		return False

def app():
	me_app = Application()

if __name__ == '__main__':
	app()