from __future__ import absolute_import
from dynamic_orchestrator.models.base_model_ import Model
from dynamic_orchestrator import util


class InlineResponse2001(Model):

    def __init__(self, filename: str=None, federation_id: str=None): 
        """InlineResponse2001 - a model defined in Swagger

        :param filename: The filename of this InlineResponse2001.  
        :type filename: str
        :param federation_id: The federation_id of this InlineResponse2001.  
        :type federation_id: str
        """
        self.swagger_types = {
            'filename': str,
            'federation_id': str
        }

        self.attribute_map = {
            'filename': 'filename',
            'federation_id': 'federation_id'
        }
        self._filename = filename
        self._federation_id = federation_id

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2001':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_1 of this InlineResponse2001. 
        :rtype: InlineResponse2001
        """
        return util.deserialize_model(dikt, cls)

    @property
    def filename(self) -> str:
        """Gets the filename of this InlineResponse2001.


        :return: The filename of this InlineResponse2001.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename: str):
        """Sets the filename of this InlineResponse2001.


        :param filename: The filename of this InlineResponse2001.
        :type filename: str
        """

        self._filename = filename

    @property
    def federation_id(self) -> str:
        """Gets the federation_id of this InlineResponse2001.


        :return: The federation_id of this InlineResponse2001.
        :rtype: str
        """
        return self._federation_id

    @federation_id.setter
    def federation_id(self, federation_id: str):
        """Sets the federation_id of this InlineResponse2001.


        :param federation_id: The federation_id of this InlineResponse2001.
        :type federation_id: str
        """

        self._federation_id = federation_id