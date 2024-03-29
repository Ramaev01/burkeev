class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sit(self):
        print("Села")
    def roll_over(self):
        print("перекатывается")
my_Dog = Dog("willie", 6)
print(my_Dog.name,my_Dog.age)
my_Dog = Dog("lucy",3)
print(my_Dog.name,my_Dog.age)

