"""
  Lesson 5: ex2.py
"""

# 1. Write a while true loop to print "Forever" forever

# INSERT YOUR CODE HERE
while True:
    print("Forever")


# 2. Write a while loop to print numbers from 0 to 42

# INSERT YOUR CODE HERE
number: int = 0
while number < 43:
    print(number)
    number += 1


# 3. Write a while true loop to print numbers from 0 to 42

# INSERT YOUR CODE HERE
num: int = 0
while True:
    if (num > 42):
        break
    print(num)
    num += 1

# 4. Write a while true loop to print numbers from 0 to 45, and instead
#    of 42, print "I am 42!" break at number 45.

# INSERT YOUR CODE HERE
num_: int = 0
while True:
    if (num_ > 45):
        break
    elif (num_ == 42):
        print('I am 42!')
    else:
        print(num_)
    num_ += 1


# 5. Write a while-else loop to count to 2, and after that print
#    "It's my turn now!" using else statement.

# INSERT YOUR CODE HERE
count: int = 0
while count <= 2:
    print(count)
    count += 1
else:
    print("It's my turn now!")
