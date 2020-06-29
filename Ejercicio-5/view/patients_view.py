import tkinter as tk
from view.patient_list import PatientList
from view.update_patient_form import UpdatePatientForm


class PatientsView(tk.Tk):
	def __init__(self):
		super().__init__()
		self.__center_window()
		self.title('Lista de Pacientes')
		self.list = PatientList(self)
		self.form = UpdatePatientForm(self)
		self.resizable(0,0)
		self.button_new = tk.Button(self, text = 'Agregar Paciente')

		self.list.pack(side = tk.LEFT, padx = 10, pady = 10)
		self.form.pack(padx = 10, pady = 10)
		self.button_new.pack(side = tk.BOTTOM, pady = 5)

	def set_controller(self, ctrl):
		self.button_new.config(command = ctrl.create_patient)
		self.list.bind_double_click(ctrl.select_patient)
		self.form.bind_save(ctrl.modify_patient)
		self.form.bind_delete(ctrl.delete_patient)
		self.form.bind_imc(ctrl.show_imc)

	def add_patient(self, patient):
		self.list.insert(patient)

	def modify_patient(self, patient, index):
		self.list.modify(patient, index)

	def delete_patient(self, index):
		self.form.clean()
		self.list.delete(index)

	def get_details(self):
		return self.form.create_patient()

	def see_patient(self, patient):
		self.form.show_patient(patient)

	def __center_window(self):
		win = self
		width = 450
		height = 300
		height_screen = win.winfo_screenwidth()
		width_screen = win.winfo_screenheight() 
		x = int((height_screen / 2) - (width / 2))
		y = int((width_screen / 2) - (height / 2))
		win.geometry('{}x{}+{}+{}'.format(width, height, x, y))