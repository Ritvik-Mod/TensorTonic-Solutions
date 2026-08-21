import pandas as pd

def create_pivot(data, index, columns, values, aggfunc):
    """
    Returns: nested dict {column_value: {index_value: agg_result}}
    """
    df = pd.DataFrame(data)
    df = df.pivot_table(index=index,columns=columns,values=values,aggfunc=aggfunc)
    df = df.fillna(0)
    return df.to_dict()