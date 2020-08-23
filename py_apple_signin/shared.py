from datetime import datetime, timedelta
from typing import Tuple

import jwt

__all__ = ['Shared']


class Shared(object):
    """
    shared code between sync and async version
    """

    ACCESS_TOKEN_URL = 'https://appleid.apple.com/auth/token'

    def __init__(self, key_id: str, private_key: str, team_id: str, bundle_id: str):
        """

        :param key_id: the private key id [find on apple developer portal -> keys -> key-detail page]
        :param private_key: the private key content [.p8 file]
                            [downloaded when the key generate,
                            you can regenerate the key on apple developer portal -> keys]
        :param team_id: the apple team id [view on apple developer portal]
        :param bundle_id: the app's bundle id
        """
        self._kid = key_id
        self._private_key = private_key
        self._team_id = team_id
        self._bundle_id = bundle_id

    def _make_up_data(self, code: str) -> Tuple[dict, dict]:
        """
        组装需要发送的数据

        :param code:
        :return: (headers, data)
        """
        client_id = self._bundle_id
        client_secret = self._client_secret()

        headers = {'content-type': "application/x-www-form-urlencoded"}
        data = {
            'client_id': client_id,
            'client_secret': client_secret,
            'code': code,
            'grant_type': 'authorization_code',
        }

        return headers, data

    def _client_secret(self) -> str:
        headers = {'key_id': self._kid}

        payload = {
            'iss': self._team_id,
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(days=180),
            'aud': 'https://appleid.apple.com',
            'sub': self._bundle_id,
        }

        return jwt.encode(payload, self._private_key, algorithm='ES256', headers=headers).decode("utf-8")
