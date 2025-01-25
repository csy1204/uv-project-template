class DeltaLakeManager:
    def __init__(self, spark, delta_table_path: str):
        self.spark = spark
        self.delta_table_path = delta_table_path

    def read_table(self):
        return self.spark.read.format("delta").load(self.delta_table_path)

    def write_table(self, df):
        df.write.format("delta").mode("overwrite").save(self.delta_table_path)

    def append_table(self, df):
        df.write.format("delta").mode("append").save(self.delta_table_path)

    def update_table(self, df, condition: str):
        df.createOrReplaceTempView("updates")
        self.spark.sql(
            f"MERGE INTO delta.`{self.delta_table_path}` AS target USING updates AS source ON {condition} WHEN MATCHED THEN UPDATE SET * WHEN NOT MATCHED THEN INSERT *"
        )

    def delete_table(self, condition: str):
        self.spark.sql(f"DELETE FROM delta.`{self.delta_table_path}` WHERE {condition}")
