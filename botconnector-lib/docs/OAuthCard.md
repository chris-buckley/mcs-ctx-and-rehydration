# OAuthCard

A card representing a request to perform a sign in via OAuth

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Text for signin request | [optional] 
**connection_name** | **str** | The name of the registered connection | [optional] 
**buttons** | [**List[CardAction]**](CardAction.md) | Action to use to perform signin | [optional] 

## Example

```python
from bot_connector.models.o_auth_card import OAuthCard

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthCard from a JSON string
o_auth_card_instance = OAuthCard.from_json(json)
# print the JSON string representation of the object
print(OAuthCard.to_json())

# convert the object into a dict
o_auth_card_dict = o_auth_card_instance.to_dict()
# create an instance of OAuthCard from a dict
o_auth_card_from_dict = OAuthCard.from_dict(o_auth_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


