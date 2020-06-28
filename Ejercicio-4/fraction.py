import re


class Fraction:
	__num = 0
	__den = 0

	def __str__(self):
		return f'{self.__num}┘{self.__den}'	

	def __init__(self, num, den = 1):
		if re.search('┘', num) is not None:
			x = num.split('┘')
			self.__num = float(x[0])
			self.__den = float(x[1])
		else:
			self.__num = float(num)
			self.__den = den

	def __mul__(self, fraction2):
		num = self.__num * fraction2.get_num()
		den = self.__den * fraction2.get_den()
		return self.__simply(num, den)

	def __truediv__(self, fraction2):
		num = self.__num * fraction2.get_den()
		den = self.__den * fraction2.get_num()

		if self.__den == fraction2.get_den():
			return self.__simply(num, den)
		else:
			return self.__simply(num, den)

	def __add__(self, fraction2):
		num1 = self.__num * fraction2.get_den()
		num2 = self.__den * fraction2.get_num()
		num = num1 + num2
		den = self.__den * fraction2.get_den() 
		return self.__simply(num, den)

	def __sub__(self, fraction2):
		num1 = self.__num * fraction2.get_den()
		num2 = self.__den * fraction2.get_num()
		num = num1 - num2
		den = self.__den * fraction2.get_den() 
		return self.__simply(num, den)

	def __simply(self, num, den):
		try:
			if num % den == 0:
				return f'{num / den}'
			else:
				return self.__valid(num, den)
		
		except ZeroDivisionError:
			return 'Math ERROR'
	
	def __valid(self, num, den):
		if den == 1:
			return f'{num / den}'
		elif den == num:
			return f'{num / den}'
		else:
			return f'{num}┘{den}'

	def get_num(self):
		return self.__num

	def get_den(self):
		return self.__den

