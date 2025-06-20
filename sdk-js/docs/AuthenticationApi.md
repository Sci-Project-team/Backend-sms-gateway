# SmsGatewayApi.AuthenticationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**loginAuthLoginPost**](AuthenticationApi.md#loginAuthLoginPost) | **POST** /auth/login | Login
[**registerAuthRegisterPost**](AuthenticationApi.md#registerAuthRegisterPost) | **POST** /auth/register | Register



## loginAuthLoginPost

> {String: Object} loginAuthLoginPost(username, password, opts)

Login

### Example

```javascript
import SmsGatewayApi from 'sms_gateway_api';

let apiInstance = new SmsGatewayApi.AuthenticationApi();
let username = "username_example"; // String | 
let password = "password_example"; // String | 
let opts = {
  'grantType': "grantType_example", // String | 
  'scope': "''", // String | 
  'clientId': "clientId_example", // String | 
  'clientSecret': "clientSecret_example" // String | 
};
apiInstance.loginAuthLoginPost(username, password, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**|  | 
 **password** | **String**|  | 
 **grantType** | **String**|  | [optional] 
 **scope** | **String**|  | [optional] [default to &#39;&#39;]
 **clientId** | **String**|  | [optional] 
 **clientSecret** | **String**|  | [optional] 

### Return type

**{String: Object}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## registerAuthRegisterPost

> UserResponse registerAuthRegisterPost(userCreate)

Register

Create a new user with generated API key

### Example

```javascript
import SmsGatewayApi from 'sms_gateway_api';

let apiInstance = new SmsGatewayApi.AuthenticationApi();
let userCreate = new SmsGatewayApi.UserCreate(); // UserCreate | 
apiInstance.registerAuthRegisterPost(userCreate, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userCreate** | [**UserCreate**](UserCreate.md)|  | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

