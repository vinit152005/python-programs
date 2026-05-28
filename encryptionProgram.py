import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)
# print(f"chars: {chars}")
# print(f"key  : {key}")

user_input = input("enter a message to encrypt: ")
encrypt = ""

for letter in user_input:
    index = chars.index(letter)
    encrypt += key[index]
print(f"Original message: {user_input}")
print(f"encrypt message: {encrypt}")

encrypt = input("enter the encrypted message: ")
user_input = ""

for letter in encrypt:
    index = key.index(letter)
    user_input += chars[index]

print(f"encrypt message: {encrypt}")
print(f"Original message: {user_input}")

