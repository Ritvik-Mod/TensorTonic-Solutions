import pandas as pd

def inspect_dataframe(data):
    """
    Returns: dict with 'rows', 'cols' (ints), 'columns' (list),
    'dtypes' (dict), 'total_values' (int)
    """
    df = pd.DataFrame(data)
    collist = df.columns.tolist()
    rows = df.shape[0]
    cols = df.shape[1]
    dt = df.dtypes.astype('str').to_dict()
    total_values = rows*cols
    return {'rows':rows, 'cols':cols, 'columns':collist, 'dtypes':dt, 'total_values':total_values}