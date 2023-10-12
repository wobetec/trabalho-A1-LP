import matplotlib.pyplot as plt
import pandas as pd
import base64
from io import BytesIO

def get_image_to_flask() -> str:
    """
    Transforma a figura do matplotlib em uma sequência de bytes para ser usada no Flask e retorna a tag imagem já com esses bytes

        Parametros:

        Returns:
            image (str): Tag imagem com os bytes da figura
    
    """
    buf = BytesIO()
    plt.savefig(buf, format='png')
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"

def esdras(df: pd.DataFrame) -> tuple:
    """
    Estrutura padrão com a visualização do Esdras

        Parametros:
            df (pd.DataFrame): DataFrame com os dados

        Returns:
            image (str): Tag imagem com os bytes da figura
            text (list): Lista com os textos para serem exibidos na página
            title (str): Título da visualização
    
    """
    df["media"] = (df["NU_NOTA_CH"] + df["NU_NOTA_CN"] + df["NU_NOTA_LC"] + df["NU_NOTA_MT"] + df["NU_NOTA_REDACAO"])/5

    amostra = df[["media", "Q006"]].groupby("Q006").mean().sort_values(by="media", ascending=True).reset_index()

    plt.bar(amostra["Q006"], amostra["media"])
    plt.xlabel('Renda Familiar')
    plt.ylabel('Média das Notas')
    plt.title('Comparação de Renda e Notas')

    text = [
        "Primeiramente, vale ressaltar que A é nenhuma renda familiar e Q é mais de 20 salários mínimos, que no ano em questão valia R$ 1212,00.",
        "Podemos ver que a renda familiar influencia diretamente na média das notas, quanto maior a renda maior a média das notas.",
        "Tal efeito pode ser relacionado com a qualidade de ensino, público e privado. Mostrando a desigualdade social no Brasil, onde a renda familiar influencia diretamente na qualidade de ensino.",
    ]

    title = "Renda e Nota - Esdras"

    return get_image_to_flask(), text, title


def get_all_vis(df: pd.DataFrame) -> list:
    """
    Retorna uma lista com todas as visualizações, de cada membro

        Parametros:
            df (pd.DataFrame): DataFrame com os dados

        Returns:
            vis (list): Lista com todas as visualizações
    
    """
    vis = []

    vis.append(esdras(df))

    return vis
