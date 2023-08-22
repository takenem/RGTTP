"""
  Lesson 4: ex2.py
"""

# 1. Create 'fruits' dictionary and add following key: values
# apple: 10
# orange: 2
# banana: 3

# INSERT YOUR CODE HERE
fruits: dict[str, int] = {'apple': 10, 'orange': 2, 'banana': 3}

# 2. Iterate over fruits in fruits dictionary using for loop,
#    print using f-strings:
#    apple: 10
#    orange: 2
#    banana: 3

# INSERT YOUR CODE HERE
for fruit in fruits.items():
    print('{0}'.format(fruit))

# 2. Iterate over the keys in 'fruits' dictionary

# INSERT YOUR CODE HERE
for key in fruits.items():
    print('{0[0]}'.format(key))

# 3. Iterate over the values in dictionary

# INSERT YOUR CODE HERE
for value in fruits.items():
    print('{0[1]}'.format(value))

# 4. Access value banana using .get() method

# INSERT YOUR CODE HERE
# I couldn't understand why type hint int is not working.
banana_value: int = fruits.get('banana')
print(banana_value)


# 5. Access value mandarin using .get() method,
#    if 'mandarin' doesn't exist, return 0

# INSERT YOUR CODE HERE
# I couldn't understand why type hint int is not working.
def find_mandarin(fruit: str) -> int:
    if 'mandarin' in fruits:
        return fruits.get('mandarin')
    else:
        return 0


print(find_mandarin('mandarin'))
# 6. Remove all items from the dictionary

# INSERT YOUR CODE HERE
fruits.clear()
print(fruits)
