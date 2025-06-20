# openapi_client.SMSApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_inbox_sms_inbox_get**](SMSApi.md#get_inbox_sms_inbox_get) | **GET** /sms/inbox | Lister tous les SMS reçus
[**get_logs_logs_get**](SMSApi.md#get_logs_logs_get) | **GET** /logs | Voir les logs des SMS
[**get_sent_messages_sms_sent_get**](SMSApi.md#get_sent_messages_sms_sent_get) | **GET** /sms/sent | Lister tous les SMS envoyés
[**send_sms_sms_post**](SMSApi.md#send_sms_sms_post) | **POST** /sms | Envoyer un SMS
[**simulate_received_sms_sms_simulate_receive_post**](SMSApi.md#simulate_received_sms_sms_simulate_receive_post) | **POST** /sms/simulate-receive | Simulate Received Sms


# **get_inbox_sms_inbox_get**
> List[SmsResponse] get_inbox_sms_inbox_get(limit=limit)

Lister tous les SMS reçus

Récupère tous les SMS reçus.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import openapi_client
from openapi_client.models.sms_response import SmsResponse
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SMSApi(api_client)
    limit = 56 # int | Nombre maximum de SMS à retourner (optional)

    try:
        # Lister tous les SMS reçus
        api_response = api_instance.get_inbox_sms_inbox_get(limit=limit)
        print("The response of SMSApi->get_inbox_sms_inbox_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->get_inbox_sms_inbox_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Nombre maximum de SMS à retourner | [optional] 

### Return type

[**List[SmsResponse]**](SmsResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logs_logs_get**
> List[Dict[str, object]] get_logs_logs_get(limit=limit, level=level, component=component)

Voir les logs des SMS

Récupère l'historique et le statut de tous les SMS envoyés.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SMSApi(api_client)
    limit = 56 # int | Nombre maximum de logs à retourner (optional)
    level = 'level_example' # str | Filtre par niveau de log (INFO, WARNING, ERROR, etc.) (optional)
    component = 'component_example' # str | Filtre par composant (optional)

    try:
        # Voir les logs des SMS
        api_response = api_instance.get_logs_logs_get(limit=limit, level=level, component=component)
        print("The response of SMSApi->get_logs_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->get_logs_logs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Nombre maximum de logs à retourner | [optional] 
 **level** | **str**| Filtre par niveau de log (INFO, WARNING, ERROR, etc.) | [optional] 
 **component** | **str**| Filtre par composant | [optional] 

### Return type

**List[Dict[str, object]]**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sent_messages_sms_sent_get**
> List[SmsResponse] get_sent_messages_sms_sent_get(limit=limit)

Lister tous les SMS envoyés

Récupère tous les SMS envoyés par l'utilisateur actuel.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import openapi_client
from openapi_client.models.sms_response import SmsResponse
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SMSApi(api_client)
    limit = 56 # int | Nombre maximum de SMS à retourner (optional)

    try:
        # Lister tous les SMS envoyés
        api_response = api_instance.get_sent_messages_sms_sent_get(limit=limit)
        print("The response of SMSApi->get_sent_messages_sms_sent_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->get_sent_messages_sms_sent_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Nombre maximum de SMS à retourner | [optional] 

### Return type

[**List[SmsResponse]**](SmsResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_sms_sms_post**
> SmsResponse send_sms_sms_post(sms_create)

Envoyer un SMS

Envoie un SMS au numéro spécifié.

- **phone_number**: Numéro complet avec indicatif international
- **message**: Contenu du SMS à envoyer

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import openapi_client
from openapi_client.models.sms_create import SmsCreate
from openapi_client.models.sms_response import SmsResponse
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SMSApi(api_client)
    sms_create = openapi_client.SmsCreate() # SmsCreate | 

    try:
        # Envoyer un SMS
        api_response = api_instance.send_sms_sms_post(sms_create)
        print("The response of SMSApi->send_sms_sms_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->send_sms_sms_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sms_create** | [**SmsCreate**](SmsCreate.md)|  | 

### Return type

[**SmsResponse**](SmsResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simulate_received_sms_sms_simulate_receive_post**
> SmsResponse simulate_received_sms_sms_simulate_receive_post(phone_number, message)

Simulate Received Sms

Simule la réception d'un SMS (uniquement pour les tests/développement).

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import openapi_client
from openapi_client.models.sms_response import SmsResponse
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SMSApi(api_client)
    phone_number = 'phone_number_example' # str | Numéro de téléphone de l'expéditeur
    message = 'message_example' # str | Contenu du message reçu

    try:
        # Simulate Received Sms
        api_response = api_instance.simulate_received_sms_sms_simulate_receive_post(phone_number, message)
        print("The response of SMSApi->simulate_received_sms_sms_simulate_receive_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->simulate_received_sms_sms_simulate_receive_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number** | **str**| Numéro de téléphone de l&#39;expéditeur | 
 **message** | **str**| Contenu du message reçu | 

### Return type

[**SmsResponse**](SmsResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

