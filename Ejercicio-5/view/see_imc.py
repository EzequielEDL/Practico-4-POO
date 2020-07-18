import tkinter as tk
from view.widgets import *
from view.patient_form import PatientForm


class SeeImc(Toplevel):
	def __init__(self, parent, height, weight):
		super().__init__(parent)
		self.rs = Resources()
		center_window(self, w = 220, h = 170)
		self.imc = tk.StringVar()
		self.body_comp = tk.StringVar()
		self.set_imc(height, weight)
		self.label1 = Label(self, text = 'IMC:', font = self.rs.font1)
		self.label2 = Label(self, text = 'Composicion corporal:', font = self.rs.font1)
		self.label3 = Label(self, text = self.imc)
		self.label4 = Label(self, text = self.body_comp)
		self.button1 = Button(self, text = ' Volver',
			image = self.rs.icon5, command = self.destroy)

		opts = {'padx': 20, 'pady': 4}
		self.label1.pack(side = tk.TOP, **opts)
		self.label3.pack(side = tk.TOP, **opts)
		self.label2.pack(side = tk.TOP, **opts)
		self.label4.pack(side = tk.TOP, **opts)
		self.button1.pack(side = tk.TOP, ipady = 1, ipadx = 5,**opts)

		self.grab_set()
		self.wait_window()

	def set_imc(self, height, weight):

		height = height / 100
		imc = weight / (height ** 2)
		print(f'{imc}')
		self.imc = '{:.4}'.format(imc)


		if imc < 18.5:
			self.body_comp = 'Peso inferior al normal'
		elif imc < 24.9:
			self.body_comp = 'Peso Normal'
		elif imc < 29.9:
			self.body_comp = 'Peso superior al normal'
		else:
			self.body_comp = 'Peso obesidad'
