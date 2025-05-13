# ActivitySet

A collection of activities

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activities** | [**List[Activity]**](Activity.md) | Activities | [optional] 
**watermark** | **str** | Maximum watermark of activities within this set | [optional] 

## Example

```python
from direct_line.models.activity_set import ActivitySet

# TODO update the JSON string below
json = "{}"
# create an instance of ActivitySet from a JSON string
activity_set_instance = ActivitySet.from_json(json)
# print the JSON string representation of the object
print(ActivitySet.to_json())

# convert the object into a dict
activity_set_dict = activity_set_instance.to_dict()
# create an instance of ActivitySet from a dict
activity_set_from_dict = ActivitySet.from_dict(activity_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


