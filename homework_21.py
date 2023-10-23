# Завдання 1
# 1. Створити клас User для користувача, клас містить наступні поля:
# Ім’я , Призвіще , Вік та Кількість підписок. У кожного поля є свої обмеження:
# a. Ім’я має містити більше 3 символів
# b. Призвіще має містити більше 4 символів
# c. Кількість років має знаходитись у діапазоні від 18 до 60
# d. Кількість підписок не більше за 999


# class User:
#     def __init__(self, first_name, last_name, age, num_subscriptions):
#         self.set_first_name(first_name)
#         self.set_last_name(last_name)
#         self.set_age(age)
#         self.set_num_subscriptions(num_subscriptions)
#
#     def set_first_name(self, first_name):
#         if len(first_name) > 3:
#             self.first_name = first_name
#         else:
#             raise ValueError("Ім'я має містити більше 3 символів")
#
#     def set_last_name(self, last_name):
#         if len(last_name) > 4:
#             self.last_name = last_name
#         else:
#             raise ValueError("Призвіще має містити більше 4 символів")
#
#     def set_age(self, age):
#         if 18 <= age <= 60:
#             self.age = age
#         else:
#             raise ValueError("Кількість років має бути в діапазоні від 18 до 60")
#
#     def set_num_subscriptions(self, num_subscriptions):
#         if num_subscriptions <= 999:
#             self.num_subscriptions = num_subscriptions
#         else:
#             raise ValueError("Кількість підписок не може бути більше 999")
#
#     def __str__(self):
#         return f'Ім\'я: {self.first_name}, Призвіще: {self.last_name}, Вік: {self.age}, Кількість підписок: {self.num_subscriptions}'
#
# # Приклад створення користувача
# try:
#     user = User("Микола", "Пістоль", 30, 500)
#     print(user)
# except ValueError as e:
#     print(f"Помилка: {e}")

# Завдання 2
# Створити Дескриптор для керування рядковими значеннями та дескриптор для керування чисельними значеннями.
# Врахувати обмеження встановлені для кожного значення. Використати створені дескриптори у класі User.

# class StringDescriptor:
#     def __init__(self, min_length):
#         self.min_length = min_length
#         self.value = ""
#
#     def __get__(self, instance, owner):
#         return self.value
#
#     def __set__(self, instance, value):
#         if len(value) >= self.min_length:
#             self.value = value
#         else:
#             raise ValueError(f"Значення має містити принаймні {self.min_length} символів")
#
# class NumericDescriptor:
#     def __init__(self, min_value, max_value):
#         self.min_value = min_value
#         self.max_value = max_value
#         self.value = 0
#
#     def __get__(self, instance, owner):
#         return self.value
#
#     def __set__(self, instance, value):
#         if self.min_value <= value <= self.max_value:
#             self.value = value
#         else:
#             raise ValueError(f"Значення має бути в діапазоні від {self.min_value} до {self.max_value}")
#
# class User:
#     first_name = StringDescriptor(3)
#     last_name = StringDescriptor(4)
#     age = NumericDescriptor(18, 60)
#     num_subscriptions = NumericDescriptor(0, 999)
#
#     def __init__(self, first_name, last_name, age, num_subscriptions):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.num_subscriptions = num_subscriptions
#
#     def __str__(self):
#         return f'Ім\'я: {self.first_name}, Призвіще: {self.last_name}, Вік: {self.age}, Кількість підписок: {self.num_subscriptions}'
#
# # Приклад створення користувача
# try:
#     user = User("Микола", "Пістоль", 30, 500)
#     print(user)
# except ValueError as e:
#     print(f"Помилка: {e}")