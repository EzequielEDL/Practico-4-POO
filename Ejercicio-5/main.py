from view.patients_view import PatientsView
from model.handle_patient import HandlePatient
from model.object_encoder import ObjectEncoder
from controller.controller import Controller

def read_file(obj_encoder):
	try: 
		dict_aux = obj_encoder.read("patients.json")
		handle = obj_encoder.decoder(dict_aux)
		return handle

	except FileNotFoundError:
		handle = HandlePatient()

def main():
	obj_encoder = ObjectEncoder()
	handle = read_file(obj_encoder)	
	view = PatientsView()
	control = Controller(view, handle)
	view.set_controller(control)
	
	control.start()

	handle_aux = control.exit_save()
	obj_encoder.save(handle_aux, "patients.json") 

if __name__ == '__main__':
	main()
	
