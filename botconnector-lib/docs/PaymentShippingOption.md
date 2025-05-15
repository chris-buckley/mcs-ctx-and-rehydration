# PaymentShippingOption

Deprecated. Bot Framework no longer supports payments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | String identifier used to reference this PaymentShippingOption | [optional] 
**label** | **str** | Human-readable description of the item | [optional] 
**amount** | [**PaymentCurrencyAmount**](PaymentCurrencyAmount.md) |  | [optional] 
**selected** | **bool** | Indicates whether this is the default selected PaymentShippingOption | [optional] 

## Example

```python
from bot_connector.models.payment_shipping_option import PaymentShippingOption

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentShippingOption from a JSON string
payment_shipping_option_instance = PaymentShippingOption.from_json(json)
# print the JSON string representation of the object
print(PaymentShippingOption.to_json())

# convert the object into a dict
payment_shipping_option_dict = payment_shipping_option_instance.to_dict()
# create an instance of PaymentShippingOption from a dict
payment_shipping_option_from_dict = PaymentShippingOption.from_dict(payment_shipping_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


