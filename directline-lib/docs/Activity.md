# Activity

An Activity is the basic communication type for the Bot Framework 3.0 protocol.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Contains the activity type. | [optional] 
**id** | **str** | Contains an ID that uniquely identifies the activity on the channel. | [optional] 
**timestamp** | **datetime** | Contains the date and time that the message was sent, in UTC, expressed in ISO-8601 format. | [optional] 
**local_timestamp** | **datetime** | Contains the local date and time of the message, expressed in ISO-8601 format.  For example, 2016-09-23T13:07:49.4714686-07:00. | [optional] 
**local_timezone** | **str** | Contains the name of the local timezone of the message, expressed in IANA Time Zone database format.  For example, America/Los_Angeles. | [optional] 
**service_url** | **str** | Contains the URL that specifies the channel&#39;s service endpoint. Set by the channel. | [optional] 
**channel_id** | **str** | Contains an ID that uniquely identifies the channel. Set by the channel. | [optional] 
**var_from** | [**ChannelAccount**](ChannelAccount.md) |  | [optional] 
**conversation** | [**ConversationAccount**](ConversationAccount.md) |  | [optional] 
**recipient** | [**ChannelAccount**](ChannelAccount.md) |  | [optional] 
**text_format** | **str** | Format of text fields Default:markdown | [optional] 
**attachment_layout** | **str** | The layout hint for multiple attachments. Default: list. | [optional] 
**members_added** | [**List[ChannelAccount]**](ChannelAccount.md) | The collection of members added to the conversation. | [optional] 
**members_removed** | [**List[ChannelAccount]**](ChannelAccount.md) | The collection of members removed from the conversation. | [optional] 
**reactions_added** | [**List[MessageReaction]**](MessageReaction.md) | The collection of reactions added to the conversation. | [optional] 
**reactions_removed** | [**List[MessageReaction]**](MessageReaction.md) | The collection of reactions removed from the conversation. | [optional] 
**topic_name** | **str** | The updated topic name of the conversation. | [optional] 
**history_disclosed** | **bool** | Indicates whether the prior history of the channel is disclosed. | [optional] 
**locale** | **str** | A locale name for the contents of the text field.  The locale name is a combination of an ISO 639 two- or three-letter culture code associated with a language  and an ISO 3166 two-letter subculture code associated with a country or region.  The locale name can also correspond to a valid BCP-47 language tag. | [optional] 
**text** | **str** | The text content of the message. | [optional] 
**speak** | **str** | The text to speak. | [optional] 
**input_hint** | **str** | Indicates whether your bot is accepting,  expecting, or ignoring user input after the message is delivered to the client. | [optional] 
**summary** | **str** | The text to display if the channel cannot render cards. | [optional] 
**suggested_actions** | [**SuggestedActions**](SuggestedActions.md) |  | [optional] 
**attachments** | [**List[Attachment]**](Attachment.md) | Attachments | [optional] 
**entities** | [**List[Entity]**](Entity.md) | Represents the entities that were mentioned in the message. | [optional] 
**channel_data** | **object** | Contains channel-specific content. | [optional] 
**action** | **str** | Indicates whether the recipient of a contactRelationUpdate was added or removed from the sender&#39;s contact list. | [optional] 
**reply_to_id** | **str** | Contains the ID of the message to which this message is a reply. | [optional] 
**label** | **str** | A descriptive label for the activity. | [optional] 
**value_type** | **str** | The type of the activity&#39;s value object. | [optional] 
**value** | **object** | A value that is associated with the activity. | [optional] 
**name** | **str** | The name of the operation associated with an invoke or event activity. | [optional] 
**relates_to** | [**ConversationReference**](ConversationReference.md) |  | [optional] 
**code** | **str** | The a code for endOfConversation activities that indicates why the conversation ended. | [optional] 
**expiration** | **datetime** | The time at which the activity should be considered to be \&quot;expired\&quot; and should not be presented to the recipient. | [optional] 
**importance** | **str** | The importance of the activity. | [optional] 
**delivery_mode** | **str** | A delivery hint to signal to the recipient alternate delivery paths for the activity.  The default delivery mode is \&quot;default\&quot;. | [optional] 
**listen_for** | **List[str]** | List of phrases and references that speech and language priming systems should listen for | [optional] 
**text_highlights** | [**List[TextHighlight]**](TextHighlight.md) | The collection of text fragments to highlight when the activity contains a ReplyToId value. | [optional] 
**semantic_action** | [**SemanticAction**](SemanticAction.md) |  | [optional] 

## Example

```python
from direct_line.models.activity import Activity

# TODO update the JSON string below
json = "{}"
# create an instance of Activity from a JSON string
activity_instance = Activity.from_json(json)
# print the JSON string representation of the object
print(Activity.to_json())

# convert the object into a dict
activity_dict = activity_instance.to_dict()
# create an instance of Activity from a dict
activity_from_dict = Activity.from_dict(activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


