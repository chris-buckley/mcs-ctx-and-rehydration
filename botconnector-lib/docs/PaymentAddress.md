# PaymentAddress

Deprecated. Bot Framework no longer supports payments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | This is the CLDR (Common Locale Data Repository) region code. For example, US, GB, CN, or JP | [optional] 
**address_line** | **List[str]** | This is the most specific part of the address. It can include, for example, a street name, a house number, apartment number, a rural delivery route, descriptive instructions, or a post office box number. | [optional] 
**region** | **str** | This is the top level administrative subdivision of the country. For example, this can be a state, a province, an oblast, or a prefecture. | [optional] 
**city** | **str** | This is the city/town portion of the address. | [optional] 
**dependent_locality** | **str** | This is the dependent locality or sublocality within a city. For example, used for neighborhoods, boroughs, districts, or UK dependent localities. | [optional] 
**postal_code** | **str** | This is the postal code or ZIP code, also known as PIN code in India. | [optional] 
**sorting_code** | **str** | This is the sorting code as used in, for example, France. | [optional] 
**language_code** | **str** | This is the BCP-47 language code for the address. It&#39;s used to determine the field separators and the order of fields when formatting the address for display. | [optional] 
**organization** | **str** | This is the organization, firm, company, or institution at this address. | [optional] 
**recipient** | **str** | This is the name of the recipient or contact person. | [optional] 
**phone** | **str** | This is the phone number of the recipient or contact person. | [optional] 

## Example

```python
from bot_connector.models.payment_address import PaymentAddress

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentAddress from a JSON string
payment_address_instance = PaymentAddress.from_json(json)
# print the JSON string representation of the object
print(PaymentAddress.to_json())

# convert the object into a dict
payment_address_dict = payment_address_instance.to_dict()
# create an instance of PaymentAddress from a dict
payment_address_from_dict = PaymentAddress.from_dict(payment_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


