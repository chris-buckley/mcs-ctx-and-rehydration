# PaymentOptions

Deprecated. Bot Framework no longer supports payments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_payer_name** | **bool** | Indicates whether the user agent should collect and return the payer&#39;s name as part of the payment request | [optional] 
**request_payer_email** | **bool** | Indicates whether the user agent should collect and return the payer&#39;s email address as part of the payment request | [optional] 
**request_payer_phone** | **bool** | Indicates whether the user agent should collect and return the payer&#39;s phone number as part of the payment request | [optional] 
**request_shipping** | **bool** | Indicates whether the user agent should collect and return a shipping address as part of the payment request | [optional] 
**shipping_type** | **str** | If requestShipping is set to true, then the shippingType field may be used to influence the way the user agent presents the user interface for gathering the shipping address | [optional] 

## Example

```python
from bot_connector.models.payment_options import PaymentOptions

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentOptions from a JSON string
payment_options_instance = PaymentOptions.from_json(json)
# print the JSON string representation of the object
print(PaymentOptions.to_json())

# convert the object into a dict
payment_options_dict = payment_options_instance.to_dict()
# create an instance of PaymentOptions from a dict
payment_options_from_dict = PaymentOptions.from_dict(payment_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


