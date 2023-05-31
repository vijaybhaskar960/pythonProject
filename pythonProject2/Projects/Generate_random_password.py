import random


letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
          'n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M',
          'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','^','&','*']

n_letters = int(input("Enter a how many letters you want characters:"))
n_numbers = int(input("Enter a how many letters you want numbers:"))
n_symbols = int(input("Enter a how many letters you want symbols:"))

password_list = []

for i in range(1, n_letters+1):
    char = random.choice(letters)
    password_list += char

for i in range(1, n_numbers+1):
    char = random.choice(numbers)
    password_list += char

for i in range(1, n_symbols+1):
    char = random.choice(symbols)
    password_list += char
print("Before shuffle password is:",password_list)
random.shuffle(password_list)
print("After shuffle password is:",password_list)
password = ''
for char in password_list:
    password += char

print(password)
