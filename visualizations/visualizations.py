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
    Seguindo a estrutura padrão definida, esta função gera uma visualização comparando a influência da renda familiar na média das notas do enem.

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
    cross_tab = pd.crosstab(df['Q006'], df['TP_FAIXA_ETARIA'])

    ax = cross_tab.plot(kind='bar', stacked=True, colormap='viridis')

    plt.xlabel('Renda Familiar')
    plt.ylabel('Contagem')
    plt.title('Distribuição da Faixa Etária pela Renda Familiar - Angelo')
    ax.legend(title='Faixa Etária', loc='center left', bbox_to_anchor=(1.0, 0.5))
    plt.ticklabel_format(style='plain', axis='y')


    text = [
        "Observamos que, em algumas situações, pessoas com recursos financeiros limitados optam por realizar a prova após a idade média esperada.",
        "A desigualdade social desempenha um papel crucial no acesso à educação de qualidade, e essa visualização ressalta a complexidade das decisões educacionais em um contexto de desigualdade.",
        "A análise destaca a necessidade contínua de promover a equidade educacional e combater a desigualdade no acesso à educação."
        "A crítica sugere que a falta de oportunidade de estudos por conta da renda familiar acarreta no tardio ingresso no mercado de trabalho."
    ]

    title = "Oportunidade de Estudo - Angelo"

    return get_image_to_flask(), text, title


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
    vis.append(angelo(df))

    return vis
