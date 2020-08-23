from aiohttp.client import ClientSession

from .shared import Shared

__all__ = ['AppleSignInAsyncApi']


class AppleSignInAsyncApi(Shared):
    """
    同步处理接口
    """

    def __init__(self, key_id: str, private_key: str, team_id: str, bundle_id: str):
        """

        :param key_id: the private key id [find on apple developer portal -> keys -> key-detail page]
        :param private_key: the private key content [.p8 file]
                            [downloaded when the key generate,
                            you can regenerate the key on apple developer portal -> keys]
        :param team_id: the apple team id [view on apple developer portal]
        :param bundle_id: the app's bundle id
        """
        super().__init__(key_id, private_key, team_id, bundle_id)
        self._session = ClientSession()
