from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns, add_mean):
        self.columns = columns
	self.add_mean = add_mean

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
	data["NOTA_MEAN"] = data[self.add_mean].mean(axis=1, skipna=True)
        data["TAREF_DIF"] = data["TAREFAS_ONLINE"]-data["FALTAS"]-data["REPROVACOES_DE"]-data["REPROVACOES_EM"]-data["REPROVACOES_GO"]-data["REPROVACOES_MF"]
        return data.drop(labels=self.columns, axis='columns')


