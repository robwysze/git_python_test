class Person:
    def __init__(self, name: str, age: int):
        self.age = age
        self.name = name

    def set_name(self, name: str):
        self.name = name

    def set_age(self, age: int):
        self.age = age

    def introduce(self):
        res = f"I'm {self.name}.\nI'm {self.age}."
        return res
