from etl_pipeline import extract, transform, load
import pandas as pd
import pytest


# Build a unit test, asserting the type of clean_stock_data
@pytest.fixture()
def clean_data():
    raw_stock_data = extract("datasets/one_piece.json")
    clean_stock_data = transform()
    return clean_stock_data
    

  
def test_transformed_data(clean_data):
    assert isinstance(clean_stock_data, pd.DataFrame)



    

    
    