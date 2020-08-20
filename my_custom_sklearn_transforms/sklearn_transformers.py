from sklearn.base import BaseEstimator, TransformerMixin


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
        data["TAREF_DIF"]=data["TAREFAS_ONLINE"]-data["FALTAS"]-data["REPROVACOES_DE"]-data["REPROVACOES_EM"]-data["REPROVACOES_GO"]-data["REPROVACOES_MF"]
        data["MEAN_H"] = data[self.mean_humanas].sum(axis=1, skipna=True)
        data["MEAN_T"] = data[self.add_mean].sum(axis=1, skipna=True)
        return data.drop(labels=self.columns, axis='columns')


