from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns, add_mean, mean_humanas):
        self.columns = columns
        self.add_mean = add_mean
        self.mean_humanas = mean_humanas

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        for nota in self.add_mean:
            data[nota] = np.where(data[nota] > 10, 10, data[nota])
            max_=data[nota].quantile(0.95)
            min_=data[nota].quantile(0.05)
            data[nota] = np.where(data[nota] > max_, max_, data[nota])
            data[nota] = np.where(data[nota] < min_, min_, data[nota])

        data["MEAN_H"] = data[self.mean_humanas].mean(axis=1, skipna=True)
        data["MEAN_T"] = data[self.add_mean].mean(axis=1, skipna=True)
        return data.drop(labels=self.columns, axis='columns')


