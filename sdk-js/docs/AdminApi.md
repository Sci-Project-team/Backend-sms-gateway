# SmsGatewayApi.AdminApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listMessagesAdminMessagesGet**](AdminApi.md#listMessagesAdminMessagesGet) | **GET** /admin/messages | List Messages
[**listUsersAdminUsersGet**](AdminApi.md#listUsersAdminUsersGet) | **GET** /admin/users | List Users



## listMessagesAdminMessagesGet

> [{String: Object}] listMessagesAdminMessagesGet()

List Messages

List all messages in the database (admin only)

### Example

```javascript
import SmsGatewayApi from 'sms_gateway_api';
let defaultClient = SmsGatewayApi.ApiClient.instance;
// Configure API key authorization: APIKeyHeader
let APIKeyHeader = defaultClient.authentications['APIKeyHeader'];
APIKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new SmsGatewayApi.AdminApi();
apiInstance.listMessagesAdminMessagesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[{String: Object}]**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listUsersAdminUsersGet

> [{String: Object}] listUsersAdminUsersGet()

List Users

List all users in the database (admin only)

### Example

```javascript
import SmsGatewayApi from 'sms_gateway_api';
let defaultClient = SmsGatewayApi.ApiClient.instance;
// Configure API key authorization: APIKeyHeader
let APIKeyHeader = defaultClient.authentications['APIKeyHeader'];
APIKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new SmsGatewayApi.AdminApi();
apiInstance.listUsersAdminUsersGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[{String: Object}]**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

