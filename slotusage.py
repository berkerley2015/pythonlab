class Student(object):
	__slots__ = ('__name', '__age')
	def __init__(self, name, age):
		self.__name = name
		self.__age = age
	#end of __init__(self, name, age)
	
	def __str__(self):
		return 'Student object (name: %s)' % self.__name
	#end of __str__(self)
	
	__repr__ = __str__
	
	@property
	def name(self):
		return self.__name
	#end of name(self)
	
	@name.setter
	def name(self, student_name):
		if not isinstance(student_name, str):
			raise ValueError('student\'s name should be a string')
		self.__name = student_name			
	#end of name(self, student_name)
	
	
#end of Student

s = Student('Michael', 28)



#s.score = 99
s.name = 'Allen Share'
print 'student\'s name is', s.name

print 'test __str__'
print Student('Michael', 29)

Student('Bob Turing', 80)