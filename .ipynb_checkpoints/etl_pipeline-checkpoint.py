import pandas as pd
import numpy as np
import os 
import logging
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)


#Funcao de Extraçao do ETL
def extract(file_path):     
    try:
        logging.info("A extração de Dados do Arquivo Json foi feito com Sucesso!")
        return pd.read_json(file_path, orient = "columns")
      
    except FileNotFoundError as file_not_found:
        logging.error("")
    
        
    
        