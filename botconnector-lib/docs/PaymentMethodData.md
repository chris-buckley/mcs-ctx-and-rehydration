# PaymentMethodData

Deprecated. Bot Framework no longer supports payments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supported_methods** | **List[str]** | Required sequence of strings containing payment method identifiers for payment methods that the merchant web site accepts | [optional] 
**data** | **object** | A JSON-serializable object that provides optional information that might be needed by the supported payment methods | [optional] 

## Example

```python
from bot_connector.models.payment_method_data import PaymentMethodData

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodData from a JSON string
payment_method_data_instance = PaymentMethodData.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodData.to_json())

# convert the object into a dict
payment_method_data_dict = payment_method_data_instance.to_dict()
# create an instance of PaymentMethodData from a dict
payment_method_data_from_dict = PaymentMethodData.from_dict(payment_method_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


