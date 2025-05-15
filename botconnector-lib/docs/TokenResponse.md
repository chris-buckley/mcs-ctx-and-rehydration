# TokenResponse

A response that includes a user token

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **str** | The channelId of the TokenResponse | [optional] 
**connection_name** | **str** | The connection name | [optional] 
**token** | **str** | The user token | [optional] 
**expiration** | **str** | Expiration for the token, in ISO 8601 format (e.g. \&quot;2007-04-05T14:30Z\&quot;) | [optional] 

## Example

```python
from bot_connector.models.token_response import TokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenResponse from a JSON string
token_response_instance = TokenResponse.from_json(json)
# print the JSON string representation of the object
print(TokenResponse.to_json())

# convert the object into a dict
token_response_dict = token_response_instance.to_dict()
# create an instance of TokenResponse from a dict
token_response_from_dict = TokenResponse.from_dict(token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


