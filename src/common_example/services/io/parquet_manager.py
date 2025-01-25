class ParquetManager:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self):
        import pandas as pd

        return pd.read_parquet(self.file_path)

    def write(self, df):
        df.to_parquet(self.file_path, index=False)
