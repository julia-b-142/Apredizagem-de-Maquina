# Definições e funções para todos os exemplos
# encoding: iso-8859-1

from datetime import datetime
import random



# Ajustando a localização para o Brasil
import os
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR')
from datetime import datetime
import pytz

import pandas as pd

# Define o fuso horário para o Brasil (Brasília)
con_fuso_horario = pytz.timezone("America/Sao_Paulo")

conSeparador= "\nXXXXXXXXXXXXX---XXXXXXXXXXXXX\n"

# Função formatar tempo de execução (dado tempo de inicio e fim, retorna h:m:milisegundos formatado)
def formata_tempo_execucao (dttInicio, dttfim):
    strTempo = dttfim - dttInicio
    str_tempo_execucao_formatado = "{:02d}:{:02d}.{:06d}".format(
    strTempo.seconds // 60,  # Minutos
    strTempo.seconds % 60,  # Segundos
    strTempo.microseconds  # Microsegundos
    )
    return str_tempo_execucao_formatado

def formata_data(dttParametro):
  return dttParametro.strftime("%d/%m/%Y - %H:%M:%S.%f")

def formata_numero(numero):
    return locale.format_string("%d", numero, grouping=True)

# Cria um array do tamanho intElementosArray, valores inteiros entre intMin e intMax)
def montar_array (intElementosArray,intMin, intMax):
  x = 0
  array = []
  while x < intTamArray:
    intElementosArray = random.randint(intMin,intMax)
    array.append (intElementosArray)
    x += 1
  return (array)

def ler_inteiro (strMensagem):
  while True:
    try:      # Se nenhuma exceção ocorrer, a cláusula except é ignorada e a execução da instrução try é finalizada
      tamanho = int(input(strMensagem))
      break  # Se a entrada for válida, sai do loop e finaliza o programa
    except ValueError:
      print("Erro: Por favor, digite um número inteiro valido.")
  return tamanho


def carregar_array():
    arrMeuArray = []
    while True:
        entrada = input("Digite um número inteiro para o array (-1 para sair): ")
        try:
            numero = int(entrada)
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
            continue
        if numero == -1:
            break
        arrMeuArray.append(numero)
        print (f"O array atual tem {str(len(arrMeuArray))}. Seu conteúdo é \n")
        print (arrMeuArray)
    return arrMeuArray

def marcar_inicio (strMensagem):
  dttInicio = datetime.now(con_fuso_horario)
  dttInicioFormatado = formata_data(dttInicio)
  print(f"Iniciando {strMensagem} as : " + str(dttInicioFormatado))
  return dttInicio

def marcar_fim (strMensagem):
  dttFim = datetime.now(con_fuso_horario)
  dttFimFormatado = formata_data (dttFim)
  print(f"Finalizando {strMensagem} as : " + str(dttFimFormatado))
  return dttFim

def ler_arquivo_csv_para_lista(nome_arquivo):
    try:
        dados = pd.read_csv(nome_arquivo)
        return dados.values.tolist()  # Converte o DataFrame para uma lista de listas
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        return None

# Importar os módulos do sistema operacional
import os
import locale

# Instalar pt_BR
!/usr/share/locales/install-language-pack pt_BR
!dpkg-reconfigure locales pt_BR

# Reiniciar o processo Python
os.kill(os.getpid(), 9)

