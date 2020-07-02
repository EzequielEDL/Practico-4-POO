class Province(object):
	__name = None
	__capital = None
	__quant_hab = None
	__quant_dep = None

	def __init__(self, name, capital, quant_hab, quant_dep):
		self.__name = self.__valid(name, 'Nombre necesario')
		self.__capital = self.__valid(capital, 'Capital necesario')
		self.__quant_hab = self.__valid(quant_hab, 'Cant. Hab. necesario')
		self.__quant_dep = self.__valid(quant_dep, 'Cant. Dep. necesario')

	def __str_(self):
		return f'{self.__name}, {self.__capital}, {self.__quant_hab},\
			{self.__quant_dep}'
	
	def __valid(self, value, message):
		if not value:
			raise ValueError(message)
		return value

	def toJSON(self):
		return dict(
			__class__ = self.__class__.__name__,
			__attributes__ = dict(
							name = self.__name,
							capital = self.__capital,
							quant_hab = self.__quant_hab,
							quant_dep = self.__quant_dep
							)
						)

	def get_name(self):
		return self.__name

	def get_capital(self):
		return self.__capital

	def get_quant_hab(self):
		return self.__quant_hab

	def get_quant_dep(self):
		return self.__quant_dep

	def set_name(self, arg):
		self.__name = arg

	def set_capital(self, arg):
		self.__capital = arg

	def set_quant_hab(self, arg):
		self.__quant_hab = arg

	def set_quant_dep(self, arg):
		self.__quant_dep = arg
