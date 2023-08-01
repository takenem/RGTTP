"""
  Lesson 2: ex4.py
"""

# 1. Print the formatted keys and values of the dictionary.
#    versions: dict[str, int] = {'Stein': 15, 'Train': 16, 'Wallaby': 17}

# INSERT YOUR CODE HERE
versions: dict[str, int] = {'Stein': 15, 'Train': 16, 'Wallaby': 17}
print("The OpenStack Stein will be RHOSP {0[Stein]}.".format(versions))
print("The OpenStack Train will be RHOSP {0[Train]}.".format(versions))
print("The OpenStack Wallaby will be RHOSP {0[Wallaby]}.".format(versions))


# 2. Print {} around the version numbers.

# INSERT YOUR CODE HERE
print(
      "The OpenStack Stein will be RHOSP"
      + "{"
      + "{0[Stein]}".format(versions) + "}"
      )
print(
      "The OpenStack Stein will be RHOSP"
      + "{"
      + "{0[Train]}".format(versions)
      + "}"
      )
print(
    "The OpenStack Stein will be RHOSP"
    + "{"
    + "{0[Wallaby]}".format(versions)
    + "}"
    )


# 3. Print numbers in decimal, byte and hexadecimal form.

# INSERT YOUR CODE HERE
# Decimal
print(
      "***Decimal*** "
      + "The OpenStack Stein will be RHOSP"
      + "{"
      + "{0[Stein]:d}".format(versions) + "}"
     )
print(
      "***Decimal*** "
      "The OpenStack Stein will be RHOSP"
      + "{"
      + "{0[Train]:d}".format(versions)
      + "}"
     )
print(
      "***Decimal*** "
      + "The OpenStack Stein will be RHOSP"
      + "{"
      + "{0[Wallaby]:d}".format(versions)
      + "}"
     )

# Byte
print(
      "***Byte*** "
      + "The OpenStack Stein will be RHOSP"
      + "{"
      + "{0[Stein]:o}".format(versions) + "}"
     )
print(
      "***Byte*** "
      + "The OpenStack Stein will be RHOSP"
      + "{"
      + "{0[Train]:o}".format(versions)
      + "}"
     )
print( 
      "***Byte*** "
      "The OpenStack Stein will be RHOSP"
      + "{"
      + "{0[Wallaby]:o}".format(versions)
      + "}"
     )

# Hexadecimal
print(
      "***Hexadecimal*** "
      + "The OpenStack Stein will be RHOSP"
      + "{"
      + "{0[Stein]:x}".format(versions) + "}"
     )
print(
      "***Hexadecimal*** "
      + "The OpenStack Stein will be RHOSP"
      + "{"
      + "{0[Train]:x}".format(versions)
      + "}"
     )
print(
      "***Hexadecimal*** "
      + "The OpenStack Stein will be RHOSP"
      + "{"
      + "{0[Wallaby]:x}".format(versions)
      + "}"
     )
