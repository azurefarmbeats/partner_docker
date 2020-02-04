# coding: utf-8

"""
    Azure FarmBeats API

    <p>  <p>Azure FarmBeats helps you build digital agricultural solutions in Azure. By providing a standardized schema to query agricultural data from various sources, Azure FarmBeats provides you:  <ul >   <li style=\"margin: 7px;\">Ability to acquire, aggregate, process and store agricultural data.</li>   <li style=\"margin: 7px;\">Capability to fuse data between data sources and generate insights.</li>   <li style=\"margin: 7px;\">Schematized access and query capabilities on ingested data.</li>  </ul>  </p>  <h><b>REST Operation Groups</b></h>  <p><b>Farm:</b></p>  <p>Farm corresponds to a physical location of interest within the system. Each Farm has a Farm name and a unique farm id.</p>  <p><b>Device:</b></p>  <p>Device corresponds to a physical device present in the farm. Each device has a unique device id. Device is typically provisioned to a farm with a farm id.</p>  <p><b>DeviceModel:</b></p>  <p>DeviceModel corresponds to the meta-data of the device such as the Manufacturer, Type of the device either Gateway or Node.</p>  <p><b>Sensor:</b></p>  <p>Sensor corresponds to a physical sensor that records values. A sensor is typically connected to a device with a device id.</p>  </p>  <p><b>SensorModel:</b></p>  <p>SensorModel corresponds to the meta-data of the sensor such as the Manufacturer, Type of the sensor either Analog or Digital, Sensor Measure such as Ambient Temperature, Pressure etc.</p>  <p><b>Telemetry:</b></p>  <p>Telemetry provides the ability to read telemetry messages for a particular sensor & time range.</p>  <p><b>Job:</b></p>  <p>Job corresponds to any workflow of activities which are executed in the system to get a desired output. Each job is associated with a job id and job type.</p>  <p><b>JobType:</b></p>  <p>JobType corresponds to different job types supported by the system. This includes system defined & user-defined job types.</p>  <p><b>ExtendedType:</b></p>  <p>ExtendedType corresponds to the list of system & user-defined types in the system. This helps setup a new Sensor or Scene or Scenefile type in the system.</p>  <p><b>Partner:</b></p>  <p>Partner corresponds to the sensor/weather/imagery integration partner.</p>  <p><b>Scene:</b></p>  <p>Scene corresponds to any generated output in the context of a Farm. Each Scene has a scene id, scene source, scene type and farm id associated with it. Each scene id  can have multiple scene files associated with it.</p>  <p><b>SceneFile:</b></p>  <p>SceneFile corresponds to all files which are generated for single scene. A single scene id can have multiple SceneFile ids associated with it.</p>  <p><b>Rule:</b></p>  <p>Rule corresponds to a condition for farm-related data to trigger an alert. Each rule will be in the context of a farm's data.</p>  <p><b>Alert:</b></p>  <p>Alert corresponds to a notification which gets generated when a rule condition is met. Each alert will be in the context of a rule.</p>  <p><b>RoleDefinition:</b></p>  <p>RoleDefinition defines allowed and disallowed actions for a role.</p>  <p><b>RoleAssignment:</b></p>  <p>RoleAssignment corresponds to the assignment of a role to a user or a service principal.</p>  </p>    # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from datahub_lib.swagger_client.api_client import ApiClient


class AlertApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def alert_get(self, id, **kwargs):  # noqa: E501
        """Returns alert for the given id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.alert_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Id of the alert object. (required)
        :return: AlertResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.alert_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.alert_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def alert_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Returns alert for the given id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.alert_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Id of the alert object. (required)
        :return: AlertResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method alert_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `alert_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/Alert/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AlertResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def alert_get_all(self, **kwargs):  # noqa: E501
        """Returns list of alerts.  # noqa: E501

        based on specified filters and date range. Requires ReadAll privileges.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.alert_get_all(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] rule_ids: Gets or sets list of rule ids for which alerts are generated.
        :param list[str] device_ids: Gets or sets list of device ids for which alerts are generated.
        :param list[str] severity_levels: Gets or sets list of rule severity levels.
        :param str status: Gets or sets alert status.
        :param list[str] ids: Gets ids of the resource.
        :param str partner_id: Gets or sets id of the partner.
        :param datetime min_created_at: Gets or sets minimum creation date of resource (inclusive).
        :param datetime max_created_at: Gets or sets maximum creation date of resource (inclusive).
        :param datetime min_last_modified_at: Gets or sets minimum last modified date of resource (inclusive).
        :param datetime max_last_modified_at: Gets or sets maximum last modified date of resource (inclusive).
        :param int max_items: Gets or sets maximum number of items needed (inclusive).  Maximum items = 5000.
        :return: AlertResponseListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.alert_get_all_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.alert_get_all_with_http_info(**kwargs)  # noqa: E501
            return data

    def alert_get_all_with_http_info(self, **kwargs):  # noqa: E501
        """Returns list of alerts.  # noqa: E501

        based on specified filters and date range. Requires ReadAll privileges.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.alert_get_all_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] rule_ids: Gets or sets list of rule ids for which alerts are generated.
        :param list[str] device_ids: Gets or sets list of device ids for which alerts are generated.
        :param list[str] severity_levels: Gets or sets list of rule severity levels.
        :param str status: Gets or sets alert status.
        :param list[str] ids: Gets ids of the resource.
        :param str partner_id: Gets or sets id of the partner.
        :param datetime min_created_at: Gets or sets minimum creation date of resource (inclusive).
        :param datetime max_created_at: Gets or sets maximum creation date of resource (inclusive).
        :param datetime min_last_modified_at: Gets or sets minimum last modified date of resource (inclusive).
        :param datetime max_last_modified_at: Gets or sets maximum last modified date of resource (inclusive).
        :param int max_items: Gets or sets maximum number of items needed (inclusive).  Maximum items = 5000.
        :return: AlertResponseListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['rule_ids', 'device_ids', 'severity_levels', 'status', 'ids', 'partner_id', 'min_created_at', 'max_created_at', 'min_last_modified_at', 'max_last_modified_at', 'max_items']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method alert_get_all" % key
                )
            params[key] = val
        del params['kwargs']

        if 'max_items' in params and params['max_items'] > 5000:  # noqa: E501
            raise ValueError("Invalid value for parameter `max_items` when calling `alert_get_all`, must be a value less than or equal to `5000`")  # noqa: E501
        if 'max_items' in params and params['max_items'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `max_items` when calling `alert_get_all`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'rule_ids' in params:
            query_params.append(('ruleIds', params['rule_ids']))  # noqa: E501
            collection_formats['ruleIds'] = 'multi'  # noqa: E501
        if 'device_ids' in params:
            query_params.append(('deviceIds', params['device_ids']))  # noqa: E501
            collection_formats['deviceIds'] = 'multi'  # noqa: E501
        if 'severity_levels' in params:
            query_params.append(('severityLevels', params['severity_levels']))  # noqa: E501
            collection_formats['severityLevels'] = 'multi'  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501
        if 'ids' in params:
            query_params.append(('ids', params['ids']))  # noqa: E501
            collection_formats['ids'] = 'multi'  # noqa: E501
        if 'partner_id' in params:
            query_params.append(('PartnerId', params['partner_id']))  # noqa: E501
        if 'min_created_at' in params:
            query_params.append(('minCreatedAt', params['min_created_at']))  # noqa: E501
        if 'max_created_at' in params:
            query_params.append(('maxCreatedAt', params['max_created_at']))  # noqa: E501
        if 'min_last_modified_at' in params:
            query_params.append(('minLastModifiedAt', params['min_last_modified_at']))  # noqa: E501
        if 'max_last_modified_at' in params:
            query_params.append(('maxLastModifiedAt', params['max_last_modified_at']))  # noqa: E501
        if 'max_items' in params:
            query_params.append(('maxItems', params['max_items']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/Alert', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AlertResponseListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def alert_update(self, id, **kwargs):  # noqa: E501
        """Updates the alert with given id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.alert_update(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Id of the alert. (required)
        :param AlertRequest input: Alert request object.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.alert_update_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.alert_update_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def alert_update_with_http_info(self, id, **kwargs):  # noqa: E501
        """Updates the alert with given id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.alert_update_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Id of the alert. (required)
        :param AlertRequest input: Alert request object.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'input']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method alert_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `alert_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'input' in params:
            body_params = params['input']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/Alert/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)