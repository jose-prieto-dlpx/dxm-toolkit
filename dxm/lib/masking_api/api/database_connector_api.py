# coding: utf-8

"""
    Masking API

    Schema for the Masking Engine API  # noqa: E501

    OpenAPI spec version: 5.1.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from dxm.lib.masking_api.api_client import ApiClient


class DatabaseConnectorApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_database_connector(self, body, **kwargs):  # noqa: E501
        """Create database connector  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_database_connector(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DatabaseConnector body: The database connector to create (required)
        :return: DatabaseConnector
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_database_connector_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_database_connector_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_database_connector_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create database connector  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_database_connector_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DatabaseConnector body: The database connector to create (required)
        :return: DatabaseConnector
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_database_connector" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `create_database_connector`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/database-connectors', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DatabaseConnector',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_database_connector(self, database_connector_id, **kwargs):  # noqa: E501
        """Delete database connector by ID  # noqa: E501

        Deletes database connector with given ID. This will also delete all rule sets and jobs which are using this connector.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_database_connector(database_connector_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int database_connector_id: The ID of the database connector to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_database_connector_with_http_info(database_connector_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_database_connector_with_http_info(database_connector_id, **kwargs)  # noqa: E501
            return data

    def delete_database_connector_with_http_info(self, database_connector_id, **kwargs):  # noqa: E501
        """Delete database connector by ID  # noqa: E501

        Deletes database connector with given ID. This will also delete all rule sets and jobs which are using this connector.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_database_connector_with_http_info(database_connector_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int database_connector_id: The ID of the database connector to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['database_connector_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_database_connector" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'database_connector_id' is set
        if self.api_client.client_side_validation and ('database_connector_id' not in params or
                                                       params['database_connector_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `database_connector_id` when calling `delete_database_connector`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'database_connector_id' in params:
            path_params['databaseConnectorId'] = params['database_connector_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/database-connectors/{databaseConnectorId}', 'DELETE',
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

    def fetch_table_metadata(self, database_connector_id, **kwargs):  # noqa: E501
        """Fetch all accessible table names  # noqa: E501

        Note that only the names of tables that are accessible by the database user will be returned  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_table_metadata(database_connector_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int database_connector_id: The ID of the database connector to fetch the tables for (required)
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_table_metadata_with_http_info(database_connector_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_table_metadata_with_http_info(database_connector_id, **kwargs)  # noqa: E501
            return data

    def fetch_table_metadata_with_http_info(self, database_connector_id, **kwargs):  # noqa: E501
        """Fetch all accessible table names  # noqa: E501

        Note that only the names of tables that are accessible by the database user will be returned  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_table_metadata_with_http_info(database_connector_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int database_connector_id: The ID of the database connector to fetch the tables for (required)
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['database_connector_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_table_metadata" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'database_connector_id' is set
        if self.api_client.client_side_validation and ('database_connector_id' not in params or
                                                       params['database_connector_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `database_connector_id` when calling `fetch_table_metadata`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'database_connector_id' in params:
            path_params['databaseConnectorId'] = params['database_connector_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/database-connectors/{databaseConnectorId}/fetch', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_database_connectors(self, **kwargs):  # noqa: E501
        """Get all database connectors  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_database_connectors(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_number: The page number for which to get database connectors. This will default to the first page if excluded
        :param int page_size: The maximum number of objects to return. This will default to the DEFAULT_API_PAGE_SIZE property if not provided
        :param int environment_id: The ID of the environment to get all database connectors from
        :return: DatabaseConnectorList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_database_connectors_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_database_connectors_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_database_connectors_with_http_info(self, **kwargs):  # noqa: E501
        """Get all database connectors  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_database_connectors_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_number: The page number for which to get database connectors. This will default to the first page if excluded
        :param int page_size: The maximum number of objects to return. This will default to the DEFAULT_API_PAGE_SIZE property if not provided
        :param int environment_id: The ID of the environment to get all database connectors from
        :return: DatabaseConnectorList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_number', 'page_size', 'environment_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_database_connectors" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_number' in params:
            query_params.append(('page_number', params['page_number']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'environment_id' in params:
            query_params.append(('environment_id', params['environment_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/database-connectors', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DatabaseConnectorList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_connection_properties(self, database_connector_id, **kwargs):  # noqa: E501
        """Get connection properties for database connector by ID  # noqa: E501

        A list of properties provided through the connection properties file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_connection_properties(database_connector_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int database_connector_id: The ID of the database connector to retrieve connection properties (required)
        :return: ConnectionPropertiesList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_connection_properties_with_http_info(database_connector_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_connection_properties_with_http_info(database_connector_id, **kwargs)  # noqa: E501
            return data

    def get_connection_properties_with_http_info(self, database_connector_id, **kwargs):  # noqa: E501
        """Get connection properties for database connector by ID  # noqa: E501

        A list of properties provided through the connection properties file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_connection_properties_with_http_info(database_connector_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int database_connector_id: The ID of the database connector to retrieve connection properties (required)
        :return: ConnectionPropertiesList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['database_connector_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_connection_properties" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'database_connector_id' is set
        if self.api_client.client_side_validation and ('database_connector_id' not in params or
                                                       params['database_connector_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `database_connector_id` when calling `get_connection_properties`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'database_connector_id' in params:
            path_params['databaseConnectorId'] = params['database_connector_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/database-connectors/{databaseConnectorId}/properties', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConnectionPropertiesList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_database_connector_by_id(self, database_connector_id, **kwargs):  # noqa: E501
        """Get database connector by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_database_connector_by_id(database_connector_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int database_connector_id: The ID of the database connector to get (required)
        :return: DatabaseConnector
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_database_connector_by_id_with_http_info(database_connector_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_database_connector_by_id_with_http_info(database_connector_id, **kwargs)  # noqa: E501
            return data

    def get_database_connector_by_id_with_http_info(self, database_connector_id, **kwargs):  # noqa: E501
        """Get database connector by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_database_connector_by_id_with_http_info(database_connector_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int database_connector_id: The ID of the database connector to get (required)
        :return: DatabaseConnector
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['database_connector_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_database_connector_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'database_connector_id' is set
        if self.api_client.client_side_validation and ('database_connector_id' not in params or
                                                       params['database_connector_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `database_connector_id` when calling `get_database_connector_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'database_connector_id' in params:
            path_params['databaseConnectorId'] = params['database_connector_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/database-connectors/{databaseConnectorId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DatabaseConnector',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def test_database_connector(self, database_connector_id, **kwargs):  # noqa: E501
        """Test database connector by ID  # noqa: E501

        WARNING: There is a known bug in the API Client where it is impossible to submit a request with an 'empty' body. As such, only the 'full' body variant of this endpoint can be used through the API Client. To use the 'empty' body variant of this endpoint, please do not use the API Client, but instead use curl or some other method of issuing HTTP requests.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.test_database_connector(database_connector_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int database_connector_id: The ID of the database connector to test (required)
        :param DatabaseConnector body: The database connector to test. This field is optional and if no password is supplied with the connector then the password associated with the databaseConnectorId will be used.
        :return: TestConnectorResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.test_database_connector_with_http_info(database_connector_id, **kwargs)  # noqa: E501
        else:
            (data) = self.test_database_connector_with_http_info(database_connector_id, **kwargs)  # noqa: E501
            return data

    def test_database_connector_with_http_info(self, database_connector_id, **kwargs):  # noqa: E501
        """Test database connector by ID  # noqa: E501

        WARNING: There is a known bug in the API Client where it is impossible to submit a request with an 'empty' body. As such, only the 'full' body variant of this endpoint can be used through the API Client. To use the 'empty' body variant of this endpoint, please do not use the API Client, but instead use curl or some other method of issuing HTTP requests.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.test_database_connector_with_http_info(database_connector_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int database_connector_id: The ID of the database connector to test (required)
        :param DatabaseConnector body: The database connector to test. This field is optional and if no password is supplied with the connector then the password associated with the databaseConnectorId will be used.
        :return: TestConnectorResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['database_connector_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method test_database_connector" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'database_connector_id' is set
        if self.api_client.client_side_validation and ('database_connector_id' not in params or
                                                       params['database_connector_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `database_connector_id` when calling `test_database_connector`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'database_connector_id' in params:
            path_params['databaseConnectorId'] = params['database_connector_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/database-connectors/{databaseConnectorId}/test', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TestConnectorResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def test_unsaved_database_connector(self, body, **kwargs):  # noqa: E501
        """Test an unsaved database connector  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.test_unsaved_database_connector(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DatabaseConnector body: The database connector to test (required)
        :return: TestConnectorResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.test_unsaved_database_connector_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.test_unsaved_database_connector_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def test_unsaved_database_connector_with_http_info(self, body, **kwargs):  # noqa: E501
        """Test an unsaved database connector  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.test_unsaved_database_connector_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DatabaseConnector body: The database connector to test (required)
        :return: TestConnectorResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method test_unsaved_database_connector" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `test_unsaved_database_connector`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/database-connectors/test', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TestConnectorResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_database_connector(self, database_connector_id, body, **kwargs):  # noqa: E501
        """Update database connector by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_database_connector(database_connector_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int database_connector_id: The ID of the database connector to update (required)
        :param DatabaseConnector body: The updated database connector (required)
        :return: DatabaseConnector
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_database_connector_with_http_info(database_connector_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_database_connector_with_http_info(database_connector_id, body, **kwargs)  # noqa: E501
            return data

    def update_database_connector_with_http_info(self, database_connector_id, body, **kwargs):  # noqa: E501
        """Update database connector by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_database_connector_with_http_info(database_connector_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int database_connector_id: The ID of the database connector to update (required)
        :param DatabaseConnector body: The updated database connector (required)
        :return: DatabaseConnector
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['database_connector_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_database_connector" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'database_connector_id' is set
        if self.api_client.client_side_validation and ('database_connector_id' not in params or
                                                       params['database_connector_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `database_connector_id` when calling `update_database_connector`")  # noqa: E501
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `update_database_connector`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'database_connector_id' in params:
            path_params['databaseConnectorId'] = params['database_connector_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/database-connectors/{databaseConnectorId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DatabaseConnector',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
