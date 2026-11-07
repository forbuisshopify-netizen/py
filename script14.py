# """სტუდენტების ქულები"""
#
# import os
#
#
# def save_scores(path: str, scores: dict[str, int]) -> None:
#     with open(path, "w", encoding="utf-8") as file:
#         for name, score in scores.items():
#             file.write(f"{name}:{score}\n")
#
#
# def add_score(path: str, name: str, score: int) -> None:
#     with open(path, "a", encoding="utf-8") as file:
#         file.write(f"{name}:{score}\n")
#
#
# def read_scores(path: str) -> dict[str, int]:
#     scores = {}
#     try:
#         with open(path, encoding="utf-8") as file:
#             for line in file:
#                 if line.strip():
#                     name, score = line.strip().split(":")
#                     scores[name] = int(score)
#     except FileNotFoundError:
#         print("⚠ ფაილი ვერ მოიძებნა")
#     return scores
#
# os.makedirs("data", exist_ok=True)
#
# save_scores("data/scores.txt", {"ნინო": 92, "გიორგი": 78, "ანა": 85})
# add_score("data/scores.txt", "დათო", 64)
# add_score("data/scores.txt", "მარიამი", 97)
#
# with open("data/scores.txt", encoding="utf-8") as file:
#     print(file.read(), end="")
#
# scores = read_scores("data/scores.txt")
# print(scores)
# print("სტუდენტები:", len(scores))
# print("საშუალო ქულა:", round(sum(scores.values()) / len(scores), 1))
# best = max(scores, key=scores.get)
# print("საუკეთესო:", best, scores[best])
#
# with open("data/passed.txt", "w", encoding="utf-8") as file:
#     for name, score in scores.items():
#         if score >= 80:
#             file.write(name + "\n")
# with open("data/passed.txt", encoding="utf-8") as file:
#     print("ჩააბარეს (80+):", file.read().splitlines())
