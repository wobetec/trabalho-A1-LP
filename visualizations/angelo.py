import pandas as pd
from visualizations.utils import get_image_to_flask
import matplotlib.pyplot as plt

def angelo(df: pd.DataFrame) -> tuple:
    """
    Estrutura padrão com a visualização do Angelo

    Parametros:
        df (pd.DataFrame): DataFrame com os dados

    Returns:
        image (str): Tag imagem com os bytes da figura
        text (list): Lista com os textos para serem exibidos na página
        title (str): Título da visualização

    """
    cross_tab = pd.crosstab(df["Q006"], df["TP_FAIXA_ETARIA"])

    ax = cross_tab.plot(kind="bar", stacked=True, colormap="viridis")

    plt.xlabel("Renda Familiar")
    plt.title("Distribuição da Faixa Etária pela Renda Familiar - Angelo")
    ax.get_legend().remove()
    ax.set_ylabel("")
    plt.ticklabel_format(style="plain", axis="y")

    text = [
        "Observamos que, em algumas situações, pessoas com recursos financeiros limitados optam por realizar a prova após a idade média esperada.",
        "A desigualdade social desempenha um papel crucial no acesso à educação de qualidade.",
        "e essa visualização ressalta a complexidade das decisões educacionais em um contexto de desigualdade.",
        "A análise destaca a necessidade contínua de promover a equidade educacional e combater a desigualdade no acesso à educação.",
        "A crítica sugere que a falta de oportunidade de estudos por conta da renda familiar acarreta no tardio ingresso no mercado de trabalho.",
    ]

    title = "Oportunidade de Estudo - Angelo"

    return get_image_to_flask(plt), text, title