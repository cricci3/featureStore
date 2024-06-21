import pytest
from feast import FeatureStore
# Inizializza il client del Feature Store con il percorso corretto al tuo repository
feature_store = FeatureStore(repo_path="bank_customer//feature_repo")


def test_apply_feature_store():
    try:
        feature_store.apply([df1_fv, df2_fv, df3_fv, df4_fv, target_fv])
        assert True
    except Exception as e:
        pytest.fail(f"Feature Store apply failed: {e}")

def test_materialize_features():
    try:
        feature_store.materialize_incremental(datetime.now().isoformat())
        assert True
    except Exception as e:
        pytest.fail(f"Materialization failed: {e}")

def test_feature_extraction(setup_feature_store):
    consumer_id = 1
    entity_rows = [{"USER_ID": consumer_id}]
    features = feature_store.get_online_features(
        feature_refs=["df1_feature_view:Gender", "df2_feature_view:CreditScore"],
        entity_rows=entity_rows
    )
    assert features["df1_feature_view:Gender"].values[0] is not None
    assert features["df2_feature_view:CreditScore"].values[0] is not None

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

def test_feature_extraction_performance(setup_feature_store):
    consumer_id = 1
    entity_rows = [{"USER_ID": consumer_id}]
    start_time = time.time()
    try:
        features = feature_store.get_online_features(
            feature_refs=["df1_feature_view:Gender", "df2_feature_view:CreditScore"],
            entity_rows=entity_rows
        )
        elapsed_time = time.time() - start_time
        assert elapsed_time < 1, f"Feature extraction took too long: {elapsed_time}s"
        assert features["df1_feature_view:Gender"].values[0] is not None
        assert features["df2_feature_view:CreditScore"].values[0] is not None
    except Exception as e:
        pytest.fail(f"Feature extraction failed: {e}")

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
