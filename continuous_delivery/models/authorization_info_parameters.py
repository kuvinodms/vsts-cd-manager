# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 1.0.1.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AuthorizationInfoParameters(Model):
    _attribute_map = {
        'authorization': {'key': 'Authorization', 'type': 'str'},
        'access_token': {'key': 'AccessToken', 'type': 'str'},
    }

    def __init__(self, authorization=None, access_token=None):
        self.authorization = authorization
        self.access_token = access_token
