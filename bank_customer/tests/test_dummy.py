import pytest
from feast import FeatureStore
# Inizializza il client del Feature Store con il percorso corretto al tuo repository
feature_store = FeatureStore(repo_path=".")

def test_data_loading():
    try:
        # Specifica una query di esempio per controllare i dati
        data = feature_store.get_online_features(
            feature_refs=["df1_feature_view:Gender", "df2_feature_view:CreditScore"],
            entity_rows=[{"USER_ID": 1}]
        )
        assert data is not None
        assert len(data) > 0
    except Exception as e:
        pytest.fail(f"Data loading failed: {e}")
import time

def test_feature_validation():
    consumer_id = 1
    entity_rows = [{"USER_ID": consumer_id}]
    features = feature_store.get_online_features(
        feature_refs=["df1_feature_view:Gender", "df2_feature_view:CreditScore"],
        entity_rows=entity_rows
    )
    for feature_name in ["df1_feature_view:Gender", "df2_feature_view:CreditScore"]:
        assert isinstance(features[feature_name].values[0], int), f"Feature {feature_name} is not of type int"

def test_teardown():
    try:
        feature_store.teardown()
        assert True
    except Exception as e:
        pytest.fail(f"Teardown failed: {e}")
