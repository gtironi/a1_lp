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
            um dataframe com os dados do arquivo .csv
            
        >>> csv_to_dataframe('test.csv')
                 Coluna2  Coluna3
        Coluna1                  
        10           0.0      Ola
        8            NaN  TudoBem
        '''
    try:
        dataframe = pd.read_csv(csv_path, sep=separator, index_col=0, encoding = encoding_parameter)
        return dataframe
    except ValueError:
        print(f'O valor passado ({csv_path}) não é uma string, por favor, passe o caminho para o seu csv como uma string')
    except FileNotFoundError:
        print((f'O valor passado ({csv_path}) não leva ao arquivo'))
    except TypeError:
        print("O valor passado para o argumento separator ou encoding_parameter é do tipo errado, certifique-se que esteja passando uma string valida")
        print("O programa irá rodar usando o argumento padrão")
        csv_to_dataframe(csv_path)
    except LookupError:
        print("O valor do encoding_parameter não é valido")
        print("O programa irá rodar usando o argumento padrão")
        csv_to_dataframe(csv_path)

def remove_colunas_irrelevantes(dataframe):
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()