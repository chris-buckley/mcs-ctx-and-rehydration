# ThumbnailCard

A thumbnail card (card with a single, small thumbnail image)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title of the card | [optional] 
**subtitle** | **str** | Subtitle of the card | [optional] 
**text** | **str** | Text for the card | [optional] 
**images** | [**List[CardImage]**](CardImage.md) | Array of images for the card | [optional] 
**buttons** | [**List[CardAction]**](CardAction.md) | Set of actions applicable to the current card | [optional] 
**tap** | [**CardAction**](CardAction.md) |  | [optional] 

## Example

```python
from direct_line.models.thumbnail_card import ThumbnailCard

# TODO update the JSON string below
json = "{}"
# create an instance of ThumbnailCard from a JSON string
thumbnail_card_instance = ThumbnailCard.from_json(json)
# print the JSON string representation of the object
print(ThumbnailCard.to_json())

# convert the object into a dict
thumbnail_card_dict = thumbnail_card_instance.to_dict()
# create an instance of ThumbnailCard from a dict
thumbnail_card_from_dict = ThumbnailCard.from_dict(thumbnail_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


