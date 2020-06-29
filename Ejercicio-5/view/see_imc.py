import tkinter as tk
from view.patient_form import PatientForm


class SeeImc(tk.Toplevel):
	def __init__(self, parent, height, weight):
		super().__init__(parent)
		self.resizable(0,0)
		self.__center_window()
		self.imc = tk.StringVar()
		self.body_comp = tk.StringVar()
		self.set_imc(height, weight)
		self.label1 = tk.Label(self, text = 'IMC:')
		self.label2 = tk.Label(self, text = 'Composicion corporal:')
		self.label3 = tk.Label(self, text = self.imc)
		self.label4 = tk.Label(self, text = self.body_comp)
		self.button1 = tk.Button(self, text = 'Volver', command = self.destroy)

		opts = {'padx': 20, 'pady': 4}
		self.label1.pack(side = tk.TOP, **opts)
		self.label3.pack(side = tk.TOP, **opts)
		self.label2.pack(side = tk.TOP, **opts)
		self.label4.pack(side = tk.TOP, **opts)
		self.button1.pack(side = tk.TOP, **opts)

		self.grab_set()
		self.wait_window()

	def set_imc(self, height, weight):
		imc = weight / (((height) / 2) ** 2)
		self.imc = '{:.1}'.format(imc)

		if imc < 18.5:
			self.body_comp = 'Peso inferior al normal'
		elif imc < 24.9:
			self.body_comp = 'Peso Normal'
		elif imc < 29.9:
			self.body_comp = 'Peso superior al normal'
		else:
			self.body_comp = 'Peso obesidad'

	def __center_window(self):
		win = self
		width = 200
		height = 150
		height_screen = win.winfo_screenwidth()
		width_screen = win.winfo_screenheight() 
		x = int((height_screen / 2) - (width / 2))
		y = int((width_screen / 2) - (height / 2))
		win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
