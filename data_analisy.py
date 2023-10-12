import pandas as pd
import numpy as np
import data_cleaner as dc

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
        media = dataframe[column].mean().round(3) #calcula a média, arredonda com 3 casas
        mediana = dataframe[column].median() #calcula a mediana
        moda = dataframe[column].mode().values[0] #calcula a moda e transforma o dataframe resultante em um valor
        tendency_metrics = (media, mediana, moda) #junta as medidas em uma tupla
        return tendency_metrics
    
    except TypeError: 
        if isinstance(dataframe, pd.DataFrame): #verifica se o argumento dataframe é do tipo dataframe
            if isinstance(dataframe[column], object) or isinstance(dataframe[column], str): #verifica se o dado é categorico
                tendency_metrics = dataframe[column].mode().values[0] #calcula a moda e transforma o dataframe resultante em um valor
                return tendency_metrics     
        else: #verifica se o argumento dataframe não é do tipo dataframe
            print(f'O argumeto passado não é do tipo pd.DataFrame') #avisa sobre o erro no argumento da função, não há como tratar de outra forma
            
    except KeyError:
        print(f'A coluna {column} não existe') #avisa sobre o erro no argumento da função, não há como tratar de outra forma

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
        desvio_padrao = dataframe[column].std().round(3) #calcula o desvio padrao, arredonda com 3 casas
        variancia = dataframe[column].var().round(3) #calcula a variancia, arredonda com 3 casas
        maximo = dataframe[column].max() #calcula o valor maximo
        minimo = dataframe[column].min() #calcula o valor minimo
        amplitude = dataframe[column].max() - dataframe[column].min() #calcula a amplitude
        dispersion_metrics = (desvio_padrao, variancia, maximo, minimo, amplitude) #junta as medidas em uma tupla
        return dispersion_metrics
    
    except TypeError:
        if isinstance(dataframe, pd.DataFrame): #verifica se o argumento dataframe é do tipo dataframe
            if isinstance(dataframe[column], object) or isinstance(dataframe[column], str): #verifica se o dado é categorico
                print(f'A coluna {column} não é um número, portanto, não tem medidas de dispersão') 
                return () #retorna uma lista vazia
        else: #verifica se o argumento dataframe não é do tipo dataframe
            print(f'O argumeto passado não é do tipo pd.DataFrame') #avisa sobre o erro no argumento da função, não há como tratar de outra forma
            
    except KeyError:
        print(f'A coluna {column} não existe') #avisa sobre o erro no argumento da função, não há como tratar de outra forma


if __name__ == "__main__":
    import doctest
    doctest.testmod()