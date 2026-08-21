import pandas as pd

def cross_tab(data, row_col, col_col):
    """
    Returns: nested dict {col_value: {row_value: frequency}}
    """
    df = pd.DataFrame(data)
    return pd.crosstab(df[row_col],df[col_col]).to_dict()