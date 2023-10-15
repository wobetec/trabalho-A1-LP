import pandas as pd
from visualizations.utils import get_image_to_flask
import matplotlib.pyplot as plt

def romolo(df: pd.DataFrame) -> tuple:
    """ "
    Analisa a distribuição de sexo, estado civil e cor/raça dos participantes do ENEN 2022

    Parametros:
        DataFrame com subset de microdados do ENEN : df (PANDAS Dataframe)

    Returns:
        Imagem com 3 facets, Texto com analise dos graficos e o titulo do grafico

    """
    plt.style.use("ggplot")
    plt.figure(figsize=(25, 10))

    plt.tight_layout()
    
    # PLOT DE SEXO
    plt.subplot(1, 3, 1)

    contagem_sexo = df["TP_SEXO"].value_counts()
    total = contagem_sexo.sum()

    dict_sexo = {"F": "Feminino", "M": "Masculino"}

    cores = ["blue", "red"]

    percentuais = [(valor / total) * 100 for valor in contagem_sexo]

    rotulos = [dict_sexo.get(valor, valor) for valor in contagem_sexo.index]
    plt.bar(rotulos, contagem_sexo, ec="black", color=cores)

    for i, valor in enumerate(contagem_sexo):
        plt.text(i, valor, f"{percentuais[i]:.2f}%", ha="center", va="bottom")

    plt.bar(rotulos, contagem_sexo, ec="black", color=cores)
    plt.xlabel("Sexo Declarado")
    plt.ylabel("contagem")

    # PLOT ESTADO CIVIL
    plt.subplot(1, 3, 2)

    contagem_est_civil = df["TP_ESTADO_CIVIL"].value_counts()
    total = contagem_est_civil.sum()

    dict_estado_civil = {
        0: "Não informado",
        1: "Solteiro(a)",
        2: "Casado(a)/Mora com companheiro(a)",
        3: "Divorciado(a)/Desquitado(a)/Separado(a)",
        4: "Viúvo(a)",
    }

    cores = ["blue", "red", "green", "orange", "purple"]

    percentuais = [(valor / total) for valor in contagem_est_civil]

    contagem_est_civil = contagem_est_civil.sort_values(ascending=False)
    percentuais = [(valor / total) for valor in contagem_est_civil]

    rotulos = [
        dict_estado_civil.get(valor, valor) for valor in contagem_est_civil.index
    ]

    plt.bar(rotulos, percentuais, ec="black", color=cores)
    plt.xlabel("Estado Civil")
    plt.ylabel("Porcentagem")

    plt.xticks(rotation=45)

    plt.title("Distribuição de Estado Civil")

    for i, valor in enumerate(percentuais):
        plt.text(i, valor, f"{valor*100:.2f}%", ha="center", va="bottom")

    # PLOT COR/RAÇA
    plt.subplot(1, 3, 3)

    contagem_cor_raca = df["TP_COR_RACA"].value_counts()
    total = contagem_cor_raca.sum()

    dict_cor_raca = {
        0: "Não declarado",
        1: "Branca",
        2: "Preta",
        3: "Parda",
        4: "Amarela",
        5: "Indígena",
        6: "Não dispõe da informação",
    }

    cores = ["blue", "red", "green", "orange", "purple", "brown", "pink"]

    percentuais = [(valor / total) for valor in contagem_cor_raca]

    contagem_cor_raca = contagem_cor_raca.sort_values(ascending=False)
    percentuais = [(valor / total) for valor in contagem_cor_raca]

    rotulos = [dict_cor_raca.get(valor, valor) for valor in contagem_cor_raca.index]

    plt.bar(rotulos, percentuais, ec="black", color=cores)
    plt.xlabel("Cor/Raça")
    plt.ylabel("Porcentagem")

    plt.xticks(rotation=45)
    plt.title("Distribuição de Cor/Raça")

    for i, valor in enumerate(percentuais): 
        plt.text(i, valor, f"{valor*100:.2f}%", ha="center", va="bottom")

    text = [
        "Foram utilizados variáveis que demomstram a demografica dos indivíduos que realizaram a prova do ENEN no ano de 2022."
        "Na atualidade, o jovem que se submete a prova do ENEN é do sexo feminino (61%), solteira (90%) se auto-declarando parda e branca (80%)."
        "O que talvez seja o mais importante notar é que temos um baixo indice de negro e indios, fato relevenate que deve ser usado nas políticas"
        "públicas de promoção a educação"
    ]

    title = "Perfil Demográfico dos participantes do ENEN 2022 - Romolo"

    return get_image_to_flask(plt), text, title