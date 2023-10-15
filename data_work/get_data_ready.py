from data_work.size_manager import load_data
import data_work.data_info as di

def get_data_ready():
    """
    Trata os dados originais para que seja possível realizar as visualizações de dados

        Parametros:

        Returns:
        df (pd.DataFrame): Dataframe pronto para ser construido visualizações
    """
    df = load_data(di.FILE_NAMES["small_file"])
    tipos_validos = [int, str, float]
    coluna_limites = {"TP_FAIXA_ETARIA": 20,
    "TP_SEXO": 2,
    "TP_ESTADO_CIVIL": 5,
    "TP_COR_RACA": 6,
    "TP_ST_CONCLUSAO": 4,
    "TP_ANO_CONCLUIU": 17,
    "TP_ESCOLA": 3,
    "IN_TREINEIRO": 2,
    "SG_UF_PROVA": 27,
    "TP_PRESENCA_CN": 3,
    "TP_PRESENCA_CH": 1,
    "TP_PRESENCA_LC": 1,
    "TP_PRESENCA_MT": 3,
    "TP_LINGUA": 2,
    "TP_STATUS_REDACAO": 8,
    "Q005": 10,
    "Q006": 10,
    "Q019": 10,
    "Q021": 10,
    "Q022": 10,
    "Q024": 10,
    "Q025": 10,
    }
    colunas_a_verificar = ["TP_FAIXA_ETARIA",
    "TP_SEXO",
    "TP_ESTADO_CIVIL",
    "TP_COR_RACA",
    "TP_ST_CONCLUSAO",
    "TP_ANO_CONCLUIU",
    "TP_ESCOLA",
    "IN_TREINEIRO",
    "SG_UF_PROVA",
    "Q005",
    "Q006",
    "Q019",
    "Q021",
    "Q022",
    "Q024",
    "Q025",
    ]

    # limitar_respostas_diferentes(df,coluna_limites)
    # remover_linhas_com_valores_em_branco(df,colunas_a_verificar)
    # tratar_tipo_dados(df, tipos_validos)

    return df

def limitar_respostas_diferentes(df, coluna_limites):
    """
    Verifica e limita o número máximo de respostas diferentes dentro de um dataframe

        Parametros:
        df (pd.DataFrame): Dataframe original
        colunas_limite (dict): Dicionário com o número máximo de respostas diferentes por coluna

        Returns:
        dataframe_modificado (pd.DataFrame): Dataframe com as colunas limitadas

    """
    dataframe_modificado = df.copy()

    for coluna, limite_coluna in coluna_limites.items():
        contagem_valores = df[coluna].value_counts()
        respostas_mais_frequentes = contagem_valores.head(limite_coluna)

        dataframe_modificado[coluna] = dataframe_modificado[coluna].apply(lambda x: x if x in respostas_mais_frequentes else None)
    
    return dataframe_modificado

def remover_linhas_com_valores_em_branco(df, colunas_a_verificar):
    """
    Remove as linhas que contem dados nulos em determinadas colunas do dataframe

        Parametros:
        df (pd.DataFrame): Dataframe original
        colunas_a_verificar (list): Lista de colunas a serem verificadas se possuem valores nulos

        Returns:
        dataframe_modificado (pd.DataFrame): Dataframe com a remoção das linhas com registros nulos
    """
    dataframe_modificado = df.copy()
    dataframe_modificado.dropna(subset=colunas_a_verificar, inplace=True)
    return dataframe_modificado

def tratar_tipo_dados(df, tipos_validos):
    """
    Verifica o tipo de dado de cada coluna do dataframe original, se não for do tipo previsto transforma o dado no tipo str

        Parametros:
        df (pd.DataFrame): Dataframe original
        tipos_validos (list): Lista com os tipos de dados que serão aceitos dentro do dataframe

        Returns:
        df (pd.DataFrame): Dataframe com os tipos de dados tratados
    """
    for coluna in df.columns:
        try:
            tipo_coluna = df[coluna].dtype
            if tipo_coluna not in tipos_validos:
                df[coluna] = df[coluna].astype(str)
        except Exception as e:
            df[coluna] = df[coluna].astype(str)
    
    return df

