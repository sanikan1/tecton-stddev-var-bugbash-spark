from tecton import FileConfig, BatchSource

demo_data_file_ds = FileConfig(uri="s3://tecton.ai.dev/sanika/stddev_var_spark_data.parquet",
                                    file_format="parquet",
                                    timestamp_field="timestamp")

demo_data_batch = BatchSource(name="demo_data_batch",
                                       batch_config=demo_data_file_ds)
