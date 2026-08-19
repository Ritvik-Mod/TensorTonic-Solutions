import pandas as pd

def set_index_column(data, index_col):
    """
    Returns: dict with 'index_values', 'columns', 'data'
    """
    df = pd.DataFrame(data)
    df = df.set_index(index_col)
    dat = df.to_dict(orient='list')
    cols = df.columns.tolist()
    ind = df.index.tolist()

    return {'index_values':ind, 'columns':cols, 'data':dat}