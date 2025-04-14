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
        
    # Captura erros relacionados a caminho inválido ou formato de arquivo incorreto
    except (FileNotFoundError, ValueError) as e:
        print(f"\nErro: {e}")

    
