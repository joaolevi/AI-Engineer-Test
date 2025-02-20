import pandas as pd

def read_csv_to_dataframe(file_path: str) -> pd.DataFrame:
    """
    Lê um arquivo CSV e o converte em um DataFrame do pandas.

    :param file_path: Caminho do arquivo CSV.
    :return: DataFrame do pandas contendo os dados do CSV.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV: {e}")
        return None

def read_xlsx_to_dataframe(file_path: str, sheet_name=0) -> pd.DataFrame:
    """
    Lê um arquivo Excel (XLSX) e o converte em um DataFrame do pandas.

    :param file_path: Caminho do arquivo XLSX.
    :param sheet_name: Nome ou índice da planilha a ser lida (padrão: primeira planilha).
    :return: DataFrame do pandas contendo os dados da planilha Excel.
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        return df
    except Exception as e:
        print(f"Erro ao ler o arquivo XLSX: {e}")
        return None
