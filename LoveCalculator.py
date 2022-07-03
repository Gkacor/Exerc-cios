print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1name2 = name1 + name2
nameLower = name1name2.lower()

t = nameLower.count("t")
r = nameLower.count("r")
u = nameLower.count("u")
e = nameLower.count("e")

true = t + r + u + e

l = nameLower.count("l")
o = nameLower.count("o")
v = nameLower.count("v")
e = nameLower.count("e")

love = l + o + v + e

trueLove = str(true) + str(love)
trueLove = int(trueLove)

if trueLove < 10 or trueLove > 90:
    print(f"Your score is {trueLove}, you go together like coke and mentos.")
elif trueLove >= 40 and trueLove <= 50:
    print(f"Your score is {trueLove}, you are alright together.")
else:
    print(f"Your score is {trueLove}.")