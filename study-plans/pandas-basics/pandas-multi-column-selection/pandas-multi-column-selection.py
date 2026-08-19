import pandas as pd

def select_columns(data, columns):
    """
    Returns: dict mapping selected column names to value lists
    """
    return pd.DataFrame(data)[columns].to_dict(orient='list')