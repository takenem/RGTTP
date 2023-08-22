"""
  Lesson 4: ex4.py
"""

# 1. Create a data variable which contains a list of objects
#    with following key and values:
#    {"category": "fruit", "name": "apple"}
#    {"category": "fruit", "name": "banana"}
#    {"category": "fruit", "name": "orange"}
#    {"category": "vegetable", "name": "carrot"}
#
#    Write a for loop to print out the fruits and vegetables.
data: list = [
    {"category": "fruit", "name": "apple"},
    {"category": "fruit", "name": "banana"},
    {"category": "fruit", "name": "orange"},
    {"category": "vegetable", "name": "carrot"}
]


for item in data:
    if item["category"] == "fruit":
        print(f'The fruit is {item["name"]}.')
    else:
        print(f'The vegetable is {item["name"]}.')
