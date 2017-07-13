def get_age():
    age=(int)(raw_input("whats your age ?"))
    return age
def get_name():
    return raw_input("whats your name?")

Age=get_age()

name=get_name()
print " Hey , " + name + " , you are "+ str(Age) + " years old, dude!"
