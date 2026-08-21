import pandas as pd

def concat_dataframes(dfs):
    """
    Returns: list [shape, data] where shape is [rows, cols]
    """
    df = [pd.DataFrame(d) for d in dfs]
    res = pd.concat(df,axis=0,ignore_index=True).reset_index(drop=True)
    shape = list(res.shape)
    return [shape,res.to_dict(orient='list')]