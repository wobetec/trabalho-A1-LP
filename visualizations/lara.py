import pandas as pd
from visualizations.utils import get_image_to_flask
import matplotlib.pyplot as plt


def lara(df: pd.DataFrame) -> tuple:
    """
    Visualização que mostra a porcentagem de participantes do gênero feminino e masculino, separando pelas raças também declaradas por esses participantes.

    Parametros:
        df (pd.DataFrame): DataFrame com os dados

    Returns:
        image (str): Tag imagem com os bytes da figura
        text (list): Lista com os textos para serem exibidos na página
        title (str): Título da visualização
    """

    grouped_data = df.groupby(["TP_COR_RACA", "TP_SEXO"]).size().unstack()

    cores = ["pink", "blue"]

    grouped_data.plot(kind="bar", stacked=True, color=cores)

    plt.xlabel("Raça")
    plt.ylabel("Contagem")
    plt.xticks(rotation=0)

    plt.title("Distribuição de Gênero por Raça no ENEM")
    text = [
        "É possível notar que os grupos 1 e 3 são os maiores, sendo então candidatos brancos ou pardos maioria no ENEM (também com um grande ppublico feminino).",
        "Em terceiro lugar de tamanho, o grupo 2 mostra os participantes negros (com grande quantidade de mulheres), sendo uma das raças mais presentes no Brasil segundo o IBGE.",
        "O abismo de quantidade do grupo 2 para o 1 e 3 é considerável, não condizendo com a diferença populacional deles, mostrando uma possível marginalização do grupo."
        "Cidadãos negros, mesmo que em grande quantidade, não estão tão presentes no concurso público quanto brancos ou pardos (indígenas também apareceram em número mínimo).",
    ]

    title = "Raça e Gênero - Lara"

    return get_image_to_flask(plt), text, title