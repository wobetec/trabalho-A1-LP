from data_work.size_manager import load_data
import data_work.data_info as di
import pandas as pd
import numpy as np


def get_data_ready() -> pd.DataFrame:
    """
    Trata os dados originais para que seja possível realizar as visualizações de dados

    Parametros:

    Returns:
    df (pd.DataFrame): Dataframe pronto para ser construido visualizações
    """
    df = load_data(di.FILE_NAMES["small_file"])
    tipos_validos = [
        np.dtypes.ObjectDType,
        np.dtypes.Float64DType,
        np.dtypes.Int64DType,
    ]
    coluna_limites = {
        "TP_FAIXA_ETARIA": 20,
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
    colunas_a_verificar = [
        "TP_FAIXA_ETARIA",
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

    print("Verificando respostas diferentes...")
    limitar_respostas_diferentes(df, coluna_limites)
    print("Verificando linhas em branco...")
    remover_linhas_com_valores_em_branco(df, colunas_a_verificar)
    print("Verificando tipos de dados...")
    tratar_tipo_dados(df, tipos_validos)

    return df


def limitar_respostas_diferentes(df: pd.DataFrame, coluna_limites: dict):
    """
    Modifica o DataFrame original limitando o número máximo de respostas diferentes por coluna.

    Parâmetros:
        df (pd.DataFrame): Dataframe original
        coluna_limites (dict): Dicionário com o número máximo de respostas diferentes por coluna
    """
    for coluna, limite_coluna in coluna_limites.items():
        contagem_valores = df[coluna].value_counts()
        respostas_mais_frequentes = contagem_valores.head(limite_coluna)

        df[coluna] = df[coluna].apply(
            lambda x: x if x in respostas_mais_frequentes else None
        )


def remover_linhas_com_valores_em_branco(df: pd.DataFrame, colunas_a_verificar: list):
    """
    Remove as linhas que contêm dados nulos em determinadas colunas do dataframe e modifica o DataFrame original.

    Parâmetros:
        df (pd.DataFrame): Dataframe original
        colunas_a_verificar (list): Lista de colunas a serem verificadas se possuem valores nulos
    """
    df.dropna(subset=colunas_a_verificar, inplace=True)


def tratar_tipo_dados(df: pd.DataFrame, tipos_validos: list):
    """
    Verifica o tipo de dado de cada coluna do dataframe original, se não for do tipo previsto transforma o dado no tipo str

    Parâmetros:
        df (pd.DataFrame): Dataframe original
        tipos_validos (list): Lista com os tipos de dados que serão aceitos dentro do dataframe
    """
    for coluna in df.columns:
        try:
            tipo_coluna = df[coluna].dtype
            if not any(isinstance(tipo_coluna, tipo) for tipo in tipos_validos):
                df[coluna] = df[coluna].astype(str)
        except Exception as e:
            df[coluna] = df[coluna].astype(str)
    
