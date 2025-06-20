# openapi_client.AdminApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_messages_admin_messages_get**](AdminApi.md#list_messages_admin_messages_get) | **GET** /admin/messages | List Messages
[**list_users_admin_users_get**](AdminApi.md#list_users_admin_users_get) | **GET** /admin/users | List Users


# **list_messages_admin_messages_get**
> List[Dict[str, object]] list_messages_admin_messages_get()

List Messages

List all messages in the database (admin only)

### Example

* Api Key Authentication (APIKeyHeader):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AdminApi(api_client)

    try:
        # List Messages
        api_response = api_instance.list_messages_admin_messages_get()
        print("The response of AdminApi->list_messages_admin_messages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->list_messages_admin_messages_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[Dict[str, object]]**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users_admin_users_get**
> List[Dict[str, object]] list_users_admin_users_get()

List Users

List all users in the database (admin only)

### Example

* Api Key Authentication (APIKeyHeader):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AdminApi(api_client)

    try:
        # List Users
        api_response = api_instance.list_users_admin_users_get()
        print("The response of AdminApi->list_users_admin_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->list_users_admin_users_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[Dict[str, object]]**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

