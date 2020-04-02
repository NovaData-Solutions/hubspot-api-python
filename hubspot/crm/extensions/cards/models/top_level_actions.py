# coding: utf-8

"""
    CRM cards

    Allows an app to extend the CRM UI by surfacing custom cards in the sidebar of record pages. These cards are defined up-front as part of app configuration, then populated by external data fetch requests when the record page is accessed by a user.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.extensions.cards.configuration import Configuration


class TopLevelActions(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'settings': 'IFrameActionBody',
        'primary': 'OneOfActionHookActionBodyIFrameActionBody',
        'secondary': 'list[AnyOfActionHookActionBodyIFrameActionBody]'
    }

    attribute_map = {
        'settings': 'settings',
        'primary': 'primary',
        'secondary': 'secondary'
    }

    def __init__(self, settings=None, primary=None, secondary=None, local_vars_configuration=None):  # noqa: E501
        """TopLevelActions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._settings = None
        self._primary = None
        self._secondary = None
        self.discriminator = None

        if settings is not None:
            self.settings = settings
        if primary is not None:
            self.primary = primary
        self.secondary = secondary

    @property
    def settings(self):
        """Gets the settings of this TopLevelActions.  # noqa: E501


        :return: The settings of this TopLevelActions.  # noqa: E501
        :rtype: IFrameActionBody
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this TopLevelActions.


        :param settings: The settings of this TopLevelActions.  # noqa: E501
        :type: IFrameActionBody
        """

        self._settings = settings

    @property
    def primary(self):
        """Gets the primary of this TopLevelActions.  # noqa: E501


        :return: The primary of this TopLevelActions.  # noqa: E501
        :rtype: OneOfActionHookActionBodyIFrameActionBody
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """Sets the primary of this TopLevelActions.


        :param primary: The primary of this TopLevelActions.  # noqa: E501
        :type: OneOfActionHookActionBodyIFrameActionBody
        """

        self._primary = primary

    @property
    def secondary(self):
        """Gets the secondary of this TopLevelActions.  # noqa: E501


        :return: The secondary of this TopLevelActions.  # noqa: E501
        :rtype: list[AnyOfActionHookActionBodyIFrameActionBody]
        """
        return self._secondary

    @secondary.setter
    def secondary(self, secondary):
        """Sets the secondary of this TopLevelActions.


        :param secondary: The secondary of this TopLevelActions.  # noqa: E501
        :type: list[AnyOfActionHookActionBodyIFrameActionBody]
        """
        if self.local_vars_configuration.client_side_validation and secondary is None:  # noqa: E501
            raise ValueError("Invalid value for `secondary`, must not be `None`")  # noqa: E501

        self._secondary = secondary

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, TopLevelActions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TopLevelActions):
            return True

        return self.to_dict() != other.to_dict()
