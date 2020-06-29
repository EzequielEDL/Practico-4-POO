import tkinter as tk
from view.widgets import *
from view.patient_list import PatientList
from view.update_patient_form import UpdatePatientForm


class PatientsView(tk.Tk):
	def __init__(self):
		super().__init__()
		self.rs = Resources()
		center_window(self, w = 600, h = 330)
		self.config(bg = self.rs.color_bg)
		self.title('Lista de Pacientes')
		self.list = PatientList(self)
		self.form = UpdatePatientForm(self)
		self.resizable(0,0)
		self.button_new = Button(self, text = ' Agregar Paciente', image = self.rs.icon4)

		self.list.pack(side = tk.LEFT, padx = 10, pady = 10)
		self.form.pack(padx = 10, pady = 10)
		self.button_new.pack(side = tk.TOP, pady = 5, ipadx = 5)

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
