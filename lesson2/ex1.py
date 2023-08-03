"""
  Lesson 2: ex1.py
"""

# 1. Create a format string to display the name and age of a person.

# INSERT YOUR CODE HERE
identification: str = "My name is {name}, {age} old.".format(name="Takemi",
                                                             age=38)
print(identification)

# 2. Print version with it's corresponding upstream codename,
#    and use padding aligned format to left, centre and right.

# INSERT YOUR CODE HERE
codename: str = "takenem"
print("{:-<10}".format(codename))
print("{:->10}".format(codename))
print("{:-^9}".format(codename))

# 3. Show different representations of an integer.

# INSERT YOUR CODE HERE
number: int = 10
print(
      ("The number is {0}.\n"
       "The binary of the number is {0:b}.\n"
       "The hex of the number is {0:x}").format(number)
     )

# 4. Format a floating-point number with fixed precision.

# INSERT YOUR CODE HERE
number_float: float = 0.65
print("The percentage of {0} is {0:.0%}".format(number_float))
