import numpy as np
import pandas as pd
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel

class Result:

    method: str = ""
    bearing_id: int = ""
    predictions: dict = {}
    r_sqr: float = 0.0
    mse: float = 0.0


    def __init__(self):
        pass

class RegressionFramework:

    data: list = None
    labels: list = None

    def __init__(self):
        pass
    
    def removeNaNValues(self, extractedSASD: pd.DataFrame) -> list:
        data = []

        # read all columns, remove nan values and store then in list
        for bearing_id in extractedSASD.columns:
            bearing_data = np.array(extractedSASD[bearing_id])
            bearing_data = bearing_data[~np.isnan(bearing_data)]
            data.append(bearing_data)
        
        return data