#
# orders = ["ყავა", "ჩაი", "ყავა", "წვენი", "ჩაი", "ყავა", "წყალი"]
#
# unique = []
# seen = set()
#
# for product in orders:
#     if product not in seen:
#         unique.append(product)
#         seen.add(product)
#
# print("უნიკალური:", unique)
#
# counts = {product: orders.count(product) for product in unique}
#
# print("სიხშირე:", list(counts.items()))
#
# popular = ""
# highest = 0
#
# for product, quantity in counts.items():
#     if quantity > highest:
#         popular = product
#         highest = quantity
#
# print("ყველაზე პოპულარული:", popular, f"({highest}-ჯერ)")
#
# last_three = orders[-1:-4:-1]
#
# print("ბოლო 3 შეკვეთა:", last_three)
