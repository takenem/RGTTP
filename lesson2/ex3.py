"""
  Lesson 2: ex3.py
"""

# 1. Create a list containing three elements representing the
#    name, age, and occupation of a person.
#    Then, print the sentence using the elements with .format()

# INSERT YOUR CODE HERE
identity: list = ["Takemi", 38, "TSE"]
print("My name is {0[0]}, I am {0[1]} years old and my occupation is \
{0[2]}.".format(identity))

# 2. The dictionary should contain keys such as
#    'title', 'author', and 'publication_year'.
#    Use the .format() method with multiple positional arguments.
#    Example:
#    "The guidebook [title] by [author] was published in [publication_year]."

# INSERT YOUR CODE HERE
print("My favorite NBA player is {player}, he played in {team}. His\
uniform number was {uniform_number}.".format(
    player="Allen Iverson",
    team="Philadelphia 76ers",
    uniform_number=3))

# 3. The dictionary should hold details about a spaceship, such as
#    'name', 'type', and 'purpose'.
#    Use the .format() method with named arguments.
#    Example:
#    "The spaceship is called the [name]. It is a [type] used for [purpose]."

# INSERT YOUR CODE HERE
spaceship_details: dict = {
    "name": "Freedom",
    "type": "Space Shuttle",
    "purpose": "Destruction of asteroids"
    }

print("The spaceship is called the {0[name]}. It is a {0[type]} used for \
{0[purpose]}.".format(spaceship_details))
