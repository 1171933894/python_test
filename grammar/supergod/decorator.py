def show(function):
    def temp(*x, **y):
        print('====')
        z = function(*x, **y)
        print('====')
        return z
    return temp
@show
def myAdd(a,b):
    return a+b
@show
def mySubstract(a,b):
    return a-b

print(myAdd(10, 4))
print(mySubstract(10, 4))