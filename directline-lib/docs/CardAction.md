# CardAction

A clickable action

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of action implemented by this button | [optional] 
**title** | **str** | Text description which appears on the button | [optional] 
**image** | **str** | Image URL which will appear on the button, next to text label | [optional] 
**text** | **str** | Text for this action | [optional] 
**display_text** | **str** | (Optional) text to display in the chat feed if the button is clicked | [optional] 
**value** | **object** | Supplementary parameter for action. Content of this property depends on the ActionType | [optional] 
**channel_data** | **object** | Channel-specific data associated with this action | [optional] 

## Example

```python
from direct_line.models.card_action import CardAction

# TODO update the JSON string below
json = "{}"
# create an instance of CardAction from a JSON string
card_action_instance = CardAction.from_json(json)
# print the JSON string representation of the object
print(CardAction.to_json())

# convert the object into a dict
card_action_dict = card_action_instance.to_dict()
# create an instance of CardAction from a dict
card_action_from_dict = CardAction.from_dict(card_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


