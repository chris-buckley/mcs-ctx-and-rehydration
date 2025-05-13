# SemanticAction

Represents a reference to a programmatic action

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | State of this action. Allowed values: &#x60;start&#x60;, &#x60;continue&#x60;, &#x60;done&#x60; | [optional] 
**id** | **str** | ID of this action | [optional] 
**entities** | [**Dict[str, Entity]**](Entity.md) | Entities associated with this action | [optional] 

## Example

```python
from direct_line.models.semantic_action import SemanticAction

# TODO update the JSON string below
json = "{}"
# create an instance of SemanticAction from a JSON string
semantic_action_instance = SemanticAction.from_json(json)
# print the JSON string representation of the object
print(SemanticAction.to_json())

# convert the object into a dict
semantic_action_dict = semantic_action_instance.to_dict()
# create an instance of SemanticAction from a dict
semantic_action_from_dict = SemanticAction.from_dict(semantic_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


