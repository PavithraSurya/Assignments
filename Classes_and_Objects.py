'''
A class is a user-defined blueprint or prototype from which
objects are created. 

Classes provide a means of bundling data and 
functionality together.

Creating a new class creates a new type of object, 
allowing new instances of that type to be made. 

Each class instance can have attributes attached to it for maintaining
its state. Class instances can also have methods (defined by their class)
for modifying their state.


An object consists of : 
State 		==> It is represented by the attributes of an object. 
			    It also reflects the properties of an object.

Behaviour   ==> It is represented by the methods of an object. 
                It also reflects the response of an object to other objects.

Identity	==> It gives a unique name to an object and enables one
				object to interact with other objects.


Instance variables are for data, unique to each instance 
Instance variables are variables whose value is assigned inside
a constructor or method with self whereas

Class variables are for attributes and methods shared by all instances of the class. 
Class variables are variables whose value is assigned in the class.

'''

class Student:
	School_Name = "Vidya Mandir"
	def __init__(self, a, b):	# Constructor
		self.Name = "India"
		self.second_name = '------'

	def add_second_name(self, v):
		self.second_name = v


	def add_student_to_section(self, v):
		self.section = v


Student1 = Student()
print(Student1.Name)
