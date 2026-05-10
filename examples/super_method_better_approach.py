


class A:
	def __init__(self):
		self.a = "aditya"
		self.b = "ball"

	def go(self):		
		self.c = "cat"
		
		d = "dada"
		
		self.e = "eleven"
		
		f = "fight"		
		return d
				


class B(A):	
	def newgo(self):
		super().go()  # Attributes loaded.
		
		# But, write require to type again the return type
		return super().go()

				
	def newgo(self):
		# Must store In a varibale	
		z = super().go()  #Attributes loaded.
		
		# This Is good approach, you are loading all the
		# attributes as well as return type						
		
		return z
				

print(B().newgo())


