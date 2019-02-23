# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from intrinio_sdk.api_client import ApiClient


class StockExchangeApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_all_stock_exchanges(self, **kwargs):  # noqa: E501
        """All Stock Exchanges  # noqa: E501

        Returns all Stock Exchanges. Returns Stock Exchanges matching parameters when specified.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_all_stock_exchanges(_async=True)
        >>> result = thread.get()

        :param async bool
        :param str city: Filter by city
        :param str country: Filter by country
        :param str country_code: Filter by ISO country code
        :param float page_size: The number of results to return
        :return: ApiResponseStockExchanges
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_all_stock_exchanges_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_stock_exchanges_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_stock_exchanges_with_http_info(self, **kwargs):  # noqa: E501
        """All Stock Exchanges  # noqa: E501

        Returns all Stock Exchanges. Returns Stock Exchanges matching parameters when specified.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_all_stock_exchanges_with_http_info(_async=True)
        >>> result = thread.get()

        :param async bool
        :param str city: Filter by city
        :param str country: Filter by country
        :param str country_code: Filter by ISO country code
        :param float page_size: The number of results to return
        :return: ApiResponseStockExchanges
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['city', 'country', 'country_code', 'page_size']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_stock_exchanges" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page_size' in params and params['page_size'] > 10000:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `get_all_stock_exchanges`, must be a value less than or equal to `10000`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'city' in params:
            query_params.append(('city', params['city']))  # noqa: E501
        if 'country' in params:
            query_params.append(('country', params['country']))  # noqa: E501
        if 'country_code' in params:
            query_params.append(('country_code', params['country_code']))  # noqa: E501
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
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/stock_exchanges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseStockExchanges',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_stock_exchange_by_id(self, identifier, **kwargs):  # noqa: E501
        """Lookup Stock Exchange  # noqa: E501

        Returns the Stock Exchange with the given `identifier`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_stock_exchange_by_id(identifier, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: A Stock Exchange identifier (MIC or Intrinio ID) (required)
        :return: StockExchange
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_stock_exchange_by_id_with_http_info(identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_stock_exchange_by_id_with_http_info(identifier, **kwargs)  # noqa: E501
            return data

    def get_stock_exchange_by_id_with_http_info(self, identifier, **kwargs):  # noqa: E501
        """Lookup Stock Exchange  # noqa: E501

        Returns the Stock Exchange with the given `identifier`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_stock_exchange_by_id_with_http_info(identifier, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: A Stock Exchange identifier (MIC or Intrinio ID) (required)
        :return: StockExchange
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_stock_exchange_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_stock_exchange_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/stock_exchanges/{identifier}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StockExchange',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_stock_exchange_price_adjustments(self, identifier, **kwargs):  # noqa: E501
        """Stock Price Adjustments by Exchange  # noqa: E501

        Returns stock price adjustments for the Stock Exchange with the given `identifier`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_stock_exchange_price_adjustments(identifier, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: A Stock Exchange identifier (MIC or Intrinio ID) (required)
        :param date date: The date for which to return price adjustments
        :param float page_size: The number of results to return
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseStockExchangeStockPriceAdjustments
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_stock_exchange_price_adjustments_with_http_info(identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_stock_exchange_price_adjustments_with_http_info(identifier, **kwargs)  # noqa: E501
            return data

    def get_stock_exchange_price_adjustments_with_http_info(self, identifier, **kwargs):  # noqa: E501
        """Stock Price Adjustments by Exchange  # noqa: E501

        Returns stock price adjustments for the Stock Exchange with the given `identifier`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_stock_exchange_price_adjustments_with_http_info(identifier, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: A Stock Exchange identifier (MIC or Intrinio ID) (required)
        :param date date: The date for which to return price adjustments
        :param float page_size: The number of results to return
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseStockExchangeStockPriceAdjustments
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'date', 'page_size', 'next_page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_stock_exchange_price_adjustments" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_stock_exchange_price_adjustments`")  # noqa: E501

        if 'page_size' in params and params['page_size'] > 10000:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `get_stock_exchange_price_adjustments`, must be a value less than or equal to `10000`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'date' in params:
            query_params.append(('date', params['date']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'next_page' in params:
            query_params.append(('next_page', params['next_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/stock_exchanges/{identifier}/prices/adjustments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseStockExchangeStockPriceAdjustments',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_stock_exchange_prices(self, identifier, **kwargs):  # noqa: E501
        """Stock Prices by Exchange  # noqa: E501

        Returns end-of-day stock prices for Securities on the Stock Exchange with `identifier` and on the `price_date` (or the latest date that prices are available)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_stock_exchange_prices(identifier, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: A Stock Exchange identifier (MIC or Intrinio ID) (required)
        :param date date: The date for which to return prices
        :param float page_size: The number of results to return
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseStockExchangeStockPrices
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_stock_exchange_prices_with_http_info(identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_stock_exchange_prices_with_http_info(identifier, **kwargs)  # noqa: E501
            return data

    def get_stock_exchange_prices_with_http_info(self, identifier, **kwargs):  # noqa: E501
        """Stock Prices by Exchange  # noqa: E501

        Returns end-of-day stock prices for Securities on the Stock Exchange with `identifier` and on the `price_date` (or the latest date that prices are available)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_stock_exchange_prices_with_http_info(identifier, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: A Stock Exchange identifier (MIC or Intrinio ID) (required)
        :param date date: The date for which to return prices
        :param float page_size: The number of results to return
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseStockExchangeStockPrices
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'date', 'page_size', 'next_page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_stock_exchange_prices" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_stock_exchange_prices`")  # noqa: E501

        if 'page_size' in params and params['page_size'] > 10000:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `get_stock_exchange_prices`, must be a value less than or equal to `10000`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'date' in params:
            query_params.append(('date', params['date']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'next_page' in params:
            query_params.append(('next_page', params['next_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/stock_exchanges/{identifier}/prices', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseStockExchangeStockPrices',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_stock_exchange_realtime_prices(self, identifier, **kwargs):  # noqa: E501
        """Realtime Stock Prices by Exchange  # noqa: E501

        Returns realtime stock prices for the Stock Exchange with the given `identifier`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_stock_exchange_realtime_prices(identifier, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: A Stock Exchange identifier (MIC or Intrinio ID) (required)
        :param str source: Return realtime prices from the specified data source
        :param float page_size: The number of results to return
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseStockExchangeRealtimeStockPrices
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_stock_exchange_realtime_prices_with_http_info(identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_stock_exchange_realtime_prices_with_http_info(identifier, **kwargs)  # noqa: E501
            return data

    def get_stock_exchange_realtime_prices_with_http_info(self, identifier, **kwargs):  # noqa: E501
        """Realtime Stock Prices by Exchange  # noqa: E501

        Returns realtime stock prices for the Stock Exchange with the given `identifier`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_stock_exchange_realtime_prices_with_http_info(identifier, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: A Stock Exchange identifier (MIC or Intrinio ID) (required)
        :param str source: Return realtime prices from the specified data source
        :param float page_size: The number of results to return
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseStockExchangeRealtimeStockPrices
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'source', 'page_size', 'next_page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_stock_exchange_realtime_prices" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_stock_exchange_realtime_prices`")  # noqa: E501

        if 'page_size' in params and params['page_size'] > 10000:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `get_stock_exchange_realtime_prices`, must be a value less than or equal to `10000`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'source' in params:
            query_params.append(('source', params['source']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'next_page' in params:
            query_params.append(('next_page', params['next_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/stock_exchanges/{identifier}/prices/realtime', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseStockExchangeRealtimeStockPrices',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_stock_exchange_securities(self, identifier, **kwargs):  # noqa: E501
        """Securities by Exchange  # noqa: E501

        Returns Securities traded on the Stock Exchange with `identifier`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_stock_exchange_securities(identifier, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: A Stock Exchange identifier (MIC or Intrinio ID) (required)
        :param float page_size: The number of results to return
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseStockExchangeSecurities
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_stock_exchange_securities_with_http_info(identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_stock_exchange_securities_with_http_info(identifier, **kwargs)  # noqa: E501
            return data

    def get_stock_exchange_securities_with_http_info(self, identifier, **kwargs):  # noqa: E501
        """Securities by Exchange  # noqa: E501

        Returns Securities traded on the Stock Exchange with `identifier`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_stock_exchange_securities_with_http_info(identifier, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: A Stock Exchange identifier (MIC or Intrinio ID) (required)
        :param float page_size: The number of results to return
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseStockExchangeSecurities
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'page_size', 'next_page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_stock_exchange_securities" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_stock_exchange_securities`")  # noqa: E501

        if 'page_size' in params and params['page_size'] > 10000:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `get_stock_exchange_securities`, must be a value less than or equal to `10000`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'next_page' in params:
            query_params.append(('next_page', params['next_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/stock_exchanges/{identifier}/securities', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseStockExchangeSecurities',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
