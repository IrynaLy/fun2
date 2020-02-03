from random import randint as rnd

userString = (str(input("HELP")))

def Ligth ( a, b, c):
    result = {a:rnd(b, c+1)}
    return result

print (Ligth(userString, 0, 20))
