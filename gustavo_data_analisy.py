import pandas as pd
import numpy as np

def measure_tendency(dataframe, column):
    '''Realiza as Medidas de Tendência Central de uma coluna especificada.

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
    tendency_metrics
        Uma tupla contendo cada medidas de tendência central, da forma [média, mediana, moda]
    '''
    media = dataframe[column].mean()
    mediana = dataframe[column].median()
    moda = dataframe[column].mode()
    tendency_metrics = tuple(media, mediana, moda)
    
    return tendency_metrics

def measure_dispersion(dataframe, column):
    '''Realiza as Medidas de Dispersão de uma coluna especificada.

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
    dispersion_metrics
        Uma tupla contendo cada medidas de dispersão, da forma [desvio padrâo, variância, máximo, mínimo, amplitude]
    '''
    desvio_padrao = dataframe[column].std().round(3)
    variancia = dataframe[column].var()
    maximo = dataframe[column].max()
    minimo = dataframe[column].min()
    amplitude = dataframe[column].max() - dataframe[column].min()
    dispersion_metrics = tuple(desvio_padrao, variancia, maximo, minimo, amplitude)
    
    return dispersion_metrics

def frequencia():
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()