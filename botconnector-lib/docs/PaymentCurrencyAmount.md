# PaymentCurrencyAmount

Deprecated. Bot Framework no longer supports payments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | A currency identifier | [optional] 
**value** | **str** | Decimal monetary value | [optional] 
**currency_system** | **str** | Currency system | [optional] 

## Example

```python
from bot_connector.models.payment_currency_amount import PaymentCurrencyAmount

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentCurrencyAmount from a JSON string
payment_currency_amount_instance = PaymentCurrencyAmount.from_json(json)
# print the JSON string representation of the object
print(PaymentCurrencyAmount.to_json())

# convert the object into a dict
payment_currency_amount_dict = payment_currency_amount_instance.to_dict()
# create an instance of PaymentCurrencyAmount from a dict
payment_currency_amount_from_dict = PaymentCurrencyAmount.from_dict(payment_currency_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


