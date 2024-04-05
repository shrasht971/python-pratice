from multipledispatch import dispatch


##Passing two parameters
@dispatch(int, int)
def product(first, second):
    result = first*second
    print(result)

@dispatch(int, int, int)
@dispatch(float, int, int)
@dispatch(int, float, int)
def product(first, second, third):
    result = first*second*third
    print(result)

product(10.6,20,90)    