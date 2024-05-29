import pytest
from feast import FeatureStore
import pandas as pd

@pytest.fixture
def feature_store():
    return FeatureStore(repo_path=".")

def test_feature_values(feature_store):
    entity_df = pd.DataFrame.from_dict({
        "customer_id": [1001, 1002],
        "event_timestamp": [pd.Timestamp("2023-05-27"), pd.Timestamp("2023-05-27")]
    })

    feature_vectors = feature_store.get_online_features(
        features=[
            "customer_feature_view:feature1",
            "customer_feature_view:feature2",
        ],
        entity_rows=entity_df
    ).to_dict()

    assert feature_vectors["feature1"] == [expected_value1, expected_value2]
    assert feature_vectors["feature2"] == [expected_value3, expected_value4]
