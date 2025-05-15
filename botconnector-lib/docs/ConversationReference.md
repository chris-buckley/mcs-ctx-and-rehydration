# ConversationReference

An object relating to a particular point in a conversation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_id** | **str** | (Optional) ID of the activity to refer to | [optional] 
**user** | [**ChannelAccount**](ChannelAccount.md) |  | [optional] 
**bot** | [**ChannelAccount**](ChannelAccount.md) |  | [optional] 
**conversation** | [**ConversationAccount**](ConversationAccount.md) |  | [optional] 
**channel_id** | **str** | Channel ID | [optional] 
**service_url** | **str** | Service endpoint where operations concerning the referenced conversation may be performed | [optional] 

## Example

```python
from bot_connector.models.conversation_reference import ConversationReference

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationReference from a JSON string
conversation_reference_instance = ConversationReference.from_json(json)
# print the JSON string representation of the object
print(ConversationReference.to_json())

# convert the object into a dict
conversation_reference_dict = conversation_reference_instance.to_dict()
# create an instance of ConversationReference from a dict
conversation_reference_from_dict = ConversationReference.from_dict(conversation_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


