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


class FileMetadataApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_file_metadata(self, body, **kwargs):  # noqa: E501
        """Create file metadata  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_file_metadata(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FileMetadata body: The file metadata to create (required)
        :return: FileMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_file_metadata_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_file_metadata_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_file_metadata_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create file metadata  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_file_metadata_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FileMetadata body: The file metadata to create (required)
        :return: FileMetadata
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
                    " to method create_file_metadata" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `create_file_metadata`")  # noqa: E501

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
            '/file-metadata', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FileMetadata',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_file_metadata(self, file_metadata_id, **kwargs):  # noqa: E501
        """Delete file metadata by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_file_metadata(file_metadata_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int file_metadata_id: The ID of the file metadata to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_file_metadata_with_http_info(file_metadata_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_file_metadata_with_http_info(file_metadata_id, **kwargs)  # noqa: E501
            return data

    def delete_file_metadata_with_http_info(self, file_metadata_id, **kwargs):  # noqa: E501
        """Delete file metadata by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_file_metadata_with_http_info(file_metadata_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int file_metadata_id: The ID of the file metadata to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file_metadata_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_file_metadata" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_metadata_id' is set
        if self.api_client.client_side_validation and ('file_metadata_id' not in params or
                                                       params['file_metadata_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `file_metadata_id` when calling `delete_file_metadata`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'file_metadata_id' in params:
            path_params['fileMetadataId'] = params['file_metadata_id']  # noqa: E501

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
            '/file-metadata/{fileMetadataId}', 'DELETE',
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

    def get_all_file_metadata(self, **kwargs):  # noqa: E501
        """Get all file metadata  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_file_metadata(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_number: The page number for which to get file metadata. This will default to the first page if excluded
        :param int page_size: The maximum number of objects to return. This will default to the DEFAULT_API_PAGE_SIZE property if not provided
        :param int ruleset_id: The ID of the ruleset to get all file metadata from
        :return: FileMetadataList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_file_metadata_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_file_metadata_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_file_metadata_with_http_info(self, **kwargs):  # noqa: E501
        """Get all file metadata  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_file_metadata_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_number: The page number for which to get file metadata. This will default to the first page if excluded
        :param int page_size: The maximum number of objects to return. This will default to the DEFAULT_API_PAGE_SIZE property if not provided
        :param int ruleset_id: The ID of the ruleset to get all file metadata from
        :return: FileMetadataList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_number', 'page_size', 'ruleset_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_file_metadata" % key
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
        if 'ruleset_id' in params:
            query_params.append(('ruleset_id', params['ruleset_id']))  # noqa: E501

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
            '/file-metadata', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FileMetadataList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_file_metadata_by_id(self, file_metadata_id, **kwargs):  # noqa: E501
        """Get file metadata by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_file_metadata_by_id(file_metadata_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int file_metadata_id: The ID of the file metadata to get (required)
        :return: FileMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_file_metadata_by_id_with_http_info(file_metadata_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_file_metadata_by_id_with_http_info(file_metadata_id, **kwargs)  # noqa: E501
            return data

    def get_file_metadata_by_id_with_http_info(self, file_metadata_id, **kwargs):  # noqa: E501
        """Get file metadata by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_file_metadata_by_id_with_http_info(file_metadata_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int file_metadata_id: The ID of the file metadata to get (required)
        :return: FileMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file_metadata_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_file_metadata_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_metadata_id' is set
        if self.api_client.client_side_validation and ('file_metadata_id' not in params or
                                                       params['file_metadata_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `file_metadata_id` when calling `get_file_metadata_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'file_metadata_id' in params:
            path_params['fileMetadataId'] = params['file_metadata_id']  # noqa: E501

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
            '/file-metadata/{fileMetadataId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FileMetadata',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_file_metadata(self, file_metadata_id, body, **kwargs):  # noqa: E501
        """Update file metadata by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_file_metadata(file_metadata_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int file_metadata_id: The ID of the file metadata to update (required)
        :param FileMetadata body: Updated fileMetadata object (required)
        :return: FileMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_file_metadata_with_http_info(file_metadata_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_file_metadata_with_http_info(file_metadata_id, body, **kwargs)  # noqa: E501
            return data

    def update_file_metadata_with_http_info(self, file_metadata_id, body, **kwargs):  # noqa: E501
        """Update file metadata by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_file_metadata_with_http_info(file_metadata_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int file_metadata_id: The ID of the file metadata to update (required)
        :param FileMetadata body: Updated fileMetadata object (required)
        :return: FileMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file_metadata_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_file_metadata" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_metadata_id' is set
        if self.api_client.client_side_validation and ('file_metadata_id' not in params or
                                                       params['file_metadata_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `file_metadata_id` when calling `update_file_metadata`")  # noqa: E501
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `update_file_metadata`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'file_metadata_id' in params:
            path_params['fileMetadataId'] = params['file_metadata_id']  # noqa: E501

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
            '/file-metadata/{fileMetadataId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FileMetadata',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
