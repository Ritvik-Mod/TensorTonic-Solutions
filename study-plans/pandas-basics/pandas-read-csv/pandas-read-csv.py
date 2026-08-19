import pandas as pd

def create_dataframe(data):
    """
    Returns: dict with 'data', 'shape', 'columns'
    """
    df = pd.DataFrame(data)
    data = df.to_dict('list')
    return {'data':data,'shape':list(df.shape),'columns':list(df.columns)}