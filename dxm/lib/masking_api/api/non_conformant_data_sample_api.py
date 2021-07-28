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


class NonConformantDataSampleApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_all_non_conformant_data_samples(self, **kwargs):  # noqa: E501
        """Get all non-conformant data samples  # noqa: E501

        Get redacted data samples associated with non-conforming data execution events.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_non_conformant_data_samples(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] execution_event_id: The ID(s) of the execution event(s) for which to get all non-conformant data samples
        :param int page_number: The page number for which to get non-conformant data samples. This will default to the first page if excluded
        :param int page_size: The maximum number of objects to return. This will default to the DEFAULT_API_PAGE_SIZE property if not provided
        :return: NonConformantDataSampleList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_non_conformant_data_samples_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_non_conformant_data_samples_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_non_conformant_data_samples_with_http_info(self, **kwargs):  # noqa: E501
        """Get all non-conformant data samples  # noqa: E501

        Get redacted data samples associated with non-conforming data execution events.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_non_conformant_data_samples_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] execution_event_id: The ID(s) of the execution event(s) for which to get all non-conformant data samples
        :param int page_number: The page number for which to get non-conformant data samples. This will default to the first page if excluded
        :param int page_size: The maximum number of objects to return. This will default to the DEFAULT_API_PAGE_SIZE property if not provided
        :return: NonConformantDataSampleList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['execution_event_id', 'page_number', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_non_conformant_data_samples" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'execution_event_id' in params:
            query_params.append(('execution_event_id', params['execution_event_id']))  # noqa: E501
            collection_formats['execution_event_id'] = 'multi'  # noqa: E501
        if 'page_number' in params:
            query_params.append(('page_number', params['page_number']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501

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
            '/non-conformant-data-sample', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NonConformantDataSampleList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
