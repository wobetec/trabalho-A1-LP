"""Este módulo é responsável por lidar com a compactação e descompactação dos arquivos, além de cortar os dados originais para gerar um arquivo menor e encapsular a utilização da pasta de dados.

"""
import pandas as pd
import data_work.data_info as di
from zipfile import ZipFile, ZIP_DEFLATED
import os

DATA_FOLDER = "../data/"

def path_to(file_name="", extension="") -> str:
    """
    Gera o absolute path para um caminho específico, baseado no diretório no qual está sendo executado, utilizando como base a pasta /data

    Parametros:
        file_name (str): Nome do arquivo
        extension (str): Extensão do arquivo

    Returns:
        data_path (str): Absolute path para o arquivo
    
    """
    relative = DATA_FOLDER

    if extension != "" and file_name != "":
        relative += file_name + "." + extension

    data_path = os.path.join(os.path.dirname(__file__), relative)

    return data_path


def unzip_file(file_name: str) -> None:
    """
    Descompacta um arquivo zipado dentro de /data

    Parametros:
        file_name (str): Nome do arquivo

    Returns:
    
    """
    with ZipFile(path_to(file_name, "zip"), "r") as zip_ref:
        zip_ref.extractall(path_to())


def zip_file(file_name: str) -> None:
    """
    Compacta um arquivo csv dentro de /data

    Parametros:
        file_name (str): Nome do arquivo

    Returns:
    
    """
    with ZipFile(path_to(file_name, "zip"), "w", ZIP_DEFLATED) as zip_ref:
        zip_ref.write(path_to(file_name, "csv"), arcname=file_name + ".csv")


def crop_data(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Corta os dados originais, ficando só com as colunas desejadas

    Parametros:
        df (pd.DataFrame): DataFrame com os dados originais
        columns (list): Lista com as colunas desejadas

    Returns:
        new_df (pd.DataFrame): DataFrame com os dados cortados
    
    """

    new_df = df[columns]

    return new_df


def save_data(df: pd.DataFrame, file_name: str) -> None:
    """
    Salva um dataframe em um arquivo csv

    Parametros:
        df (pd.DataFrame): DataFrame com os dados
        file_name (str): Nome do arquivo

    Returns:
    
    """
    df.to_csv(path_to(file_name, "csv"), index=False, encoding="ISO-8859-1", sep=";")


def load_data(file_name: str) -> pd.DataFrame:
    """
    Carrega um arquivo csv em um dataframe

    Parametros:
        file_name (str): Nome do arquivo

    Returns:
        df (pd.DataFrame): DataFrame com os dados
    
    """

    df = pd.read_csv(path_to(file_name, "csv"), encoding="ISO-8859-1", sep=";")
    return df


def create_data():
    """
    Driver function para:
        1- Carregar arquivo original
        2- Cortar o arquivo original
        3- Salvar o arquivo cortado
        4- Compactar o arquivo cortado

    Parametros:

    Returns:
    
    """
    if not os.path.exists(path_to(di.FILE_NAMES["full_file"], "csv")):
        print("Arquivo orignal nao encontrado, por favor, baixe o arquivo e tente novamente.")
        return
    
    print("Abrindo arquivo original...")
    full_df = load_data(di.FILE_NAMES["full_file"])

    print("Cortando o arquivo...")
    small_df = crop_data(full_df, di.USED_COLUMNS)

    print("Salvando o arquivo menor...")
    save_data(small_df, di.FILE_NAMES["small_file"])

    print("Zipando o arquivo...")
    zip_file(di.FILE_NAMES["small_file"])

    print("Arquivo criado com sucesso!")


def initialize_data():
    """
    Driver function para descompactar o arquivo menor caso não tenha sido previamente

    Parametros:

    Returns:
    
    """

    if os.path.exists(path_to(di.FILE_NAMES["small_file"], "csv")):
        print("O arquivo menor já foi descompactado.")
        return
    
    if not os.path.exists(path_to(di.FILE_NAMES["small_file"], "zip")):
        print("Arquivo menor nao encontrado, por favor, crie o arquivo e tente novamente.")
        raise FileExistsError
    
    print("Descompactando o arquivo...")
    unzip_file(di.FILE_NAMES["small_file"])

    print("Arquivo inicializado com sucesso!")


if __name__ == "__main__":
    initialize_data()
    pass
