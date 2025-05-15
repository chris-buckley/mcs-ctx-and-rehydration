# PaymentRequestCompleteResult

Deprecated. Bot Framework no longer supports payments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** | Result of the payment request completion | [optional] 

## Example

```python
from bot_connector.models.payment_request_complete_result import PaymentRequestCompleteResult

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRequestCompleteResult from a JSON string
payment_request_complete_result_instance = PaymentRequestCompleteResult.from_json(json)
# print the JSON string representation of the object
print(PaymentRequestCompleteResult.to_json())

# convert the object into a dict
payment_request_complete_result_dict = payment_request_complete_result_instance.to_dict()
# create an instance of PaymentRequestCompleteResult from a dict
payment_request_complete_result_from_dict = PaymentRequestCompleteResult.from_dict(payment_request_complete_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


