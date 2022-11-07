class Human:
    def __init__(self, name, height, weight, age):
        self.name = name
        self.heigth = height
        self.weight = weight
        self.age = age


class SampleClass:
    def __init__(self, type):
        self.type = type

    def compare(h1, h2):
        if (h1.age > h2.age):
            return 1
        elif (h1.age == h2.age):
            return 0
        else:
            return -1
