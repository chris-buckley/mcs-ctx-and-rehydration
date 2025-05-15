# PaymentRequest

Deprecated. Bot Framework no longer supports payments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of this payment request | [optional] 
**method_data** | [**List[PaymentMethodData]**](PaymentMethodData.md) | Allowed payment methods for this request | [optional] 
**details** | [**PaymentDetails**](PaymentDetails.md) |  | [optional] 
**options** | [**PaymentOptions**](PaymentOptions.md) |  | [optional] 
**expires** | **str** | Expiration for this request, in ISO 8601 duration format (e.g., &#39;P1D&#39;) | [optional] 

## Example

```python
from bot_connector.models.payment_request import PaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRequest from a JSON string
payment_request_instance = PaymentRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentRequest.to_json())

# convert the object into a dict
payment_request_dict = payment_request_instance.to_dict()
# create an instance of PaymentRequest from a dict
payment_request_from_dict = PaymentRequest.from_dict(payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


