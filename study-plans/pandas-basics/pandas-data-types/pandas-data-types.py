import pandas as pd

def data_types_overview(data):
    """
    Returns: dict with 'dtypes', 'type_counts', 'num_columns'
    """
    df = pd.DataFrame(data)
    cols = df.shape[1]
    dt = df.dtypes.astype('str').to_dict()
    tc = df.dtypes.astype('str').value_counts().to_dict()
    return {'dtypes':dt, 'type_counts':tc, 'num_columns':cols}