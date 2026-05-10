"""
Suppose I require single method from superclass
without Inheritance, How would I?

No need to Inherit all the methods from superclass
to subclass like Traditional Inheritance.

Just call the classnameA.methodnameA() In your
classB
"""

class A:
	def add(self):
		return 10 + 3
	
	def sub(self):
		return 10 - 4
	
	def mul(self):
		return 10 * 3
	
	def div(self):
		return 10 // 3


class B:
	def ownself(self):
		return "ownself"

	def do_something(self):
		return A().mul()


print(B().do_something())
