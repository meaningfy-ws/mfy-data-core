from typing import List
import hvac
import json
import os
import dotenv
dotenv.load_dotenv(verbose=True, override=True)


from mfy_data_core.adapters.abstract_store import SecretsStoreABC


class VaultSecretsStore(SecretsStoreABC):

    default_vault_addr : str = os.environ.get('VAULT_ADDR')
    default_vault_token : str = os.environ.get('VAULT_TOKEN')
    default_secret_mount : str = None
    default_secret_paths : List[str] = None
    
    def __init__(self,
                 vault_addr: str = None,
                 vault_token: str = None,
                 secret_mount: str = None,
                 secret_paths: List[str] = None
                 ):
        self._vault_addr = vault_addr if vault_addr else self.default_vault_addr
        self._vault_token = vault_token if vault_token else self.default_vault_token
        self._secret_mount = secret_mount if secret_mount else self.default_secret_mount
        self._secret_paths = secret_paths if secret_paths else self.default_secret_paths
        self._client = hvac.Client(url=self._vault_addr, token=self._vault_token)

    def get_secrets(self, path: str) -> dict:
        secret_response = self._client.secrets.kv.v2.read_secret_version(
            path=path, mount_point=self._secret_mount)
        result_data_str = str(secret_response['data']['data'])
        result_data_json = result_data_str.replace("'", "\"")
        result_data = json.loads(result_data_json)
        return result_data

    def get_secret(self, secret_key: str, default_value: str = None):
        """
            This method extracts from the vault of a secret based on the name of the secret.
        :param secret_key: the name of the secret sought.
        :param default_value: the default return value in case the secret is not found.
        :return:
        """
        
        secrets_dict = {}
        for path in self.secret_paths:
            secrets_dict.update(self.get_secrets(path))
        if secret_key in secrets_dict.keys():
            return secrets_dict[secret_key]
        else:
            return default_value
        

