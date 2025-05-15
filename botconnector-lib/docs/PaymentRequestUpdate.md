# PaymentRequestUpdate

Deprecated. Bot Framework no longer supports payments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID for the payment request to update | [optional] 
**details** | [**PaymentDetails**](PaymentDetails.md) |  | [optional] 
**shipping_address** | [**PaymentAddress**](PaymentAddress.md) |  | [optional] 
**shipping_option** | **str** | Updated shipping options | [optional] 

## Example

```python
from bot_connector.models.payment_request_update import PaymentRequestUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRequestUpdate from a JSON string
payment_request_update_instance = PaymentRequestUpdate.from_json(json)
# print the JSON string representation of the object
print(PaymentRequestUpdate.to_json())

# convert the object into a dict
payment_request_update_dict = payment_request_update_instance.to_dict()
# create an instance of PaymentRequestUpdate from a dict
payment_request_update_from_dict = PaymentRequestUpdate.from_dict(payment_request_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


