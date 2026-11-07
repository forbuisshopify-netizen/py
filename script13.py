# """წყარო — დავალება (1).odt"""
#
#
# # სავარჯიშო 1 — ალგორითმის სირთულე და შემოწმებების რაოდენობა
# def constant_checks(data, target):
#     # მხოლოდ პირველ ელემენტს ვადარებთ. შედარებების რაოდენობა მაქსიმუმ ერთია.
#     checks = matches = 0
#     for item in data:
#         checks += 1
#         matches += item == target
#         break
#     return checks, matches
#
#
# def linear_checks(data, target):
#     checks = matches = 0
#     for item in data:
#         checks += 1
#         matches += item == target
#     return checks, matches
#
#
# def quadratic_checks(data, target):
#     # ვითვლით დალაგებულ წყვილებს, რომელთა ჯამი target-ის ტოლია.
#     checks = matches = 0
#     for left in data:
#         for right in data:
#             checks += 1
#             matches += left + right == target
#     return checks, matches
#
# data = [1, 2, 3, 4, 5]
# for label, function in [("O(1)", constant_checks), ("O(n)", linear_checks),
#                         ("O(n²)", quadratic_checks)]:
#     checks, matches = function(data, 5)
#     print(f"{label}: შემოწმება = {checks}, დამთხვევა = {matches}")
#
#
# # სავარჯიშო 2 — სტეკი და პალინდრომი
# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         return self.items.pop()
#
#     def is_empty(self):
#         return not self.items
#
#
# def reverse_text(text):
#     stack = Stack()
#     for char in text:
#         stack.push(char)
#     result = []
#     while not stack.is_empty():
#         result.append(stack.pop())
#     return "".join(result)
#
#
# def is_palindrome(text):
#     clean = "".join(text.casefold().split())
#     return clean == reverse_text(clean)
#
# print(reverse_text("Python"))
# print(reverse_text("გამარჯობა"))
# print(is_palindrome("ანა"))
# print(is_palindrome("Never odd or even"))
# print(is_palindrome("Python"))
