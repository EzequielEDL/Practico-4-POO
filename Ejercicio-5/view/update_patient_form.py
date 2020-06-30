from view.patient_form import PatientForm
import tkinter as tk
from view.widgets import *
from tkinter import ttk


class UpdatePatientForm(PatientForm):
	def __init__(self, master, **kwargs):
		super().__init__(master, **kwargs)
		self.rs = Resources()
		self.button_save = Button(self, text = ' Guardar', image = self.rs.icon3)
		self.button_delete = Button(self, text = ' Borrar', image = self.rs.icon2)
		self.button_imc = Button(self, text = ' Ver IMC', image = self.rs.icon1)
		opts = {'ipadx': 5, 'ipady': 1, 'padx': 5, 'pady': 5}
		self.button_save.pack(side = tk.RIGHT, **opts)
		self.button_delete.pack(side = tk.RIGHT, **opts)
		self.button_imc.pack(side = tk.RIGHT, **opts)

	def bind_save(self, callback):
		self.button_save.config(command = callback)

	def bind_delete(self, callback):
		self.button_delete.config(command = callback)

	def bind_imc(self, callback):
		self.button_imc.config(command = callback)
