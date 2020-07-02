from view.province_view import ProvinceView
from model.handle_province import HandleProvince
from model.object_encoder import ObjectEncoder
from model.province import Province
#from controller.controller import Controller


def read_file(obj_encoder):
	try: 
		dict_aux = obj_encoder.read("datos.json")
		handle = obj_encoder.decoder(dict_aux)
		return handle

	except FileNotFoundError:
		handle = HandlePatient()

def main():
	obj_encoder = ObjectEncoder()
	handle = read_file(obj_encoder)
	view = ProvinceView()
	
	#control = Controller(view, handle)
	#view.set_controller(control)
	
	#control.start()

	#handle_aux = control.exit_save()
	#obj_encoder.save(handle_aux, "provinces.json") 

if __name__ == '__main__':
	main()