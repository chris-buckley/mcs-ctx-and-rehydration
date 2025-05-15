# SigninCard

A card representing a request to sign in

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Text for signin request | [optional] 
**buttons** | [**List[CardAction]**](CardAction.md) | Action to use to perform signin | [optional] 

## Example

```python
from bot_connector.models.signin_card import SigninCard

# TODO update the JSON string below
json = "{}"
# create an instance of SigninCard from a JSON string
signin_card_instance = SigninCard.from_json(json)
# print the JSON string representation of the object
print(SigninCard.to_json())

# convert the object into a dict
signin_card_dict = signin_card_instance.to_dict()
# create an instance of SigninCard from a dict
signin_card_from_dict = SigninCard.from_dict(signin_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


