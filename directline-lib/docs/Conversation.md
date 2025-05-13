# Conversation

An object representing a conversation or a conversation token

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_id** | **str** | ID for this conversation | [optional] 
**token** | **str** | Token scoped to this conversation | [optional] 
**expires_in** | **int** | Expiration for token | [optional] 
**stream_url** | **str** | URL for this conversation&#39;s message stream | [optional] 
**reference_grammar_id** | **str** | ID for the reference grammar for this bot | [optional] 
**e_tag** | **str** |  | [optional] 

## Example

```python
from direct_line.models.conversation import Conversation

# TODO update the JSON string below
json = "{}"
# create an instance of Conversation from a JSON string
conversation_instance = Conversation.from_json(json)
# print the JSON string representation of the object
print(Conversation.to_json())

# convert the object into a dict
conversation_dict = conversation_instance.to_dict()
# create an instance of Conversation from a dict
conversation_from_dict = Conversation.from_dict(conversation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


