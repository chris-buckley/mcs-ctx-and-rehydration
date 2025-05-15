# PaymentItem

Deprecated. Bot Framework no longer supports payments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Human-readable description of the item | [optional] 
**amount** | [**PaymentCurrencyAmount**](PaymentCurrencyAmount.md) |  | [optional] 
**pending** | **bool** | When set to true this flag means that the amount field is not final. | [optional] 

## Example

```python
from bot_connector.models.payment_item import PaymentItem

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentItem from a JSON string
payment_item_instance = PaymentItem.from_json(json)
# print the JSON string representation of the object
print(PaymentItem.to_json())

# convert the object into a dict
payment_item_dict = payment_item_instance.to_dict()
# create an instance of PaymentItem from a dict
payment_item_from_dict = PaymentItem.from_dict(payment_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


