"""
  Lesson 1: ex2.py
"""

# Here is my shopping list:
#
# 2.99 Apples
# 1.79 Milk
# 3.49 Bread
# 6.99 Chicken
# 2.49 Pasta

# 1. Make a python list of the 5 items above and print it out.

# INSERT YOUR CODE HERE
shopping_list = [
    {"Apples": 2.99},
    {"Milk": 1.79},
    {"Bread": 3.49},
    {"Chicken": 6.99},
    {"Pasta": 2.49}
]

# 2. Use python as your calculator and print out the total cost of
#    all items on shopping list.

# INSERT YOUR CODE HERE
shopping_sum = shopping_list[0]["Apples"] + \
               shopping_list[1]["Milk"] + \
               shopping_list[2]["Bread"] + \
               shopping_list[3]["Chicken"] + \
               shopping_list[4]["Pasta"]

print(round(shopping_sum,2))

# 3. I have decided that we need 5 cartons of milk, can you recalculate
#    it and print it out again?

# INSERT YOUR CODE HERE
shopping_sum = shopping_list[0]["Apples"] + \
               shopping_list[1]["Milk"]*5 + \
               shopping_list[2]["Bread"] + \
               shopping_list[3]["Chicken"] + \
               shopping_list[4]["Pasta"]
               
print(round(shopping_sum,2))

# 4. Print out every item of your shopping list on a new line.

# INSERT YOUR CODE HERE
for item in shopping_list:
    shopping_item = list(item.keys())[0]
    print(shopping_item)

