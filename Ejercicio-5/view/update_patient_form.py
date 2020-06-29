from view.patient_form import PatientForm
import tkinter as tk
from tkinter import ttk


class UpdatePatientForm(PatientForm):
	def __init__(self, master, **kwargs):
		super().__init__(master, **kwargs)
		self.button_save = tk.Button(self, text = 'Guardar')
		self.button_delete = tk.Button(self, text = 'Borrar')
		self.button_imc = tk.Button(self, text = 'Ver IMC')
		self.button_save.pack(side = tk.RIGHT, ipadx = 5, padx = 5, pady = 5)
		self.button_delete.pack(side = tk.RIGHT, ipadx = 5, padx = 5, pady = 5)
		self.button_imc.pack(side = tk.RIGHT, ipadx = 5, padx = 5, pady = 5)

	def bind_save(self, callback):
		self.button_save.config(command = callback)

	def bind_delete(self, callback):
		self.button_delete.config(command = callback)

	def bind_imc(self, callback):
		self.button_imc.config(command = callback)
