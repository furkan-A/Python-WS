
class Person():
    def __init__(self, fname, lname, age):
        self.first_name = fname
        self.last_name = lname
        self.age = age
    
    def eat(self):
        print("Person is eating")

class Student(Person):  # inheritance yapilma sekli
    
    def __init__(self, fname, lname, age, school):
        super().__init__(fname, lname, age)
        self.school = school

    def eat(self):
        print("Student is eating")

    def __len__(self):      #  heryerde olana metotlarin burada da olusturulma sekli
        return self.age

p1 = Person('Ali', 'Korkmaz', 36)
s1 = Student('Furkan', 'Aktaş', 21, 'Ege Uni')

print(type(p1))
print(type(s1))

print(p1.eat())
print(s1.eat())

name  = 'furkanaktas'

print(len(name))
print(len(s1))  