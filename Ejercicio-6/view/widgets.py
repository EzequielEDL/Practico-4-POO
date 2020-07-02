from tkinter import *
from tkinter import font
from PIL import Image, ImageTk


class Resources():
	def __init__(self):
		#	colors
		self.color_bg = '#0e172e'
		self.color_bg2 = '#000000'
		self.color_bg3 = '#242f49'
		self.color_bt = '#18e758'
		self.color_lb1 = '#ffffff'

		#	font
		self.font1 = font.Font(family = 'Helvetica', weight='bold')
		self.font2 = font.Font(family = 'Helvetica')
		
		#	image/icon/variable
		#self.icon1 = PhotoImage(file = "icon/details.png")
		
class Label(Label):
	def __init__(self, master, **kwargs):
		super().__init__(master)
		self.rs = Resources()
		self.config(
			text = '/n',
			font = self.rs.font2,
			fg = self.rs.color_lb1,
			bg = self.rs.color_bg
			)
		self.config(**kwargs)

class Entry(Entry):
	def __init__(self, master, **kwargs):
		super().__init__(master)
		self.rs = Resources()
		self.config(
			bd = 0, font = self.rs.font2,
			bg = self.rs.color_bg3,
			fg = self.rs.color_lb1,
			selectbackground = self.rs.color_bt
			)
		self.config(**kwargs)

class Button(Button):
	def __init__(self, master, **kwargs):
		super().__init__(master)
		self.rs = Resources()
		self.config(
			compound = LEFT,
			bd = 0,
			fg = self.rs.color_lb1,
			text = "/n",
			bg = self.rs.color_bt,
			activeforeground = self.rs.color_lb1,
			activebackground = self.rs.color_bg2,
			font = self.rs.font1
			)
		self.config(**kwargs)

class Listbox(Listbox):
	def __init__(self, master, **kwargs):
		super().__init__(master)
		self.rs = Resources()
		self.config(
			font = self.rs.font2,
			bg = self.rs.color_bg3,
			bd = 2,
			fg = self.rs.color_lb1,
			activestyle = 'none',
			selectbackground = self.rs.color_bt,
			selectforeground = self.rs.color_bg2,
			width = 20,
			highlightthickness = 0,
			height = 15,
			takefocus = 0,
			relief = SUNKEN
			)
		self.config(**kwargs)

class Toplevel(Toplevel):
	def __init__(self, master, **kwargs):
		super().__init__(master)
		self.rs = Resources()
		self.resizable(0,0)
		self.config(
			bg = self.rs.color_bg
			)
		self.config(**kwargs)

class Frame(Frame):
	def __init__(self, master, **kwargs):
		super().__init__(master)
		self.rs = Resources()
		self.config(
			bg = self.rs.color_bg
			)
		self.config(**kwargs)

class LabelFrame(LabelFrame):
	def __init__(self, master, **kwargs):
		super().__init__(master)
		self.rs = Resources()
		self.config(
			fg = self.rs.color_lb1,
			font = self.rs.font1,
			bg = self.rs.color_bg
			)
		self.config(**kwargs)

class Tk(Tk):
 	def __init__(self, **kargs):
 		super().__init__()
 		self.rs = Resources()
 		self.config(
			bg = self.rs.color_bg
			)
 		self.config(**kargs)

def center_window(self, w, h):
		win = self
		width = w
		height = h
		height_screen = win.winfo_screenwidth()
		width_screen = win.winfo_screenheight() 
		x = int((height_screen / 2) - (width / 2))
		y = int((width_screen / 2) - (height / 2))
		win.geometry('{}x{}+{}+{}'.format(width, height, x, y))