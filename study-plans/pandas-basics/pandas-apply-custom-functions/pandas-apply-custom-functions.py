import pandas as pd

def apply_transform(data, column, operation):
    """
    Returns: dict with original columns plus column_transformed
    """
    df = pd.DataFrame(data)
    if(operation=='normalize'):
        df[f"{column}_transformed"] = df[column].apply(lambda x : round((x-min(df[column]))/(max(df[column]) - min(df[column])),4))
        return df.to_dict(orient='list')

    if(operation=='double'):
        df[f"{column}_transformed"] = df[column].apply(lambda x : x*2)
        return df.to_dict(orient='list')
    
    df[f"{column}_transformed"] = df[column].apply(operation)
    return df.to_dict(orient='list')    