from view.widgets import *
from view.province_form import ProvinceForm


class NewProvince(Toplevel):
	def __init__(self, master):
		super().__init__(master)
		fields = ('Nombre', 'Capital', 'Cantidad de Habitantes',
		'Cantidad de departamentos/partidos')
		self.rs = Resources()
		self.title('Nueva Provincia')
		center_window(self, w = 480, h = 250)
		self.province = None
		self.province_form = ProvinceForm(self)
		self.button1 = Button(self, text = ' Confirmar',
			image = self.rs.icon2, command = self.confirm)
		self.province_form.maping(fields)
		self.province_form.grid(row = 0, column = 0, padx = 20, pady = 15)
		self.button1.grid(row = 1, column = 0, ipadx = 5,
			ipady = 2)

	def confirm(self):
		self.province =  self.province_form.create_value()

		if self.province:
			self.destroy()

	def show(self):
		self.grab_set()
		self.wait_window()
		return self.province
