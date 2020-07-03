from view.widgets import *
from model.province import Province
from tkinter import messagebox
import requests


class ProvinceForm(LabelFrame):
	__fields = ('Nombre', 'Capital', 'Cantidad de Habitantes',
		'Cantidad de departamentos/partidos', 'Temperatura',
		'Sensación térmica', 'Humedad')

	def __init__(self, master):
		super().__init__(master)
		self.rs = Resources()
		self.config(text = 'Provincia', pady = 10)
		self.frame = Frame(self)
		self.frame.grid(row = 0, column = 0)

	def maping(self, fields):
		self.entries = list(map(self.create_field, enumerate(fields)))

	def create_field(self, field):
		position, text = field
		label = Label(self.frame, text = text)
		entry = Entry(self.frame, width = 17)
		opts = {'padx': 5, 'pady': 5}
		label.grid(row = position, column = 0, **opts)
		entry.grid(row = position, column = 1, **opts)
		return entry

	def show_value(self, value):
		temp, feels_like, humidity = self.request_province(value.get_name())

		self.values = (value.get_name(), value.get_capital(),
			value.get_quant_hab(), value.get_quant_dep(), 
			temp, feels_like, humidity)

		for entry, value in zip(self.entries, self.values):
			entry.delete(0, END)
			entry.insert(0, value)

	def create_value(self):
		self.values = [e.get() for e in self.entries]
		value = None
		
		try:
			value = Province(*self.values)
		
		except ValueError as e:
			messagebox.showerror('Error de Validacion', str(e), parent = self)

		return value

	def clean(self):
		for entry in self.entries:
			entry.delete(0, END)

	def request_province(self, name):
		url = f'https://api.openweathermap.org/data/2.5/weather?q={name}&units=metric&appid=ec1ca8a3fdeaa0029772d8479aeda4af'
		request = requests.get(url)
		province_json = request.json()
		try:
			temp = province_json['main']['temp']
			feels_like = province_json['main']['feels_like']
			humidity = province_json['main']['humidity']

		except KeyError:
			temp, feels_like, humidity = 'None', 'None', 'None'

		return temp, feels_like, humidity