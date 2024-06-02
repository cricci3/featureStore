# Importing dependencies
from feast import Entity, Field, FeatureView, FileSource, ValueType,FeatureService
from feast.types import Float32, Int64, String, Float64, Bool
from datetime import timedelta

# Declaring an entity for the dataset
consumer_data = Entity(
    name="USER_ID",
    value_type=ValueType.INT64,
    description="The ID of the consumer")

# -----------------------------------------------------------------

# Declaring the source of the first set of features
f_source1 = FileSource(
    path=r"data/data_df1.parquet",
    event_timestamp_column="event_timestamp"
)

# Defining the first set of features
df1_fv = FeatureView(
    name="df1_feature_view",
    ttl=timedelta(days=2000),
    entities=[consumer_data],
    schema=[
        Field(name="Gender", dtype=Int64),
        Field(name="Age", dtype=Int64)
    ],
    source=f_source1
)

# -----------------------------------------------------------------

# Declaring the source of the second set of features
f_source2 = FileSource(
    path=r"data/data_df2.parquet",
    event_timestamp_column="event_timestamp"
)

# Defining the second set of features
df2_fv = FeatureView(
    name="df2_feature_view",
    ttl=timedelta(days=2000),
    entities=[consumer_data],
    schema=[
        Field(name="CreditScore", dtype=Int64),
        Field(name="Tenure", dtype=Int64),
        Field(name="Balance", dtype=Float64),
        Field(name="EstimatedSalary", dtype=Float64)
    ],
    source=f_source2
)

# -----------------------------------------------------------------

# Declaring the source of the third set of features
f_source3 = FileSource(
    path=r"data/data_df3.parquet",
    event_timestamp_column="event_timestamp"
)

# Defining the third set of features
df3_fv = FeatureView(
    name="df3_feature_view",
    ttl=timedelta(days=2000),
    entities=[consumer_data],
    schema=[
        Field(name="NumOfProducts", dtype=Int64),
        Field(name="HasCrCard", dtype=Int64),
        Field(name="IsActiveMember", dtype=Int64)
    ],
    source=f_source3
)

# -----------------------------------------------------------------

# Declaring the source of the fourth set of features
f_source4 = FileSource(
    path=r"data/data_df4.parquet",
    event_timestamp_column="event_timestamp"
)

# Defining the fourth set of features
df4_fv = FeatureView(
    name="df4_feature_view",
    ttl=timedelta(days=2000),
    entities=[consumer_data],
    schema=[
        Field(name="Geography_France", dtype=Bool),
        Field(name="Geography_Germany", dtype=Bool),
        Field(name="Geography_Spain", dtype=Bool)
    ],
    source=f_source4
)

# -----------------------------------------------------------------

# Declaring the source of the targets
target_source = FileSource(
    path=r"data/target_df.parquet",
    event_timestamp_column="event_timestamp"
)

# Defining the targets
target_fv = FeatureView(
    name="target_feature_view",
    entities=[consumer_data],
    ttl=timedelta(days=2000),
    schema=[
        Field(name="Exited", dtype=Int64)
        ],
    source=target_source
)

churn_features = FeatureService(
    name="user_activity",
    features=[df1_fv, df2_fv,df3_fv,df4_fv],
    tags={"Description": "Used for training a RandomForest and a  Logistic Regression model"}
)