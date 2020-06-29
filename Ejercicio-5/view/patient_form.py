import tkinter as tk
from tkinter import messagebox
from model.patient import Patient


class PatientForm(tk.LabelFrame):
	fields = ('Apellido', 'Nombre', 'Telefono', 'Altura', 'Peso')

	def __init__(self, master, **kwargs):
		super().__init__(master, text = 'Paciente', padx = 10, pady = 10,
			**kwargs)
		self.frame = tk.Frame(self)
		self.entries = list(map(self.create_field, enumerate(self.fields)))
		self.frame.pack()

	def create_field(self, field):
		position, text = field
		label = tk.Label(self.frame, text = text)
		entry = tk.Entry(self.frame, width = 25)
		label.grid(row = position, column = 0, pady = 5)
		entry.grid(row = position, column = 1, pady = 5)
		return entry

	def show_patient(self, patient):
		values = (patient.get_lastname(), patient.get_name(),
			patient.get_phone(), patient.get_height(), patient.get_weight())

		for entry, value in zip(self.entries, values):
			entry.delete(0, tk.END)
			entry.insert(0, value)

	def create_patient(self):
		values = [e.get() for e in self.entries]
		patient = None
		
		try:
			patient = Patient(*values)
		
		except ValueError as e:
			messagebox.showerror('Error de Validacion', str(e), parent = self)

		return patient

	def clean(self):
		for entry in self.entries:
			entry.delete(0, tk.END)
