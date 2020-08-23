from aiohttp.client import ClientSession

from .dt import AppleConfig
from .shared import Shared

__all__ = ['AppleSignInAsyncApi']


class AppleSignInAsyncApi(Shared):
    """
    苹果登陆异步处理接口

    Apple SignIn async process interface
    """

    def __init__(self, config: AppleConfig):
        super().__init__(config)
        self._session = ClientSession()
