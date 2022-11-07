class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 継承
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

# インスタンス化
yamada = Student("山田", 20, 2)

# コンポジション
class Student_:
    def __init__(self, person, grade):
        self.name = person.name
        self.age = person.age
        self.grade = grade

# インスタンス化
yamada = Student(Person("山田", 20), 2)