#######################################################

# a lambda function that adds 10 to the input argument
f = lambda x: x+10
val1 = f(5)
val2 = f(100)
print(val1, val2)

# a lambda function that multiplies two input arguments and returns the result
f = lambda x,y: x*y
val3 = f(2,10)
val4 = f(7,5)
print(val3, val4)

#######################################################

def myfunc(n):
    return lambda x: x * n

doubler = myfunc(2)
print(doubler(6))

tripler = myfunc(3)
print(tripler(6))

#######################################################

points2D = [(1, 9), (4, 1), (5, -3), (10, 2)]
sorted_by_y = sorted(points2D, key= lambda x: x[1])
print(sorted_by_y)

mylist = [- 1, -4, -2, -3, 1, 2, 3, 4]
sorted_by_abs = sorted(mylist, key= lambda x: abs(x))
print(sorted_by_abs)

#######################################################

a  = [1, 2, 3, 4, 5, 6]
b = list(map(lambda x: x * 2 , a))

# However, try to prefer list comprehension
# Use map if you have an already defined function
c = [x*2 for x in a]
print(b)
print(c)

#######################################################

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = list(filter(lambda x: (x%2 == 0) , a))

# However, the same can be achieved with list comprehension
c = [x for x in a if x%2 == 0]
print(b)
print(c)

#######################################################

from functools import reduce
a = [1, 2, 3, 4]
product_a = reduce(lambda x, y: x*y, a)
print(product_a)
sum_a = reduce(lambda x, y: x+y, a)
print(sum_a)