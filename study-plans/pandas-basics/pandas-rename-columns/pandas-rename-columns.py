import pandas as pd

def rename_columns(data, rename_map):
    """
    Returns: dict mapping renamed column names to value lists
    """
    return pd.DataFrame(data).rename(columns=rename_map).to_dict(orient='list')