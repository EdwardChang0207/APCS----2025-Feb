class Person:
    def __init__(self, gender, age, name):
        self.gender = gender
        self.age = age
        self.name = name
    def sayHi(self):
        print(f'hi,我是{self.name}')

pan = Person('male', 29, '潘周聃')
chou = Person('male', 46, '周杰倫')

print(pan.name)
print(f'{pan.age}歲')

# print(type(12)) #type()->判斷資料型態
pan.sayHi()
chou.sayHi()

