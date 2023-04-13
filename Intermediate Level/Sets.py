#Sets : unordered, mutable, no duplicates

#myset = set("Hello")
#print(myset)

#myset = set()

#myset.add(1)
#myset.add(2)
#myset.add(3)

#myset.remove(3)
#print(myset.pop())
#myset.clear()

#print(myset)

###########################################

#odds = {1,3,5,7,9}
#evens = {0,2,4,6,8}
#primes = {2,3,5,7}

#u = odds.union(evens) #Unija
#print(u)

#i = odds.intersection(evens) #Presek
#print(i)

#diff = odds.difference(primes) #Razlika 
#print(diff)

#o = odds.symmetric_difference(primes)
#print(o)  

###########################################

a = frozenset([1,2,3,4])
a.add(2)
a.remove(4)
print(a)