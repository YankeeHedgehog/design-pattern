class Person {
  name: string
  age: number
  constructor(name: string, age: number) {
    this.name = name
    this.age = age
  }

  public sayHello = () => {
    console.log(`Hello, I'm ${this.name} . I ${this.age} years old.`)
  }
}

const person = new Person('mahito', 23)
person.sayHello()

class Student {
  name: string
  age: number
  belong: string
  constructor(person: Person, belong: string) {
    this.name = person.name
    this.age = person.age
    this.belong = belong
  }

  public sayHello = () => {
    console.log(`Hello, I'm ${this.name} . I ${this.age} years old and belong to ${this.belong}`)
  }
}

const student = new Student(person, 'Oita university')
student.sayHello()