# coding: utf-8

"""
    Azure FarmBeats API

    <p>  <p>Azure FarmBeats helps you build digital agricultural solutions in Azure. By providing a standardized schema to query agricultural data from various sources, Azure FarmBeats provides you:  <ul >   <li style=\"margin: 7px;\">Ability to acquire, aggregate, process and store agricultural data.</li>   <li style=\"margin: 7px;\">Capability to fuse data between data sources and generate insights.</li>   <li style=\"margin: 7px;\">Schematized access and query capabilities on ingested data.</li>  </ul>  </p>  <h><b>REST Operation Groups</b></h>  <p><b>Farm:</b></p>  <p>Farm corresponds to a physical location of interest within the system. Each Farm has a Farm name and a unique farm id.</p>  <p><b>Device:</b></p>  <p>Device corresponds to a physical device present in the farm. Each device has a unique device id. Device is typically provisioned to a farm with a farm id.</p>  <p><b>DeviceModel:</b></p>  <p>DeviceModel corresponds to the meta-data of the device such as the Manufacturer, Type of the device either Gateway or Node.</p>  <p><b>Sensor:</b></p>  <p>Sensor corresponds to a physical sensor that records values. A sensor is typically connected to a device with a device id.</p>  </p>  <p><b>SensorModel:</b></p>  <p>SensorModel corresponds to the meta-data of the sensor such as the Manufacturer, Type of the sensor either Analog or Digital, Sensor Measure such as Ambient Temperature, Pressure etc.</p>  <p><b>Telemetry:</b></p>  <p>Telemetry provides the ability to read telemetry messages for a particular sensor & time range.</p>  <p><b>Job:</b></p>  <p>Job corresponds to any workflow of activities which are executed in the system to get a desired output. Each job is associated with a job id and job type.</p>  <p><b>JobType:</b></p>  <p>JobType corresponds to different job types supported by the system. This includes system defined & user-defined job types.</p>  <p><b>ExtendedType:</b></p>  <p>ExtendedType corresponds to the list of system & user-defined types in the system. This helps setup a new Sensor or Scene or Scenefile type in the system.</p>  <p><b>Partner:</b></p>  <p>Partner corresponds to the sensor/weather/imagery integration partner.</p>  <p><b>Scene:</b></p>  <p>Scene corresponds to any generated output in the context of a Farm. Each Scene has a scene id, scene source, scene type and farm id associated with it. Each scene id  can have multiple scene files associated with it.</p>  <p><b>SceneFile:</b></p>  <p>SceneFile corresponds to all files which are generated for single scene. A single scene id can have multiple SceneFile ids associated with it.</p>  <p><b>Rule:</b></p>  <p>Rule corresponds to a condition for farm-related data to trigger an alert. Each rule will be in the context of a farm's data.</p>  <p><b>Alert:</b></p>  <p>Alert corresponds to a notification which gets generated when a rule condition is met. Each alert will be in the context of a rule.</p>  <p><b>RoleDefinition:</b></p>  <p>RoleDefinition defines allowed and disallowed actions for a role.</p>  <p><b>RoleAssignment:</b></p>  <p>RoleAssignment corresponds to the assignment of a role to a user or a service principal.</p>  <p><b>WeatherDataModel:</b></p>  <p>WeatherDataModel corresponds to the metadata of the Weather Station such as name and weather measures such as Precipitation, Rainfall etc.</p>  <p><b>WeatherDataLocation:</b></p>  <p>WeatherDataLocation corresponds to the instance of Weather Station for a particular location (latitude/longitude).</p>  </p>    # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from datahub_lib.swagger_client.api_client import ApiClient
from datahub_lib.swagger_client.exceptions import (
    ApiTypeError,
    ApiValueError
)


class SceneFileApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def scene_file_create(self, **kwargs):  # noqa: E501
        """Creates new scene file with given request body.  # noqa: E501

        User need to use blobPath or uploadSASUrl to save actual content of file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scene_file_create(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param SceneFileRequest input: User's scene file request.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CreateSceneFileResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.scene_file_create_with_http_info(**kwargs)  # noqa: E501

    def scene_file_create_with_http_info(self, **kwargs):  # noqa: E501
        """Creates new scene file with given request body.  # noqa: E501

        User need to use blobPath or uploadSASUrl to save actual content of file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scene_file_create_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param SceneFileRequest input: User's scene file request.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CreateSceneFileResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['input']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method scene_file_create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'input' in local_var_params:
            body_params = local_var_params['input']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/SceneFile', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateSceneFileResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def scene_file_delete(self, id, **kwargs):  # noqa: E501
        """Deletes scene file with given id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scene_file_delete(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: Id of scene file to be deleted. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.scene_file_delete_with_http_info(id, **kwargs)  # noqa: E501

    def scene_file_delete_with_http_info(self, id, **kwargs):  # noqa: E501
        """Deletes scene file with given id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scene_file_delete_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: Id of scene file to be deleted. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method scene_file_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `scene_file_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/SceneFile/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def scene_file_get(self, id, **kwargs):  # noqa: E501
        """Returns scene file for the given id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scene_file_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: scene file id (system-generated). (required)
        :param bool generate_download_sas_url: Specify if SAS URL need to be generated to download content of a file (Default: false).
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: GetSceneFileResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.scene_file_get_with_http_info(id, **kwargs)  # noqa: E501

    def scene_file_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Returns scene file for the given id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scene_file_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: scene file id (system-generated). (required)
        :param bool generate_download_sas_url: Specify if SAS URL need to be generated to download content of a file (Default: false).
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(GetSceneFileResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'generate_download_sas_url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method scene_file_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `scene_file_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'generate_download_sas_url' in local_var_params and local_var_params['generate_download_sas_url'] is not None:  # noqa: E501
            query_params.append(('generateDownloadSASUrl', local_var_params['generate_download_sas_url']))  # noqa: E501

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
            '/SceneFile/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetSceneFileResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def scene_file_get_all(self, **kwargs):  # noqa: E501
        """Returns list of scene file.  # noqa: E501

        If generateDownloadSASUrl is true and there are more than 10 scene files then it will throw BadRequest with HTTP status code 400.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scene_file_get_all(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[str] types: Gets or sets list of types of scene files.  <remark>Refer /ExtendedType APIs with key \"SceneFileType\" for more information.</remark>
        :param list[str] content_types: Gets or sets list of content types of scene files.  <remark>Refer /ExtendedType APIs with key \"SceneFileContentType\" for more information.</remark>
        :param str scene_id: Gets or sets scene id of scene files.
        :param bool generate_download_sas_url: Gets or sets a value indicating whether download SAS URLs need to be generated.
        :param list[str] names: Gets or sets list of names of scene files which is specified while creating a scene file.
        :param list[str] includes: Gets or sets list of properties to be included in SceneFileResponse. Default value is None.
        :param list[str] ids: Gets or sets ids of the resource.
        :param str partner_id: Gets or sets id of the partner.
        :param datetime min_created_at: Gets or sets minimum creation date of resource (inclusive).
        :param datetime max_created_at: Gets or sets maximum creation date of resource (inclusive).
        :param datetime min_last_modified_at: Gets or sets minimum last modified date of resource (inclusive).
        :param datetime max_last_modified_at: Gets or sets maximum last modified date of resource (inclusive).
        :param str property_filter: Gets or sets property filter query.eg. \"x.y.z eq 'somestringvalue' and p.q gt 5 and a eq false\".  Only AND operation is supported.  Supported Operators: EQ,NE,LE,LT,GT,GE,CONTAINS,NCONTAINS.
        :param int max_items: Gets or sets maximum number of items needed (inclusive).  Maximum items = 1000.
        :param str x_ms_continuation: Gets or sets continuation token.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: GetSceneFileResponseListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.scene_file_get_all_with_http_info(**kwargs)  # noqa: E501

    def scene_file_get_all_with_http_info(self, **kwargs):  # noqa: E501
        """Returns list of scene file.  # noqa: E501

        If generateDownloadSASUrl is true and there are more than 10 scene files then it will throw BadRequest with HTTP status code 400.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scene_file_get_all_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[str] types: Gets or sets list of types of scene files.  <remark>Refer /ExtendedType APIs with key \"SceneFileType\" for more information.</remark>
        :param list[str] content_types: Gets or sets list of content types of scene files.  <remark>Refer /ExtendedType APIs with key \"SceneFileContentType\" for more information.</remark>
        :param str scene_id: Gets or sets scene id of scene files.
        :param bool generate_download_sas_url: Gets or sets a value indicating whether download SAS URLs need to be generated.
        :param list[str] names: Gets or sets list of names of scene files which is specified while creating a scene file.
        :param list[str] includes: Gets or sets list of properties to be included in SceneFileResponse. Default value is None.
        :param list[str] ids: Gets or sets ids of the resource.
        :param str partner_id: Gets or sets id of the partner.
        :param datetime min_created_at: Gets or sets minimum creation date of resource (inclusive).
        :param datetime max_created_at: Gets or sets maximum creation date of resource (inclusive).
        :param datetime min_last_modified_at: Gets or sets minimum last modified date of resource (inclusive).
        :param datetime max_last_modified_at: Gets or sets maximum last modified date of resource (inclusive).
        :param str property_filter: Gets or sets property filter query.eg. \"x.y.z eq 'somestringvalue' and p.q gt 5 and a eq false\".  Only AND operation is supported.  Supported Operators: EQ,NE,LE,LT,GT,GE,CONTAINS,NCONTAINS.
        :param int max_items: Gets or sets maximum number of items needed (inclusive).  Maximum items = 1000.
        :param str x_ms_continuation: Gets or sets continuation token.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(GetSceneFileResponseListResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['types', 'content_types', 'scene_id', 'generate_download_sas_url', 'names', 'includes', 'ids', 'partner_id', 'min_created_at', 'max_created_at', 'min_last_modified_at', 'max_last_modified_at', 'property_filter', 'max_items', 'x_ms_continuation']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method scene_file_get_all" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'max_items' in local_var_params and local_var_params['max_items'] > 1000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `max_items` when calling `scene_file_get_all`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and 'max_items' in local_var_params and local_var_params['max_items'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `max_items` when calling `scene_file_get_all`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'types' in local_var_params and local_var_params['types'] is not None:  # noqa: E501
            query_params.append(('types', local_var_params['types']))  # noqa: E501
            collection_formats['types'] = 'multi'  # noqa: E501
        if 'content_types' in local_var_params and local_var_params['content_types'] is not None:  # noqa: E501
            query_params.append(('contentTypes', local_var_params['content_types']))  # noqa: E501
            collection_formats['contentTypes'] = 'multi'  # noqa: E501
        if 'scene_id' in local_var_params and local_var_params['scene_id'] is not None:  # noqa: E501
            query_params.append(('sceneId', local_var_params['scene_id']))  # noqa: E501
        if 'generate_download_sas_url' in local_var_params and local_var_params['generate_download_sas_url'] is not None:  # noqa: E501
            query_params.append(('generateDownloadSASUrl', local_var_params['generate_download_sas_url']))  # noqa: E501
        if 'names' in local_var_params and local_var_params['names'] is not None:  # noqa: E501
            query_params.append(('names', local_var_params['names']))  # noqa: E501
            collection_formats['names'] = 'multi'  # noqa: E501
        if 'includes' in local_var_params and local_var_params['includes'] is not None:  # noqa: E501
            query_params.append(('includes', local_var_params['includes']))  # noqa: E501
            collection_formats['includes'] = 'multi'  # noqa: E501
        if 'ids' in local_var_params and local_var_params['ids'] is not None:  # noqa: E501
            query_params.append(('ids', local_var_params['ids']))  # noqa: E501
            collection_formats['ids'] = 'multi'  # noqa: E501
        if 'partner_id' in local_var_params and local_var_params['partner_id'] is not None:  # noqa: E501
            query_params.append(('PartnerId', local_var_params['partner_id']))  # noqa: E501
        if 'min_created_at' in local_var_params and local_var_params['min_created_at'] is not None:  # noqa: E501
            query_params.append(('minCreatedAt', local_var_params['min_created_at']))  # noqa: E501
        if 'max_created_at' in local_var_params and local_var_params['max_created_at'] is not None:  # noqa: E501
            query_params.append(('maxCreatedAt', local_var_params['max_created_at']))  # noqa: E501
        if 'min_last_modified_at' in local_var_params and local_var_params['min_last_modified_at'] is not None:  # noqa: E501
            query_params.append(('minLastModifiedAt', local_var_params['min_last_modified_at']))  # noqa: E501
        if 'max_last_modified_at' in local_var_params and local_var_params['max_last_modified_at'] is not None:  # noqa: E501
            query_params.append(('maxLastModifiedAt', local_var_params['max_last_modified_at']))  # noqa: E501
        if 'property_filter' in local_var_params and local_var_params['property_filter'] is not None:  # noqa: E501
            query_params.append(('propertyFilter', local_var_params['property_filter']))  # noqa: E501
        if 'max_items' in local_var_params and local_var_params['max_items'] is not None:  # noqa: E501
            query_params.append(('maxItems', local_var_params['max_items']))  # noqa: E501

        header_params = {}
        if 'x_ms_continuation' in local_var_params:
            header_params['x-ms-continuation'] = local_var_params['x_ms_continuation']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/SceneFile', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetSceneFileResponseListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def scene_file_update(self, id, **kwargs):  # noqa: E501
        """Updates scene file with given id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scene_file_update(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: Id of scene file to be updated. (required)
        :param SceneFileRequest input: New state of scene file.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.scene_file_update_with_http_info(id, **kwargs)  # noqa: E501

    def scene_file_update_with_http_info(self, id, **kwargs):  # noqa: E501
        """Updates scene file with given id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scene_file_update_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: Id of scene file to be updated. (required)
        :param SceneFileRequest input: New state of scene file.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'input']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method scene_file_update" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `scene_file_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'input' in local_var_params:
            body_params = local_var_params['input']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/SceneFile/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
