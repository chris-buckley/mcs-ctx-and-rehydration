# Transcript

Transcript

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activities** | [**List[Activity]**](Activity.md) | A collection of Activities that conforms to the Transcript schema. | [optional] 

## Example

```python
from bot_connector.models.transcript import Transcript

# TODO update the JSON string below
json = "{}"
# create an instance of Transcript from a JSON string
transcript_instance = Transcript.from_json(json)
# print the JSON string representation of the object
print(Transcript.to_json())

# convert the object into a dict
transcript_dict = transcript_instance.to_dict()
# create an instance of Transcript from a dict
transcript_from_dict = Transcript.from_dict(transcript_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


