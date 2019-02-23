# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from intrinio_sdk.models.historical_data import HistoricalData  # noqa: F401,E501
from intrinio_sdk.models.sic_index import SICIndex  # noqa: F401,E501


class ApiResponseSICIndexHistoricalData(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'historical_data': 'list[HistoricalData]',
        'index': 'SICIndex',
        'next_page': 'str'
    }

    attribute_map = {
        'historical_data': 'historical_data',
        'index': 'index',
        'next_page': 'next_page'
    }

    def __init__(self, historical_data=None, index=None, next_page=None):  # noqa: E501
        """ApiResponseSICIndexHistoricalData - a model defined in Swagger"""  # noqa: E501

        self._historical_data = None
        self._index = None
        self._next_page = None
        self.discriminator = None

        if historical_data is not None:
            self.historical_data = historical_data
        if index is not None:
            self.index = index
        if next_page is not None:
            self.next_page = next_page

    @property
    def historical_data(self):
        """Gets the historical_data of this ApiResponseSICIndexHistoricalData.  # noqa: E501


        :return: The historical_data of this ApiResponseSICIndexHistoricalData.  # noqa: E501
        :rtype: list[HistoricalData]
        """
        return self._historical_data

    @historical_data.setter
    def historical_data(self, historical_data):
        """Sets the historical_data of this ApiResponseSICIndexHistoricalData.


        :param historical_data: The historical_data of this ApiResponseSICIndexHistoricalData.  # noqa: E501
        :type: list[HistoricalData]
        """

        self._historical_data = historical_data

    @property
    def index(self):
        """Gets the index of this ApiResponseSICIndexHistoricalData.  # noqa: E501


        :return: The index of this ApiResponseSICIndexHistoricalData.  # noqa: E501
        :rtype: SICIndex
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this ApiResponseSICIndexHistoricalData.


        :param index: The index of this ApiResponseSICIndexHistoricalData.  # noqa: E501
        :type: SICIndex
        """

        self._index = index

    @property
    def next_page(self):
        """Gets the next_page of this ApiResponseSICIndexHistoricalData.  # noqa: E501

        The token required to request the next page of the data  # noqa: E501

        :return: The next_page of this ApiResponseSICIndexHistoricalData.  # noqa: E501
        :rtype: str
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        """Sets the next_page of this ApiResponseSICIndexHistoricalData.

        The token required to request the next page of the data  # noqa: E501

        :param next_page: The next_page of this ApiResponseSICIndexHistoricalData.  # noqa: E501
        :type: str
        """

        self._next_page = next_page

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiResponseSICIndexHistoricalData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
