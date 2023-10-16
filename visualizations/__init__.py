"""
Esse módulo contém as visualizações e retornar elas de forma a serem renderizadas pelo flask.
"""

import pandas as pd

from visualizations.esdras import esdras
from visualizations.lara import lara
from visualizations.angelo import angelo
from visualizations.romolo import romolo


def get_all_vis(df: pd.DataFrame) -> list:
    """
    Retorna uma lista com todas as visualizações, de cada membro.

    Parametros:
        df (pd.DataFrame): DataFrame com os dados

    Returns:
        vis (list): Lista com todas as visualizações

    """
    vis = []

    vis.append(esdras(df))
    vis.append(lara(df))
    vis.append(angelo(df))
    vis.append(romolo(df))
    return vis