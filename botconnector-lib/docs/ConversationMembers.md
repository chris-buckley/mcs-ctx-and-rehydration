# ConversationMembers

Conversation and its members

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Conversation ID | [optional] 
**members** | [**List[ChannelAccount]**](ChannelAccount.md) | List of members in this conversation | [optional] 

## Example

```python
from bot_connector.models.conversation_members import ConversationMembers

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationMembers from a JSON string
conversation_members_instance = ConversationMembers.from_json(json)
# print the JSON string representation of the object
print(ConversationMembers.to_json())

# convert the object into a dict
conversation_members_dict = conversation_members_instance.to_dict()
# create an instance of ConversationMembers from a dict
conversation_members_from_dict = ConversationMembers.from_dict(conversation_members_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


