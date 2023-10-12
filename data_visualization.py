import matplotlib.pyplot as plt

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
    except TypeError:
        print(f'O argumeto passado não é do tipo pd.DataFrame') #avisa sobre o erro no argumento da função, não há como tratar de outra forma
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()