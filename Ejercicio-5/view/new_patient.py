from view.patient_form import PatientForm
import tkinter as tk


class NewPatient(tk.Toplevel):
	def __init__(self, parent):
		super().__init__(parent)
		self.resizable(0,0)
		self.__center_window()
		self.patient = None
		self.form = PatientForm(self)
		self.button_add = tk.Button(self, text = 'Confirmar', command = self.confirm)
		self.form.pack(padx = 10, pady = 10)
		self.button_add.pack(pady = 10)

	def confirm(self):
		self.patient = self.form.create_patient()

		if self.patient:
			self.destroy()

	def show(self):
		self.grab_set()
		self.wait_window()
		return self.patient

	def __center_window(self):
		win = self
		width = 350
		height = 270
		height_screen = win.winfo_screenwidth()
		width_screen = win.winfo_screenheight() 
		x = int((height_screen / 2) - (width / 2))
		y = int((width_screen / 2) - (height / 2))
		win.geometry('{}x{}+{}+{}'.format(width, height, x, y))