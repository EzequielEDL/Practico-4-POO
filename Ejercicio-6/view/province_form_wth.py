from view.widgets import *
from view.province_form import ProvinceForm


class ProvinceFormWth(ProvinceForm):
	def __init__(self, master):
		super().__init__(master)		
		fields = ('Nombre', 'Capital', 'Cantidad de Habitantes',
		'Cantidad de departamentos/partidos', 'Temperatura', 'Sensación térmica', 'Humedad')
		super().maping(fields)

