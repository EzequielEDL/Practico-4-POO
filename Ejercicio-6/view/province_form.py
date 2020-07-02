from view.widgets import *


class ProvinceForm(LabelFrame):
	fields = ('Nombre', 'Capital', 'Cantidad de Habitantes',
		'Cantidad de departamentos/partidos')

	def __init__(self, master):
		super().__init__(master)

		self.config(text = 'Provincias', padx = 15, pady = 10)
		self.frame = Frame(self)
		self.entries = list(map(self.add_field, enumerate(self.fields)))
		self.frame.grid(row = 0, column = 0)

	def create_field(self, field):
		position, text = field
		label = Label(self.frame, text = text)
		entry = Entry(self.frame, width = 25)
		opts = {'padx': 5, 'pady': 5}
		label.grid(row = position, column = 0, **opts)
		entry.grid(row = position, column = 1, **opts)
		return entry

	def show_value(self, value):
		values = (value.get_name(), value.get_capital(),
			value.get_quat_hab(), value.get_quat_dep())

		for entry, value in zip(self.entries, values):
			entry.delete(0, END)
			entry.insert(0, value)

	def create_value(self):
		values = [e.get() for e in self.entries]
		value = None
		
		try:
			value = value(*values)
		
		except ValueError as e:
			messagebox.showerror('Error de Validacion', str(e), parent = self)

		return value

	def clean(self):
		for entry in self.entries:
			entry.delete(0, tk.END)