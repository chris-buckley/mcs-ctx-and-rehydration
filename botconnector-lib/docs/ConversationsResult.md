# ConversationsResult

Conversations result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continuation_token** | **str** | Paging token | [optional] 
**conversations** | [**List[ConversationMembers]**](ConversationMembers.md) | List of conversations | [optional] 

## Example

```python
from bot_connector.models.conversations_result import ConversationsResult

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationsResult from a JSON string
conversations_result_instance = ConversationsResult.from_json(json)
# print the JSON string representation of the object
print(ConversationsResult.to_json())

# convert the object into a dict
conversations_result_dict = conversations_result_instance.to_dict()
# create an instance of ConversationsResult from a dict
conversations_result_from_dict = ConversationsResult.from_dict(conversations_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


