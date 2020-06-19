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


class DeviceRequest(object):
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
        'device_model_id': 'str',
        'hardware_id': 'str',
        'farm_id': 'str',
        'reporting_interval': 'int',
        'location': 'Location',
        'parent_device_id': 'str',
        'name': 'str',
        'description': 'str',
        'properties': 'dict(str, object)'
    }

    attribute_map = {
        'device_model_id': 'deviceModelId',
        'hardware_id': 'hardwareId',
        'farm_id': 'farmId',
        'reporting_interval': 'reportingInterval',
        'location': 'location',
        'parent_device_id': 'parentDeviceId',
        'name': 'name',
        'description': 'description',
        'properties': 'properties'
    }

    def __init__(self, device_model_id=None, hardware_id=None, farm_id=None, reporting_interval=None, location=None, parent_device_id=None, name=None, description=None, properties=None, local_vars_configuration=None):  # noqa: E501
        """DeviceRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._device_model_id = None
        self._hardware_id = None
        self._farm_id = None
        self._reporting_interval = None
        self._location = None
        self._parent_device_id = None
        self._name = None
        self._description = None
        self._properties = None
        self.discriminator = None

        self.device_model_id = device_model_id
        self.hardware_id = hardware_id
        if farm_id is not None:
            self.farm_id = farm_id
        if reporting_interval is not None:
            self.reporting_interval = reporting_interval
        if location is not None:
            self.location = location
        if parent_device_id is not None:
            self.parent_device_id = parent_device_id
        self.name = name
        if description is not None:
            self.description = description
        if properties is not None:
            self.properties = properties

    @property
    def device_model_id(self):
        """Gets the device_model_id of this DeviceRequest.  # noqa: E501

        Gets or sets id of the associated Device Model.  # noqa: E501

        :return: The device_model_id of this DeviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._device_model_id

    @device_model_id.setter
    def device_model_id(self, device_model_id):
        """Sets the device_model_id of this DeviceRequest.

        Gets or sets id of the associated Device Model.  # noqa: E501

        :param device_model_id: The device_model_id of this DeviceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and device_model_id is None:  # noqa: E501
            raise ValueError("Invalid value for `device_model_id`, must not be `None`")  # noqa: E501

        self._device_model_id = device_model_id

    @property
    def hardware_id(self):
        """Gets the hardware_id of this DeviceRequest.  # noqa: E501

        Gets or sets unique id for the device such as MAC address etc.  # noqa: E501

        :return: The hardware_id of this DeviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._hardware_id

    @hardware_id.setter
    def hardware_id(self, hardware_id):
        """Sets the hardware_id of this DeviceRequest.

        Gets or sets unique id for the device such as MAC address etc.  # noqa: E501

        :param hardware_id: The hardware_id of this DeviceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and hardware_id is None:  # noqa: E501
            raise ValueError("Invalid value for `hardware_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                hardware_id is not None and len(hardware_id) > 200):
            raise ValueError("Invalid value for `hardware_id`, length must be less than or equal to `200`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                hardware_id is not None and len(hardware_id) < 3):
            raise ValueError("Invalid value for `hardware_id`, length must be greater than or equal to `3`")  # noqa: E501

        self._hardware_id = hardware_id

    @property
    def farm_id(self):
        """Gets the farm_id of this DeviceRequest.  # noqa: E501

        Gets or sets id of the farm to which the device is provisioned to.  Sensor Partners needs to ignore this field while creating and need to pass the old value while updating device.  # noqa: E501

        :return: The farm_id of this DeviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._farm_id

    @farm_id.setter
    def farm_id(self, farm_id):
        """Sets the farm_id of this DeviceRequest.

        Gets or sets id of the farm to which the device is provisioned to.  Sensor Partners needs to ignore this field while creating and need to pass the old value while updating device.  # noqa: E501

        :param farm_id: The farm_id of this DeviceRequest.  # noqa: E501
        :type: str
        """

        self._farm_id = farm_id

    @property
    def reporting_interval(self):
        """Gets the reporting_interval of this DeviceRequest.  # noqa: E501

        Gets or sets reporting interval of telemetry in seconds.  # noqa: E501

        :return: The reporting_interval of this DeviceRequest.  # noqa: E501
        :rtype: int
        """
        return self._reporting_interval

    @reporting_interval.setter
    def reporting_interval(self, reporting_interval):
        """Sets the reporting_interval of this DeviceRequest.

        Gets or sets reporting interval of telemetry in seconds.  # noqa: E501

        :param reporting_interval: The reporting_interval of this DeviceRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                reporting_interval is not None and reporting_interval > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `reporting_interval`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                reporting_interval is not None and reporting_interval < 0):  # noqa: E501
            raise ValueError("Invalid value for `reporting_interval`, must be a value greater than or equal to `0`")  # noqa: E501

        self._reporting_interval = reporting_interval

    @property
    def location(self):
        """Gets the location of this DeviceRequest.  # noqa: E501


        :return: The location of this DeviceRequest.  # noqa: E501
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this DeviceRequest.


        :param location: The location of this DeviceRequest.  # noqa: E501
        :type: Location
        """

        self._location = location

    @property
    def parent_device_id(self):
        """Gets the parent_device_id of this DeviceRequest.  # noqa: E501

        Gets or sets id of the parent device to which this device is connected to.  Eg.A Node connected to a Gateway; Node will have parentDeviceId as the Gateway.  # noqa: E501

        :return: The parent_device_id of this DeviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._parent_device_id

    @parent_device_id.setter
    def parent_device_id(self, parent_device_id):
        """Sets the parent_device_id of this DeviceRequest.

        Gets or sets id of the parent device to which this device is connected to.  Eg.A Node connected to a Gateway; Node will have parentDeviceId as the Gateway.  # noqa: E501

        :param parent_device_id: The parent_device_id of this DeviceRequest.  # noqa: E501
        :type: str
        """

        self._parent_device_id = parent_device_id

    @property
    def name(self):
        """Gets the name of this DeviceRequest.  # noqa: E501

        Gets or sets name to identify resource.  # noqa: E501

        :return: The name of this DeviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceRequest.

        Gets or sets name to identify resource.  # noqa: E501

        :param name: The name of this DeviceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 100):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 3):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `3`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this DeviceRequest.  # noqa: E501

        Gets or sets textual description of resource.  # noqa: E501

        :return: The description of this DeviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeviceRequest.

        Gets or sets textual description of resource.  # noqa: E501

        :param description: The description of this DeviceRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 1000):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 3):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `3`")  # noqa: E501

        self._description = description

    @property
    def properties(self):
        """Gets the properties of this DeviceRequest.  # noqa: E501

        Gets or sets additional properties of the resource.  # noqa: E501

        :return: The properties of this DeviceRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this DeviceRequest.

        Gets or sets additional properties of the resource.  # noqa: E501

        :param properties: The properties of this DeviceRequest.  # noqa: E501
        :type: dict(str, object)
        """

        self._properties = properties

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
        if not isinstance(other, DeviceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceRequest):
            return True

        return self.to_dict() != other.to_dict()
