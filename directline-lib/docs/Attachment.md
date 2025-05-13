# Attachment

An attachment within an activity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** | mimetype/Contenttype for the file | [optional] 
**content_url** | **str** | Content Url | [optional] 
**content** | **object** | Embedded content | [optional] 
**name** | **str** | (OPTIONAL) The name of the attachment | [optional] 
**thumbnail_url** | **str** | (OPTIONAL) Thumbnail associated with attachment | [optional] 

## Example

```python
from direct_line.models.attachment import Attachment

# TODO update the JSON string below
json = "{}"
# create an instance of Attachment from a JSON string
attachment_instance = Attachment.from_json(json)
# print the JSON string representation of the object
print(Attachment.to_json())

# convert the object into a dict
attachment_dict = attachment_instance.to_dict()
# create an instance of Attachment from a dict
attachment_from_dict = Attachment.from_dict(attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


