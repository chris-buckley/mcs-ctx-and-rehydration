# PaymentRequestComplete

Deprecated. Bot Framework no longer supports payments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Payment request ID | [optional] 
**payment_request** | [**PaymentRequest**](PaymentRequest.md) |  | [optional] 
**payment_response** | [**PaymentResponse**](PaymentResponse.md) |  | [optional] 

## Example

```python
from bot_connector.models.payment_request_complete import PaymentRequestComplete

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRequestComplete from a JSON string
payment_request_complete_instance = PaymentRequestComplete.from_json(json)
# print the JSON string representation of the object
print(PaymentRequestComplete.to_json())

# convert the object into a dict
payment_request_complete_dict = payment_request_complete_instance.to_dict()
# create an instance of PaymentRequestComplete from a dict
payment_request_complete_from_dict = PaymentRequestComplete.from_dict(payment_request_complete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


