# PagedMembersResult

Page of members.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continuation_token** | **str** | Paging token | [optional] 
**members** | [**List[ChannelAccount]**](ChannelAccount.md) | The Channel Accounts. | [optional] 

## Example

```python
from bot_connector.models.paged_members_result import PagedMembersResult

# TODO update the JSON string below
json = "{}"
# create an instance of PagedMembersResult from a JSON string
paged_members_result_instance = PagedMembersResult.from_json(json)
# print the JSON string representation of the object
print(PagedMembersResult.to_json())

# convert the object into a dict
paged_members_result_dict = paged_members_result_instance.to_dict()
# create an instance of PagedMembersResult from a dict
paged_members_result_from_dict = PagedMembersResult.from_dict(paged_members_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


