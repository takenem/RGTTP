"""
  Lesson 3: ex4.py
"""

# 1. Create your own Shopping List type.
#
# a. Initialize the ShoppingList class with shopping_list
#    shopping_list = ['apples', 'milk', 'bread', 'carrot', 'pasta']
#
# b. Add in_list method, that checks if the item is in list or not,
#    use the format() or f-strings to return the string based on truth:
#    - 'apples' is in the shopping list.
#    - 'apples' not in the shopping list.
#
# c. Add special function when printing the list to output:
#    * Replace the list with {} and print using format().
#    My shopping list: ['apples', 'milk', 'bread', 'carrot', 'pasta']
#
# d. Add special function for   of two objects to output:
#    * Based on the truth.
#    - True
#    - False

# INSERT CODE HERE
shopping_list: list[str] = ['Land Cruser', 'Hilux', 'Fortuner', 'Prado']


def in_list(item: str, list: list) -> str:
    if item in list:
        return "{} is in my shopping list".format(item)
    else:
        return "{} is not in my shopping list.".format(item)


print(in_list("Land Cruser", shopping_list))
print(in_list("Wrangler", shopping_list))


def add_list(item: str) -> list:
    shopping_list2: list[str] = ['Land Cruser',
                                 'Hilux',
                                 'Fortuner',
                                 'Prado',
                                 '{}'.format(item)]
    return shopping_list2


print(add_list('Wrangler'))


def comparison(item: str, item2: str) -> bool:
    if item and item2 in shopping_list:
        return True
    else:
        return False


print(comparison('Land Cruser', 'Hilux'))
