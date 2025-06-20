# SmsGatewayApi.SMSApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getInboxSmsInboxGet**](SMSApi.md#getInboxSmsInboxGet) | **GET** /sms/inbox | Lister tous les SMS reçus
[**getLogsLogsGet**](SMSApi.md#getLogsLogsGet) | **GET** /logs | Voir les logs des SMS
[**getSentMessagesSmsSentGet**](SMSApi.md#getSentMessagesSmsSentGet) | **GET** /sms/sent | Lister tous les SMS envoyés
[**sendSmsSmsPost**](SMSApi.md#sendSmsSmsPost) | **POST** /sms | Envoyer un SMS
[**simulateReceivedSmsSmsSimulateReceivePost**](SMSApi.md#simulateReceivedSmsSmsSimulateReceivePost) | **POST** /sms/simulate-receive | Simulate Received Sms



## getInboxSmsInboxGet

> [SmsResponse] getInboxSmsInboxGet(opts)

Lister tous les SMS reçus

Récupère tous les SMS reçus.

### Example

```javascript
import SmsGatewayApi from 'sms_gateway_api';
let defaultClient = SmsGatewayApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2PasswordBearer
let OAuth2PasswordBearer = defaultClient.authentications['OAuth2PasswordBearer'];
OAuth2PasswordBearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SmsGatewayApi.SMSApi();
let opts = {
  'limit': 56 // Number | Nombre maximum de SMS à retourner
};
apiInstance.getInboxSmsInboxGet(opts, (error, data, response) => {
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
 **limit** | **Number**| Nombre maximum de SMS à retourner | [optional] 

### Return type

[**[SmsResponse]**](SmsResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLogsLogsGet

> [{String: Object}] getLogsLogsGet(opts)

Voir les logs des SMS

Récupère l&#39;historique et le statut de tous les SMS envoyés.

### Example

```javascript
import SmsGatewayApi from 'sms_gateway_api';
let defaultClient = SmsGatewayApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2PasswordBearer
let OAuth2PasswordBearer = defaultClient.authentications['OAuth2PasswordBearer'];
OAuth2PasswordBearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SmsGatewayApi.SMSApi();
let opts = {
  'limit': 56, // Number | Nombre maximum de logs à retourner
  'level': "level_example", // String | Filtre par niveau de log (INFO, WARNING, ERROR, etc.)
  'component': "component_example" // String | Filtre par composant
};
apiInstance.getLogsLogsGet(opts, (error, data, response) => {
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
 **limit** | **Number**| Nombre maximum de logs à retourner | [optional] 
 **level** | **String**| Filtre par niveau de log (INFO, WARNING, ERROR, etc.) | [optional] 
 **component** | **String**| Filtre par composant | [optional] 

### Return type

**[{String: Object}]**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSentMessagesSmsSentGet

> [SmsResponse] getSentMessagesSmsSentGet(opts)

Lister tous les SMS envoyés

Récupère tous les SMS envoyés par l&#39;utilisateur actuel.

### Example

```javascript
import SmsGatewayApi from 'sms_gateway_api';
let defaultClient = SmsGatewayApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2PasswordBearer
let OAuth2PasswordBearer = defaultClient.authentications['OAuth2PasswordBearer'];
OAuth2PasswordBearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SmsGatewayApi.SMSApi();
let opts = {
  'limit': 56 // Number | Nombre maximum de SMS à retourner
};
apiInstance.getSentMessagesSmsSentGet(opts, (error, data, response) => {
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
 **limit** | **Number**| Nombre maximum de SMS à retourner | [optional] 

### Return type

[**[SmsResponse]**](SmsResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sendSmsSmsPost

> SmsResponse sendSmsSmsPost(smsCreate)

Envoyer un SMS

Envoie un SMS au numéro spécifié.  - **phone_number**: Numéro complet avec indicatif international - **message**: Contenu du SMS à envoyer

### Example

```javascript
import SmsGatewayApi from 'sms_gateway_api';
let defaultClient = SmsGatewayApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2PasswordBearer
let OAuth2PasswordBearer = defaultClient.authentications['OAuth2PasswordBearer'];
OAuth2PasswordBearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SmsGatewayApi.SMSApi();
let smsCreate = new SmsGatewayApi.SmsCreate(); // SmsCreate | 
apiInstance.sendSmsSmsPost(smsCreate, (error, data, response) => {
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
 **smsCreate** | [**SmsCreate**](SmsCreate.md)|  | 

### Return type

[**SmsResponse**](SmsResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## simulateReceivedSmsSmsSimulateReceivePost

> SmsResponse simulateReceivedSmsSmsSimulateReceivePost(phoneNumber, message)

Simulate Received Sms

Simule la réception d&#39;un SMS (uniquement pour les tests/développement).

### Example

```javascript
import SmsGatewayApi from 'sms_gateway_api';
let defaultClient = SmsGatewayApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2PasswordBearer
let OAuth2PasswordBearer = defaultClient.authentications['OAuth2PasswordBearer'];
OAuth2PasswordBearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SmsGatewayApi.SMSApi();
let phoneNumber = "phoneNumber_example"; // String | Numéro de téléphone de l'expéditeur
let message = "message_example"; // String | Contenu du message reçu
apiInstance.simulateReceivedSmsSmsSimulateReceivePost(phoneNumber, message, (error, data, response) => {
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
 **phoneNumber** | **String**| Numéro de téléphone de l&#39;expéditeur | 
 **message** | **String**| Contenu du message reçu | 

### Return type

[**SmsResponse**](SmsResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

