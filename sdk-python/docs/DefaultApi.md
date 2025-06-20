# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_db_structure_debug_db_structure_get**](DefaultApi.md#check_db_structure_debug_db_structure_get) | **GET** /debug/db-structure | Check Db Structure
[**debug_mqtt_storage_debug_mqtt_storage_get**](DefaultApi.md#debug_mqtt_storage_debug_mqtt_storage_get) | **GET** /debug/mqtt-storage | Debug Mqtt Storage
[**debug_services_debug_services_get**](DefaultApi.md#debug_services_debug_services_get) | **GET** /debug/services | Debug Services
[**get_all_messages_debug_all_messages_get**](DefaultApi.md#get_all_messages_debug_all_messages_get) | **GET** /debug/all-messages | Get All Messages
[**mqtt_status_debug_mqtt_status_get**](DefaultApi.md#mqtt_status_debug_mqtt_status_get) | **GET** /debug/mqtt-status | Mqtt Status
[**root_get**](DefaultApi.md#root_get) | **GET** / | Root


# **check_db_structure_debug_db_structure_get**
> object check_db_structure_debug_db_structure_get()

Check Db Structure

Check database structure

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Check Db Structure
        api_response = api_instance.check_db_structure_debug_db_structure_get()
        print("The response of DefaultApi->check_db_structure_debug_db_structure_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->check_db_structure_debug_db_structure_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_mqtt_storage_debug_mqtt_storage_get**
> object debug_mqtt_storage_debug_mqtt_storage_get()

Debug Mqtt Storage

Check if MQTT service has storage service

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Debug Mqtt Storage
        api_response = api_instance.debug_mqtt_storage_debug_mqtt_storage_get()
        print("The response of DefaultApi->debug_mqtt_storage_debug_mqtt_storage_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->debug_mqtt_storage_debug_mqtt_storage_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_services_debug_services_get**
> object debug_services_debug_services_get()

Debug Services

Debug endpoint to check service status

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Debug Services
        api_response = api_instance.debug_services_debug_services_get()
        print("The response of DefaultApi->debug_services_debug_services_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->debug_services_debug_services_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_messages_debug_all_messages_get**
> object get_all_messages_debug_all_messages_get()

Get All Messages

Debug endpoint to see all messages

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Get All Messages
        api_response = api_instance.get_all_messages_debug_all_messages_get()
        print("The response of DefaultApi->get_all_messages_debug_all_messages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_messages_debug_all_messages_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mqtt_status_debug_mqtt_status_get**
> object mqtt_status_debug_mqtt_status_get()

Mqtt Status

Debug endpoint to check MQTT service status

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Mqtt Status
        api_response = api_instance.mqtt_status_debug_mqtt_status_get()
        print("The response of DefaultApi->mqtt_status_debug_mqtt_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->mqtt_status_debug_mqtt_status_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **root_get**
> object root_get()

Root

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Root
        api_response = api_instance.root_get()
        print("The response of DefaultApi->root_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->root_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

