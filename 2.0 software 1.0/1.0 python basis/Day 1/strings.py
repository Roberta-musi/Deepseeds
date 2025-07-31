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



# email= input("Enter your email")
# if "@" in email and "." in email:
#     username= email.split("@")[0]
#     domain= email.split("@")[1]
#     print(f"username: {username}")
#     print(f"Domain: {domain}")
# else:print("Invalid email format")


# text= "The quick brown fox jumps over the lazy dog"
# print(f'Text:{text}')
# print(f"Lenght: {len(text)} characters")
# print(f"Words:{len(text.split())} words")
# print(f"Uppercase: {text.upper()}")
# print(f"Title case:{text.title()}")
# print(f"contains 'fox':{'fox' in text}")

# 24th July
# Strings method ad string operators
# just a funcrtion or simply something()

message= "Good morning"
# convert from upper case to lower case and vice versa

mesaage_lower=message.lower()
message_upper= message.upper()
print(f"The lower case conversion is: {mesaage_lower} and uppercase conversion is:{message_upper}")

# slice method
greetings="welcme back"
how_python_sees_it= list(greetings)
print(f"python view: {how_python_sees_it}")
extract_text=greetings[0:3]

print(f"Extracted text: {extract_text}")
#exercise1
full_name="jOhN dOe"
j=full_name[0].upper()
n=full_name[3].lower()
d=full_name[5].upper()
o=full_name[6].lower()
#full-name[0]=j
#print(f"my full naame is:{full_name}")
#print(f"letter J:{j}")
#full_name="j"+ full_name[:1]#
name=full_name[1:4].lower()
complete=full_name[6:8].lower()
print(f"my full name is:{j}{name} {d}{complete}")