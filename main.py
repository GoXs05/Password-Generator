import random
import string

def generate_password(uppercase, lowercase, numbers, special_characters, pwlength):

  password = []

  if uppercase:
    password += [random.choice(string.ascii_uppercase) for _ in range(pwlength)]

  if lowercase:
    password += [random.choice(string.ascii_lowercase) for _ in range(pwlength)]

  if numbers:
    password += [random.choice(string.digits) for _ in range(pwlength)]

  if special_characters:
    password += [random.choice(string.punctuation) for _ in range(pwlength)]


  while password.__len__() < length:

    if uppercase:
      password += [random.choice(string.ascii_uppercase) for _ in range(pwlength)]

    elif lowercase:
      password += [random.choice(string.ascii_lowercase) for _ in range(pwlength)]

    elif numbers:
      password += [random.choice(string.digits) for _ in range(pwlength)]

    elif special_characters:
      password += [random.choice(string.punctuation) for _ in range(pwlength)]


  random.shuffle(password)


  return "".join(password)



print(f" * * * * * * * * * * * * * * * * * * ")
print(f"Welcome to Gokul's Password Generator!")
print(f" * * * * * * * * * * * * * * * * * * \n")



length = 0
while length < 4 or length > 25:
  length = int(input("Enter the desired password length (must be an integer between 4 and 25, inclusive): "))
  if length < 4:
    print(f"Please enter a number greater than or equal to 4 (for security).\n")
  if length > 25:
    print(f"Please enter a length less than 50.\n")


char_types = 0
while char_types == 0:
  uppercase_input = ""
  lowercase_input = ""
  numbers_input = ""
  special_characters_input = ""


  while uppercase_input != "y" and uppercase_input != "n":
    uppercase_input = input("Include uppercase letters (y/n)? ")
    if uppercase_input != "y" and uppercase_input != "n":
      print(f"Please enter either y or n.\n")
    else:
      uppercase = uppercase_input == "y"

  while lowercase_input != "y" and lowercase_input != "n":
    lowercase_input = input("Include lowercase letters (y/n)? ")
    if lowercase_input != "y" and lowercase_input != "n":
      print(f"Please enter either y or n.\n")
    else:
      lowercase = lowercase_input == "y"

  while numbers_input != "y" and numbers_input != "n":
    numbers_input = input("Include numbers (y/n)? ")
    if numbers_input != "y" and numbers_input != "n":
      print(f"Please enter either y or n.\n")
    else:
      numbers = numbers_input == "y"

  while special_characters_input != "y" and special_characters_input != "n":
    special_characters_input = input("Include special characters (y/n)? ")
    if special_characters_input != "y" and special_characters_input != "n":
      print(f"Please enter either y or n.\n")
    else:
      special_characters = special_characters_input == "y"

  char_types = (uppercase + lowercase + numbers + special_characters)
  if char_types == 0:
    print(f"\nPlease select at least one type of character to include in the password.\n")


char_type_length = int(length/char_types)

password = generate_password(uppercase, lowercase, numbers, special_characters, char_type_length)
print(f"\n\nYour password is: {password}")


if length >= 12 and uppercase and lowercase and numbers and special_characters:
  security_level = "high"
elif length >= 8 and (uppercase + lowercase + numbers + special_characters) >= 3:
  security_level = "medium"
elif length >= 4 and (uppercase + lowercase + numbers + special_characters) >= 1:
  security_level = "low"

print(f"\n\nThis password's security level is {security_level}. ")


if security_level == "low" or security_level == "medium":
  if (uppercase + lowercase + numbers + special_characters) != 4 and length < 12:
    print(f"To make your password more secure, add more types of characters and make the length longer. For example: ")
  elif (uppercase + lowercase + numbers + special_characters) == 4 and length < 12:
    print(f"To make your password more secure, make the length longer. For example: ")
  elif (uppercase + lowercase + numbers + special_characters) != 4 and length >= 12:
    print(f"To make your password more secure, add more types of characters. For example: ")
  print(f"\t{generate_password(1, 1, 1, 1, 5)}\n\n")


print(f" * * * * * * * * * * * * * * * * * * * * * * * ")
print(f"Thank you for using Gokul's Password Generator!")
print(f" * * * * * * * * * * * * * * * * * * * * * * * ")