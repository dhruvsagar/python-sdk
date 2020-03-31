# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from intrinio_sdk.api_client import ApiClient


class OptionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_options(self, symbol, **kwargs):  # noqa: E501
        """Options  # noqa: E501

        Returns the master list of option contracts for a given symbol.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_options(symbol, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str symbol: The option symbol, corresponding to the underlying security. (required)
        :param str type: The option contract type.
        :param float strike: The strike price of the option contract. This will return options contracts with strike price equal to this price.
        :param float strike_greater_than: The strike price of the option contract. This will return options contracts with strike prices greater than this price.
        :param float strike_less_than: The strike price of the option contract. This will return options contracts with strike prices less than this price.
        :param str expiration: The expiration date of the option contract. This will return options contracts with expiration dates on this date.
        :param str expiration_after: The expiration date of the option contract. This will return options contracts with expiration dates after this date.
        :param str expiration_before: The expiration date of the option contract. This will return options contracts with expiration dates before this date.
        :param int page_size: The number of results to return
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseOptions
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_options_with_http_info(symbol, **kwargs)  # noqa: E501
        else:
            (data) = self.get_options_with_http_info(symbol, **kwargs)  # noqa: E501
            return data

    def get_options_with_http_info(self, symbol, **kwargs):  # noqa: E501
        """Options  # noqa: E501

        Returns the master list of option contracts for a given symbol.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_options_with_http_info(symbol, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str symbol: The option symbol, corresponding to the underlying security. (required)
        :param str type: The option contract type.
        :param float strike: The strike price of the option contract. This will return options contracts with strike price equal to this price.
        :param float strike_greater_than: The strike price of the option contract. This will return options contracts with strike prices greater than this price.
        :param float strike_less_than: The strike price of the option contract. This will return options contracts with strike prices less than this price.
        :param str expiration: The expiration date of the option contract. This will return options contracts with expiration dates on this date.
        :param str expiration_after: The expiration date of the option contract. This will return options contracts with expiration dates after this date.
        :param str expiration_before: The expiration date of the option contract. This will return options contracts with expiration dates before this date.
        :param int page_size: The number of results to return
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseOptions
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['symbol', 'type', 'strike', 'strike_greater_than', 'strike_less_than', 'expiration', 'expiration_after', 'expiration_before', 'page_size', 'next_page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_options" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'symbol' is set
        if ('symbol' not in params or
                params['symbol'] is None):
            raise ValueError("Missing the required parameter `symbol` when calling `get_options`")  # noqa: E501

        if 'page_size' in params and params['page_size'] > 10000:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `get_options`, must be a value less than or equal to `10000`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'symbol' in params:
            path_params['symbol'] = params['symbol']  # noqa: E501

        query_params = []
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501
        if 'strike' in params:
            query_params.append(('strike', params['strike']))  # noqa: E501
        if 'strike_greater_than' in params:
            query_params.append(('strike_greater_than', params['strike_greater_than']))  # noqa: E501
        if 'strike_less_than' in params:
            query_params.append(('strike_less_than', params['strike_less_than']))  # noqa: E501
        if 'expiration' in params:
            query_params.append(('expiration', params['expiration']))  # noqa: E501
        if 'expiration_after' in params:
            query_params.append(('expiration_after', params['expiration_after']))  # noqa: E501
        if 'expiration_before' in params:
            query_params.append(('expiration_before', params['expiration_before']))  # noqa: E501
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
            '/options/{symbol}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseOptions',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_options_chain(self, symbol, expiration, **kwargs):  # noqa: E501
        """Options Chain  # noqa: E501

        Returns all options contracts and their prices for the given symbol and expiration date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_options_chain(symbol, expiration, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str symbol: The option symbol, corresponding to the underlying security. (required)
        :param str expiration: The expiration date of the options contract (required)
        :param date date: The date of the option price. Returns option prices on this date.
        :param str type: The option contract type.
        :param float strike: The strike price of the option contract. This will return options contracts with strike price equal to this price.
        :param float strike_greater_than: The strike price of the option contract. This will return options contracts with strike prices greater than this price.
        :param float strike_less_than: The strike price of the option contract. This will return options contracts with strike prices less than this price.
        :param str moneyness: The moneyness of the options contracts to return. 'all' will return all options contracts. 'in_the_money' will return options contracts that are in the money (call options with strike prices below the current price, put options with strike prices above the current price). 'out_of_they_money' will return options contracts that are out of the money (call options with strike prices above the current price, put options with strike prices below the current price). 'near_the_money' will return options contracts that are $0.50 or less away from being in the money.
        :param int page_size: The number of results to return
        :return: ApiResponseOptionsChain
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_options_chain_with_http_info(symbol, expiration, **kwargs)  # noqa: E501
        else:
            (data) = self.get_options_chain_with_http_info(symbol, expiration, **kwargs)  # noqa: E501
            return data

    def get_options_chain_with_http_info(self, symbol, expiration, **kwargs):  # noqa: E501
        """Options Chain  # noqa: E501

        Returns all options contracts and their prices for the given symbol and expiration date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_options_chain_with_http_info(symbol, expiration, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str symbol: The option symbol, corresponding to the underlying security. (required)
        :param str expiration: The expiration date of the options contract (required)
        :param date date: The date of the option price. Returns option prices on this date.
        :param str type: The option contract type.
        :param float strike: The strike price of the option contract. This will return options contracts with strike price equal to this price.
        :param float strike_greater_than: The strike price of the option contract. This will return options contracts with strike prices greater than this price.
        :param float strike_less_than: The strike price of the option contract. This will return options contracts with strike prices less than this price.
        :param str moneyness: The moneyness of the options contracts to return. 'all' will return all options contracts. 'in_the_money' will return options contracts that are in the money (call options with strike prices below the current price, put options with strike prices above the current price). 'out_of_they_money' will return options contracts that are out of the money (call options with strike prices above the current price, put options with strike prices below the current price). 'near_the_money' will return options contracts that are $0.50 or less away from being in the money.
        :param int page_size: The number of results to return
        :return: ApiResponseOptionsChain
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['symbol', 'expiration', 'date', 'type', 'strike', 'strike_greater_than', 'strike_less_than', 'moneyness', 'page_size']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_options_chain" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'symbol' is set
        if ('symbol' not in params or
                params['symbol'] is None):
            raise ValueError("Missing the required parameter `symbol` when calling `get_options_chain`")  # noqa: E501
        # verify the required parameter 'expiration' is set
        if ('expiration' not in params or
                params['expiration'] is None):
            raise ValueError("Missing the required parameter `expiration` when calling `get_options_chain`")  # noqa: E501

        if 'page_size' in params and params['page_size'] > 10000:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `get_options_chain`, must be a value less than or equal to `10000`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'symbol' in params:
            path_params['symbol'] = params['symbol']  # noqa: E501
        if 'expiration' in params:
            path_params['expiration'] = params['expiration']  # noqa: E501

        query_params = []
        if 'date' in params:
            query_params.append(('date', params['date']))  # noqa: E501
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501
        if 'strike' in params:
            query_params.append(('strike', params['strike']))  # noqa: E501
        if 'strike_greater_than' in params:
            query_params.append(('strike_greater_than', params['strike_greater_than']))  # noqa: E501
        if 'strike_less_than' in params:
            query_params.append(('strike_less_than', params['strike_less_than']))  # noqa: E501
        if 'moneyness' in params:
            query_params.append(('moneyness', params['moneyness']))  # noqa: E501
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
            '/options/chain/{symbol}/{expiration}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseOptionsChain',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_options_expirations(self, symbol, **kwargs):  # noqa: E501
        """Options Expirations  # noqa: E501

        Returns all option contract expiration dates for a given symbol.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_options_expirations(symbol, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str symbol: The option symbol, corresponding to the underlying security. (required)
        :param str after: Return option contract expiration dates after this date.
        :param str before: Return option contract expiration dates before this date.
        :return: ApiResponseOptionsExpirations
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_options_expirations_with_http_info(symbol, **kwargs)  # noqa: E501
        else:
            (data) = self.get_options_expirations_with_http_info(symbol, **kwargs)  # noqa: E501
            return data

    def get_options_expirations_with_http_info(self, symbol, **kwargs):  # noqa: E501
        """Options Expirations  # noqa: E501

        Returns all option contract expiration dates for a given symbol.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_options_expirations_with_http_info(symbol, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str symbol: The option symbol, corresponding to the underlying security. (required)
        :param str after: Return option contract expiration dates after this date.
        :param str before: Return option contract expiration dates before this date.
        :return: ApiResponseOptionsExpirations
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['symbol', 'after', 'before']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_options_expirations" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'symbol' is set
        if ('symbol' not in params or
                params['symbol'] is None):
            raise ValueError("Missing the required parameter `symbol` when calling `get_options_expirations`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'symbol' in params:
            path_params['symbol'] = params['symbol']  # noqa: E501

        query_params = []
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501
        if 'before' in params:
            query_params.append(('before', params['before']))  # noqa: E501

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
            '/options/expirations/{symbol}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseOptionsExpirations',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_options_prices(self, identifier, **kwargs):  # noqa: E501
        """Option Prices  # noqa: E501

        Returns all option prices for a given option contract identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_options_prices(identifier, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: The Intrinio ID or code of the options contract to request prices for. (required)
        :param str start_date: Return option contract prices on or after this date.
        :param str end_date: Return option contract prices on or before this date.
        :param int page_size: The number of results to return
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseOptionPrices
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_options_prices_with_http_info(identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_options_prices_with_http_info(identifier, **kwargs)  # noqa: E501
            return data

    def get_options_prices_with_http_info(self, identifier, **kwargs):  # noqa: E501
        """Option Prices  # noqa: E501

        Returns all option prices for a given option contract identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_options_prices_with_http_info(identifier, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: The Intrinio ID or code of the options contract to request prices for. (required)
        :param str start_date: Return option contract prices on or after this date.
        :param str end_date: Return option contract prices on or before this date.
        :param int page_size: The number of results to return
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseOptionPrices
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'start_date', 'end_date', 'page_size', 'next_page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_options_prices" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_options_prices`")  # noqa: E501

        if 'page_size' in params and params['page_size'] > 10000:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `get_options_prices`, must be a value less than or equal to `10000`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'start_date' in params:
            query_params.append(('start_date', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('end_date', params['end_date']))  # noqa: E501
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
            '/options/prices/{identifier}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseOptionPrices',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
