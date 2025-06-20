# SmsCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number** | **str** | Le numéro de téléphone complet avec indicatif | 
**message** | **str** | Le contenu du message SMS | 

## Example

```python
from openapi_client.models.sms_create import SmsCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SmsCreate from a JSON string
sms_create_instance = SmsCreate.from_json(json)
# print the JSON string representation of the object
print(SmsCreate.to_json())

# convert the object into a dict
sms_create_dict = sms_create_instance.to_dict()
# create an instance of SmsCreate from a dict
sms_create_from_dict = SmsCreate.from_dict(sms_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


