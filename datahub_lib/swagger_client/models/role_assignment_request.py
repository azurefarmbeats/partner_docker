# coding: utf-8

"""
    Azure FarmBeats API

    <p>  <p>Azure FarmBeats helps you build digital agricultural solutions in Azure. By providing a standardized schema to query agricultural data from various sources, Azure FarmBeats provides you:  <ul >   <li style=\"margin: 7px;\">Ability to acquire, aggregate, process and store agricultural data.</li>   <li style=\"margin: 7px;\">Capability to fuse data between data sources and generate insights.</li>   <li style=\"margin: 7px;\">Schematized access and query capabilities on ingested data.</li>  </ul>  </p>  <h><b>REST Operation Groups</b></h>  <p><b>Farm:</b></p>  <p>Farm corresponds to a physical location of interest within the system. Each Farm has a Farm name and a unique farm id.</p>  <p><b>Device:</b></p>  <p>Device corresponds to a physical device present in the farm. Each device has a unique device id. Device is typically provisioned to a farm with a farm id.</p>  <p><b>DeviceModel:</b></p>  <p>DeviceModel corresponds to the meta-data of the device such as the Manufacturer, Type of the device either Gateway or Node.</p>  <p><b>Sensor:</b></p>  <p>Sensor corresponds to a physical sensor that records values. A sensor is typically connected to a device with a device id.</p>  </p>  <p><b>SensorModel:</b></p>  <p>SensorModel corresponds to the meta-data of the sensor such as the Manufacturer, Type of the sensor either Analog or Digital, Sensor Measure such as Ambient Temperature, Pressure etc.</p>  <p><b>Telemetry:</b></p>  <p>Telemetry provides the ability to read telemetry messages for a particular sensor & time range.</p>  <p><b>Job:</b></p>  <p>Job corresponds to any workflow of activities which are executed in the system to get a desired output. Each job is associated with a job id and job type.</p>  <p><b>JobType:</b></p>  <p>JobType corresponds to different job types supported by the system. This includes system defined & user-defined job types.</p>  <p><b>ExtendedType:</b></p>  <p>ExtendedType corresponds to the list of system & user-defined types in the system. This helps setup a new Sensor or Scene or Scenefile type in the system.</p>  <p><b>Partner:</b></p>  <p>Partner corresponds to the sensor/weather/imagery integration partner.</p>  <p><b>Scene:</b></p>  <p>Scene corresponds to any generated output in the context of a Farm. Each Scene has a scene id, scene source, scene type and farm id associated with it. Each scene id  can have multiple scene files associated with it.</p>  <p><b>SceneFile:</b></p>  <p>SceneFile corresponds to all files which are generated for single scene. A single scene id can have multiple SceneFile ids associated with it.</p>  <p><b>Rule:</b></p>  <p>Rule corresponds to a condition for farm-related data to trigger an alert. Each rule will be in the context of a farm's data.</p>  <p><b>Alert:</b></p>  <p>Alert corresponds to a notification which gets generated when a rule condition is met. Each alert will be in the context of a rule.</p>  <p><b>RoleDefinition:</b></p>  <p>RoleDefinition defines allowed and disallowed actions for a role.</p>  <p><b>RoleAssignment:</b></p>  <p>RoleAssignment corresponds to the assignment of a role to a user or a service principal.</p>  <p><b>WeatherDataModel:</b></p>  <p>WeatherDataModel corresponds to the metadata of the Weather Station such as name and weather measures such as Precipitation, Rainfall etc.</p>  <p><b>WeatherDataLocation:</b></p>  <p>WeatherDataLocation corresponds to the instance of Weather Station for a particular location (latitude/longitude).</p>  </p>    # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from datahub_lib.swagger_client.configuration import Configuration


class RoleAssignmentRequest(object):
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
        'role_definition_id': 'str',
        'object_id': 'str',
        'object_id_type': 'str',
        'tenant_id': 'str'
    }

    attribute_map = {
        'role_definition_id': 'roleDefinitionId',
        'object_id': 'objectId',
        'object_id_type': 'objectIdType',
        'tenant_id': 'tenantId'
    }

    def __init__(self, role_definition_id=None, object_id=None, object_id_type=None, tenant_id=None, local_vars_configuration=None):  # noqa: E501
        """RoleAssignmentRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._role_definition_id = None
        self._object_id = None
        self._object_id_type = None
        self._tenant_id = None
        self.discriminator = None

        self.role_definition_id = role_definition_id
        self.object_id = object_id
        self.object_id_type = object_id_type
        self.tenant_id = tenant_id

    @property
    def role_definition_id(self):
        """Gets the role_definition_id of this RoleAssignmentRequest.  # noqa: E501

        Gets or sets roleDefinitionId of the role assignment.  # noqa: E501

        :return: The role_definition_id of this RoleAssignmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._role_definition_id

    @role_definition_id.setter
    def role_definition_id(self, role_definition_id):
        """Sets the role_definition_id of this RoleAssignmentRequest.

        Gets or sets roleDefinitionId of the role assignment.  # noqa: E501

        :param role_definition_id: The role_definition_id of this RoleAssignmentRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and role_definition_id is None:  # noqa: E501
            raise ValueError("Invalid value for `role_definition_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                role_definition_id is not None and len(role_definition_id) > 200):
            raise ValueError("Invalid value for `role_definition_id`, length must be less than or equal to `200`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                role_definition_id is not None and len(role_definition_id) < 3):
            raise ValueError("Invalid value for `role_definition_id`, length must be greater than or equal to `3`")  # noqa: E501

        self._role_definition_id = role_definition_id

    @property
    def object_id(self):
        """Gets the object_id of this RoleAssignmentRequest.  # noqa: E501

        Gets or sets objectId of the role assignment.  # noqa: E501

        :return: The object_id of this RoleAssignmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this RoleAssignmentRequest.

        Gets or sets objectId of the role assignment.  # noqa: E501

        :param object_id: The object_id of this RoleAssignmentRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and object_id is None:  # noqa: E501
            raise ValueError("Invalid value for `object_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                object_id is not None and len(object_id) > 200):
            raise ValueError("Invalid value for `object_id`, length must be less than or equal to `200`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                object_id is not None and len(object_id) < 3):
            raise ValueError("Invalid value for `object_id`, length must be greater than or equal to `3`")  # noqa: E501

        self._object_id = object_id

    @property
    def object_id_type(self):
        """Gets the object_id_type of this RoleAssignmentRequest.  # noqa: E501

        Gets or sets objectIdType of the role assignment.  # noqa: E501

        :return: The object_id_type of this RoleAssignmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._object_id_type

    @object_id_type.setter
    def object_id_type(self, object_id_type):
        """Sets the object_id_type of this RoleAssignmentRequest.

        Gets or sets objectIdType of the role assignment.  # noqa: E501

        :param object_id_type: The object_id_type of this RoleAssignmentRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and object_id_type is None:  # noqa: E501
            raise ValueError("Invalid value for `object_id_type`, must not be `None`")  # noqa: E501
        allowed_values = ["UserId", "ServicePrincipalId"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and object_id_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `object_id_type` ({0}), must be one of {1}"  # noqa: E501
                .format(object_id_type, allowed_values)
            )

        self._object_id_type = object_id_type

    @property
    def tenant_id(self):
        """Gets the tenant_id of this RoleAssignmentRequest.  # noqa: E501

        Gets or sets tenantId of the role assignment.  # noqa: E501

        :return: The tenant_id of this RoleAssignmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this RoleAssignmentRequest.

        Gets or sets tenantId of the role assignment.  # noqa: E501

        :param tenant_id: The tenant_id of this RoleAssignmentRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and tenant_id is None:  # noqa: E501
            raise ValueError("Invalid value for `tenant_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                tenant_id is not None and len(tenant_id) > 200):
            raise ValueError("Invalid value for `tenant_id`, length must be less than or equal to `200`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                tenant_id is not None and len(tenant_id) < 3):
            raise ValueError("Invalid value for `tenant_id`, length must be greater than or equal to `3`")  # noqa: E501

        self._tenant_id = tenant_id

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
        if not isinstance(other, RoleAssignmentRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RoleAssignmentRequest):
            return True

        return self.to_dict() != other.to_dict()
