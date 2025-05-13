# MediaCard

Media card

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title of this card | [optional] 
**subtitle** | **str** | Subtitle of this card | [optional] 
**text** | **str** | Text of this card | [optional] 
**image** | [**ThumbnailUrl**](ThumbnailUrl.md) |  | [optional] 
**media** | [**List[MediaUrl]**](MediaUrl.md) | Media URLs for this card. When this field contains more than one URL, each URL is an alternative format of the same content. | [optional] 
**buttons** | [**List[CardAction]**](CardAction.md) | Actions on this card | [optional] 
**shareable** | **bool** | This content may be shared with others (default:true) | [optional] 
**autoloop** | **bool** | Should the client loop playback at end of content (default:true) | [optional] 
**autostart** | **bool** | Should the client automatically start playback of media in this card (default:true) | [optional] 
**aspect** | **str** | Aspect ratio of thumbnail/media placeholder. Allowed values are \&quot;16:9\&quot; and \&quot;4:3\&quot; | [optional] 
**duration** | **str** | Describes the length of the media content without requiring a receiver to open the content. Formatted as an ISO 8601 Duration field. | [optional] 
**value** | **object** | Supplementary parameter for this card | [optional] 

## Example

```python
from direct_line.models.media_card import MediaCard

# TODO update the JSON string below
json = "{}"
# create an instance of MediaCard from a JSON string
media_card_instance = MediaCard.from_json(json)
# print the JSON string representation of the object
print(MediaCard.to_json())

# convert the object into a dict
media_card_dict = media_card_instance.to_dict()
# create an instance of MediaCard from a dict
media_card_from_dict = MediaCard.from_dict(media_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


