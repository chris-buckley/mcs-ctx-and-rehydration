# PaymentResponse

Deprecated. Bot Framework no longer supports payments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method_name** | **str** | The payment method identifier for the payment method that the user selected to fulfil the transaction | [optional] 
**details** | **object** | A JSON-serializable object that provides a payment method specific message used by the merchant to process the transaction and determine successful fund transfer | [optional] 
**shipping_address** | [**PaymentAddress**](PaymentAddress.md) |  | [optional] 
**shipping_option** | **str** | If the requestShipping flag was set to true in the PaymentOptions passed to the PaymentRequest constructor, then shippingOption will be the id attribute of the selected shipping option | [optional] 
**payer_email** | **str** | If the requestPayerEmail flag was set to true in the PaymentOptions passed to the PaymentRequest constructor, then payerEmail will be the email address chosen by the user | [optional] 
**payer_phone** | **str** | If the requestPayerPhone flag was set to true in the PaymentOptions passed to the PaymentRequest constructor, then payerPhone will be the phone number chosen by the user | [optional] 

## Example

```python
from bot_connector.models.payment_response import PaymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentResponse from a JSON string
payment_response_instance = PaymentResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentResponse.to_json())

# convert the object into a dict
payment_response_dict = payment_response_instance.to_dict()
# create an instance of PaymentResponse from a dict
payment_response_from_dict = PaymentResponse.from_dict(payment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


