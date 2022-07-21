from tecton import FileConfig, BatchSource

# declare a FileDSConfig, which can be used as a parameter to a `BatchDataSource`
demo_data_file_ds = FileConfig(uri="s3://tecton.ai.dev/sanika/test3.parquet",
                                    file_format="parquet",
                                    timestamp_field="timestamp")

# This FileDSConfig can then be included as an parameter a BatchDataSource declaration.
# For example,
demo_data_batch = BatchSource(name="demo_data_batch",
                                       batch_config=demo_data_file_ds)
