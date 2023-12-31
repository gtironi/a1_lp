import data_analisy as da
import data_cleaner as dc
import data_visualization as vis
import os

if not os.path.exists("imagens"):
    os.makedirs("imagens")


## Tratamento dos dados
dataframe_without_tratament = dc.csv_to_dataframe('censo_escolar_2021.csv') #lê o dado

dataframe_names_corrected = dc.corrige_nome_estados(dataframe_without_tratament) # corrige o nome dos estados na coluna NO_UF

dataframe_no_irrelevant_coluns = dc.remove_colunas_irrelevantes(dataframe_names_corrected, 3600) #retira colunas com mais de 3600 NaN

dataframe_no_NaN = dataframe_no_irrelevant_coluns.dropna(axis = 0) #retira linhas com NaN

dataframe = dc.replace_88888_values(dataframe_no_NaN) #altera os valores 88888 pelo maior valor imediatamente anteriror a ele


## Visualizações

vis.visualizacao_gustavo(dataframe) #cria e salva a visualização do gustavo em um arquivo

vis.visualizacao_marciano(dataframe) #cria e salva a visualização do marciano em um arquivo

vis.visualizacao_tambosi(dataframe) # Cria e salva a visualização do Tambosi em 2 arquivos

vis.visualizacao_vilas(dataframe_without_tratament) # Cria e salva a visualização do Vilas em um arquivo png

