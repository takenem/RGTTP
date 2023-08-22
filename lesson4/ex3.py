"""
  Lesson 4: ex3.py
"""

# 1. Create dictionary using comprehension
# {key, value = i, i**2}

# INSERT YOUR CODE HERE
dictionary1: dict[int, int] = {i: i**2 for i in range(0, 10)}
print(dictionary1)

# 2. Create another comprehension and add +1 to each key's value.
# {key, value = i, i+1}

# INSERT YOUR CODE HERE
dictionary2: dict[int, int] = {i: i+1 for i in range(0, 10)}
print(dictionary2)

# 3. Create 'fruits' defaultdict():
# apple: 10
# orange: 2
# banana: 3
# and for any other key set it's default value to 0

# INSERT YOUR CODE HERE
fruits: dict[str, int] = {}


def defaultdict(key: str, value: int = 0) -> dict[str, int]:
    if key in fruits:
        return fruits
    else:
        fruits.update({key: value})
        return fruits


defaultdict('apple', 10)
defaultdict('orange', 2)
defaultdict('banana', 3)

print(fruits)

# 4. Sort the 'fruits' dictionary using sorted() method
# by keys and values, dictionary does not have .sort()

# INSERT YOUR CODE HERE
sorted_fruits: dict[str, int] = dict(sorted(fruits.items()))
print(sorted_fruits)


# 5. Return 'sorted_fruits' dictionary using sorted() method,
# sort by values.
def sort_key_fruits() -> dict[str, int]:
    sorted(sorted_fruits.values())
    return sorted_fruits


print(sort_key_fruits())


# 6. Reverse the 'sorted_fruits' dictionary and print the dictionary.

# INSERT YOUR CODE HERE
def sort_reverse_fruits() -> dict[str, int]:
    sorted(sorted_fruits, reverse=True)
    return sorted_fruits


print(sort_reverse_fruits())
