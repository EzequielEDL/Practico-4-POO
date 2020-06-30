from view.patient_form import PatientForm
import tkinter as tk
from view.widgets import *


class NewPatient(Toplevel):
	def __init__(self, parent):
		super().__init__(parent)
		self.rs = Resources()
		center_window(self, w = 350, h = 290)
		self.patient = None
		self.form = PatientForm(self)
		self.button_add = Button(self, text = ' Confirmar',
			command = self.confirm, image = self.rs.icon4)
		self.form.pack(padx = 10, pady = 10)
		opts = {'ipadx': 5, 'ipady': 1, 'padx': 5, 'pady': 5}
		self.button_add.pack(**opts)

	def confirm(self):
		self.patient = self.form.create_patient()

		if self.patient:
			self.destroy()

	def show(self):
		self.grab_set()
		self.wait_window()
		return self.patient