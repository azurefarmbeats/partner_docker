# coding: utf-8

"""
    Azure FarmBeats API

    <p>  <p>Azure FarmBeats helps you build digital agricultural solutions in Azure. By providing a standardized schema to query agricultural data from various sources, Azure FarmBeats provides you:  <ul >   <li style=\"margin: 7px;\">Ability to acquire, aggregate, process and store agricultural data.</li>   <li style=\"margin: 7px;\">Capability to fuse data between data sources and generate insights.</li>   <li style=\"margin: 7px;\">Schematized access and query capabilities on ingested data.</li>  </ul>  </p>  <h><b>REST Operation Groups</b></h>  <p><b>Farm:</b></p>  <p>Farm corresponds to a physical location of interest within the system. Each Farm has a Farm name and a unique farm id.</p>  <p><b>Device:</b></p>  <p>Device corresponds to a physical device present in the farm. Each device has a unique device id. Device is typically provisioned to a farm with a farm id.</p>  <p><b>DeviceModel:</b></p>  <p>DeviceModel corresponds to the meta-data of the device such as the Manufacturer, Type of the device either Gateway or Node.</p>  <p><b>Sensor:</b></p>  <p>Sensor corresponds to a physical sensor that records values. A sensor is typically connected to a device with a device id.</p>  </p>  <p><b>SensorModel:</b></p>  <p>SensorModel corresponds to the meta-data of the sensor such as the Manufacturer, Type of the sensor either Analog or Digital, Sensor Measure such as Ambient Temperature, Pressure etc.</p>  <p><b>Telemetry:</b></p>  <p>Telemetry provides the ability to read telemetry messages for a particular sensor & time range.</p>  <p><b>Job:</b></p>  <p>Job corresponds to any workflow of activities which are executed in the system to get a desired output. Each job is associated with a job id and job type.</p>  <p><b>JobType:</b></p>  <p>JobType corresponds to different job types supported by the system. This includes system defined & user-defined job types.</p>  <p><b>ExtendedType:</b></p>  <p>ExtendedType corresponds to the list of system & user-defined types in the system. This helps setup a new Sensor or Scene or Scenefile type in the system.</p>  <p><b>Partner:</b></p>  <p>Partner corresponds to the sensor/weather/imagery integration partner.</p>  <p><b>Scene:</b></p>  <p>Scene corresponds to any generated output in the context of a Farm. Each Scene has a scene id, scene source, scene type and farm id associated with it. Each scene id  can have multiple scene files associated with it.</p>  <p><b>SceneFile:</b></p>  <p>SceneFile corresponds to all files which are generated for single scene. A single scene id can have multiple SceneFile ids associated with it.</p>  <p><b>Rule:</b></p>  <p>Rule corresponds to a condition for farm-related data to trigger an alert. Each rule will be in the context of a farm's data.</p>  <p><b>Alert:</b></p>  <p>Alert corresponds to a notification which gets generated when a rule condition is met. Each alert will be in the context of a rule.</p>  <p><b>RoleDefinition:</b></p>  <p>RoleDefinition defines allowed and disallowed actions for a role.</p>  <p><b>RoleAssignment:</b></p>  <p>RoleAssignment corresponds to the assignment of a role to a user or a service principal.</p>  </p>    # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class WeatherMeasure(object):
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
        'name': 'str',
        'data_type': 'str',
        'measure_enum_definition': 'dict(str, int)',
        'type': 'str',
        'unit': 'str',
        'aggregation_type': 'str',
        'depth': 'float',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'data_type': 'dataType',
        'measure_enum_definition': 'measureEnumDefinition',
        'type': 'type',
        'unit': 'unit',
        'aggregation_type': 'aggregationType',
        'depth': 'depth',
        'description': 'description'
    }

    def __init__(self, name=None, data_type=None, measure_enum_definition=None, type=None, unit=None, aggregation_type='None', depth=None, description=None):  # noqa: E501
        """WeatherMeasure - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._data_type = None
        self._measure_enum_definition = None
        self._type = None
        self._unit = None
        self._aggregation_type = None
        self._depth = None
        self._description = None
        self.discriminator = None

        self.name = name
        self.data_type = data_type
        if measure_enum_definition is not None:
            self.measure_enum_definition = measure_enum_definition
        self.type = type
        self.unit = unit
        if aggregation_type is not None:
            self.aggregation_type = aggregation_type
        if depth is not None:
            self.depth = depth
        if description is not None:
            self.description = description

    @property
    def name(self):
        """Gets the name of this WeatherMeasure.  # noqa: E501

        Gets or sets name of the Weather Measure.  For measure from different depths, please specify the depth. Eg.soil_moisture_15cm  This name has to be consistent with the telemetry data.  # noqa: E501

        :return: The name of this WeatherMeasure.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WeatherMeasure.

        Gets or sets name of the Weather Measure.  For measure from different depths, please specify the depth. Eg.soil_moisture_15cm  This name has to be consistent with the telemetry data.  # noqa: E501

        :param name: The name of this WeatherMeasure.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")  # noqa: E501
        if name is not None and len(name) < 3:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `3`")  # noqa: E501

        self._name = name

    @property
    def data_type(self):
        """Gets the data_type of this WeatherMeasure.  # noqa: E501

        Gets or sets weather telemetry data type.  # noqa: E501

        :return: The data_type of this WeatherMeasure.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this WeatherMeasure.

        Gets or sets weather telemetry data type.  # noqa: E501

        :param data_type: The data_type of this WeatherMeasure.  # noqa: E501
        :type: str
        """
        if data_type is None:
            raise ValueError("Invalid value for `data_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Double", "Enum"]  # noqa: E501
        if data_type not in allowed_values:
            raise ValueError(
                "Invalid value for `data_type` ({0}), must be one of {1}"  # noqa: E501
                .format(data_type, allowed_values)
            )

        self._data_type = data_type

    @property
    def measure_enum_definition(self):
        """Gets the measure_enum_definition of this WeatherMeasure.  # noqa: E501

        Gets or sets weather measure enum definition.  # noqa: E501

        :return: The measure_enum_definition of this WeatherMeasure.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._measure_enum_definition

    @measure_enum_definition.setter
    def measure_enum_definition(self, measure_enum_definition):
        """Sets the measure_enum_definition of this WeatherMeasure.

        Gets or sets weather measure enum definition.  # noqa: E501

        :param measure_enum_definition: The measure_enum_definition of this WeatherMeasure.  # noqa: E501
        :type: dict(str, int)
        """

        self._measure_enum_definition = measure_enum_definition

    @property
    def type(self):
        """Gets the type of this WeatherMeasure.  # noqa: E501

        Gets or sets measurement type of weather telemetry data. (See ExtendedTypes with key \"WeatherMeasureType\" to know all valid values).  # noqa: E501

        :return: The type of this WeatherMeasure.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WeatherMeasure.

        Gets or sets measurement type of weather telemetry data. (See ExtendedTypes with key \"WeatherMeasureType\" to know all valid values).  # noqa: E501

        :param type: The type of this WeatherMeasure.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def unit(self):
        """Gets the unit of this WeatherMeasure.  # noqa: E501

        Gets or sets unit of weather telemetry data. (See ExtendedTypes with key \"WeatherMeasureUnit\" to know all valid values).  # noqa: E501

        :return: The unit of this WeatherMeasure.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this WeatherMeasure.

        Gets or sets unit of weather telemetry data. (See ExtendedTypes with key \"WeatherMeasureUnit\" to know all valid values).  # noqa: E501

        :param unit: The unit of this WeatherMeasure.  # noqa: E501
        :type: str
        """
        if unit is None:
            raise ValueError("Invalid value for `unit`, must not be `None`")  # noqa: E501

        self._unit = unit

    @property
    def aggregation_type(self):
        """Gets the aggregation_type of this WeatherMeasure.  # noqa: E501

        Gets or sets aggregation done on weather telemetry data.  # noqa: E501

        :return: The aggregation_type of this WeatherMeasure.  # noqa: E501
        :rtype: str
        """
        return self._aggregation_type

    @aggregation_type.setter
    def aggregation_type(self, aggregation_type):
        """Sets the aggregation_type of this WeatherMeasure.

        Gets or sets aggregation done on weather telemetry data.  # noqa: E501

        :param aggregation_type: The aggregation_type of this WeatherMeasure.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Average", "Maximum", "Minimum", "StandardDeviation"]  # noqa: E501
        if aggregation_type not in allowed_values:
            raise ValueError(
                "Invalid value for `aggregation_type` ({0}), must be one of {1}"  # noqa: E501
                .format(aggregation_type, allowed_values)
            )

        self._aggregation_type = aggregation_type

    @property
    def depth(self):
        """Gets the depth of this WeatherMeasure.  # noqa: E501

        Gets or sets depth in centimeters.  # noqa: E501

        :return: The depth of this WeatherMeasure.  # noqa: E501
        :rtype: float
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        """Sets the depth of this WeatherMeasure.

        Gets or sets depth in centimeters.  # noqa: E501

        :param depth: The depth of this WeatherMeasure.  # noqa: E501
        :type: float
        """

        self._depth = depth

    @property
    def description(self):
        """Gets the description of this WeatherMeasure.  # noqa: E501

        Gets or sets description of the Weather Measure.  # noqa: E501

        :return: The description of this WeatherMeasure.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WeatherMeasure.

        Gets or sets description of the Weather Measure.  # noqa: E501

        :param description: The description of this WeatherMeasure.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 1000:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1000`")  # noqa: E501
        if description is not None and len(description) < 3:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `3`")  # noqa: E501

        self._description = description

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
        if issubclass(WeatherMeasure, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WeatherMeasure):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other