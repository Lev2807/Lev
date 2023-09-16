# class str22:
#     string = '1, 2, 3, 4, 5'

#     def printData(self):
#         print(self.string[0])
#         print(self.string[-1])

# data = str22()
# data.printData()


# a = {1: 2, 2: 5}
# print(a)


# class A:
#     a = [1, 2, 3, 4, 5]

# class B(A):
#     def printData(self):
#         print(self.a[0])
#         print(self.a[-1])

#     def printData2(self):
#         if len(self.a) % 2 == 0:
#             print('Нету среднего элемента')

#         else:
#             res = len(self.a) / 2

#             res = int(res)

#             print(self.a[res])

# data = B()
# data.printData2()
# data.printData()


# class MyStr:
#     def __init__(self, str1, str2):
#         self.str1 = str1
#         self.str2 = str2

#     def printData(self):
#         a = self.str1 + self.str2[0]
#         b = self.str2 + self.str1[0]
#         print(a, b)

# data = MyStr('Lev', 'Roman')
# data.printData()


# class Calc:
#     num1 = 21
#     num2 = 12

#     def __call__(self):
#         print(self.num1 + self.num2)

# data = Calc()
# data()


# class A:
#     a = [1, 2, 3, 4, 5]

# class B(A):
#     def printData(self):
#         self.a = set(self.a)
#         print(self.a)

# class C(A):
#     def printData2(self):
#         self.a = tuple(self.a)
#         print(self.a)

# data = B()
# data.printData()

# data = C()
# data.printData2()


# a = [1, 2, 3, 4, 5]
# b = min(a)
# c = max(a)

# indexMax = a.index(c)
# indexMin = a.index(b)

# a[indexMax] = a[indexMin]

# print(a)


# class PrintDataPerson:
#     @staticmethod
#     def printData():
#         print('Lev')

#     @staticmethod
#     def printData2():
#         print('Musikhin')

# PrintDataPerson.printData()
# PrintDataPerson.printData2()


# class Strings:
#     str1 = 'Lev'
#     str2 = 'Roman'

#     def __call__(self):
#         for i in self.str1:
#             print(i)

#         for i in reversed(self.str2):
#             print(i)

# data = Strings()
# data()


# a = 8.5
# a = int(a)
# print(a)


# a = True
# a = int(a)
# print(a)


# a = str(input())
# b = str(input())

# def printData(a, b):
#     if len(a) > len(b):
#         print(a)

#     else:
#         print(b)


# printData(a, b)


# def printData(*scores):
    
#     for score in scores:
#         print(score)

# printData(100, 95, 88, 92, 1, 1, 1, 1, 1, 1, 1)


# def printData(*scores):
#     sumRes = 0

#     for score in scores:
#         sumRes += score
    
#     print(sumRes)

# printData(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


# def printScores(*scores):
#     myList = []

#     for score in scores:
#         myList.append(score)

#     print(myList)

# printScores(100, 95, 88, 92)


# def printData(*scores):
#     a = set()
#     b = []

#     for score in scores:
#         if  score < 5:
#             a.add(score)

#         else:
#             b.append(score)

#     print(a)
#     print(b)

# printData(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


# def printData():
#     a = 'Hello world'
#     print(a)

# def printData2():
#     printData()

# printData2()


# class A:
#     a = [1, 2, 3, 4, 5]

# class B(A):
#     def printData(self):
#         print(self.a)

# data = B()
# data.printData()


# a = [1, 2, 3, 4, 5]

# a.reverse()
# print(a)


# a = [1, 2, 3, 4, 5]

# a.pop(2)
# print(a)


# a = (1, 2, 3, 4, 5)
# print(min(a))
# print(max(a))


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# index1 = a.index(6)
# index2 = a.index(10)
# print(index1, index2)


# a = (1, 2, 3, 4, 5)
# a = list(a)
# a[0] = 100
# a[4] = 500
# a = tuple(a)
# print(a)


# a = {"key1": 12, 21:"key2", 30: 45}
# print(a["key1"])
# print(a[30])
# del a["key1"], a[30]

# print(a)


# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}

# c = a & b
# print(c)


# a = (1, 2, 3)
# b = (4, 5)

# print(a + b)


# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = []

# for i in a:
#     if i <= 5:
#         i = 0
#         b.append(i)

#     else:
#         i = 1
#         b.append(i)

# print(b)


# a = {1, 2, 3, 4, 5}
# a = list(a)
# a[0] = 100
# a[-1] = 100
# a = set(a)
# print(a)


# a = [1, 2, 3, 4, 5]
# a.reverse()
# print(a)

# a = (1, 2, 3, 4, 5)
# print(a[0])
# print(a)


# a = [1, 2, 3, 4, 5]
# index1 = a.index(3)
# print(index1)


# class Person:
#     name = 'Lev'
#     age = 11

#     def printData(self):
#         print(self.name, self.age)

# data = Person()
# data.printData()


# class Tablica:
#     students = []

#     def addDataList(self, element):
#         self.students.append(element)
    
#     def deleteDataList(self, element):
#         self.students.remove(element)
    
#     def clearDataList(self):
#         self.students.clear()

#     def printDataList(self):
#         print(self.students)

# data = Tablica()
# data.addDataList('Lev')
# data.addDataList('Roman')
# data.addDataList('Timur')
# data.printDataList()
# data.addDataList('Egor')
# data.printDataList()
# data.deleteDataList('Roman')
# data.deleteDataList('Lev')
# data.printDataList()


# class List1:
#     a = [1, 2, 3, 4, 5]

#     def printData(self):
#         self.a.reverse()
#         print(self.a)

# data = List1()
# data.printData()



