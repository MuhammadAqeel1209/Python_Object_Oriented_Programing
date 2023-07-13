# Python program showing the use of
# @property
class Geeks:
	def __init__(self):
		self._age = 0
		self._name = "Ali"
	
	# using property decorator
	# a getter function
	@property
	def age(self):
		# print("getter method called")
		return self._age
	@property	
	def name(self):
		return self._name
	# a setter function
	@age.setter
	def age(self, a):
		if(a < 18):
			raise ValueError("Sorry you age is below eligibility criteria")
		# print("setter method called")
		self._age = a
	@name.setter
	def name(self,n):
		self._name = n
mark = Geeks()

mark.age = 25
mark.name = "Aqeel"
print(mark.age)
print(mark.name)
