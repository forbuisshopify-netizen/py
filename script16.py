#
#
# # სავარჯიშო 1 — JSON ფაილის შენახვა და წაკითხვა
# import json
#
# from pathlib import Path
# from tempfile import TemporaryDirectory
#
# def save_json(path, data):
#     with open(path, "w", encoding="utf-8") as file:
#         json.dump(data, file, ensure_ascii=False, indent=2)
#
#
# def load_json(path, default=None):
#     try:
#         with open(path, encoding="utf-8") as file:
#             return json.load(file)
#     except (FileNotFoundError, json.JSONDecodeError):
#         return default
#
# with TemporaryDirectory() as folder:
#     path = Path(folder) / "student.json"
#     save_json(path, {"name": "ნინო", "scores": [90, 85], "pair": (1, 2)})
#     student = load_json(path)
#     print(student)
#     print(type(student["pair"]))  # JSON-ში tuple მასივად ინახება და list-ად იკითხება.
#     print(load_json(Path(folder) / "missing.json", default={}))
#     path.write_text('{"name": "ნინო",}', encoding="utf-8")
#     print(load_json(path, default="არასწორი ფაილი"))
#
#
# # სავარჯიშო 2 — ფილმების რეიტინგი და Movie კლასი
# import json
# from dataclasses import asdict, dataclass, field
#
# @dataclass
# class Movie:
#     title: str
#     year: int = 2000
#     rating: float = 0.0
#     genres: list[str] = field(default_factory=list)
#
#     def __post_init__(self):
#         if not 0 <= self.rating <= 10:
#             raise ValueError("რეიტინგი უნდა იყოს 0-დან 10-მდე")
#
#
# def best_movies(movies, min_rating):
#     selected = (movie for movie in movies if movie.rating >= min_rating)
#     return sorted(selected, key=lambda movie: movie.rating, reverse=True)
#
# movies = [
#     Movie("მონანიება", 1984, 9.1, ["დრამა"]),
#     Movie("გზა", 2020, 7.5),
#     Movie("მოგზაურობა", rating=8.2, genres=["თავგადასავალი"]),
# ]
# print(movies[0])
# print(movies[0] == Movie("მონანიება", 1984, 9.1, ["დრამა"]))
# movies[1].genres.append("კომედია")
# print(movies[1].genres, movies[2].genres)
# for movie in best_movies(movies, 8):
#     print(movie.title, movie.rating)
# print(json.dumps(asdict(movies[0]), ensure_ascii=False))
# try:
#     Movie("ცუდი", 2000, 11)
# except ValueError as error:
#     print("შეცდომა:", error)
