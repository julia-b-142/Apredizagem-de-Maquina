# Descrição do Trabalho

O grupo deverá desenvolver um analisador de dados que carregue,
processe e visualize informações de um conjunto de dados fornecido*.

O sistema deve ser implementado em Python, utilizando as bibliotecas
Pandas para manipulação de dados e Matplotlib para visualização gráfica.
O trabalho deverá seguir o padrão de desenvolvimento PEP 8 – Style Guide
for Python Code (referência) (1 ponto).

https://www.kaggle.com/datasets/mahmoudelhemaly/students-grading-da
taset

# Requisitos do Projeto – Itens:

## O programa deve permitir o carregamento de um arquivo CSV ou JSON com dados de alunos (students-grading-dataset). (1
ponto)

Perguntar ao usuário o caminho do arquivo

O usuário deve poder visualizar um resumo estatístico dos dados carregados.
Quantidade de dados carregados
Quantidade de homens e mulheres
Quantos registros sem dados sobre a educação dos pais.


## Limpeza de dados (3 pontos)

Remover os registros que tem a educação dos pais vazios.
Alterar os dados de presença (Attendance) que estão null para a mediana.
Apresentar o somatório de Attendance.


## Consulta a dados (2 pontos)

O usuário pode escolher uma das colunas e o sistema deve apresentar: média, mediana, moda, desvio padrão dos dados daquela coluna.


## Gráficos (3 pontos)

O sistema deve produzir gráfico de dispersão para “horas de sono” x “nota final”
Gráfico de barras – idade x média das notas intermediárias (midterm_Score)
Gráfico de pizza para as idades (Agrupadas: até 17; 18 a 21; 21 a 24; 25 ou mais).


O sistema que não importar os dados OU travar durante a execução do código,
seja por bug ou por não validação de entrada de usuário – 0 PONTOS.
Validar, entre outros, se o caminho do arquivo existe, se a coluna para a qual se está
pedindo as médias, modas... É uma coluna numérica.


## Pontos extras (o máximo de pontos do trabalho é 10! Se passar, fica com apenas
com 10)

1 ponto: Documentação utilizando docstrings.

O resultado deve ser apresentado utilizando o Sphinx, pydoc ou MkDocs.
0,1 ponto para cada função que tiver controle de erro (máximo 1 ponto).
1 ponto se o sistema tiver um log de ações do usuário (todas).

Nesse caso deve pedir o nome do usuário como entrada (nesse caso não precisa ter crítica, exceto se é
um nome composto APENAS por caracteres, com ao menos 3. Os nomes podem ser duplicados).

1 ponto se o git do projeto “contar” a história da evolução. Com commits de todos alunos,
evoluções, controle de bugs, etc...




