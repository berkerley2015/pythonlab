def function(self, name='world'):
	print 'Hello, %s!' % name
#endof tempalte(self, name='world')

Hello = type('Hello', (object,), dict(sayHello=function))

hellor = Hello()

hellor.sayHello()

print 'type of Hello is', type(Hello)

print 'type of hellor is', type(hellor)

print 'type of sayHello is', type(hellor.sayHello)
