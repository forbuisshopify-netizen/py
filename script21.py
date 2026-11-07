# """JSON ფაილის შენახვა და წაკითხვა"""
#
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
