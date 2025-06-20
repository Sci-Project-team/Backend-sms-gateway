# SmsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number** | **str** | Le numéro de téléphone complet avec indicatif | 
**message** | **str** | Le contenu du message SMS | 
**id** | **str** |  | 
**status** | [**SmsStatus**](SmsStatus.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**error_message** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.sms_response import SmsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SmsResponse from a JSON string
sms_response_instance = SmsResponse.from_json(json)
# print the JSON string representation of the object
print(SmsResponse.to_json())

# convert the object into a dict
sms_response_dict = sms_response_instance.to_dict()
# create an instance of SmsResponse from a dict
sms_response_from_dict = SmsResponse.from_dict(sms_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


