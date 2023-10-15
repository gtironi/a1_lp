import matplotlib.pyplot as plt
import pandas as pd

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
        plt.savefig('visualizacao_gustavo.png') #salva o plot em um arquivo
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
        plt.savefig("visualizacao_marciano.png", bbox_inches='tight') # salva o plot em um arquivo
    except (TypeError, AttributeError):
        print(f'O argumeto passado não é do tipo pd.DataFrame') #avisa sobre o erro no argumento da função, não há como tratar de outra forma


def visualizacao_tambosi(df):
    """
    Plota um histograma com a distribuição de datas de inicio de aulas por estado.

    Parameters:
        df (pd.DataFrame): DataFrame contendo a data.

    Returns:
        None
    """
    try:
        # 1. AGRUPAR POR REGIÃO
        datas_estado = df.groupby("NO_REGIAO")
    except (TypeError, AttributeError):
        print('O argumeto passado não é do tipo pd.DataFrame') #avisa sobre o erro no argumento da função, não há como tratar de outra forma
    
    # 2. REALIZAR A ANALISE PARA CADA REGIAO
    for region, data in datas_estado :   

        try:
            data_formatado = pd.to_datetime(data["DT_ANO_LETIVO_INICIO"], format='%d%b%Y:%H:%M:%S') # Transformar data em datetime
        
        except ValueError: # Provavelmente foi esquecida a limpeza da base!
            print("Você esqueceu a limpeza da base!")
            df = df.dropna()

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
        
        
            

if __name__ == "__main__":
    import doctest
    doctest.testmod()
