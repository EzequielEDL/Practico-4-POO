from view.widgets import *
from tkinter import Tk


class ProvinceView(Tk):
	def __init__(self):
		super().__init__()
		center_window(self, w = 700, h = 350)
		self.resizable(0, 0)
		self.title('Lista de Provincias')

		self.label = Label(self, text = '')
		self.grid()






		self.mainloop()