# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from dynamic_orchestrator.models.base_model_ import Model
from dynamic_orchestrator import util


class RequestBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, app_instance_id: str=None, operation: str=None, app_model: object=None, application_parameters: object=None):  # noqa: E501
        """RequestBody - a model defined in Swagger

        :param app_instance_id: The app_instance_id of this RequestBody.  # noqa: E501
        :type app_instance_id: str
        :param operation: The operation of this RequestBody.  # noqa: E501
        :type operation: str
        :param app_model: The app_model of this RequestBody.  # noqa: E501
        :type app_model: object
        :param application_parameters: The application_parameters of this RequestBody.  # noqa: E501
        :type application_parameters: object
        """
        self.swagger_types = {
            'app_instance_id': str,
            'operation': str,
            'app_model': object,
            'application_parameters': object
        }

        self.attribute_map = {
            'app_instance_id': 'app_instance_id',
            'operation': 'operation',
            'app_model': 'app_model',
            'application_parameters': 'application_parameters'
        }
        self._app_instance_id = app_instance_id
        self._operation = operation
        self._app_model = app_model
        self._application_parameters = application_parameters

    @classmethod
    def from_dict(cls, dikt) -> 'RequestBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The request_body of this RequestBody.  # noqa: E501
        :rtype: RequestBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app_instance_id(self) -> str:
        """Gets the app_instance_id of this RequestBody.


        :return: The app_instance_id of this RequestBody.
        :rtype: str
        """
        return self._app_instance_id

    @app_instance_id.setter
    def app_instance_id(self, app_instance_id: str):
        """Sets the app_instance_id of this RequestBody.


        :param app_instance_id: The app_instance_id of this RequestBody.
        :type app_instance_id: str
        """

        self._app_instance_id = app_instance_id

    @property
    def operation(self) -> str:
        """Gets the operation of this RequestBody.


        :return: The operation of this RequestBody.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation: str):
        """Sets the operation of this RequestBody.


        :param operation: The operation of this RequestBody.
        :type operation: str
        """

        self._operation = operation

    @property
    def app_model(self) -> object:
        """Gets the app_model of this RequestBody.


        :return: The app_model of this RequestBody.
        :rtype: object
        """
        return self._app_model

    @app_model.setter
    def app_model(self, app_model: object):
        """Sets the app_model of this RequestBody.


        :param app_model: The app_model of this RequestBody.
        :type app_model: object
        """

        self._app_model = app_model

    @property
    def application_parameters(self) -> object:
        """Gets the application_parameters of this RequestBody.


        :return: The application_parameters of this RequestBody.
        :rtype: object
        """
        return self._application_parameters

    @application_parameters.setter
    def application_parameters(self, application_parameters: object):
        """Sets the application_parameters of this RequestBody.


        :param application_parameters: The application_parameters of this RequestBody.
        :type application_parameters: object
        """

        self._application_parameters = application_parameters