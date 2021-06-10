from numpy.core.defchararray import array
import pandas as pd
import numpy as np 
import pickle



model_path = '/Users/arshad_221b/Projects/heart attack /finalized_model.sav'
model = pickle.load(open(model_path, 'rb'))

l = [0.708333, 1, 1.000000, 0.481132, 0.244292, 1, 0, 0.603053, 0.0, 0.370968, 0.0, 0.0, 0.333333]

l = array(l)
l = l.reshape(1,-1)
o = model.predict(l)
if o[0] == 1:
    print('Heart Attack!')
else:
    print('Nothing')