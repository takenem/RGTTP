"""
  Lesson 2: ex2.py
"""

# 1. Use string formatting with empty curly brackets {}
#    to take the argument passed into format and print a
#    sentence of your choice.

# INSERT YOUR CODE HERE
player: str = "Allen Iverson"
team: str = "Philadelphia 76ers"
uniform_number: int = 3

print(
      ("My favorite NBA player is {}.\n"
       "He played for the {} for a long teime.\n"
       "His uniform_number was {}.").format(player, team, uniform_number)
     )

# 2. Use string formatting with positional arguments and
#    print the sentence: "Don't Panic!"

# INSERT YOUR CODE HERE
sentence: str = "Don't Panic!"
print("{}".format(sentence))

# 3. Use string formatting with named arguments and
#    print the sentence: "[name] is really [what]!" and
#    fill in the brackets with your name and "great".

# INSERT YOUR CODE HERE
name: str = "Takemi"
what: str = "great"
print("{} is really {}!".format(name, what))
