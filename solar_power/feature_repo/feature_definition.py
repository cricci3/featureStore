# Importing dependencies
from feast import Entity, Field, FeatureView, FileSource, ValueType
from feast.types import Float32, Int64, String
from datetime import timedelta

# Declaring an entity for the dataset
sensor_data = Entity(
    name="DATA_ID",
    value_type=ValueType.INT64,
    description="The ID of the sensor data")

# Declaring the source of the first set of features
f_source1 = FileSource(
    path=r"data/data_df1.parquet",
    event_timestamp_column="DATA_TIME"
)

# Defining the first set of features
df1_fv = FeatureView(
    name="df1_feature_view",
    ttl=timedelta(days=2000),
    entities=[sensor_data],
    schema=[
        Field(name="PLANT_ID", dtype=Int64),
        Field(name="SOURCE_KEY", dtype=String)
    ],
    source=f_source1
)

# Declaring the source of the second set of features
f_source2 = FileSource(
    path=r"data/data_df2.parquet",
    event_timestamp_column="DATA_TIME"
)

# Defining the second set of features
df2_fv = FeatureView(
    name="df2_feature_view",
    ttl=timedelta(days=2000),
    entities=[sensor_data],
    schema=[
        Field(name="DC_POWER", dtype=Float32),
        Field(name="AC_POWER", dtype=Float32)
    ],
    source=f_source2
)

# Declaring the source of the third set of features
f_source3 = FileSource(
    path=r"data/data_df3.parquet",
    event_timestamp_column="DATA_TIME"
)

# Defining the third set of features
df3_fv = FeatureView(
    name="df3_feature_view",
    ttl=timedelta(days=2000),
    entities=[sensor_data],
    schema=[
        Field(name="DAILY_YIELD", dtype=Float32),
        Field(name="TOTAL_YIELD", dtype=Float32)
    ],
    source=f_source3
)

# Declaring the source of the targets
target_source = FileSource(
    path=r"data/target_df.parquet",
    event_timestamp_column="DATA_TIME"
)

# Defining the targets
target_fv = FeatureView(
    name="target_feature_view",
    entities=[sensor_data],
    ttl=timedelta(days=2000),
    schema=[
        Field(name="TARGET", dtype=Int64)
        ],
    source=target_source
)
