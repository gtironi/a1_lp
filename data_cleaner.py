import pandas as pd
import numpy as np
import data_analisy as da

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
        dataframe = pd.read_csv(csv_path, sep=separator, encoding = encoding_parameter, low_memory=False) #lẽ o arquivo, usando alguns argumentos pré definidos
        return dataframe #retorna o dataframe lido

    except ValueError:
        print(f'O valor passado ({csv_path}) não é uma string, por favor, passe o caminho para o seu csv como uma string') #avisa sobre o erro no argumento da função, não há como tratar de outra forma
    except FileNotFoundError:
        print((f'O valor passado ({csv_path}) não leva ao arquivo')) #avisa sobre o erro no argumento path da função, não há como tratar de outra forma
    except TypeError:
        print("O valor passado para o argumento separator ou encoding_parameter é do tipo errado, certifique-se que esteja passando uma string valida") #avisa sobre o erro no argumento da função, não há como tratar de outra forma
    except LookupError:
        print("O valor do encoding_parameter não é valido") #avisa que o padrão pedido não existe

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
        if int(num_NaN_values) > len(dataframe): #verifica se a quantidade passada é mairo que o dataframe
            num_non_NaN_values = 1
        else:
            num_non_NaN_values = len(dataframe) - int(num_NaN_values) #calcula a quantidade de valores que a coluna deve ter para não ser excluida
        dataframe_sem_colunas_irrelevantes = dataframe.dropna(axis = 1, thresh = num_non_NaN_values) #retira as colunas com menos valores não NaN que o especificado
        return dataframe_sem_colunas_irrelevantes #retorna o dataframe sem as colunas
    except AttributeError: 
        print(f"O atributo passado ({dataframe}) não é um dataframe") #avisa sobre o erro no argumento da função, não há como tratar de outra forma
    except (TypeError, ValueError):
        print(f"O valor passado para num_NaN_values ({num_NaN_values}), deve ser numerico") #avisa sobre o erro no argumento da função, não há como tratar de outra forma

def replace_88888_values(dataframe):
    '''Substitui os valores 88888 pelo maior valor imediatamente 
       anterior em todas as colunas possiveis.

    Parameters
    ----------
    dataframe: dataframe
        O dataframe a ser tratado

    Raises
    ------
        TypeError
            Ignora as variáveis categoricas
        ValueError
            Ignora as variáveis categoricas
        IndexError
            Ignora colunas com apenas um valor
        
    Returns
    -------
    dataframe
        O dataframe com os valores 88888 trocados
        
    >>> data = pd.DataFrame({'A':[88888, 4, 6, 9],'B':[3, np.NaN, 8, 88888],'C':['opa', 'ola', np.NaN, 'oi'],'D':[1, 1, 1, 1]})
    >>> replace_88888_values(data)
       A    B    C  D
    0  9  3.0  opa  1
    1  4  NaN  ola  1
    2  6  8.0  NaN  1
    3  9  8.0   oi  1
    '''
    for column in dataframe.columns:
        try:
            max = sorted(dataframe[column].unique())[-2]
            dataframe[column].replace(88888, int(max), inplace = True)
        except (TypeError, IndexError, ValueError):
            pass
    return dataframe



def corrige_nome_estados(df_censo):
    '''Corrige o nome dos estados do dataframe censo_escolar_2021

    Parameters
    ----------
    df_censo: dataframe
        O dataframe do censo_escolar

    Raises
    ------
    KeyError
        O dataframe indicado não possui a coluna NO_UF
    TypeError
        O df_censo não é um dataframe

    Returns
    -------
    dataframe
        O dataframe com os nome dos estados corretos

    >>> df = csv_to_dataframe("censo_escolar_2021.csv")
    >>> corrige_nome_estados(df)
           NU_ANO_CENSO NO_REGIAO  CO_REGIAO     NO_UF SG_UF  CO_UF  ... QT_TUR_EJA  QT_TUR_EJA_FUND QT_TUR_EJA_MED  QT_TUR_ESP QT_TUR_ESP_CC  QT_TUR_ESP_CE
    0              2021     Norte          1  Rondônia    RO     11  ...        0.0              0.0            0.0         0.0           0.0            0.0
    1              2021     Norte          1  Rondônia    RO     11  ...       11.0              7.0            4.0         5.0           5.0            0.0
    2              2021     Norte          1  Rondônia    RO     11  ...        0.0              0.0            0.0         0.0           0.0            0.0
    3              2021     Norte          1  Rondônia    RO     11  ...        0.0              0.0            0.0         3.0           3.0            0.0
    4              2021     Norte          1  Rondônia    RO     11  ...        0.0              0.0            0.0         2.0           2.0            0.0
    ...             ...       ...        ...       ...   ...    ...  ...        ...              ...            ...         ...           ...            ...
    80600          2021  Nordeste          2   Alagoas    AL     27  ...        0.0              0.0            0.0         1.0           1.0            0.0
    80601          2021  Nordeste          2   Alagoas    AL     27  ...        0.0              0.0            0.0         5.0           5.0            0.0
    80602          2021  Nordeste          2   Alagoas    AL     27  ...        0.0              0.0            0.0         0.0           0.0            0.0
    80603          2021  Nordeste          2   Alagoas    AL     27  ...        0.0              0.0            0.0         1.0           1.0            0.0
    80604          2021  Nordeste          2   Alagoas    AL     27  ...        NaN              NaN            NaN         NaN           NaN            NaN
    <BLANKLINE>
    [80605 rows x 370 columns]
    '''

    try:
        df_censo["NO_UF"] = df_censo["NO_UF"].replace("Rond⌠nia", "Rondônia")
        df_censo["NO_UF"] = df_censo["NO_UF"].replace("Parß", "Pará")
        df_censo["NO_UF"] = df_censo["NO_UF"].replace("Amapß", "Amapá")
        df_censo["NO_UF"] = df_censo["NO_UF"].replace("Maranhπo", "Maranhão")
        df_censo["NO_UF"] = df_censo["NO_UF"].replace("Piauφ", "Piauí")
        df_censo["NO_UF"] = df_censo["NO_UF"].replace("Cearß", "Ceará")
        df_censo["NO_UF"] = df_censo["NO_UF"].replace("Paraφba","Paraíba")
        return df_censo

    except KeyError:
        print("O data frame indicado não possui a coluna NO_UF.")
    except TypeError:
        print("O atributo indicado não é um dataframe.")



if __name__ == "__main__":
    import doctest
    doctest.testmod()
