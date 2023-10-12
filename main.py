import data_analisy as da
import data_cleaner as dc
import data_visualization as vis


## Tratamento dos dados
dataframe_without_tratament = dc.csv_to_dataframe('censo_escolar_2021.csv') #lê o dado

dataframe_no_irrelevant_coluns = dc.remove_colunas_irrelevantes(dataframe_without_tratament, 3600) #retira colunas com mais de 3600 NaN

dataframe_no_NaN = dataframe_no_irrelevant_coluns.dropna(axis = 0) #retira linhas com NaN

dataframe = dc.replace_88888_values(dataframe_no_NaN) #altera os valores 88888 pelo maior valor imediatamente anteriror a ele

## Visualizações

vis.visualizacao_gustavo(dataframe) #cria e salva a visualização do gustavo em um arquivo