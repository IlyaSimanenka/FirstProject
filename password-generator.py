import random
passwords = '38rtq378rxmw3q'
lenght = int(input('enter password lenght'))
passenter = ''
for i in range(lenght):
    passenter += random.choice(passwords)
print(passenter)
