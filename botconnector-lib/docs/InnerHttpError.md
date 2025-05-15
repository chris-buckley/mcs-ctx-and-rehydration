# InnerHttpError

Object representing inner http error

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** | HttpStatusCode from failed request | [optional] 
**body** | **object** | Body from failed request | [optional] 

## Example

```python
from bot_connector.models.inner_http_error import InnerHttpError

# TODO update the JSON string below
json = "{}"
# create an instance of InnerHttpError from a JSON string
inner_http_error_instance = InnerHttpError.from_json(json)
# print the JSON string representation of the object
print(InnerHttpError.to_json())

# convert the object into a dict
inner_http_error_dict = inner_http_error_instance.to_dict()
# create an instance of InnerHttpError from a dict
inner_http_error_from_dict = InnerHttpError.from_dict(inner_http_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


