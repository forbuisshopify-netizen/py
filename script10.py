# """ჩარჩოიანი ტექსტი"""
#
# from functools import wraps
#
#
# def framed(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         return f"*** {func(*args, **kwargs)} ***"
#     return wrapper
#
#
# @framed
# def greet(name):
#     """აბრუნებს მისალმებას."""
#     return f"გამარჯობა, {name}"
#
#
# @framed
# def order_summary(item, quantity=1):
#     return f"{item} × {quantity}"
#
# print(greet("ნინო"))
# print(order_summary("ხაჭაპური", quantity=2))
# print(order_summary("ჩაი"))
# print(greet.__name__, "|", greet.__doc__)
