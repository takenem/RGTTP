"""
  Lesson 3: ex3.py
"""

# Here is my shopping list:
shopping_list: list[str] = ['apples', 'milk', 'bread', 'carrot', 'pasta']

# 1. Sort the list using built-in function sorted() and print that list

# INSERT CODE HERE
shopping_list_sorted: list[str] = sorted(shopping_list)
print(shopping_list_sorted)

# 2. Sort the list using .sort() method and print that list

# INSERT CODE HERE
shopping_list.sort()
print(shopping_list)

# 3. Use the built-in function reversed(), reverse the list and print that list

# INSERT CODE HERE
shopping_list_reversed: list[str] = list(reversed(shopping_list))
print(shopping_list_reversed)

# 4. Reverse the list using sort() method and print the list

# INSERT CODE HERE
shopping_list_reversed.sort()
print(shopping_list_reversed)


# 5. Reverse the list using sorted() method and print the list

# INSERT CODE HERE
shopping_list_reversed_sorted: list[str] = sorted(shopping_list_reversed)
print(shopping_list_reversed_sorted)
