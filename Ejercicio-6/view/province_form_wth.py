from view.widgets import *
from view.province_form import ProvinceForm


class ProvinceFormWth(ProvinceForm):
	def __init__(self, master):
		super().__init__(master)		
		ProvinceForm.fields = ProvinceForm.fields + ('Temperatura', 'Sensación térmica', 'Humedad') 
		super().mapeo()

		