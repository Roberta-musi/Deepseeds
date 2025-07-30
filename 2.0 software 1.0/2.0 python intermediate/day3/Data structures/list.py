#creating  lists
# shopping_cart=["apples", "bread", "milk", "eggs"]
# numbers=[1, 2, 3, 4, 5]
# mixed_items=["alice", 25, True, 3.14]
# empty_cart=[]

# print(f"shopping cart: {shopping_cart}")
# print(f"Numbers: {numbers}")
# print(f"Mixed items: {mixed_items}")

#Accessing list items
# fruits=["apple", "banana", "cherry", "date", "elderberry"]
# print(f"first fruit:{fruits[0]}")
# print(f"second fruit:{fruits[1]}")
# print(f"last fruit: {fruits[-1]}")
# print(f"second to the last fruit:{fruits[-2]}")
# #getting slices(portions) of the list
# print(f"first three fruits:{fruits[0:3]}")
# print(f"from second to end: {fruits[1:]}")
# print(f"Every second fruit: {fruits[::2]}")

# #modifying list
# groceries=["milk", "bread", "eggs"]
# print(f"Original list: {groceries}")
# #adding single items(like adding items to your cart)
# groceries.append("cheese")
# print(f"after adding cheese:{groceries}")
# #ADDING MULTIPLE ITEMS AT ONCE
# groceries.extend(["apples", "bananas"])
# print(f"after adding fruits: {groceries}")
# #inserting an item at a specific position
# groceries.insert(1, "yogurt")
# print(f"after inserting yogurt: {groceries}")
# #changing an existing item
# groceries[0]="almond milk"
# print(f"after changing milk: {groceries}")
# #removing items
# groceries.remove("bread")
# print(f"after removing bread: {groceries}")
# removed_item=groceries.pop()
# print(f"after popping:{groceries}")
# specific_item=groceries.pop(1)
# print(f"removed item at index 1:{specific_item}")
# print(f"final list: {groceries}")

#list methods

# test_scores=[85, 92, 78, 88, 79, 94]
# print(f"number of scores:{len(test_scores)}")
# print(f"Highest score: {max(test_scores)}")
# print(f"Average score: {sum(test_scores)/len(test_scores):.1f}")
# #checking if items exist
# print(f"is 85 in the list: {85 in test_scores}")
# print(f"is 100 in the list: {100 in test_scores}")
# print(f"number of 85 in the list: {test_scores.count(85)}")
# test_scores.sort()
# print(f"print sorted list: {test_scores}")
# test_scores.reverse()
# print(f"print reversed list: {test_scores}")
# test_scores.sort(reverse=True)
# print(f"print list in descending order: {test_scores}")
# test_scores.remove(85)
# print(f"list after removing 85:{test_scores}")
# removed_items=test_scores.pop()
# print(f"after popping test_scores:{test_scores}")

# name="roberta"
# reversed_name=name[::-1]
# print(f"reversed name is :{reversed_name}")
#working with loops

# students=["Alice","Bob", "Charlie", "Diana","Eve"]
# #simple iteration
# print("class roster:")
# for student in students:
#     print(f"-{student}")

# #iteration with index numbers
# print("\nNumbered class roster:")
# for i, student in enumerate(students):
#     print(f"{i + 1}. {student}")
# #processing each item
# prices=[19.99, 25.05, 12.75, 33.20, 8.99]
# print("\nPrice with tax:")
# for price in prices:
#     price_with_tax=price*1.08
#     print(f"${price:.2f}-> ${price_with_tax:.2f}")

# #favorite movies
# favorite_movies=[]
# def add_movie(movie):
#     favorite_movies.append(movie)
# def remove_movie(movie):
#     if movie in favorite_movies:
#         print    

# def analyze_array(arr, target):
#     average=sum(arr)/len(arr)
#     target_status="seen" if target in arr else "unseen"
#     return average, target_status

# #testing function
# array1=[2,4,5,6]
# target1=9
# avg1, status1=analyze_array(array1,target1)
# print(f"array1:{array1}, target:{target1}, averge:{avg1}, status:{status1}\n")
# array2=[4,5,7,8,6]
# target2=4

#another method

# def average_target(array, target):
#     total=0
#     length=0
#     average=total/len(array)
#     for number in array:
#         numbers=[2, 4,5,6]
#         total=total+number
#         length=length+1