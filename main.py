print ('Hello World')
class Student:
    amound = 0
    print("Hi")
    def __init__(self, name = None):
        self.name = name
        Student.amound += 1
    def __str__(self, name=None):
        return f'login {self.name}'
andri = Student()
dima = Student()
maris = Student()
print(dima.name)
print(andri.name)
print(dima.amound)
print(andri.amound)
print(maris.amound)
dima = Student(name = 'DIMA GLOBUS')
print(dima)