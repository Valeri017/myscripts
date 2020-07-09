class User:
	name = ''
	surname = ''
	age = 0
	email = ''

	def set(self, name, sutname, age):
		self.name = name
		self.surname = surname
		self.age = age

admin = User()
admin.name = 'Admin'
admin.age = 27
admin.email = 'valerij.batalov@list.ru'
print(admin.name)

bob = User()
bob.name = 'Bob'
print(bob.name)