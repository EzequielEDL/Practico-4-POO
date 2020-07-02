from view.widgets import *
from view.province_form import ProvinceForm


class ProvinceFormWth(ProvinceForm):
	def __init__(self, master):
		super().__init__(master)
		
		fields = ('Temperatura', 'Sensación térmica', 'Humedad') + ProvinceForm.fields
		super().create_field(fields)

		