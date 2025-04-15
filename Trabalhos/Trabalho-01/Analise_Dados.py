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
        
        # Requisito 3 - Consulta de Dados
        colunas_numericas = [
            'Attendance (%)', 'Midterm_Score', 'Final_Score',
            'Assignments_Avg', 'Quizzes_Avg', 'Participation_Score',
            'Projects_Score', 'Total_Score', 'Study_Hours_per_Week',
            'Stress_Level', 'Sleep_Hours_per_Night'
        ]

        while True:
            print("\n--- MENU DE CONSULTA DE DADOS ---")
            for idx, coluna in enumerate(colunas_numericas, start=1):
                print(f"{idx}. {coluna}")
            print("0. Sair da consulta e continuar o programa")

            try:
                escolha = int(input("Selecione o número da coluna para análise: "))
                if escolha == 0:
                    break
                elif 1 <= escolha <= len(colunas_numericas):
                    coluna_selecionada = colunas_numericas[escolha - 1]
                    print(f"\nAnálise da Coluna: {coluna_selecionada}")
                    print(f"Média: {df[coluna_selecionada].mean():.2f}")
                    print(f"Mediana: {df[coluna_selecionada].median():.2f}")
                    print(f"Moda: {df[coluna_selecionada].mode()[0]:.2f}")
                    print(f"Desvio Padrão: {df[coluna_selecionada].std():.2f}")
                else:
                    print("Opção inválida. Escolha um número válido.")
            except ValueError:
                print("Entrada inválida. Digite apenas números.")

        # Requisito 4 - Gráficos
            plt.figure(figsize=(10, 6))
            plt.scatter(df['Sleep_Hours_per_Night'], df['Total_Score'])
            plt.xlabel("Horas de Sono")
            plt.ylabel("Nota Final")
            plt.title("Gráfico de Dispersão: Horas de Sono X Nota Final")
            plt.show()

            plt.figure(figsize=(10, 6))
            df.groupby('Age')['Midterm_Score'].mean().plot(kind='bar')
            plt.xlabel("Idade")
            plt.ylabel("Média das Notas Intermediárias")
            plt.title("Gráfico de Barras: Idade X Média das Notas Intermediárias")
            plt.show()

            age_bins = [0, 17, 21, 24, float('inf')]
            age_labels = ['Até 17', '18 a 21', '22 a 24', '25 ou mais']
            df['Age Group'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels, right=False)
            age_group_counts = df['Age Group'].value_counts()
            plt.figure(figsize=(8, 8))
            plt.pie(age_group_counts, labels=age_group_counts.index, autopct='%1.1f%%', startangle=90)
            plt.title('Idades')
            plt.show()
                
    # Captura erros relacionados a caminho inválido ou formato de arquivo incorreto
    except (FileNotFoundError, ValueError) as e:
        print(f"\nErro: {e}")

#  Verifica se o script está sendo executado diretamente pelo Python
if __name__ == "__main__":
  
  # Solicita ao usuário que informe o caminho do arquivo de dados (CSV ou JSON)
  file_path = input("Entre com o caminho do arquivo: ")
  # Chama a função principal passando o caminho do arquivo informado
  analise_student_data(file_path)
    
