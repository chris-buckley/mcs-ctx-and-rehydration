# ConversationParameters

Parameters for creating a new conversation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_group** | **bool** | IsGroup | [optional] 
**bot** | [**ChannelAccount**](ChannelAccount.md) |  | [optional] 
**members** | [**List[ChannelAccount]**](ChannelAccount.md) | Members to add to the conversation | [optional] 
**topic_name** | **str** | (Optional) Topic of the conversation (if supported by the channel) | [optional] 
**tenant_id** | **str** | (Optional) The tenant ID in which the conversation should be created | [optional] 
**activity** | [**Activity**](Activity.md) |  | [optional] 
**channel_data** | **object** | Channel specific payload for creating the conversation | [optional] 

## Example

```python
from bot_connector.models.conversation_parameters import ConversationParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationParameters from a JSON string
conversation_parameters_instance = ConversationParameters.from_json(json)
# print the JSON string representation of the object
print(ConversationParameters.to_json())

# convert the object into a dict
conversation_parameters_dict = conversation_parameters_instance.to_dict()
# create an instance of ConversationParameters from a dict
conversation_parameters_from_dict = ConversationParameters.from_dict(conversation_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


