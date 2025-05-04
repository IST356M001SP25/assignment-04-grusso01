
import pandas as pd

def get_column_names(df : pd.DataFrame) -> list[str]:
    return df.columns.tolist()


def get_columns_of_type(df : pd.DataFrame, numpy_type: any) -> list[str]:
   
    columns = []
    for col in df.columns:
        if df[col].dtype == numpy_type:
            columns.append(col)
    return columns


def get_unique_values(df : pd.DataFrame, column_name: str) -> list:

    return df[column_name].unique().tolist()

def get_file_extension(file_path : str) -> str:
 
    return file_path.split('.')[-1]

def load_file(file_path: str, ext: str) -> pd.DataFrame:

    if ext == 'csv':
        return pd.read_csv(file_path, header=0)
    elif ext == 'xlsx':
        return pd.read_excel(file_path)
    elif ext == 'json':
        return pd.read_json(file_path, orient='records')
    else:
        return None

if __name__ == '__main__':
    df = pd.DataFrame({ 
        "name": ["Alice", "Bob", "Chris", "Dee", "Eddie", "Fiona"],
        "age": [25, 30, 35, 40, 45, 50],
        "state": ["NY", "PA", "NY", "NY", "PA", "NJ"],
        "balance": [100.0, 200.0, 250.0, 310.0, 100.0, 60.0]
        })
    cols = get_column_names(df)
    print(f"Columns: {cols}")
    cols = get_columns_of_type(df, 'object')
    print(f"Object Columns: {cols}")
    cols = get_columns_of_type(df, 'int64')
    print(f"Int64 Columns: {cols}")
    cols = get_columns_of_type(df, 'float64')
    print(f"Float64 Columns: {cols}")
    unique = get_unique_values(df, 'state')
    print(f"Unique States: {unique}")