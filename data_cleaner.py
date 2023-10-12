import pandas as pd
import numpy as np

def csv_to_dataframe(csv_path, separator=";", encoding_parameter = 'cp860'):
    '''Transforma um arquivo .csv em um dataframe de acordo com alguns parametros.

        Parameters
        ----------
        csv_path : str
            O caminho para o arquivo a ser lido
        separator : str, optional
            O separador do csv
        encoding_parameter : str, optional
            Define a codificação padrão que será usada
            
        Raises
        ------
        ValueError
            O argumento csv_path é do tipo errado
        FileNotFoundError
            O caminho para o arquivo está errado
        TypeError
            O argumento separator ou encoding_parameter não é uma string
        LookupError
            O encoding_parameter é invalido

        Returns
        -------
        dataframe
            Um dataframe com os dados do arquivo .csv
            
        >>> csv_to_dataframe('test.csv')
           Coluna1  Coluna2 Coluna3
        0       10      0.0     Ola
        1        8      NaN     Ola
        2       10     10.0     NaN
        3        2      4.0    Tudo
        '''
    try:
        dataframe = pd.read_csv(csv_path, sep=separator, encoding = encoding_parameter, low_memory=False)
        return dataframe
    except ValueError:
        print(f'O valor passado ({csv_path}) não é uma string, por favor, passe o caminho para o seu csv como uma string')
    except FileNotFoundError:
        print((f'O valor passado ({csv_path}) não leva ao arquivo'))
    except TypeError:
        print("O valor passado para o argumento separator ou encoding_parameter é do tipo errado, certifique-se que esteja passando uma string valida")
    except LookupError:
        print("O valor do encoding_parameter não é valido")


def remove_colunas_irrelevantes(dataframe, num_NaN_values):
    '''Remove as colunas com mais NaN do que o especificado.

    Parameters
    ----------
    dataframe: dataframe
        O dataframe a ser tratado
    num_NaN_values: int, float
        Numero de valores NaN para a coluna ser removida

    Raises
    ------
    AttributeError
        O argumento dataframe não é um dataframe
    TypeError
        O argumento num_NaN_values não é um inteiro
    ValueError
        O argumento num_NaN_values não é um inteiro
        
    Returns
    -------
    dataframe_sem_colunas_irrelevantes
        O dataframe sem as colunas com mais NaN do que o especificado
        
    >>> data = pd.DataFrame({'A':[1, 4, 6, 9],'B':[3, np.NaN, 8, np.NaN],'C':[7, 3, np.NaN, 2],'D':[1, np.NaN, np.NaN, np.NaN]})
    >>> remove_colunas_irrelevantes(data, num_NaN_values = 2)
       A    B    C
    0  1  3.0  7.0
    1  4  NaN  3.0
    2  6  8.0  NaN
    3  9  NaN  2.0
    '''
    try:
        num_non_NaN_values = len(dataframe) - int(num_NaN_values)
        dataframe_sem_colunas_irrelevantes = dataframe.dropna(axis = 1, thresh = num_non_NaN_values)
        return dataframe_sem_colunas_irrelevantes
    except AttributeError:
        print(f"O atributo passado ({dataframe}) não é um dataframe")
    except (TypeError, ValueError):
        print(f"O valor passado para num_NaN_values ({num_NaN_values}), deve ser um inteiro")

if __name__ == "__main__":
    import doctest
    doctest.testmod()