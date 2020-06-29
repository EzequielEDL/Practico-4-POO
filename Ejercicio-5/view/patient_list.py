import tkinter as tk
from tkinter import messagebox
from view.widgets import *


class PatientList(Frame):
	def __init__(self, master, **kargs):
		super().__init__(master)
		self.listbox1 = Listbox(self, **kargs)
		scroll = Scrollbar(self, command = self.listbox1.yview)
		self.listbox1.config(yscrollcommand = scroll.set)
		scroll.pack(side = tk.RIGHT, fill = tk.Y)
		self.listbox1.pack(side = tk.LEFT, fill = tk.BOTH, expand = 1)

	def insert(self, patient, index = tk.END):
		text = f'{patient.get_name()}, {patient.get_lastname()}'
		self.listbox1.insert(index, text)

	def delete(self, index):
		self.listbox1.delete(index, index)

	def modify(self, patient, index):
		self.delete(index)
		self.insert(patient, index)

	def bind_double_click(self, callback):
		handler = lambda _: callback(self.listbox1.curselection()[0])
		self.listbox1.bind('<Double-Button-1>', handler)
