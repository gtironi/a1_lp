import pandas as pd
import numpy as np

def summary(dataframe, column):
    '''Realiza as medidas de resumo de uma coluna especificada.

    Parameters
    ----------
    dataframe: dataframe
        O dataframe a ser analisado
    column: str
        O nome da coluna a ser resumida

    Raises
    ------
        
    Returns
    -------
    summary
        Uma tupla contendo cada medida de resumo, da forma [média, mediana, moda, desvio padrão, variância]
    '''
    media = dataframe[column].mean()
    mediana = dataframe[column].median()
    moda = dataframe[column].mode()
    desvio_padrao = dataframe[column].std().round(3)
    variancia = 
    
    summary = tuple(media, mediana, moda, desvio_padrao, variancia)
    
    return summary 

def frequencia():
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()