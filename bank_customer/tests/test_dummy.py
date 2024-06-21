import pytest
from datetime import datetime
from feast import FeatureStore

# Inizializza il client del Feature Store
feature_store = FeatureStore(repo_path=r"bank_customer/feature_repo")

@pytest.fixture(scope="module")
def setup_feature_store():
    # Applica le definizioni delle feature nel Feature Store
    feature_store.apply([df1_fv, df2_fv, df3_fv, df4_fv, target_fv])
    yield
    # Clean up dopo i test
    feature_store.teardown()

def test_feature_extraction(setup_feature_store):
    # Esempio di consumer_id
    consumer_id = 1
    entity_rows = [{"USER_ID": consumer_id}]

    # Estrai le feature per il consumatore specificato
    features = feature_store.get_online_features(
        feature_refs=["df1_feature_view:Gender", "df2_feature_view:CreditScore"],
        entity_rows=entity_rows
    )

    # Verifica che le feature estratte siano non vuote
    assert features["df1_feature_view:Gender"].values[0] is not None
    assert features["df2_feature_view:CreditScore"].values[0] is not None
