class Patient(object):
	__lastname = None
	__name = None
	__phone = None
	__height = None
	__weight = None

	def __init__(self, lastname, name, phone, height, weight):
		self.__lastname = self.__valid(lastname, 'Apellido necesario')
		self.__name = self.__valid(name, 'Nombre necesario')
		self.__phone = self.__valid(phone, 'Telefono necesario')
		self.__height = self.__valid(height, 'Altura necesario')
		self.__weight = self.__valid(weight, 'Peso necesario')

	def __valid(self, value, message):
		if not value:
			raise ValueError(message)
		return value

	def toJSON(self):
		return dict(
			__class__ = self.__class__.__name__,
			__attributes__ = dict(
							name = self.__name,
							lastname = self.__lastname,
							phone = self.__phone,
							height = self.__height,
							weight = self.__weight,
							)
						)

	def get_name(self):
		return self.__name

	def get_lastname(self):
		return self.__lastname

	def get_phone(self):
		return self.__phone

	def get_height(self):
		return self.__height

	def get_weight(self):
		return self.__weight

	def set_name(self, arg):
		self.__name = arg

	def set_lastname(self, arg):
		self.__lastname = arg

	def set_phone(self, arg):
		self.__phone = arg

	def set_height(self, arg):
		self.__height = arg

	def set_weight(self, arg):
		self.__weight = arg
