#A 10
def outer_function():
    a = 20
    print('a =',a)         #Gives a its first value
    def inner_function():
        a = 30
        print('a =',a)
    inner_function()

a = 10
outer_function()
print('a =',a)
