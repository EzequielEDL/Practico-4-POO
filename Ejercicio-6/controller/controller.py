from view.new_province import NewProvince


class Controller(object):
	
	def __init__(self, view, handle):
		self.__view = view
		self.__handle = handle
		self.__selection = -1

	def select_province(self, index):
		self.__selection = index
		province = self.__handle[index]
		self.__view.see_province(province)

	def start(self):
		for i in self.__handle:
			self.__view.add_province(i)
		
		self.__view.mainloop()

	def create_province(self):
		new_province = NewProvince(self.__view).show()

		if new_province:
			self.__handle.append(new_province)
			self.__view.add_province(new_province)

	def exit_save(self):
		return self.__handle.toJSON()
