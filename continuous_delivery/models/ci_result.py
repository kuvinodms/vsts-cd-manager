# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 1.0.1.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CiResult(Model):
    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
        'status_message': {'key': 'statusMessage', 'type': 'str'},
    }

    def __init__(self, status=None, status_message=None):
        self.status = status
        self.status_message = status_message
