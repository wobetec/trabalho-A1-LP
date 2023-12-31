"""
Esse arquivo contém as listas e dicionários referentes aos dados. Como por exemplo os nomes dos aquivos .csv, as colunas que serão utilizadas e as equivalências entre os códigos e os valores reais do dataset utilizado.
"""

FILE_NAMES = {
    "full_file": "MICRODADOS_ENEM_2022",
    "small_file": "microdados_resumidos",
}

USED_COLUMNS = (
    [  # Colunas do dataset original que serão utilizadas para gerar o dataset menor
        "TP_FAIXA_ETARIA",  # faixa etária
        "TP_SEXO",  # sexo
        "TP_ESTADO_CIVIL",  # estado civil
        "TP_COR_RACA",  # cor/raça
        "TP_ST_CONCLUSAO",  # situação de conclusão do ensino médio
        "TP_ANO_CONCLUIU",  # ano de conclusão do ensino médio
        "TP_ESCOLA",  # tipo de escola do ensino médio
        "IN_TREINEIRO",  # é treineiro?
        "SG_UF_PROVA",  # estado de prova
        "TP_PRESENCA_CN",  # presença na prova de ciências da natureza
        "TP_PRESENCA_CH",  # presença na prova de ciências humanas
        "TP_PRESENCA_LC",  # presença na prova de linguagens e códigos
        "TP_PRESENCA_MT",  # presença na prova de matemática
        "NU_NOTA_CN",  # nota da prova de ciências da natureza
        "NU_NOTA_CH",  # nota da prova de ciências humanas
        "NU_NOTA_LC",  # nota da prova de linguagens e códigos
        "NU_NOTA_MT",  # nota da prova de matemática
        "TP_LINGUA",  # língua estrangeira
        "TP_STATUS_REDACAO",  # status da redação
        "NU_NOTA_COMP1",  # nota da competência 1 da redação
        "NU_NOTA_COMP2",  # nota da competência 2 da redação
        "NU_NOTA_COMP3",  # nota da competência 3 da redação
        "NU_NOTA_COMP4",  # nota da competência 4 da redação
        "NU_NOTA_COMP5",  # nota da competência 5 da redação
        "NU_NOTA_REDACAO",  # nota da redação
        "Q005",  # quantidade de pessoas que moram na residência
        "Q006",  # renda mensal familiar
        "Q019",  # televisão a cores?
        "Q021",  # tv por assinatura?
        "Q022",  # telefone celular?
        "Q024",  # computador?
        "Q025",  # internet?
    ]
)

DICT_TP_FAIXA_ETARIA = {
    1: (0, 16),
    2: (17, 17),
    3: (18, 18),
    4: (19, 19),
    5: (20, 20),
    6: (21, 21),
    7: (22, 22),
    8: (23, 23),
    9: (24, 24),
    10: (25, 25),
    11: (26, 30),
    12: (31, 35),
    13: (36, 40),
    14: (41, 45),
    15: (46, 50),
    16: (51, 55),
    17: (56, 60),
    18: (61, 65),
    19: (66, 70),
    20: (71, 100),
}

DICT_TP_SEXO = {
    "M": "Masculino",
    "F": "Feminino",
}

DICT_TP_ESTADO_CIVIL = {
    0: "Não informado",
    1: "Solteiro(a)",
    2: "Casado(a)/Mora com companheiro(a)",
    3: "Divorciado(a)/Desquitado(a)/Separado(a)",
    4: "Viúvo(a)",
}

DICT_TP_COR_RACA = {
    0: "Não declarado",
    1: "Branca",
    2: "Preta",
    3: "Parda",
    4: "Amarela",
    5: "Indígena",
    6: "Não dispõe da informação",
}
