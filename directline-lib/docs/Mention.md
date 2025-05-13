# Mention

Mention information (entity type: \"mention\")

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mentioned** | [**ChannelAccount**](ChannelAccount.md) |  | [optional] 
**text** | **str** | Sub Text which represents the mention (can be null or empty) | [optional] 
**type** | **str** | Type of this entity (RFC 3987 IRI) | [optional] 

## Example

```python
from direct_line.models.mention import Mention

# TODO update the JSON string below
json = "{}"
# create an instance of Mention from a JSON string
mention_instance = Mention.from_json(json)
# print the JSON string representation of the object
print(Mention.to_json())

# convert the object into a dict
mention_dict = mention_instance.to_dict()
# create an instance of Mention from a dict
mention_from_dict = Mention.from_dict(mention_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


