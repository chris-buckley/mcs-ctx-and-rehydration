# MessageReaction

Message reaction object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**MessageReactionTypes**](MessageReactionTypes.md) |  | [optional] 

## Example

```python
from bot_connector.models.message_reaction import MessageReaction

# TODO update the JSON string below
json = "{}"
# create an instance of MessageReaction from a JSON string
message_reaction_instance = MessageReaction.from_json(json)
# print the JSON string representation of the object
print(MessageReaction.to_json())

# convert the object into a dict
message_reaction_dict = message_reaction_instance.to_dict()
# create an instance of MessageReaction from a dict
message_reaction_from_dict = MessageReaction.from_dict(message_reaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


