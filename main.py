#new stuff incoming
import numpy as np


#using relu as activation function
#maybe use sigmoid later

def activate(x):
  return max(0,x)

#neuron class with value and layer(maybe layer can be removed)

class Neuron:
  def __init__(self, value,layer):
    self.value = value
    self.layer = layer
  
class Link:
  def __init__(self,weight)
 
    
