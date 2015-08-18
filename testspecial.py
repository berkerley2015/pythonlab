class Student(object):
	def __init__(self):
		self.name = 'Michael'
	#endof __init__(self)
	def __getattr__(self, attr):
		if attr == 'score':
			return lambda: 98
		#endof if
	#endof __getattr__(self)
#end of Student(object)

print Student().score()