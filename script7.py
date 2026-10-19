# text = "Python არის მარტივი, Python არის ძლიერი და Python პოპულარულია."
#
# clean = text.lower().replace(",", "").replace(".", "")
# words = clean.split()
#
# counts = {}
# for w in words:
#     counts[w] = counts.get(w, 0) + 1
#
# for w, c in counts.items():
#     print(f"{w}: {c}")
#
# best_word, best_count = None, 0
# for w, c in counts.items():
#     if c > best_count:
#         best_word, best_count = w, c
#
# print(f"ყველაზე ხშირი: '{best_word}' ({best_count}-ჯერ)")
# print(f"სხვადასხვა სიტყვა: {len(set(words))}")



#
# prices = {"ლეპტოპი": 2500, "მაუსი": 40, "კლავიატურა": 120, "მონიტორი": 650}
# stock = {"ლეპტოპი": 2, "მაუსი": 10, "კლავიატურა": 1, "მონიტორი": 3}
#
# orders = [
#     ("ნინო", "ლეპტოპი", 1),
#     ("გიორგი", "მაუსი", 3),
#     ("ანა", "კლავიატურა", 1),
#     ("ნინო", "მაუსი", 2),
#     ("გიორგი", "კლავიატურა", 1),
#     ("ანა", "ტელეფონი", 1),
#     ("ლუკა", "ლეპტოპი", 1),
#     ("ლუკა", "მონიტორი", 5),
# ]
#
# spent = {}
# sold_out = []
# failed_customers = set()
#
# for customer, product, qty in orders:
#     if product not in prices:
#         print(f"❌ {customer}: '{product}' არ იყიდება")
#         failed_customers.add(customer)
#     elif stock[product] < qty:
#         print(f"⚠️ {customer}: {product} — მარაგში მხოლოდ {stock[product]} ცალია")
#         failed_customers.add(customer)
#     else:
#         stock[product] -= qty
#         cost = prices[product] * qty
#         spent[customer] = spent.get(customer, 0) + cost
#         print(f"✅ {customer}: {product} x{qty} = {cost} ლარი")
#         if stock[product] == 0:
#             sold_out.append(product)
#
# print("--- ანგარიში ---")
# for customer, total in spent.items():
#     print(f"{customer}: {total} ლარი")
# print(f"შემოსავალი: {sum(spent.values())} ლარი")
# print(f"ამოწურულია: {sold_out}")
# print(f"წარუმატებელი შეკვეთა ჰქონდათ: {sorted(failed_customers)}")
