# Thing

Thing (entity type: \"https://schema.org/Thing\")

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the thing | [optional] 
**name** | **str** | The name of the thing | [optional] 

## Example

```python
from direct_line.models.thing import Thing

# TODO update the JSON string below
json = "{}"
# create an instance of Thing from a JSON string
thing_instance = Thing.from_json(json)
# print the JSON string representation of the object
print(Thing.to_json())

# convert the object into a dict
thing_dict = thing_instance.to_dict()
# create an instance of Thing from a dict
thing_from_dict = Thing.from_dict(thing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


