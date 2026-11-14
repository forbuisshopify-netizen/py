# """ლექცია 21 — API კომუნიკაცია"""
#
# import requests
#
# BASE_URL = "https://jsonplaceholder.typicode.com"
#
#
# # სავარჯიშო 1 — get_user: მომხმარებლის მიღება API-დან
# def get_user(user_id):
#     response = requests.get(f"{BASE_URL}/users/{user_id}", timeout=10)
#
#     if response.status_code == 404:
#         return None
#
#     response.raise_for_status()
#     return response.json()
#
#
# for user_id in (1, 2, 999):
#     user = get_user(user_id)
#
#     if user is None:
#         print(f"მომხმარებელი {user_id} ვერ მოიძებნა")
#     else:
#         print(f'{user["name"]} | {user["email"]} | {user["address"]["city"]}')
#
#
# # სავარჯიშო 2 — CRUD ოპერაციები (CREATE, READ, PUT, PATCH, DELETE)
# def crud_tour():
#     # 1. CREATE — ახალი პოსტის შექმნა
#     response = requests.post(
#         f"{BASE_URL}/posts",
#         json={"title": "ახალი პოსტი", "body": "ტექსტი", "userId": 1},
#         timeout=10,
#     )
#     response.raise_for_status()
#     new_id = response.json()["id"]
#     print(f"CREATE: {response.status_code}, id={new_id}")
#
#     # 2. READ — ყალბი API ახალ პოსტს რეალურად არ ინახავს, ამიტომ 404 ბრუნდება
#     response = requests.get(f"{BASE_URL}/posts/{new_id}", timeout=10)
#     if response.status_code != 404:
#         response.raise_for_status()
#     print(f"READ {new_id}: {response.status_code}")
#
#     # 3. PUT — პირველი პოსტის სრული შეცვლა
#     response = requests.put(
#         f"{BASE_URL}/posts/1",
#         json={
#             "id": 1,
#             "title": "სრულად შეცვლილი",
#             "body": "ახალი ტექსტი",
#             "userId": 1,
#         },
#         timeout=10,
#     )
#     response.raise_for_status()
#     print(f'UPDATE (PUT): {response.status_code}, title={response.json()["title"]}')
#
#     # 4. PATCH — მხოლოდ title-ის შეცვლა
#     response = requests.patch(
#         f"{BASE_URL}/posts/1",
#         json={"title": "ნაწილობრივ შეცვლილი"},
#         timeout=10,
#     )
#     response.raise_for_status()
#     print(f'UPDATE (PATCH): {response.status_code}, title={response.json()["title"]}')
#
#     # 5. DELETE — პირველი პოსტის წაშლის იმიტაცია
#     response = requests.delete(f"{BASE_URL}/posts/1", timeout=10)
#     response.raise_for_status()
#     print(f"DELETE: {response.status_code}, {response.json()}")
#
#
# crud_tour()
#
