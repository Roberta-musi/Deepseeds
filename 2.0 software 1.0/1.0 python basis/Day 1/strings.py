# first_name= "John"
# # concaetenation
# last_name= "Ngala"

# full_names= first_name + last_name
# # interpolation
# print(f"my full names are {full_names}")

# laugh= "Ha"*7
# print(laugh)

# # lenght
# message= "Hello, python"
# print(len(message))

# name= "Alice"
# age= 30
# score= 95.5

# # Mehtod 1: f-strings(recommended- like fill-in-the-blank)
# print(f"Hello, {name}! You are {age} years old.")
# print(f"Your score is {score:.1f}%")

# # Method 2: format() method
# print("Hello, {}! You are {} years old." .format(name,age))

# # Method 3: formating older style
# print("Hello, %s! You are %d years old." %(name, age))



email= input("Enter your email")
if "@" in email and "." in email:
    username= email.split("@")[0]
    domain= email.split("@")[1]
    print(f"username: {username}")
    print(f"Domain: {domain}")
else:print("Invalid email format")


text= "The quick brown fox jumps over the lazy dog"
print(f'Text:{text}')
print(f"Lenght: {len(text)} characters")
print(f"Words:{len(text.split())} words")
print(f"Uppercase: {text.upper()}")
print(f"Title case:{text.title()}")
print(f"contains 'fox':{'fox' in text}")