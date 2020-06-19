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


class SensorRequest(object):
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
        'hardware_id': 'str',
        'sensor_model_id': 'str',
        'location': 'Location',
        'depth': 'float',
        'port': 'DevicePort',
        'device_id': 'str',
        'name': 'str',
        'description': 'str',
        'properties': 'dict(str, object)'
    }

    attribute_map = {
        'hardware_id': 'hardwareId',
        'sensor_model_id': 'sensorModelId',
        'location': 'location',
        'depth': 'depth',
        'port': 'port',
        'device_id': 'deviceId',
        'name': 'name',
        'description': 'description',
        'properties': 'properties'
    }

    def __init__(self, hardware_id=None, sensor_model_id=None, location=None, depth=None, port=None, device_id=None, name=None, description=None, properties=None, local_vars_configuration=None):  # noqa: E501
        """SensorRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._hardware_id = None
        self._sensor_model_id = None
        self._location = None
        self._depth = None
        self._port = None
        self._device_id = None
        self._name = None
        self._description = None
        self._properties = None
        self.discriminator = None

        if hardware_id is not None:
            self.hardware_id = hardware_id
        self.sensor_model_id = sensor_model_id
        if location is not None:
            self.location = location
        if depth is not None:
            self.depth = depth
        if port is not None:
            self.port = port
        if device_id is not None:
            self.device_id = device_id
        self.name = name
        if description is not None:
            self.description = description
        if properties is not None:
            self.properties = properties

    @property
    def hardware_id(self):
        """Gets the hardware_id of this SensorRequest.  # noqa: E501

        Gets or sets id of the sensor given by manufacturer.  # noqa: E501

        :return: The hardware_id of this SensorRequest.  # noqa: E501
        :rtype: str
        """
        return self._hardware_id

    @hardware_id.setter
    def hardware_id(self, hardware_id):
        """Sets the hardware_id of this SensorRequest.

        Gets or sets id of the sensor given by manufacturer.  # noqa: E501

        :param hardware_id: The hardware_id of this SensorRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                hardware_id is not None and len(hardware_id) > 200):
            raise ValueError("Invalid value for `hardware_id`, length must be less than or equal to `200`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                hardware_id is not None and len(hardware_id) < 1):
            raise ValueError("Invalid value for `hardware_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._hardware_id = hardware_id

    @property
    def sensor_model_id(self):
        """Gets the sensor_model_id of this SensorRequest.  # noqa: E501

        Gets or sets id of the associated sensor Model.  # noqa: E501

        :return: The sensor_model_id of this SensorRequest.  # noqa: E501
        :rtype: str
        """
        return self._sensor_model_id

    @sensor_model_id.setter
    def sensor_model_id(self, sensor_model_id):
        """Sets the sensor_model_id of this SensorRequest.

        Gets or sets id of the associated sensor Model.  # noqa: E501

        :param sensor_model_id: The sensor_model_id of this SensorRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sensor_model_id is None:  # noqa: E501
            raise ValueError("Invalid value for `sensor_model_id`, must not be `None`")  # noqa: E501

        self._sensor_model_id = sensor_model_id

    @property
    def location(self):
        """Gets the location of this SensorRequest.  # noqa: E501


        :return: The location of this SensorRequest.  # noqa: E501
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this SensorRequest.


        :param location: The location of this SensorRequest.  # noqa: E501
        :type: Location
        """

        self._location = location

    @property
    def depth(self):
        """Gets the depth of this SensorRequest.  # noqa: E501

        Gets or sets depth in centimeters.  # noqa: E501

        :return: The depth of this SensorRequest.  # noqa: E501
        :rtype: float
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        """Sets the depth of this SensorRequest.

        Gets or sets depth in centimeters.  # noqa: E501

        :param depth: The depth of this SensorRequest.  # noqa: E501
        :type: float
        """

        self._depth = depth

    @property
    def port(self):
        """Gets the port of this SensorRequest.  # noqa: E501


        :return: The port of this SensorRequest.  # noqa: E501
        :rtype: DevicePort
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this SensorRequest.


        :param port: The port of this SensorRequest.  # noqa: E501
        :type: DevicePort
        """

        self._port = port

    @property
    def device_id(self):
        """Gets the device_id of this SensorRequest.  # noqa: E501

        Gets or sets id of the associated device.  # noqa: E501

        :return: The device_id of this SensorRequest.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this SensorRequest.

        Gets or sets id of the associated device.  # noqa: E501

        :param device_id: The device_id of this SensorRequest.  # noqa: E501
        :type: str
        """

        self._device_id = device_id

    @property
    def name(self):
        """Gets the name of this SensorRequest.  # noqa: E501

        Gets or sets name to identify resource.  # noqa: E501

        :return: The name of this SensorRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SensorRequest.

        Gets or sets name to identify resource.  # noqa: E501

        :param name: The name of this SensorRequest.  # noqa: E501
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
        """Gets the description of this SensorRequest.  # noqa: E501

        Gets or sets textual description of resource.  # noqa: E501

        :return: The description of this SensorRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SensorRequest.

        Gets or sets textual description of resource.  # noqa: E501

        :param description: The description of this SensorRequest.  # noqa: E501
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
        """Gets the properties of this SensorRequest.  # noqa: E501

        Gets or sets additional properties of the resource.  # noqa: E501

        :return: The properties of this SensorRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this SensorRequest.

        Gets or sets additional properties of the resource.  # noqa: E501

        :param properties: The properties of this SensorRequest.  # noqa: E501
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
        if not isinstance(other, SensorRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SensorRequest):
            return True

        return self.to_dict() != other.to_dict()
