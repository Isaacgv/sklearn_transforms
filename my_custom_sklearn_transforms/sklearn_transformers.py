from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

class AddMean(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        #data["NOTA_MEAN"]= data[self.columns].mean(axis=1, skipna=True)
        data["NOTA_MEAN"]= data[self.columns].mean(axis=1, skipna=True)
        data["TAREF_DIF"]=df_data_1["TAREFAS_ONLINE"]-df_data_1["FALTAS"]-df_data_1["REPROVACOES_DE"]-df_data_1["REPROVACOES_EM"]-df_data_1["REPROVACOES_GO"]-df_data_1["REPROVACOES_MF"]
        return data
