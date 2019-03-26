#new stuff incoming
import numpy as np


#using relu as activation function
#maybe use sigmoid later

def activate(x):
  return max(0,x)

#setting data
x=np.array([
        [1,1,0],
        [1,0,1],
        [0,0,0],
        [1,1,1],
        [0,0,1]
    ])

y=np.array([1,1,1,0,1])

#init layer i , h , o
i = np.empty([3,1])
h = np.empty([2,1])
o = np.empty([1,1])


