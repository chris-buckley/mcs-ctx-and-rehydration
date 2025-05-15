# PaymentDetails

Deprecated. Bot Framework no longer supports payments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | [**PaymentItem**](PaymentItem.md) |  | [optional] 
**display_items** | [**List[PaymentItem]**](PaymentItem.md) | Contains line items for the payment request that the user agent may display | [optional] 
**shipping_options** | [**List[PaymentShippingOption]**](PaymentShippingOption.md) | A sequence containing the different shipping options for the user to choose from | [optional] 
**modifiers** | [**List[PaymentDetailsModifier]**](PaymentDetailsModifier.md) | Contains modifiers for particular payment method identifiers | [optional] 
**error** | **str** | Error description | [optional] 

## Example

```python
from bot_connector.models.payment_details import PaymentDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentDetails from a JSON string
payment_details_instance = PaymentDetails.from_json(json)
# print the JSON string representation of the object
print(PaymentDetails.to_json())

# convert the object into a dict
payment_details_dict = payment_details_instance.to_dict()
# create an instance of PaymentDetails from a dict
payment_details_from_dict = PaymentDetails.from_dict(payment_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


