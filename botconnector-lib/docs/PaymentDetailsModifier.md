# PaymentDetailsModifier

Deprecated. Bot Framework no longer supports payments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supported_methods** | **List[str]** | Contains a sequence of payment method identifiers | [optional] 
**total** | [**PaymentItem**](PaymentItem.md) |  | [optional] 
**additional_display_items** | [**List[PaymentItem]**](PaymentItem.md) | Provides additional display items that are appended to the displayItems field in the PaymentDetails dictionary for the payment method identifiers in the supportedMethods field | [optional] 
**data** | **object** | A JSON-serializable object that provides optional information that might be needed by the supported payment methods | [optional] 

## Example

```python
from bot_connector.models.payment_details_modifier import PaymentDetailsModifier

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentDetailsModifier from a JSON string
payment_details_modifier_instance = PaymentDetailsModifier.from_json(json)
# print the JSON string representation of the object
print(PaymentDetailsModifier.to_json())

# convert the object into a dict
payment_details_modifier_dict = payment_details_modifier_instance.to_dict()
# create an instance of PaymentDetailsModifier from a dict
payment_details_modifier_from_dict = PaymentDetailsModifier.from_dict(payment_details_modifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


