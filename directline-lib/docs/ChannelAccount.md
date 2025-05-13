# ChannelAccount

Channel account information needed to route a message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Channel id for the user or bot on this channel (Example: joe@smith.com, or @joesmith or 123456) | [optional] 
**name** | **str** | Display friendly name | [optional] 
**aad_object_id** | **str** | This account&#39;s object ID within Azure Active Directory (AAD) | [optional] 
**role** | **str** | Role of the entity behind the account (Example: User, Bot, etc.) | [optional] 

## Example

```python
from direct_line.models.channel_account import ChannelAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelAccount from a JSON string
channel_account_instance = ChannelAccount.from_json(json)
# print the JSON string representation of the object
print(ChannelAccount.to_json())

# convert the object into a dict
channel_account_dict = channel_account_instance.to_dict()
# create an instance of ChannelAccount from a dict
channel_account_from_dict = ChannelAccount.from_dict(channel_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


