# ThumbnailUrl

Thumbnail URL

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL pointing to the thumbnail to use for media content | [optional] 
**alt** | **str** | HTML alt text to include on this thumbnail image | [optional] 

## Example

```python
from bot_connector.models.thumbnail_url import ThumbnailUrl

# TODO update the JSON string below
json = "{}"
# create an instance of ThumbnailUrl from a JSON string
thumbnail_url_instance = ThumbnailUrl.from_json(json)
# print the JSON string representation of the object
print(ThumbnailUrl.to_json())

# convert the object into a dict
thumbnail_url_dict = thumbnail_url_instance.to_dict()
# create an instance of ThumbnailUrl from a dict
thumbnail_url_from_dict = ThumbnailUrl.from_dict(thumbnail_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


