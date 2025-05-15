# MicrosoftPayMethodData

Deprecated. Bot Framework no longer supports payments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | Microsoft Pay Merchant ID | [optional] 
**supported_networks** | **List[str]** | Deprecated. Bot Framework no longer supports payments. | [optional] 
**supported_types** | **List[str]** | Deprecated. Bot Framework no longer supports payments. | [optional] 

## Example

```python
from bot_connector.models.microsoft_pay_method_data import MicrosoftPayMethodData

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftPayMethodData from a JSON string
microsoft_pay_method_data_instance = MicrosoftPayMethodData.from_json(json)
# print the JSON string representation of the object
print(MicrosoftPayMethodData.to_json())

# convert the object into a dict
microsoft_pay_method_data_dict = microsoft_pay_method_data_instance.to_dict()
# create an instance of MicrosoftPayMethodData from a dict
microsoft_pay_method_data_from_dict = MicrosoftPayMethodData.from_dict(microsoft_pay_method_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


