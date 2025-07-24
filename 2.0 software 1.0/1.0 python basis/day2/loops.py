#for loop
#starting point
#condition
#increment or decrement

# names =["Will", "Faith", "Musi", "aliasambom", "niambom", "fumbom"]
# for name in names:
#     print(name)
#     if name.endswith("mbom"):
#         print(f"we dan catch you: {name}")
#     else:
#         print(f"welcome to the party: {name}")

# names =["Will", "Faith", "Musi", "aliasambom", "niambom", "fumbom"]
# count=1
# for name in names:
#     print(f"{count}.{name}")
#     count=count+1

# print("counting to 5:")
# for number in range(1, 6):
#     print(f"count: {number}")

# #range function
# for i in range(5):
#     print(i)
#     #range(start, stop)
# for i in range(2 ,7):
#     print(i)
# #range(start, stop, step)
# for i in range (0, 10, 2):
#         print(i)
# #range(countdown)
# for i in range (10, 0, -1):
#      print(f"countdown: {i}")
#      print("blast off!")  

#basic while loop
# count=1
# while count<=5:
#     print(f"count is:{count}")
#     count+=1 #same as count=count+1
#     #user input loop
#     user_input=""
#     while user_input !="quit":
#         user_input =input("Enter 'quit' to exit:")
#         if user_input !="quit":
#             print(f"you entered: {user_input}")
#     print("goodbye!!")  
    #continue-skip to next iteration
# print("\nprinting only odd numbers:")
# for number in range (1, 10):
#     if number % 2 ==0:
#         continue #skip even numbers
#     print(f"Odd number: {number}")

#multiplication time table
# print("Multiplication table:")
# for i in range(1, 4): #rows
#     for j in range(1,4): #columns
#         result=i * j
#         print(f"{i} x{j} ={result}")
#         print()

#pattern printing
print("Triangle pattern")
for row in range (1, 6):
    for star in range(row):
        print("*",end="")  
    print() #new line after each      


        

    
    