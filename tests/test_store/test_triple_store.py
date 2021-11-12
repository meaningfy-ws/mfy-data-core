
from mfy_data_core_fakes.adapters.fake_storage import FakeTripleStore


def test_triple_store():
    triple_store = FakeTripleStore()
    tmp_store = triple_store.with_query(sparql_query="Use SPARQL query")
    assert type(tmp_store) == FakeTripleStore
    assert tmp_store == triple_store
    tmp_df = tmp_store.get_dataframe()
    assert tmp_df is not None
