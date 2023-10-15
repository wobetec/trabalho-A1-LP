# trabalho-A1-LP
Trabalho de A1 da disciplina de Linguagens de Programação EMAp 2023.2

Uma prévia do trabalho, isto é, a *página html estática gerada após toda a execução*, bem como a documentação dos módulos pode ser vista no [github pages](https://wobetec.github.io/trabalho-A1-LP/)


# Integrantes
* Esdras Cavalcanti de Almeida
* Lara Peclart Dalese
* Marcelo Angelo da Silva Filho
* Romolo Guida Junior


# Dados utilizados
Utilizamos os microdados do Enem 2022 que pode ser encontrado [aqui](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem).

O dataset escolhido é grande e o `.zip` original possui cerca de 700Mb, já o dataset em si tem por volta de 1.5Gb. 

Como gostamos dos dados e queriamos trabalhar com eles, pegamos o dataset orignal e removemos boa parte das colunas (as que consideramos menos relevantes para as análises que desejamos fazer). 

Ainda assim, ficamos com um arquivo de ~350Mb, maior que o limite de 100Mb do GitHub. 

Por isso criamos um módulo a mais responsável por fazer a compactação e descompactação desse arquivo para permitir salvá-lo no GitHub.

O módulo `data_work/size_manager.py` possui essa responsabilidade, bem como de cortar o arquivo original (função que só foi utilizada para gerar o dataset menor).


# Execução da aplicação

Ao executar o arquivo `main.py` ele se encarregará de fazer a descompactação dos dados, caso ainda não tenha sido feita previamente.

Esse driver code irá iniciar um servidor flask local, no qual serão mostradas as análises.

    python main.py

Com a ressalva de utilizar `python3` para o linux

Certifique-se de instalar os módulos do `requirements.txt`. O python utilizado foi o `3.11.5`.

# Execução dos testes

## UnitTest
Para executar os testes é possível rodar cara arquivo `test_*` em `/tests` ou podem ser executados todos de uma vez rodando:

    python ./tests/run_tests.py


## DocTest
Para executar os doctests basta rodar o arquivo `.py` dentro de `/doctest`:

    python .\doctest\run_tests.py


# Documentação
Para criar a documentação geramos os arquivos `.rst` com o comando

    sphinx-apidoc -o docs [module]

Depois utilizamos o seguinte comando dentro do diretório `\docs` para atualizar a documentação:

    make html

A documentação pode ser visualizada abrindo arquivo [index.html](docs/_build/html/index.html) ou através do [github pages](https://wobetec.github.io/trabalho-A1-LP/).


