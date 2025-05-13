# TokenParameters

Parameters for creating a token

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**ChannelAccount**](ChannelAccount.md) |  | [optional] 
**trusted_origins** | **List[str]** | Trusted origins to embed within the token | [optional] 
**e_tag** | **str** |  | [optional] 

## Example

```python
from direct_line.models.token_parameters import TokenParameters

# TODO update the JSON string below
json = "{}"
# create an instance of TokenParameters from a JSON string
token_parameters_instance = TokenParameters.from_json(json)
# print the JSON string representation of the object
print(TokenParameters.to_json())

# convert the object into a dict
token_parameters_dict = token_parameters_instance.to_dict()
# create an instance of TokenParameters from a dict
token_parameters_from_dict = TokenParameters.from_dict(token_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


