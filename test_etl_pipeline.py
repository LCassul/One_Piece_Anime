from etl_pipeline import extract, transform, load
import pandas as pd


# Build a unit test, asserting the type of clean_stock_data
def test_transformed_data():
    raw_stock_data = extract("datasets/one_piece.json")
    clean_stock_data = transform()
    assert isinstance(clean_stock_data, pd.DataFrame)

  

pipeline_type = "ETL"
# Create an AssertionError
assert isinstance(pipeline_type, str)  

   



    

    
    