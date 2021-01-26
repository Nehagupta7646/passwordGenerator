#it is a password generator project of python
import random
passlen = int(input("Enter the length of password"))
s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*?_()"
p = "".join(random.sample(s,passlen))
print(p)