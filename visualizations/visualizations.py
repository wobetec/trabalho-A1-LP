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

def romolo(df: pd.DataFrame) -> tuple:
    """"
    EStrutura de visualização do Romolo
        Parametros:
            DataFrame com subset de microdados do ENEN : df (PANDAS Dataframe)

        Returns:
            Imagem com 3 facets, Texto com analise dos graficos e o titulo do grafico

    """
    plt.style.use("ggplot")
    plt.figure(figsize = (25,10))
                    

    #PLOT DE SEXO
    plt.subplot(1,3,1)

    contagem_sexo = df["TP_SEXO"].value_counts()
    total = contagem_sexo.sum()

    dict_sexo = {"F":"Feminino","M":"Masculino"}

    cores = ["blue", "red"]

    percentuais = [(valor / total) * 100 for valor in contagem_sexo]

    rotulos = [dict_sexo.get(valor, valor) for valor in contagem_sexo.index]
    plt.bar(rotulos, contagem_sexo, ec="black", color=cores)

    for i, valor in enumerate(contagem_sexo):
        plt.text(i, valor, f"{percentuais[i]:.2f}%", ha='center', va='bottom')

    plt.bar(rotulos, contagem_sexo, ec="black", color=cores)
    plt.xlabel("Sexo Declarado")
    plt.ylabel("contagem")


    #PLOT ESTADO CIVIL
    plt.subplot(1,3,2)

    contagem_est_civil = df["TP_ESTADO_CIVIL"].value_counts()
    total = contagem_est_civil.sum()

    dict_estado_civil = {
        0: "Não informado",
        1: "Solteiro(a)",
        2: "Casado(a)/Mora com companheiro(a)",
        3: "Divorciado(a)/Desquitado(a)/Separado(a)",
        4: "Viúvo(a)"
    }

    cores = ["blue", "red", "green", "orange", "purple"]

    percentuais = [(valor / total) for valor in contagem_est_civil]

    contagem_est_civil = contagem_est_civil.sort_values(ascending=False)
    percentuais = [(valor / total) for valor in contagem_est_civil]

    rotulos = [dict_estado_civil.get(valor, valor) for valor in contagem_est_civil.index]

    plt.bar(rotulos, percentuais, ec="black", color=cores)
    plt.xlabel("Estado Civil")
    plt.ylabel("Porcentagem")

    plt.xticks(rotation=45)

    plt.title("Distribuição de Estado Civil")

    for i, valor in enumerate(percentuais):
        plt.text(i, valor, f"{valor*100:.2f}%", ha='center', va='bottom')

    plt.show()

    #PLOT COR/RAÇA

    contagem_cor_raca = df["TP_COR_RACA"].value_counts()
    total = contagem_cor_raca.sum()

    dict_cor_raca = {
        0: "Não declarado",
        1: "Branca",
        2: "Preta",
        3: "Parda",
        4: "Amarela",
        5: "Indígena",
        6: "Não dispõe da informação"
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
        plt.text(i, valor, f"{valor*100:.2f}%", ha='center', va='bottom')

    plt.show()
    
                    
    text = ["Foram utilizados variáveis que demomstram a demografica dos indivíduos que realizaram a prova do ENEN no ano de 2022."
            "Na atualidade, o jovem que se submete a prova do ENEN é do sexo feminino (61%), solteira (90%) se auto-declarando parda e branca (80%)."
            "O que talvez seja o mais importante notar é que temos um baixo indice de negro e indios, fato relevenate que deve ser usado nas políticas"
            "públicas de promoção a educação"]
    
    title = ["Perfil Demográfico dos participantes do ENEN 2022 - Romolo"]

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
    vis.append(romolo(df))
    return vis
