from view.widgets import *


class NewProvince(Toplevel):
	def __init__(self, master):
		super().__init__(master)
		self.rs = Resources()
		center_window(self, w = 350, h = 280)
		
		self.province = None

	


	def confirm(self):
		self.province

		if self.province:
			self.destroy()

	def show(self):
		self.grab_set()
		self.wait_window()
		return self.province
