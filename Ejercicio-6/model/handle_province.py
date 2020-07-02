from model.province import Province


class HandleProvince(object):
	__list_province = None

	def __init__(self):
		self.__list_province = []

	def __str__(self):
		return f'{self.__list_province}'

	def __getitem__(self, index):
		return self.__list_province[index]

	def __setitem__(self, index, value):
		self.__list_province[index] = value

	def __len__(self):
		return len(self.__list_province)

	#	Convert to JSON
	def toJSON(self):
		provinces = []

		for i in self.__list_province:
			provinces.append(i.toJSON())

		d = dict(
			__class__ = self.__class__.__name__,
			data = provinces
			)

		return d

	def append(self, value):
		self.__list_province.append(value)

	def delete(self, index):
		self.__list_province.pop(index)

	def modify(self, value, xvalue):
		index = self.__find_index(xvalue)
		self.__list_province[index] = province

	def get_list_province(self):
		return self.__list_province

	def __find_index(self, value):
		i = 0	

		while i < len(self.__list_province) and self.__list_province[i] != value:
			i += 1

		if i < len(self.__list_province):
			return i
	