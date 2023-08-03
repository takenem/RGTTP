"""
  Lesson 3: ex1.py
"""

# Here is my shopping list:
shopping_list: list[str] = ['apples', 'milk', 'bread', 'carrot', 'pasta']

# 1. Add banana to a shopping list.

# INSERT CODE HERE
shopping_list.append('banana')
print(shopping_list)

# 2. Add chocolate in the third position in your shopping list

# INSERT CODE HERE
shopping_list.insert(2, 'chocolate')
print(shopping_list)

# 3. Extend shopping list by the following items:
# ['chocolate', 'carrot', 'avocado']

# INSERT CODE HERE
additional_shopping_list: list = ['chocolate', 'carrot', 'avocado']
shopping_list.extend(additional_shopping_list)
print(shopping_list)

# 4. Remove first chocolate only

# INSERT CODE HERE
shopping_list.pop(2)
print(shopping_list)

# 5. Remove last item from the list

# INSERT CODE HERE
shopping_list.pop(-1)
print(shopping_list)

# 6. Remove third item from the list

# INSERT CODE HERE
shopping_list.pop(2)
print(shopping_list)

# 7. Count how many carrots are in the shopping list?

# INSERT CODE HERE
count_carrot: int = shopping_list.count('carrot')
print(count_carrot)

# 8. Get the index of the chocolate (careful can throw traceback)

# INSERT CODE HERE
index_chocolate: int = shopping_list.index('chocolate')
print(index_chocolate)


# 9. Get the index of carrot, make sure this code is executed

# INSERT CODE HERE
def check_index(item: str, list: list) -> list:
    item_index = [index for index, name in enumerate(list)
                  if name == item]
    return item_index


print(check_index('carrot', shopping_list))
