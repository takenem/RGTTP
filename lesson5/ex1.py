"""
  Lesson 5: ex1.py
"""

# 1. Create even() function that return "I am even!" if number is even
#    or "I am odd!" if the number is odd.

# INSERT YOUR CODE HERE


def even(number: int) -> str:
    if (number % 2 == 0):
        return "I am even!"
    else:
        return "I am odd!"


print(even(100))


# 2. Create safe_even() function, that will output "I am not number!" if
#    the input is not an number otherwise will work same as even()

# INSERT YOUR CODE HERE
def safe_even(number: int) -> str:
    if type(number) != int:
        return "I am not number!"
    elif (number % 2 == 0):
        return "I am even!"
    else:
        return "I am odd!"


# print(safe_even('a'))
print(safe_even(100))


# 3. Create a function fizz_buzz(),
#    replacing any number divisible by three with the word "fizz",
#    and any number divisible by five with the word "buzz",
#    and any number divisible by both 3 and 5 with the word "fizzbuzz",
#    and number if number is not divisible by any.

# INSERT YOUR CODE HERE
def fizz_buzz(number: int) -> str:
    if (type(number) != int):
        return "Not a number!"
    if (number % 3 == 0) and (number % 5 == 0):
        return "fizzbuzz"
    elif (number % 3 == 0):
        return "fizz"
    elif (number % 5 == 0):
        return "buzz"
    else:
        return str(number)


# 4. Execute fizz_buzz() function from 1 to the 100

# INSERT YOUR CODE HERE
for number in range(1, 101):
    print(fizz_buzz(number))
