import pandas as pd

def drop_duplicates(data):
    """
    Returns: list [rows_before, rows_after, cleaned_data]
    """
    df = pd.DataFrame(data)
    rows_before = df.shape[0]

    cleaned_data = df.drop_duplicates(keep='first')
    
    rows_after = cleaned_data.shape[0]

    return [rows_before,rows_after,cleaned_data.to_dict(orient='list')]