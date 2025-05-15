# AttachmentData

Attachment data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Content-Type of the attachment | [optional] 
**name** | **str** | Name of the attachment | [optional] 
**original_base64** | **bytearray** | Attachment content | [optional] 
**thumbnail_base64** | **bytearray** | Attachment thumbnail | [optional] 

## Example

```python
from bot_connector.models.attachment_data import AttachmentData

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentData from a JSON string
attachment_data_instance = AttachmentData.from_json(json)
# print the JSON string representation of the object
print(AttachmentData.to_json())

# convert the object into a dict
attachment_data_dict = attachment_data_instance.to_dict()
# create an instance of AttachmentData from a dict
attachment_data_from_dict = AttachmentData.from_dict(attachment_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


