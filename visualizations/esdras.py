import pandas as pd
from visualizations.utils import get_image_to_flask
import matplotlib.pyplot as plt
import numpy as np

def esdras(df: pd.DataFrame) -> tuple:
    """
    Seguindo a estrutura padrão definida, esta função gera uma visualização comparando a influência da renda familiar na média das notas do enem.

    Parametros:
        df (pd.DataFrame): DataFrame com os dados

    Returns:
        image (str): Tag imagem com os bytes da figura
        text (list): Lista com os textos para serem exibidos na página
        title (str): Título da visualização

    """
    df["media"] = ( df["NU_NOTA_CH"] + df["NU_NOTA_CN"] + df["NU_NOTA_LC"] + df["NU_NOTA_MT"] + df["NU_NOTA_REDACAO"] ) / 5

    amostra = (
        df[["media", "Q006"]]
        .groupby("Q006")
        .mean()
        .sort_values(by="media", ascending=True)
        .reset_index()
    )

    cores = np.linspace(0, 1, len(amostra["Q006"]))
    cor_map = plt.get_cmap("YlOrRd")

    plt.bar(amostra["Q006"], amostra["media"], color=cor_map(cores))
    plt.xlabel("Renda Familiar")
    plt.ylabel("Média das Notas")
    plt.title("Comparação de Renda e Notas")

    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.6)

    plt.tight_layout()

    text = [
        "Inicialmente, é importante destacar que 'A' representa uma ausência de renda familiar, enquanto 'Q' representa uma renda superior a 20 salários mínimos, que, no período em questão, correspondia a R$ 1.212,00.",
        "É evidente que a renda familiar exerce uma influência direta sobre a média das notas, pois à medida que a renda aumenta, a média das notas também tende a crescer.",
        "Essa conexão pode ser atribuída à qualidade do sistema educacional, seja público ou privado. Isso reflete a desigualdade social no Brasil, onde a renda familiar desempenha um papel significativo na determinação da qualidade da educação disponível.",
    ]

    title = "Renda e Nota - Esdras"

    return get_image_to_flask(plt), text, title