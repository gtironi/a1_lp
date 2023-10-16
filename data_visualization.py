import matplotlib.pyplot as plt
import pandas as pd
import os


def visualizacao_gustavo(dataframe):
    '''Plota o gráfico que mostra a quantidade média de TVs por escola, por estado

    Parameters
    ----------
    dataframe: dataframe
        O dataframe a ser plotado

    Raises
    ------
    TypeError
        O parametro dataframe não é um dataframe
    AttributeError
        O parametro dataframe não é um dataframe

    Returns
    -------
    
    >>> visualizacao_gustavo('Erro')
    O argumeto passado não é do tipo pd.DataFrame
    '''
    try:
        media_tv_por_estado = dataframe.groupby('SG_UF')['QT_EQUIP_TV'].mean() #agrupa o dataframe por estado, seleciona a coluna 'QT_EQUIP_TV' e calcula a média

        estados = list(media_tv_por_estado.index) #seleciona e guarda o index da serie, que são os estados
        media_tv = list(media_tv_por_estado.values) #separa os valores da serie, que são a quantidade media de TVs

        plt.bar(estados, media_tv, color = "y") #plota o gráfico

        plt.title('Quantidade média de TVs por escola, por estado') #coloca titulo no grafico
        plt.xlabel('Estados') #define a label no eixo x
        plt.ylabel('Quantidade média de TVs') #define a label no eixo y
        plt.savefig(os.path.join("Imagens", "visualizacao_gustavo.png"))
        plt.close()
    except (TypeError,AttributeError):
        print(f'O argumeto passado não é do tipo pd.DataFrame') #avisa sobre o erro no argumento da função, não há como tratar de outra forma
        

def visualizacao_marciano(dataframe):
    '''Plota o gráfico que mostra a quantidade de escolas sem internet por estado, de acordo com a base de dados

    Parameters
    ----------
    dataframe: dataframe
        O dataframe a ser plotado

    Raises
    ------
    TypeError
        O parametro dataframe não é um dataframe
    AttributeError
        O parametro dataframe não é um dataframe
        
    Returns
    -------
    
    >>> visualizacao_marciano('Erro')
    O argumeto passado não é do tipo pd.DataFrame
    '''
    try:
        colunas_selecionadas = dataframe[dataframe["NO_REGIAO"] == "Norte"]
        escolas_sem_internet = colunas_selecionadas[colunas_selecionadas["IN_INTERNET"] == 0]
        
        n_escolas_sem_internet = escolas_sem_internet.groupby('NO_UF')['IN_INTERNET'].count().sort_values()

        n_escolas_sem_internet.plot(kind='bar', color='red') # plota o grafico a partir da base de dados
        plt.xlabel('Estado') # define label do eixo x
        plt.ylabel('Número de Escolas') # define label do eixo y
        plt.title('Quantidade de escolas sem acesso à Internet por Estado') #define título
        plt.xticks(rotation=45) # roda o nome dos estados em 45 graus
        plt.savefig(os.path.join("Imagens", "visualizacao_marciano.png"))
        plt.close() # salva o plot em um arquivo
    except (TypeError, AttributeError):
        print(f'O argumeto passado não é do tipo pd.DataFrame') #avisa sobre o erro no argumento da função, não há como tratar de outra forma


def visualizacao_tambosi(df):
    """
    Plota um histograma com a distribuição de datas de inicio de aulas por estado.
    
    Parameters
    ----------
    dataframe: dataframe
        O dataframe a ser analisado
    
    Raises
    ------
    TypeError
        O parametro dataframe não é um dataframe
    AttributeError
        O parametro dataframe não é um dataframe
    KeyError
        Nao existe uma coluna NO_REGIAO
    ValueError
        Há registros fora do formato '%d%b%Y:%H:%M:%S' na coluna 'DT_ANO_LETIVO_INICIO'
    

    Returns
    ----------
        None
        
    >>> visualizacao_tambosi ('Erro')
    O argumeto passado não é do tipo pd.DataFrame
    
    >>> c = pd.DataFrame({"Coluna":[1, 2, 3, 4]})
    >>> visualizacao_tambosi(c)
    No seu DataFrame, não existe uma coluna NO_REGIAO
    """

    try:
        # 1. AGRUPAR POR REGIÃO
        datas_estado = df.groupby("NO_REGIAO")
        
    except (TypeError, AttributeError):
        print('O argumeto passado não é do tipo pd.DataFrame') #avisa sobre o erro no argumento da função, não há como tratar de outra forma
        return
    
    except KeyError: 
        print('No seu DataFrame, não existe uma coluna NO_REGIAO')
        return
    
    
    # 2. REALIZAR A ANALISE PARA CADA REGIAO
    for region, data in datas_estado :   

        try:
            data_formatado = pd.to_datetime(data["DT_ANO_LETIVO_INICIO"], format='%d%b%Y:%H:%M:%S') # Transformar data em datetime
        
        except ValueError: # Provavelmente foi esquecida a limpeza da base!
            data = data.dropna()
            data_formatado = pd.to_datetime(data["DT_ANO_LETIVO_INICIO"], format='%d%b%Y:%H:%M:%S') # Transformar data em datetime

        # 3. AGRUPAR POR SEMANA
        data[f"Semana do ano - {region}"] = data_formatado.dt.strftime('%Y-%U')

        # 4. CONTAR A FREQUENCIA DE CADA SEMANA
        semanal = data[f"Semana do ano - {region}"].value_counts()

        # 5. ORDENAR O SERIES PELO INDEX ASC
        semanal_ord = semanal.sort_index()

        # 6. PARA CADA REGIAO, PLOTAR UM HISTOGRAMA DE DATA POR FREQUENCIA
        plt.figure(figsize=(10, 3))
        semanal_ord.plot(kind='bar', color='yellow')
        plt.xlabel('Semana do ano')
        plt.ylabel('Ocorrências')
        plt.title(f'Distribuição de Data de Inicio das Aulas - {region}')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f"(Tambosi) Distribuicao Inicio Aulas - {region}")

def visualizacao_vilas(dataframe):
    '''
    Plota uma peça gráfica que mostra a distribuição de matrículas nos respectivos níveis de ensino para cada dependência administrativa.

    Parameters
    ----------
    dataframe : pd.DataFrame
        Dataframe contendo as informações necessárias para criar a visualização. Deve conter as colunas:
        "NO_REGIAO", "NO_UF", "TP_DEPENDENCIA", "QT_MAT_INF_INT", "QT_MAT_INF_CRE_INT", "QT_MAT_INF_PRE_INT",
        "QT_MAT_FUND_INT", "QT_MAT_FUND_AI_INT", "QT_MAT_FUND_AF_INT", "QT_MAT_MED_INT".

    Raises
    ------
    TypeError
        Se o argumento passado não for do tipo pd.DataFrame.
    ValueError
        Se o dataframe não contiver todas as colunas necessárias.

    Returns
    -------
    None

    Examples
    --------
    >>> visualizacao_vilas('Erro')
    O argumento passado não é do tipo pd.Dataframe
    '''

    try:
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError('O argumento passado não é do tipo pd.DataFrame')
        
        required_columns = ["NO_REGIAO", "NO_UF", "TP_DEPENDENCIA", 
                            "QT_MAT_INF_INT", "QT_MAT_INF_CRE_INT", "QT_MAT_INF_PRE_INT",
                            "QT_MAT_FUND_INT", "QT_MAT_FUND_AI_INT", "QT_MAT_FUND_AF_INT", "QT_MAT_MED_INT"]

        for column in required_columns:
            if column not in dataframe.columns:
                raise ValueError(f'Coluna "{column}" não encontrada no dataframe.')

        indicadores_iniciais = dataframe.copy()
        indicadores_iniciais["QT_MAT_INF"] = indicadores_iniciais["QT_MAT_INF_INT"] + indicadores_iniciais["QT_MAT_INF_CRE_INT"] + indicadores_iniciais["QT_MAT_INF_PRE_INT"]
        indicadores_iniciais["QT_MAT_FUND"] = indicadores_iniciais["QT_MAT_FUND_INT"] + indicadores_iniciais["QT_MAT_FUND_AI_INT"] + indicadores_iniciais["QT_MAT_FUND_AF_INT"]
        indicadores_iniciais["QT_MAT_MED"] = indicadores_iniciais["QT_MAT_MED_INT"]

        # Criando o novo dataframe com as colunas desejadas
        novo_dataframe = indicadores_iniciais[["NO_REGIAO", "NO_UF", "TP_DEPENDENCIA", "QT_MAT_INF", "QT_MAT_FUND", "QT_MAT_MED"]]
        treated_dataframe = novo_dataframe.loc[(novo_dataframe[["QT_MAT_INF", "QT_MAT_FUND", "QT_MAT_MED"]] != 0).any(axis=1)]

        # Agrupando os dados por TP_DEPENDENCIA e somando as métricas
        grupo_dependencia = treated_dataframe.groupby('TP_DEPENDENCIA').agg({
            'QT_MAT_INF': 'sum',
            'QT_MAT_FUND': 'sum',
            'QT_MAT_MED': 'sum'
        })

        # Criando uma figura com 3 subplots
        fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(18, 6))

        # Gráfico para QT_MAT_INF por TP_DEPENDENCIA
        bars1 = ax[0].bar(grupo_dependencia.index, grupo_dependencia['QT_MAT_INF'], color='skyblue')
        ax[0].set_xlabel('TP_DEPENDENCIA')
        ax[0].set_ylabel('Soma de QT_MAT_INF')
        ax[0].set_title('Soma de QT_MAT_INF por TP_DEPENDENCIA')
        for bar in bars1:
            yval = bar.get_height()
            ax[0].text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')

        # Gráfico para QT_MAT_FUND por TP_DEPENDENCIA
        bars2 = ax[1].bar(grupo_dependencia.index, grupo_dependencia['QT_MAT_FUND'], color='lightgreen')
        ax[1].set_xlabel('TP_DEPENDENCIA')
        ax[1].set_ylabel('Soma de QT_MAT_FUND')
        ax[1].set_title('Soma de QT_MAT_FUND por TP_DEPENDENCIA')
        for bar in bars2:
            yval = bar.get_height()
            ax[1].text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')

        # Gráfico para QT_MAT_MED por TP_DEPENDENCIA
        bars3 = ax[2].bar(grupo_dependencia.index, grupo_dependencia['QT_MAT_MED'], color='lightcoral')
        ax[2].set_xlabel('TP_DEPENDENCIA')
        ax[2].set_ylabel('Soma de QT_MAT_MED')
        ax[2].set_title('Soma de QT_MAT_MED por TP_DEPENDENCIA')
        for bar in bars3:
            yval = bar.get_height()
            ax[2].text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')

        # Definindo o eixo x para mostrar apenas 1, 2, 3, 4
        for a in ax:
            a.set_xticks([1, 2, 3, 4])

        # Ajustando o layout para evitar sobreposição
        plt.tight_layout()
        plt.savefig(os.path.join("Imagens", "visualizacao_vilas_png"), bbox_inches='tight')
        plt.close()

    except (TypeError, ValueError) as e:
        print(f'Erro: {e}')

if __name__ == "__main__":
    import doctest
    doctest.testmod()
