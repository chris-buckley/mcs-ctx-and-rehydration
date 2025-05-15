# ConversationResourceResponse

A response containing a resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_id** | **str** | ID of the Activity (if sent) | [optional] 
**service_url** | **str** | Service endpoint where operations concerning the conversation may be performed | [optional] 
**id** | **str** | Id of the resource | [optional] 

## Example

```python
from bot_connector.models.conversation_resource_response import ConversationResourceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationResourceResponse from a JSON string
conversation_resource_response_instance = ConversationResourceResponse.from_json(json)
# print the JSON string representation of the object
print(ConversationResourceResponse.to_json())

# convert the object into a dict
conversation_resource_response_dict = conversation_resource_response_instance.to_dict()
# create an instance of ConversationResourceResponse from a dict
conversation_resource_response_from_dict = ConversationResourceResponse.from_dict(conversation_resource_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


