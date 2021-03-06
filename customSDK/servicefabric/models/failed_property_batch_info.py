# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .property_batch_info import PropertyBatchInfo


class FailedPropertyBatchInfo(PropertyBatchInfo):
    """Derived from PropertyBatchInfo. Represents the property batch failing.
    Contains information about the specific batch failure.

    All required parameters must be populated in order to send to Azure.

    :param kind: Required. Constant filled by server.
    :type kind: str
    :param error_message: The error message of the failed operation. Describes
     the exception thrown due to the first unsuccessful operation in the
     property batch.
    :type error_message: str
    :param operation_index: The index of the unsuccessful operation in the
     property batch.
    :type operation_index: int
    """

    _validation = {
        'kind': {'required': True},
    }

    _attribute_map = {
        'kind': {'key': 'Kind', 'type': 'str'},
        'error_message': {'key': 'ErrorMessage', 'type': 'str'},
        'operation_index': {'key': 'OperationIndex', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(FailedPropertyBatchInfo, self).__init__(**kwargs)
        self.error_message = kwargs.get('error_message', None)
        self.operation_index = kwargs.get('operation_index', None)
        self.kind = 'Failed'
