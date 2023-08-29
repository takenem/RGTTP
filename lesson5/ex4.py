"""
  Lesson 5: ex4.py
"""

# 1. Write a function get_index() that returns the index of
#    a character in a string

# INSERT YOUR CODE HERE


def get_index(word: str, char: str) -> int | None:
    for index, letter in enumerate(word):
        if (letter == char):
            return index
    return None


print(get_index("Land Cruser", "L"))


# 2. Write a function shout() that returns each word
#  capitalized with "!" and on it's own line.

# INSERT YOUR CODE HERE
def shout(sentence: str) -> str | None:
    for word in sentence.split():
        capitalzed_word = print(f"{word.upper()}!")
    return capitalzed_word


shout("How are you doing?")


# 3. Write a function extract_longer() that extracts
#    words longer or equal to n-characters and return a list,
#    otherwise return False

# INSERT YOUR CODE HERE
def extract_longer(n: int, sentence: str) -> list[str] | bool:
    result: list[str] = []
    for word in sentence.split():
        if len(word) >= n:
            result.append(word)
    return result if result else False


print(extract_longer(6, "I love Land Cruser!"))