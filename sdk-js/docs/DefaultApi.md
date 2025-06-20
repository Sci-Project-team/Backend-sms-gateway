# SmsGatewayApi.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkDbStructureDebugDbStructureGet**](DefaultApi.md#checkDbStructureDebugDbStructureGet) | **GET** /debug/db-structure | Check Db Structure
[**debugMqttStorageDebugMqttStorageGet**](DefaultApi.md#debugMqttStorageDebugMqttStorageGet) | **GET** /debug/mqtt-storage | Debug Mqtt Storage
[**debugServicesDebugServicesGet**](DefaultApi.md#debugServicesDebugServicesGet) | **GET** /debug/services | Debug Services
[**getAllMessagesDebugAllMessagesGet**](DefaultApi.md#getAllMessagesDebugAllMessagesGet) | **GET** /debug/all-messages | Get All Messages
[**mqttStatusDebugMqttStatusGet**](DefaultApi.md#mqttStatusDebugMqttStatusGet) | **GET** /debug/mqtt-status | Mqtt Status
[**rootGet**](DefaultApi.md#rootGet) | **GET** / | Root



## checkDbStructureDebugDbStructureGet

> Object checkDbStructureDebugDbStructureGet()

Check Db Structure

Check database structure

### Example

```javascript
import SmsGatewayApi from 'sms_gateway_api';

let apiInstance = new SmsGatewayApi.DefaultApi();
apiInstance.checkDbStructureDebugDbStructureGet((error, data, response) => {
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

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## debugMqttStorageDebugMqttStorageGet

> Object debugMqttStorageDebugMqttStorageGet()

Debug Mqtt Storage

Check if MQTT service has storage service

### Example

```javascript
import SmsGatewayApi from 'sms_gateway_api';

let apiInstance = new SmsGatewayApi.DefaultApi();
apiInstance.debugMqttStorageDebugMqttStorageGet((error, data, response) => {
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

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## debugServicesDebugServicesGet

> Object debugServicesDebugServicesGet()

Debug Services

Debug endpoint to check service status

### Example

```javascript
import SmsGatewayApi from 'sms_gateway_api';

let apiInstance = new SmsGatewayApi.DefaultApi();
apiInstance.debugServicesDebugServicesGet((error, data, response) => {
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

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllMessagesDebugAllMessagesGet

> Object getAllMessagesDebugAllMessagesGet()

Get All Messages

Debug endpoint to see all messages

### Example

```javascript
import SmsGatewayApi from 'sms_gateway_api';

let apiInstance = new SmsGatewayApi.DefaultApi();
apiInstance.getAllMessagesDebugAllMessagesGet((error, data, response) => {
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

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mqttStatusDebugMqttStatusGet

> Object mqttStatusDebugMqttStatusGet()

Mqtt Status

Debug endpoint to check MQTT service status

### Example

```javascript
import SmsGatewayApi from 'sms_gateway_api';

let apiInstance = new SmsGatewayApi.DefaultApi();
apiInstance.mqttStatusDebugMqttStatusGet((error, data, response) => {
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

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rootGet

> Object rootGet()

Root

### Example

```javascript
import SmsGatewayApi from 'sms_gateway_api';

let apiInstance = new SmsGatewayApi.DefaultApi();
apiInstance.rootGet((error, data, response) => {
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

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

