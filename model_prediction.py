import pickle
from numpy.core.defchararray import array

model_path = '/Users/arshad_221b/Projects/heart attack /finalized_model.sav'
model = pickle.load(open(model_path, 'rb'))

def prediction(l):
    l = [float(x) for x in l]
    l = array(l)
    l = l.reshape(1,-1)
    o = model.predict(l)
    if o[0] == 1:
        return('Heart Attack!')
    else:
        return('No Heart Attack!')



