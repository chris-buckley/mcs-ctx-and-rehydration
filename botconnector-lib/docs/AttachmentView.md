# AttachmentView

Attachment View name and size

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view_id** | **str** | Id of the attachment | [optional] 
**size** | **int** | Size of the attachment | [optional] 

## Example

```python
from bot_connector.models.attachment_view import AttachmentView

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentView from a JSON string
attachment_view_instance = AttachmentView.from_json(json)
# print the JSON string representation of the object
print(AttachmentView.to_json())

# convert the object into a dict
attachment_view_dict = attachment_view_instance.to_dict()
# create an instance of AttachmentView from a dict
attachment_view_from_dict = AttachmentView.from_dict(attachment_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


