class Cat:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def speak(self):
        return f'Hello, this is {self.name} with age {self.age}!'
