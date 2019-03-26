import numpy as np
#sigmoid in scipy
from scipy.special import expit

#using relu as activation function
def relu(x):
  return max(0,x)

#Hyper Parameter
n_i = 500
l_r = 0.1

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

w1 = np.random.random([2,3])
w2 = np.random.random([1,2])

b1 = np.random.random([2,1])
b2 = np.random.random([1,1])

#feed forward function
def ff(i,h,o,w1,w2,b1,b2):
    h = expit(np.add(np.dot(w1,i),b1))
    o = expit(np.add(np.dot(w2,h),b2))
    return o

#define Cost function
def Cost(error):
    return np.multiply(0.5,np.power(error,2))

#derivative of activation function
def der_act(x):
    return np.multiply(expit(x),np.subtract(1,expit(x)))
i = np.array([[1],
              [1],
              [0]
    ])

for iteration in range(n_i):
    cost = 0
    for j in range(x.shape[0]):
        y_pred = ff(i,h,o,w1,w2,b1,b2)
        error = np.subtract(y[j] , y_pred)
        cost += Cost(error)
    print(cost)
    w1 = np.subtract(w1,der_act())
