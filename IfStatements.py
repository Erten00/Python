
IsMale = True
IsTall = True

if IsMale & IsTall:
    print("You are a tall male")
elif IsMale and not(IsTall):
    print("You are a short male")
elif IsTall and not(IsMale):
    print("You are a tall woman")
else:
    print("You are either not male and not tall")