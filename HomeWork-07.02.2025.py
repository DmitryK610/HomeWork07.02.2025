#1
class Counter:
    def __init__(self, count):
        self.count = count

    def increment(self):
        self.count +=1
        return self.count

    def decrement(self):
        self.count -=1
        return self.count
    def reset(self):
        self.count = 0

    def get_count(self):
        return self.count

counter = Counter(5)
print(counter.increment())
print(counter.get_count())

#2
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def change_email(self, new_email):
        self.email = new_email

    def hello_user(self):
        print(f"Привет, {self.name.title()}, адрес твоей электронной почты: {self.email}")

user = User("Вася", "vasy@mail.ru")
user.hello_user()
user.change_email("Vasy@gmail.com")
user.hello_user()

#3
class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def square(self):
        return self.side_length ** 2

    def perimeter(self):
        return self.side_length * 4

    def change_side_length(self, new_side_length):
        self.side_length = new_side_length

square = Square(10)
print(square.square())
print(square.perimeter())
square.change_side_length(5)
print(square.square())
print(square.perimeter())

#4
class Bank:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def withdraw_balance(self, n):
        if self.balance >= 0:
            if n <= self.balance:
                self.balance = self.balance - n
                print(f"Текущий баланс после снятия {n}  : {self.balance} ")
            else:
                print("Недостаточно средств для снятия")

    def replenishment_balance(self, n):
        if n > 0:
            self.balance = self.balance + n
            print(f"Текущий баланс после пополнения {n} : {self.balance}")

    def get_balance(self):
        print(f"Баланс счета {self.account_number} составляет {self.balance}")

bank = Bank(382383, 1000)
bank.withdraw_balance(994)
bank.replenishment_balance(38)
bank.get_balance()

#5
class Animal:
    def speak(self):
        print(f"")

class Dog(Animal):
    def speak(self):
        print("Гав")

class Cat(Animal):
    def speak(self):
        print("Мяу")

#6
class Gradebook:
    average_list = []
    def __init__(self):
        self.students = {}

    def add_student(self, name, grades):
        if name not in self.students:
            self.students[name] = grades
        else:
            print(f"Студент с именем {name} уже существует.")

    def add_grade(self, name, grade):
        if name in self.students:
            self.students[name].append(grade)
        else:
            print(f"Студента с именем {name} не существует.")

    def average(self, name):

        grades = self.students[name]
        average_grade = sum(grades)/len(grades)
        self.average_list.append(average_grade)
        return average_grade
    def average_class(self):
        return f"Средний балл по классу: {round(sum(self.average_list)/len(self.average_list), 2)}"
gradebook = Gradebook()
gradebook.add_student("Вася", [4, 5, 3, 4])
gradebook.add_student("Петя", [5, 5, 5, 5])
gradebook.add_student("Олег", [3, 4, 3, 5])
gradebook.add_grade("Вася", 5)
print(gradebook.average("Вася"))
print(gradebook.average("Петя"))
print(gradebook.average("Олег"))
print(gradebook.average_class())