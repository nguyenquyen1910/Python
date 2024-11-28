class my_class:
    name="Quyen",
    age=18,
    country="Nghe An",
    def __init__(self,english,score):
        self.english=english
        self.score=score
p1=my_class("Toeic",700)
print(p1.english)
print(p1.score)
    

# Ham string trong class
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name} {self.age}"
    def myfunc(self):
        print("Hello my name is",self.name)
p1=Person("Quyen",19)
print(p1)
p1.myfunc() # Phuong thuc goi ham co ben trong class