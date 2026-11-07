# """სტეკი და პალინდრომი"""
#
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
