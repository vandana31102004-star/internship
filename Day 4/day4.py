""""
student = {
    "name": "Amit",
    "age": 21,
    "course": "Engineering"
}
print(student["name"])

student["age"] = 22
student["city"] = "Delhi"
print(student)
"""


marks = {"math": 80, "science": 75, "english": 85,}
print(marks.get("math"))
print(marks.get("history", 0))
for subject, score in marks.items():
    