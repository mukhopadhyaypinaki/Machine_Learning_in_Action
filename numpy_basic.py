from numpy import *

print(random.rand(4,4)) #random 4*4 array

randmat = mat(random.rand(4,4)) # convert array to matrix
print(randmat)

invRandmat = randmat.I
print(invRandmat)

print(randmat*invRandmat) #gives an identity matrix

myeye = eye(4) # eye creates a identity matrix 4*4
print(myeye)

my_array = array(arange(12))

print(my_array)

tile_1 = tile(my_array,(4,1))

print(tile_1)