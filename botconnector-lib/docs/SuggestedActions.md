# SuggestedActions

SuggestedActions that can be performed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **List[str]** | Ids of the recipients that the actions should be shown to.  These Ids are relative to the channelId and a subset of all recipients of the activity | [optional] 
**actions** | [**List[CardAction]**](CardAction.md) | Actions that can be shown to the user | [optional] 

## Example

```python
from bot_connector.models.suggested_actions import SuggestedActions

# TODO update the JSON string below
json = "{}"
# create an instance of SuggestedActions from a JSON string
suggested_actions_instance = SuggestedActions.from_json(json)
# print the JSON string representation of the object
print(SuggestedActions.to_json())

# convert the object into a dict
suggested_actions_dict = suggested_actions_instance.to_dict()
# create an instance of SuggestedActions from a dict
suggested_actions_from_dict = SuggestedActions.from_dict(suggested_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


