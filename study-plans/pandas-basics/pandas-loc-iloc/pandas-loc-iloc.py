import pandas as pd

def iloc_selection(data, row, col):
    """
    Returns: list [element, row_values, col_values]
    """
    df = pd.DataFrame(data)
    element = df.iloc[row,col]
    row_values = df.iloc[row].values.tolist()
    col_values = df.iloc[:,col].values.tolist()
    return [element,row_values,col_values]