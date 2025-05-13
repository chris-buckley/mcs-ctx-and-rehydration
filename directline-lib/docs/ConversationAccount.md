# ConversationAccount

Conversation account represents the identity of the conversation within a channel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_group** | **bool** | Indicates whether the conversation contains more than two participants at the time the activity was generated | [optional] 
**conversation_type** | **str** | Indicates the type of the conversation in channels that distinguish between conversation types | [optional] 
**tenant_id** | **str** | This conversation&#39;s tenant ID | [optional] 
**id** | **str** | Channel id for the user or bot on this channel (Example: joe@smith.com, or @joesmith or 123456) | [optional] 
**name** | **str** | Display friendly name | [optional] 
**aad_object_id** | **str** | This account&#39;s object ID within Azure Active Directory (AAD) | [optional] 
**role** | **str** | Role of the entity behind the account (Example: User, Bot, etc.) | [optional] 

## Example

```python
from direct_line.models.conversation_account import ConversationAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationAccount from a JSON string
conversation_account_instance = ConversationAccount.from_json(json)
# print the JSON string representation of the object
print(ConversationAccount.to_json())

# convert the object into a dict
conversation_account_dict = conversation_account_instance.to_dict()
# create an instance of ConversationAccount from a dict
conversation_account_from_dict = ConversationAccount.from_dict(conversation_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


