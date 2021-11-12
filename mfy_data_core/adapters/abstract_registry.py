

from abc import ABC, abstractmethod

from mfy_data_core.adapters.abstract_store import FeatureStoreABC, IndexStoreABC, ObjectStoreABC, TripleStoreABC


class StoreRegistryABC(ABC):

    @abstractmethod
    def es_index_store(self) -> IndexStoreABC:
        raise NotImplementedError

    @abstractmethod
    def minio_object_store(self, minio_bucket: str) -> ObjectStoreABC:
        raise NotImplementedError

    @abstractmethod
    def es_feature_store(self) -> FeatureStoreABC:
        raise NotImplementedError

    @abstractmethod
    def minio_feature_store(self) -> FeatureStoreABC:
        raise NotImplementedError

    @abstractmethod
    def sparql_triple_store(self, endpoint_url: str) -> TripleStoreABC:
        raise NotImplementedError
    
