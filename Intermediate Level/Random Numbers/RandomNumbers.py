#######################################################

import random

# random float in [0,1)
a = random.random()
print(a)

# random float in range [a,b]
a = random.uniform(1,10)
print(a)

# random integer in range [a,b]. b is included
a = random.randint(1,10)
print(a)

# random integer in range [a,b). b is excluded
a = random.randrange(1,10)
print(a)

# random float from a normal distribution with mu and sigma
a = random.normalvariate(0, 1)
print(a)

# choose a random element from a sequence
a = random.choice(list("ABCDEFGHI"))
print(a)

# choose k unique random elements from a sequence
a = random.sample(list("ABCDEFGHI"), 3)
print(a)

# choose k elements with replacement, and return k sized list
a = random.choices(list("ABCDEFGHI"),k=3)
print(a)

# shuffle list in place
a = list("ABCDEFGHI")
random.shuffle(a)
print(a)

#######################################################

print('Seeding with 1...\n')

random.seed(1)
print(random.random())
print(random.uniform(1,10))
print(random.choice(list("ABCDEFGHI")))

print('\nRe-seeding with 42...\n')
random.seed(42)  # Re-seed

print(random.random())
print(random.uniform(1,10))
print(random.choice(list("ABCDEFGHI")))

print('\nRe-seeding with 1...\n')
random.seed(1)  # Re-seed

print(random.random())
print(random.uniform(1,10))
print(random.choice(list("ABCDEFGHI")))

print('\nRe-seeding with 42...\n')
random.seed(42)  # Re-seed

print(random.random())
print(random.uniform(1,10))
print(random.choice(list("ABCDEFGHI")))

#######################################################

import secrets

# random integer in range [0, n).
a = secrets.randbelow(10)
print(a)

# return an integer with k random bits.
a = secrets.randbits(5)
print(a)

# choose a random element from a sequence
a = secrets.choice(list("ABCDEFGHI"))
print(a)

#######################################################

import numpy as np

np.random.seed(1)
# rand(d0,d1,…,dn)
# generate nd array with random floats, arrays has size (d0,d1,…,dn)
print(np.random.rand(3))
# reset the seed
np.random.seed(1)
print(np.random.rand(3))

# generate nd array with random integers in range [a,b) with size n
values = np.random.randint(0, 10, (5,3))
print(values)

# generate nd array with Gaussian values, array has size (d0,d1,…,dn)
# values from standard normal distribution with mean 0.0 and standard deviation 1.0
values = np.random.randn(5)
print(values)

# randomly shuffle a nd array.
# only shuffles the array along the first axis of a multi-dimensional array
arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
np.random.shuffle(arr)
print(arr)