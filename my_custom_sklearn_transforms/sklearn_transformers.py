from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns, add_mean, faltas, horas, reprovad, mean_humanas, hrs_humanas, rp_humanas):
        self.columns = columns
        self.add_mean = add_mean
	self.faltas = faltas
	self.horas = horas
	self.reprovad = reprovad
	self.mean_humanas = mean_humanas
	self.hrs_humanas = hrs_humanas
	self.rp_humanas = rp_humanas

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        data["NOTA_MEAN"] = data[self.add_mean].mean(axis=1, skipna=True)
	data["TOTAL_FALTAS"] = data[self.faltas].sum(axis=1, skipna=True)
	data["TOTAL_REPROV"] = data[self.reprovad].sum(axis=1, skipna=True)
        data["TAREF_DIF"] = data["EXERCICIOS"]-data["TOTAL_FALTAS"]-data["TOTAL_REPROV"]
        return data.drop(labels=self.columns, axis='columns')


