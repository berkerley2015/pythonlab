class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value : self.append(value)
		return type.__new__(cls, name, bases, attrs)
	#endof __new__(cls, name, bases, attrs)
#endof ListMetaclass(type)

class MyList(list):
	__metaclass__ = ListMetaclass
	def __str__(self):
		counter = 0
		for element in self:
			counter = counter + 1
		#endof for
		return 'number of elements in mylist is %d' % counter
	#endof __str__(self)
#endof MyList(list)

myList = MyList()
myList.add(5)
myList.add(9)
print myList