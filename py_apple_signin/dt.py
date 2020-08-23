from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin

__all__ = ['AppleConfig']


@dataclass
class AppleConfig(DataClassJsonMixin):
    """
    苹果登陆的配置项目
    """

    key_id: str
    """
    the private key id [find on apple developer portal -> keys -> key-detail page]
    """

    private_key: str
    """
    the private key content [.p8 file]
    [downloaded when the key generate,
    you can regenerate the key on apple developer portal -> keys]
    """

    team_id: str
    """
    the apple team id [view on apple developer portal]
    """

    bundle_id: str
    """
    the app's bundle id
    """
