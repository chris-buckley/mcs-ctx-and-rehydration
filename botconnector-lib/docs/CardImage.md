# CardImage

An image on a card

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL thumbnail image for major content property | [optional] 
**alt** | **str** | Image description intended for screen readers | [optional] 
**tap** | [**CardAction**](CardAction.md) |  | [optional] 

## Example

```python
from bot_connector.models.card_image import CardImage

# TODO update the JSON string below
json = "{}"
# create an instance of CardImage from a JSON string
card_image_instance = CardImage.from_json(json)
# print the JSON string representation of the object
print(CardImage.to_json())

# convert the object into a dict
card_image_dict = card_image_instance.to_dict()
# create an instance of CardImage from a dict
card_image_from_dict = CardImage.from_dict(card_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


