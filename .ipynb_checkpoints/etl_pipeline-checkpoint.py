import pandas as pd
import numpy as np
import os 
import logging
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)


#Funcao de Extraçao do ETL
def extract(file_path):     
    try:
      df = pd.read_json(file_path, orient = "columns")
      logging.info("A extração de Dados do Arquivo Json foi feito com Sucesso!")
      return df

    except FileNotFoundError as file_not_found:
        logging.error(f" Arquivo não encontrado - {file_not_found}")


# Funcao de Transformação do ETL

def transform():
    
    raw_one_piece = extract("datasets/one_piece.json")
    
    # Agora raw_dict é um dicionário puro!
    raw_dict = raw_one_piece.to_dict(orient='index')
    df_dict_data =  pd.DataFrame(raw_dict) 
    
    #for one_piece_id, one_piece_info in raw_dict.items():
       #  print(one_piece_id, ":", one_piece_info, "grams")
    return df_dict_data




# Funcao de Load do ETL

def load():
     
    stock_data = transform()
    # Guarda o ficheiro (não atribuas isto a uma variável)
    stock_data.to_csv("datasets/datos.csv", index=False) 
    
    # Retorna as primeiras linhas do DataFrame original
    return stock_data.head()


         

   



    

    
    