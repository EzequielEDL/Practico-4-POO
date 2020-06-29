from model.patient import Patient
import csv


class HandlePatient(object):
	__list_patient = None

	def __init__(self):
		self.__list_patient = []

	def __str__(self):
		return f'{self.__list_patient}'

	def __getitem__(self, index):
		return self.__list_patient[index]

	def __setitem__(self, index, value):
		self.__list_patient[index] = value

	def __len__(self):
		return len(self.__list_patient)

	#	Convert to JSON
	def toJSON(self):
		patients = []

		for i in self.__list_patient:
			patients.append(i.toJSON())

		d = dict(
			__class__ = self.__class__.__name__,
			data = patients
			)

		return d

	def append(self, patient):
		self.__list_patient.append(patient)

	def del_patient(self, index):
		self.__list_patient.pop(index)

	def mod_patient(self, patient, xpatient):
		index = self.__find_index(xpatient)
		self.__list_patient[index] = patient

	def get_list_patient(self):
		return self.__list_patient

	def __find_index(self, patient):
		i = 0

		while i < len(self.__list_patient) and self.__list_patient[i] != patient:
			i += 1

		if i < len(self.__list_patient):
			return i

'''
	#   Carga de un archivo CSV
	def load_file_csv(self):
		file = open('files/patients.csv')
		reader = csv.reader(file, delimiter = ',')

		for row in reader:
			patient = Patient(*row)
			self.__list_patient.append(patient)

		file.close()

'''