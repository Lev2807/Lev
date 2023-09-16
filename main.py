
# class Person:
#     name = 'Lev'
#     age = 11

#     def printData(self):
#         print(self.name, self.age)


# data = Person()
# data.printData()


# class Person:

#     def printMes(self):
#         print('Hello')


#     def printData(self):
#         self.printMes()



# data = Person()
# data.printData()

# class Person:


#     __age = 22

#     def printDataAge(self):
#         print(self.__age)

# data = Person()
# data.printDataAge()

# class MyLenStr:
#     str1 = 'Lev'

#     def printData(self):
#         print(len (self.str1))

# string = MyLenStr()
# string.printData()


# class Calc:
#     num1 = 12
#     num2 = 21

#     def plus(self):
#         print(self.num1 + self.num2)

# answer = Calc()
# answer.plus()     


# class String:
    
#     def printData(self, str1):
#         print(len(str1))

# str2 = String()
# str2.printData('qwertyuiop')

# class CheckAge:

#     def printData(self, age):
#         if age < 18:
#             print('Ты маленький!')

#         else:
#             print('Ты взрослый')

# personAge = CheckAge()
# personAge.printData(19)

# class Calc:
#     num1 = 22
#     num2 = 33

#     def plus(self):
#         return self.num1 + self.num2

# res Calc()
# print(res.plus())

# def printMes():
#     return 'Hello world'

# a = printMes()
# print(a)
# print(type(a))


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def printData(self):
#         print(self.name, self.age)

# res = Person('Roman', 22)
# res.printData()


# class CheckPassword:

#     def printData(self, str1):
#         if len(str1) < 8:
#             print('Ненадёжный пароль!')

#         else:
#             print('Надёжный пароль')

# user = CheckPassword()
# user.printData('6371527356')


# class CheckPassword:
#     def __init__(self, password):
#         self.password = password

#     def check(self):
#         if len(self.password) < 8:
#             print('Ненадёжный пароль!')

#         else:
#             print('Надёжный пароль')

# password = CheckPassword('18898906698')
# password.check()


# class Step:
#     num1 = 5

#     def printData(self):
#         print(self.num1 ** 2)

# data = Step()
# data.printData()


# class Sum:

#     def printData(self, a, b):
#         print(a / b)

# data = Sum()
# data.printData(20, 5)


# class DataPerson:
#     __name = 'Lev'

#     def printData(self):
#         print(self.__name)

# data = DataPerson()
# data.printData()


# class DataPerson:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def printData(self):
#         print(self.name,self.age)

# person = DataPerson('Roman', 22)
# person.printData()

# name = 'Lev'
# age = 11

# print('Привет меня зовут', name,' мне', age,' лет')



# class MaxElement:
#     def __init__(self, num1, num2):
#          self.num1 = num1
#          self.num2 = num2

#     def printData(self):
#         print(max(self.num1, self.num2))

# data = MaxElement(22, 45)
# data.printData()


# class Data:
#     name = 'Lev'
#     age  = 11

# class Person(Data):
#     pass

# a = Person()
# print(type(a))


# class PersonName:
#     def __init__(self, name, count):
#         self.name = name
#         self.count = count

#     def printData(self):
#         for i in range(self.count):
#             print(self.name)

# data = PersonName('Lev', 13)
# data.printData()


# class String:
#     def __init__(self,str1):
#         self.str1 = str1

#     def printData(self):
#         if len(self.str1) <=10:
#             print('Маленький пароль!')

#         else:
#             print('Большой пароль')

# data = String('3456745567')
# data.printData()


# class PrivatAtribut:
#     __name = 'Lev'

#     def printData(self):
#         print(self.__name)

# data = PrivatAtribut()
# data.printData()


# class Calc:
#     num1 = 1
#     num2 = 99

#     def plus(self):
#         print(self.num1 + self.num2)

# class Method(Calc):
#     num3 = 88

# class A(Method):
#     def l(self):
#         print(self.num1)

# res = A()
# res.l()


# class Calc:
#     num1 = 21
#     num2 = 12

# class Calc2(Calc):
    
#     def printData(self):
#         print(self.num1 + self.num2)

# data = Calc2()
# data.printData()


# class Num:
#     num1 = 12

#     def printData(self):
#         if self.num1 < 100:
#             del self.num1

#         else:
#             print(self.num1)

# data = Num()
# data.printData()
        

# class A:
#     num1 = 22

# class B:
#     num2 = 33

# class C(A, B):
#     pass

# c = C()
# print(c.num1)
# print(c.num2)


# class A:
#     num1 = 12

# class B:
#     num2 = 21

# class C(A, B):

#     def printData(self):
#         print(self.num1 + self.num2)

# data = C()
# data.printData()


# class nameAge:

#     @staticmethod
#     def printData(name, age):
#         print(f"Hello, {name}, age {age}"")

# nameAge.printData('Lev', 11)


# class Num:

#     @staticmethod
#     def printData(num1, num2):
#         return num1**num2

# print(Num.printData(23, 3))


# class PrivatNum:
#     __num1 = 12
#     __num2 = 21

#     def printData(self):
#         print(self.__num1 + self.__num2)

# data = PrivatNum()
# data.printData()


# class A:
#     num1 = 15
#     num2 = 35

# class B(A):
#     def printData(self):
#         print(self.num1 + self.num2)

# data = B()
# data.printData()


# class String:

#     def printData(self, str1):
#         print(len(str1))

# data = String()
# data.printData('31554657468')


# from datetime import datetime
# class Time:
#     def printData(self):
#         timeNow = datetime.now()
#         print(timeNow)

# data = Time()
# data.printData()


# import random

# class RandomNum:

#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2

#     def printData(self):
#         a = random.uniform(self.num1, self.num2)
#         print(a)

# data = RandomNum(13, 26)
# data.printData()


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f'Hello {self.name}, age {self.age}'

# person = Person('Lev', 11)
# print(person)


# class NumberString:
#     num1 = 22

#     def printData(self):
#         a = str(self.num1)
#         print(a)
#         print(type(a))

# data = NumberString()
# data.printData()


# class Listik:
#     listik = [1, 3, 5, 2, 4]

# class Listik2(Listik):

#     def printData(self):
#         print(max(self.listik))
#         print(min(self.listik))

# data = Listik2()
# data.printData()


# class String:

#     def __init__(self, str1):
#         self.str1 = str1

#     def printData(self):
#         print(self.str1)
#         print(len(self.str1))
#         print(self.str1[0])
#         print(self.str1[-1])

# data = String('My name is Lev')
# data.printData()


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def printData(self):
#         print(self.name, self.age)

# person = Person('Lev', 11)
# person.printData()

# print(person.name)
# print(person.age)


# class Person:
#     __num = 101

#     def __printNum(self):
#         print(self.__num)

#     def printN(self):
#         self.__printNum()

# person = Person()
# person.printN()


# class Numbers:
#     num1 = 12
#     num2 = 21

# data = Numbers()
# data.num1 = 24
# print(data.num1)


# class Person:
#     __name = 'Lev'
#     __surname = 'Musikhin'

#     def printData(self):
#         print(f"Hello {self.__name} {self.__surname}")

# data = Person()
# data.printData()

# data.__name = 'Roman'
# data.printData()


# class Name:
#     @staticmethod
#     def printData():
#         print('Lev')

# Name.printData()


# class Calc:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2

#     def printData(self):
#         print(self.num1 + self.num2)

# data = Calc(21, 12)
# data.printData()


# class Person:
#     name = 'Lev'
#     age = 11

# class Person2(Person):
#     def printData(self):
#         print(self.name, self.age)

# data = Person2()
# data.printData()


# class Person:
#     def __init__(self, name):
#         self.__name = name
#         self.__age = 1

#     def set_age(self, age):
#         if 1 < age < 110:
#             self.__age = age
#         else:
#             print('Недопустимый возраст')

#     def get_age(self):
#         return self.__age

#     def get_name(self):
#         return self.__name

#     def display_info(self):
#         print(f'Имя: {self.__name}\tВозраст: {self.__age}')


# tom = Person('Tom')
# tom.display_info()
# tom.set_age(-3486)
# tom.set_age(25)
# tom.display_info()


# class String:

#     def __init__(self, str1):
#         self.str1 = str1

#     def printData(self):
#         print(len(self.str1))

# data = String('qerrttghjyft')
# data.printData()


# class CheckLine:
#     def __init__(self, str1):
#         self.__str1 = str1

#     def set_str1(self, str1):
#         if len(str1) > 8:
#             self.__str1 = str1
#         else:
#             print('Короткая строка')

#     def get_str1(self):
#         return self.__str1

#     def display_info(self):
#         print(self.__str1)


# data = CheckLine('54')
# data.set_str1('qwertyu')
# data.display_info()


# class A:
#     def printData(self):
#         print('Hello')

# class B:
#     def printData2(self):
#         print('World')
    
# class C(A, B):
#     pass

# data = C()
# data.printData()
# data.printData2()


# class Numbers:
#     __num1 = 21
#     __num2 = 12

#     def printData(self):
#         print(self.__num1, self.__num2)

# data = Numbers()
# data.printData()
        

# class MyList:
#     def printData(self, list1):
#         list1.reverse()
#         print(list1)

# data = MyList()
# data.printData([1,2,3,4,5])


# class MyList:
#     def printData(self, list1):
#         for i in list1:
#             print(i)

# data = MyList()
# data.printData([1,2,3,4,5])


# class MyList:
#     @staticmethod
#     def printData():
#         list1 = [1,2,3,4,5]
#         print(list1)

# MyList.printData()


# class Registration:
#     def __init__(self, name, password, againPassword):
#         self.name = name
#         self.password = password
#         self.againPassword = againPassword

#     def printData(self):
#         if len(self.password) < 10:
#             print('Короткий пароль!')

#         else:
#             print('Подтвердите пароль')

#     def printData2(self):
#         if self.password == self.againPassword:
#             print(f'Пользователь {self.name} зарегестрирован')

#         else:
#             print('Пароли не совпадают!')

# namePerson = 'Lev'
# passwordPerson = str(input())
# againPassword = str(input())

# data = Registration(namePerson, passwordPerson, againPassword)
# data.printData2()


# class Number:
#     number1 = 12
#     number2 = 21

#     def io(self):
#         print(self.number1, self.number2)

# a = Number()
# a.number1 = 500
# a.number2 = 100
# a.io()



# class Number1:
#     __number1 = 12
#     __number2 = 31

#     def io(self):
#         print(self.__number1, self.__number2)

# b = Number1()
# b.__number1 = 400
# b.__number2 = 990
# b.io()


# def number(num):
#     match num:
#         case 1:
#             print('Lev')

#         case 2:
#             print('Roman')

#         case _:
#             print('Error')

# number(66)


# def number(value, num1, num2):
#     match value:
#         case '+':
#             return num1 + num2

#         case '-':
#             return num1 - num2

#         case '*':
#             return num1 * num2

#         case '/':
#             return num1 / num2

# print(number('*', 8, 9))


# def number(num1, str1):
#     match num1:
#         case 1:
#             print(str1)

#         case 2:
#             print(len(str1))

#         case 3:
#             print(str1[0], str1[-1])

#         case _:
#             print('Error')

# number(66, 'qwertyu')            


# def printData(num1):
#     match num1:
#         case 1:
#             a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#             print(a)   

#         case 2:
#             b = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#             print(b)

#         case 3:
#             c = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#             print(c)

#         case _:
#             print('Error')

# printData(2)


# class Calc:
#     __num1 = 12
#     __num2 = 21

#     def printData(self):
#         print(self.__num1 + self.__num2)


# data = Calc()
# data.printData()


# a = lambda a, b: a + b

# print(a(22, 33))


# a = lambda b, c, d, e, f : print(max(b, c, d, e, f))

# a(21, 34, -4, 87, 678)


# class Person:
#     def __init__(self, name):
#         self.__name = name
#         self.__age = age

#     def get_checkAge(self, age):
#         if age >= 18:
#             self.__age = age

#         else:
#             print('Маленький человек')

#     def set_age(self):
#         return self.__age

#     def set_name(self):
#         return self.__name

#     def printData(self):
#         print(self.__name, self.__age)

# person1 = Person('Roman')
# person1.printData()

# person1.get_checkAge(22)
# person1.printData()


# class Person:
#     def __init__(self, name):
#         self.__name = name
#         self.__password = ''

#     def get_checkPassword(self, password):
#         if len(password) >= 10:
#             self.__password = password

#         else:
#             print('Маленький пароль!')

#     def set_password(self):
#         return self.__password

#     def set_name(self):
#         return self.__name

#     def printData(self):
#         print(self.__name, self.__password)

# person1 = Person('Lev')
# person1.printData()

# person1.get_checkPassword('1212124545657')
# person1.printData()


# def print_nello(language):
#     match language:
#         case 'Uk':
#             print('Привет')
#         case 'English':
#             print('Hello')
#         case 'German':
#             print('Hallo')


# def print_data(user):
#     match user:
#         case ('Tom', 37):
#             print("default user")
#         case ('Tom', age):
#             print(f"Age: {age}")
#         case (name, 22):
#             print(f"name: {name}")
#         case (name, age):
#             print(f"Name: {name} Age: {age}")


# print_data(('Tom', 37))
# print_data(('Tom', 28))
# print_data(('Sam', 22))
# print_data(('Bob', 41))
# print_data(('Tom', 33, 'Google'))


# def printData(str1):
#     match str1:
#         case 1:
#             a = [1, 2, 3, 4, 5]
#             print(a)

#         case 2:
#             b = (1, 2, 3, 4, 5)
#             print(b)

#         case 3:
#             c = {1, 2, 3, 4, 5}
#             print(c)

#         case 4:
#             d = {1:2, 4:5}
#             print(d)

#         case _:
#             print('Error')

# printData(2)


# class CheckIndexList:
#     a = [1, 2, 3, 4, 5]
#     def printData(self, index):
#         if index <= len(self.a):
#             print(self.a[index])

#         else:
#             print('Несуществует такого елемента!')

# data = CheckIndexList()
# data.printData(2)


# class Culc:
#     def printData(self, num1, num2):
#         try:
#             a = num1 / num2
#             print(a)
        
#         except(ZeroDivisionError):
#             print('На ноль делить нельзя')

# data = Culc()
# data.printData(21, 0)


# a = [1, 2, 3, 4, 5]
# a = set(a)
# print(type(a))


# class Calc:
#     num1 = 12
#     num2 = 21

#     def printData(self):
#         num1 = str(self.num1)
#         num2 = str(self.num2)
#         print(type(num1), type(num2))
#         print(num1, num2)

# data = Calc()
# data.printData()


# class A:
#     a = [1, 2, 3, 4, 5]

# class B(A):
#     def printData(self):
#         print(self.a[0])
#         print(self.a[-1])

# data = B()
# data.printData()


# class SumClass:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
    
#     def printData(self):
#         if type(self.num1) == int and type(self.num2) == int:
#             print(self.num1 + self.num2)

#         else:
#             print('Error')

# data = SumClass('12', 21)
# data.printData()


# class A:
#     a = [1, 2, 3, 4, 5]

# class B(A):
#     def printData(self, index):
#         try:
#             print(self.a[index])

#         except(IndexError):
#             print('Error')

# data = B()
# data.printData(5)


# class RandomSymvol:
#     a = []
#     def printData(self):
#        for i in range(10):
#         i = random.randint(0, 20)
#            self.a.append(i)
#         print(self.a)
           

# data = RandomSymvol()
# data.printData()


# class List1:
#     a = [1, 2, 3, 4, 5]

#     def printData(self):
#         a = tuple(self.a)
#         print(type(a))
#         print(a)

#     def printData2(self):
#         a = set(self.a)
#         print(type(a))
#         print(a)

# data = List1()
# data.printData()
# data.printData2()
