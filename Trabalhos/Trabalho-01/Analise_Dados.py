import pandas as pd
import matplotlib.pyplot as plt
import os

#Tratamento de erros dos arquivos
def analise_student_data(file_path):
    try:
         # Verifica se o caminho do arquivo realmente existe no sistema
        if not os.path.exists(file_path):
            # Lança uma exceção se o arquivo não for encontrado
            raise FileNotFoundError("O arquivo não foi encontrado")

         # Verifica se o arquivo é do tipo CSV
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        
        # Se não for CSV, verifica se é JSON
        elif file_path.endswith(".json"):
            df = pd.read_json(file_path)
            
        # Se o formato do arquivo não for suportado, lança um erro
        else:
            raise ValueError("Formato inválido! Use arquivos .CSV ou .JSON")
        
        # Requisito 1 do Trabalho - Resumo das Informações
        quant_dados = len(df)
        quant_masculino = len(df[df['Gender'] == 'Male'])
        quant_feminino = len(df[df['Gender'] == 'Female'])
        sem_educacao_parental = df['Parent_Education_Level'].isnull().sum()

        print(f"Quantidade de dados carregados: {quant_dados}") #diminuir 1 dos registros
        print(f"Quantidade de homens: {quant_masculino}")
        print(f"Quantidade de mulheres: {quant_feminino}")
        print(f"Quantidade de registros sem dados sobre a educação dos pais: {sem_educacao_parental}")
        
        # Requisito 2 - Limpeza de dados
        df.dropna(subset=['Parent_Education_Level'], inplace=True)
        df['Attendance (%)'] = df['Attendance (%)'].fillna(df['Attendance (%)'].median())
        total_attendance = df['Attendance (%)'].sum()
        print(f"Total Attendance: {total_attendance:.2f}")

        
    # Captura erros relacionados a caminho inválido ou formato de arquivo incorreto
    except (FileNotFoundError, ValueError) as e:
        print(f"\nErro: {e}")

#  Verifica se o script está sendo executado diretamente pelo Python
if __name__ == "__main__":
  
  # Solicita ao usuário que informe o caminho do arquivo de dados (CSV ou JSON)
  file_path = input("Entre com o caminho do arquivo: ")
  # Chama a função principal passando o caminho do arquivo informado
  analise_student_data(file_path)
    
