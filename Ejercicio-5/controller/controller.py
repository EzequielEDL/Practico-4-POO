from view.patients_view import PatientsView
from model.handle_patient import HandlePatient
from view.new_patient import NewPatient
from view.see_imc import SeeImc

class Controller():

	def __init__(self, view, handle):
		self.__view = view
		self.__handle = handle
		self.__selection = -1

	def show_imc(self):
		patient = self.__view.get_details()
		height = float(patient.get_height())
		weight = float(patient.get_weight())
		SeeImc(self.__view, height, weight)

	def delete_patient(self):
		if self.__selection == -1:
			return

		self.__view.delete_patient(self.__selection)
		self.__handle.del_patient(self.__selection)
		#self.__selection = -1

	def select_patient(self, index):
		self.__selection = index
		patient = self.__handle[index]
		self.__view.see_patient(patient)

	def start(self):
		for i in self.__handle:
			self.__view.add_patient(i)
		
		self.__view.mainloop()

	def modify_patient(self):
		if self.__selection == -1:
			return

		patient = self.__view.get_details()
		self.__handle.mod_patient(patient, self.__handle[self.__selection])
		self.__view.modify_patient(patient, self.__selection)

	def create_patient(self):
		new_patient = NewPatient(self.__view).show()

		if new_patient:
			self.__handle.append(new_patient)
			self.__view.add_patient(new_patient)

	def exit_save(self):
		return self.__handle.toJSON()