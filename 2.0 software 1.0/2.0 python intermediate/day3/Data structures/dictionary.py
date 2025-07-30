# student_info={
#     "alice": "Alice Johnson",
#     "age": 20,
#     "major": "computerscience",
#     "gpa": 3.8,
#     "is_graduate": False

# }
# print(f"{student_info}")
# print(f"{list(student_info.keys())}")
# print(f"{list(student_info.values())}")
# student_info["age"]=3.7
# print(f"{student_info}")
# #adding multiple items at once
# student_info.update({
#     "email": "musiroberta46@gmail.com",
#     "phone": "650838964"
#               })
# print(f"after updating we have:{student_info}")
# #removing information
# removed_phone=student_info.pop("phone")
# print(f"Removed phone:{removed_phone}")
# print(f"after removing phone dictionary{student_info}")

# #removing a key value pair
# del student_info["alice"]
# print(f"after deleting alice:{student_info}")