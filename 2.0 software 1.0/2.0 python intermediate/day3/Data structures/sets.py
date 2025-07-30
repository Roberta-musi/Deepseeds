#sets
unique_numbers={1, 2, 3, 4, 5}
colors={"red","blue", "green", "yellow"}
mixed_set={1,"hello", 3.14, True}
#creating sets from list
numbers_with_duplicate=[1,2,2,4,4,3,5,6]
unique_numbers_from_list=set(numbers_with_duplicate)
#empty set
empty_set=set()
print(f"unique numbers:{unique_numbers}")
print(f"from list with duplicates:{unique_numbers_from_list}")

#set operations
#unions
#intersection
#difference
#symetric difference
python_students={"Alice","Bob","Charlie","Diane"}
java_students={"Bob","Charlie","Eve","Frank"}
javascript_students={"Charlie", "Diana", "Eve","Grace"}
#union 
All_programming_students=python_students| java_students|javascript_students
print(f"All programming students:{All_programming_students}")

#modiifying sets
my_skills={"python", "javascript","HTML"}
print(f"initial skills:{my_skills}")
#adding single skills
my_skills.add("CSS")
print(f"after learning CSS:{my_skills}")
#Adding multiple skills at once
new_skills={"Node.Js", "MongoDB","Docker"}
my_skills.update(new_skills)
print(f"After bootcamp:{my_skills}")

# to remove skills we either use Discard or Remove method, but dicard method is safer
my_skills.remove("HTML")
print(f"after removing HTML:{my_skills}")
#removing and returning an arbitrary elrment, we use pop
removed_skills=my_skills.pop()
print(f"randomly removed skills:{removed_skills}")
print(f"after randomly removing:{my_skills}")
