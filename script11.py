# """ციფრული საფულე და გადასახადი"""
#
# def make_wallet(balance):
#     def spend(amount):
#         nonlocal balance
#         if amount > balance:
#             return f"არასაკმარისი თანხა (ბალანსი: {balance} ₾)"
#         balance -= amount
#         return f"დაიხარჯა {amount} ₾, დარჩა {balance} ₾"
#     return spend
#
#
# def make_tax(rate):
#     def price_with_tax(price):
#         return round(price * (100 + rate) / 100, 2)
#     return price_with_tax
#
# nino = make_wallet(100)
# luka = make_wallet(30)
#
# print(nino(40))
# print(nino(70))
# print(luka(25))
# print(nino(60))
#
# georgia_vat = make_tax(18)
# low_tax = make_tax(5)
# print(georgia_vat(100), low_tax(100))
# print(list(map(georgia_vat, [10, 25.5, 99])))
