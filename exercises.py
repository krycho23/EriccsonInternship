import string
import random

# task 1
#Reverse the order of words in a sentence. I.e.: “She sells sea shells” -> “shells sea sells She”.
#Both input and output should be strings.

print("############TEST1##############")
input = "She sells sea shells"
output = input.split()
output = output[::-1]
output = " ".join(output)
print(output)

# task 2
# Translate input text string to string of numbers on feature-phone keyboard basis. I.e. “a” is one press of
# button 2, “b” - two presses of 2, etc. “Eve has a cat”-> 3388833#4427777#2#22228. (One can use # as a space).
# Translation should be case insensitive.

print("############TEST2##############")
phone_mapping = {}
number = list(range(2,10))
iter = 0
counter = 0
for letter in string.ascii_lowercase[0:15]:
    iter+=1 # how many numbers
    if iter%3==1:
        phone_mapping[letter] = str(number[counter])
    elif iter%3==2:
        phone_mapping[letter] = str(number[counter]*11)
    else:
        phone_mapping[letter] = str(number[counter] * 111)
        counter += 1  # count which iter, which number

phone_mapping["p"] = "7"
phone_mapping["q"] = "77"
phone_mapping["r"] = "777"
phone_mapping["s"] = "7777"
phone_mapping["t"] = "8"
phone_mapping["u"] = "88"
phone_mapping["v"] = "888"
phone_mapping["w"] = "9"
phone_mapping["x"] = "99"
phone_mapping["y"] = "999"
phone_mapping["z"] = "9999"
phone_mapping[" "] = "#"

input = "Eve has a cat"
input = input.lower()
print(input)
output = ""
for inp in input:
    output += phone_mapping[inp]
print(output)

# task 3
# how many different digits are in number
print("############TEST3##############")
test_number = [177,128,192237,2222222222,232222222222245,0,-1]

def checkDigits(test_number):
    test_number = abs(test_number)
    test_number = str(test_number)
    digits = []
    for digit in test_number:
        digit = int(digit)
        digits.append(digit)

    digits = set(digits)
    check_value = len(digits)
    return check_value

for test in test_number:
    print(str(checkDigits(test)))

# task 4
# Palindrome. Write a program which tells if a word or a sentence is a palindrome. I.e. “A toyota”, “11 02 2011”,
# “Anna”. Ignore spaces or letter case.
print("############TEST4##############")
data = ["A toyota", "11 02 2011", "Anna", "Coronavirus-related scams"]

def isPalindrome(s):
    s = s.replace(" ", "")
    s = s.lower()
    rev = s[::-1]
    if (s == rev):
        return True
    return False

for d in data:
    print(isPalindrome(d))
