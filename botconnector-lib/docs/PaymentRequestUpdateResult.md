# PaymentRequestUpdateResult

Deprecated. Bot Framework no longer supports payments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**PaymentDetails**](PaymentDetails.md) |  | [optional] 

## Example

```python
from bot_connector.models.payment_request_update_result import PaymentRequestUpdateResult

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRequestUpdateResult from a JSON string
payment_request_update_result_instance = PaymentRequestUpdateResult.from_json(json)
# print the JSON string representation of the object
print(PaymentRequestUpdateResult.to_json())

# convert the object into a dict
payment_request_update_result_dict = payment_request_update_result_instance.to_dict()
# create an instance of PaymentRequestUpdateResult from a dict
payment_request_update_result_from_dict = PaymentRequestUpdateResult.from_dict(payment_request_update_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


