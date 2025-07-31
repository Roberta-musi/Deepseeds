# def read_simple_file():
#     """demonstrate basic file reading____________www"""

#     file=open("sample.txt","r")
#     #print(f"here is the file i want to read______________:{file}")
#     content=file.read()
#     print(f"here is the content of the file i want to read:{content}")
#     file.close()
#     return content
# read_simple_file()

# def read_simple_text():
#     """"""
#     with open ("sample.txt", "r") as file:
#         content=file.read()
#         print(f"content is:{content}")
#         return content
    
# read_simple_text()    

# def read_simple_file():
#     """"""
#     filename="new_file.txt"
#     try:
#      with open(filename, "r") as file:
#             content=file.read()
#             return content
#     except FileNotFoundError:
#         return "file not found dude, please try again"
# read_simple_file()    

# #Reading lines
# def line_by_line():
#     filename="to_becreated.txt"
#     try:
#         with open(filename, "r") as file:
#             print("\n\nreading line by line")
#             for i, line in enumerate(file, 1):
#                 print(f"\n\nLine {i}:{line.strip()}")
#     except FileNotFoundError:
#         return "file not found, please try again"
# line_by_line() 
# result=line_by_line()
# print(result)                

# writing to a file
from datetime import datetime
filename="record.txt"
with open(filename,"a") as file:
    while True:
        user_input=input("plese let us know what you have learnt today:\n(or type exit to quit):\n")
        if user_input=="exit":
            print("Exiting and saving all records")
            break
        datetime.now().strftime("%y-%m-%d")
        current_time=datetime.now().strftime("%y-%m-%d %H:%M")
        entry=f"{current_time} -{user_input}"
        file.write(f"{entry}\n")
        print("saved: entry")


