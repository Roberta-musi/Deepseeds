#creating tuples
point_coordinator=(4,5)# it can be created without parantheses
#accessing tuples
book_info=("1984","George")
title=book_info[0]
author=book_info[1]
#tuple unpacking
title,author = book_info
print(f"using unpacking - book:{title} by {author}")
#partial unpacking
first_name, last_name, *other_info=("john", "smith",30, "engineer", "new york")
print(f"Name:{first_name}, {last_name}")
print(f"other info: {other_info}")