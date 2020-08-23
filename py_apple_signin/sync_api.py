from requests import Session

from .dt import AppleConfig
from .shared import Shared

__all__ = ['AppleSignInApi']


class AppleSignInApi(Shared):
    """
    苹果登陆同步处理接口
    """

    def __init__(self, config: AppleConfig):
        super().__init__(config)
        self._session = Session()
