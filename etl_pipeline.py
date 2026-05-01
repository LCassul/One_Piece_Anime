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
    
        
    
        