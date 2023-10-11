import pandas as pd
import numpy as np

def measure_tendency(dataframe, column):
    '''Realiza as Medidas de Tendência Central de uma coluna especificada.

    Parameters
    ----------
    dataframe: dataframe
        O dataframe a ser analisado
    column: str
        O nome da coluna a ser analisada

    Raises
    ------
    TypeError
        O parametro dataframe não é um dataframe ou a coluna é categórica
    KeyError
        A coluna passada não existe
        
    Returns
    -------
    tendency_metrics
        Uma tupla contendo cada medidas de tendência central.
        Se a variável for numerica, será da forma (média, mediana, moda)
        Se a variável for categorica, será apeans a moda
    
    >>> data = dc.remove_colunas_irrelevantes(dc.csv_to_dataframe('test.csv'), 2)
    >>> measure_tendency(data, 'Coluna1')
    (7.5, 9.0, 10)
    
    >>> measure_tendency(data, 'Errado')
    A coluna Errado não existe
    
    >>> measure_tendency(data, 'Coluna3')
    'Ola'
    
    >>> measure_tendency(3, 'Coluna3')
    O argumeto passado não é do tipo pd.DataFrame
    '''
    try:
        media = dataframe[column].mean()
        mediana = dataframe[column].median()
        moda = dataframe[column].mode().values[0]
        tendency_metrics = (media, mediana, moda)
    except TypeError:
        if isinstance(dataframe, pd.DataFrame):
            if isinstance(dataframe[column], object) or isinstance(dataframe[column], str):
                tendency_metrics = dataframe[column].mode().values[0]
        elif not isinstance(dataframe, pd.DataFrame):
            print(f'O argumeto passado não é do tipo pd.DataFrame')
    except KeyError:
        print(f'A coluna {column} não existe')
    finally:
        try:    
            return tendency_metrics
        except:
            pass


def measure_dispersion(dataframe, column):
    '''Realiza as Medidas de Dispersão de uma coluna especificada. 
       Só funciona para variáveis numéricas.

    Parameters
    ----------
    dataframe: dataframe
        O dataframe a ser analisado
    column: str
        O nome da coluna a ser analisada

    Raises
    ------
    TypeError
        O parametro dataframe não é um dataframe ou a coluna é categórica
    KeyError
        A coluna passada não existe
        
    Returns
    -------
    dispersion_metrics
        Uma tupla contendo cada medidas de dispersão, da forma (desvio padrâo, variância, máximo, mínimo, amplitude)
    
    >>> data = dc.remove_colunas_irrelevantes(dc.csv_to_dataframe('test.csv'), 2)
    >>> measure_dispersion(data, 'Coluna1')
    (3.786, 14.333, 10, 2, 8)
    
    >>> measure_dispersion(data, 'Errado')
    A coluna Errado não existe
    
    >>> measure_dispersion(data, 'Coluna3')
    A coluna Coluna3 não é um número, portanto, não tem medidas de dispersão
    ()
    
    >>> measure_dispersion(3, 'Coluna3')
    O argumeto passado não é do tipo pd.DataFrame
    '''
    try:
        desvio_padrao = dataframe[column].std().round(3)
        variancia = dataframe[column].var().round(3)
        maximo = dataframe[column].max()
        minimo = dataframe[column].min()
        amplitude = dataframe[column].max() - dataframe[column].min()
        dispersion_metrics = (desvio_padrao, variancia, maximo, minimo, amplitude)
        
        return dispersion_metrics
    except TypeError:
        if isinstance(dataframe, pd.DataFrame):
            if isinstance(dataframe[column], object) or isinstance(dataframe[column], str):
                print(f'A coluna {column} não é um número, portanto, não tem medidas de dispersão')
                return ()
        elif not isinstance(dataframe, pd.DataFrame):
            print(f'O argumeto passado não é do tipo pd.DataFrame')
    except KeyError:
        print(f'A coluna {column} não existe')

def frequencia():
    pass


import data_cleaner as dc

data = dc.remove_colunas_irrelevantes(dc.csv_to_dataframe('test.csv'), 3600)
print(data.head())

print(measure_tendency(data, 'Colunas3'))


if __name__ == "__main__":
    import doctest
    doctest.testmod()