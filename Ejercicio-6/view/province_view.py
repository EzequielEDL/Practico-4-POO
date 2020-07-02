from view.widgets import *
from view.province_list import ProvinceList
from view.province_form_wth import ProvinceFormWth


class ProvinceView(Tk):
	def __init__(self):
		super().__init__()
		self.rs = Resources()
		center_window(self, w = 720, h = 390)

		self.frame_list = ProvinceList(self)
		self.button_add = Button(self, text = ' Agregar provincia',
			image = self.rs.icon1)
		self.frame_province = ProvinceFormWth(self)

		self.label = Label(self, text = '')
	
		opts = {'padx': 20, 'pady': 20}
		self.frame_list.grid(rowspan = 2, column = 0, sticky = 'n', **opts)
		self.frame_province.grid(row = 0, column = 1, sticky = 'n', **opts)
		self.button_add.grid(row = 0, column = 1, sticky = 's', ipadx = 5,
			ipady = 2)

	def set_controller(self, ctrl):
		self.button_add.config(command = ctrl.create_province)
		self.frame_list.bind_double_click(ctrl.select_province)

	def add_province(self, province):
		self.frame_list.insert(province)

	def see_province(self, province):
		self.frame_province.show_value(province)