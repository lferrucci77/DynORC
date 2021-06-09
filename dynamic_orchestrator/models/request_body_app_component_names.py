# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from dynamic_orchestrator.models.base_model_ import Model
from dynamic_orchestrator import util


class RequestBodyAppComponentNames(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, component_name: str=None):  # noqa: E501
        """RequestBodyAppComponentNames - a model defined in Swagger

        :param component_name: The component_name of this RequestBodyAppComponentNames.  # noqa: E501
        :type component_name: str
        """
        self.swagger_types = {
            'component_name': str
        }

        self.attribute_map = {
            'component_name': 'component_name'
        }
        self._component_name = component_name

    @classmethod
    def from_dict(cls, dikt) -> 'RequestBodyAppComponentNames':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The request_body_app_component_names of this RequestBodyAppComponentNames.  # noqa: E501
        :rtype: RequestBodyAppComponentNames
        """
        return util.deserialize_model(dikt, cls)

    @property
    def component_name(self) -> str:
        """Gets the component_name of this RequestBodyAppComponentNames.


        :return: The component_name of this RequestBodyAppComponentNames.
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name: str):
        """Sets the component_name of this RequestBodyAppComponentNames.


        :param component_name: The component_name of this RequestBodyAppComponentNames.
        :type component_name: str
        """

        self._component_name = component_name