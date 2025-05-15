''' Import Libraries'''
import pandas as pd
import numpy as np


class Classifier:
    ''' This is a class prototype for any classifier. It contains two empty methods: predict, fit'''
    def __init__(self):
        self.model_params = {}
        pass
    
    def predict(self, x):
        '''This method takes in x (numpy array) and returns a prediction y'''
        raise NotImplementedError
    
    def fit(self, x, y):
        '''This method is used for fitting a model to data: x, y'''
        raise NotImplementedError



            
class Prior(Classifier):
    
    def __init__(self):
        super().__init__()

    def predict(self, x):
        '''This method takes in x (numpy array) and returns a prediction y'''
        return max(self.model_params, key=self.model_params.get)
    
    def fit(self, x, y):
        '''This method is used for fitting a model to data: x (numpy array), y (numpy array)'''
        # If x and y are pandas dataframe, then we can also use .value_counts() to make it easier
        counts = {}
        
        for label in y:
            if label in counts:
                counts[label] += 1
            else:
                counts[label] = 1

        # Or we can use - unique, counts = np.unique(y, return_counts=True) and zip both unique and counts
        tot = len(y)
        self.model_params = {l: count / tot for l, count in counts.items()}  
        