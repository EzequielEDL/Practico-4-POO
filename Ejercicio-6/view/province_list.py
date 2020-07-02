from view.widgets import *
from tkinter import ttk


class ProvinceList(Frame):
	def __init__(self, master):
		super().__init__(master)
		self.rs = Resources()
		self.listbox1 = Listbox(self)

		style = ttk.Style()
		style.theme_use('clam')
		style.configure("Vertical.TScrollbar", gripcount = 0, background = self.rs.color_bt,
			darkcolor = self.rs.color_bg3, lightcolor = self.rs.color_bt,
			troughcolor = self.rs.color_bg3, bordercolor = self.rs.color_bg3,
			arrowcolor = self.rs.color_bg)
		scroll = ttk.Scrollbar(self, command = self.listbox1.yview, orient = 'vertical')
		
		self.listbox1.config(yscrollcommand = scroll.set)

		scroll.pack(side = RIGHT, fill = Y)
		self.listbox1.pack(side = LEFT, fill = BOTH, expand = 1)

	def insert(self, value, index = END):
		text = f'{value.get_name()}'
		self.listbox1.insert(index, text)

	def delete(self, index):
		self.listbox1.delete(index, index)

	def modify(self, value, index):
		self.delete(index)
		self.insert(value, index)

	def bind_double_click(self, callback):
		handler = lambda _: callback(self.listbox1.curselection()[0])
		self.listbox1.bind('<Double-Button-1>', handler)
