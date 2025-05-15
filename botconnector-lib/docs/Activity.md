# Activity

An Activity is the basic communication type for the Bot Framework 3.0 protocol.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ActivityTypes**](ActivityTypes.md) |  | [optional] 
**id** | **str** | Contains an ID that uniquely identifies the activity on the channel. | [optional] 
**timestamp** | **datetime** | Contains the date and time that the message was sent, in UTC, expressed in ISO-8601 format. | [optional] 
**local_timestamp** | **datetime** | Contains the local date and time of the message, expressed in ISO-8601 format.  For example, 2016-09-23T13:07:49.4714686-07:00. | [optional] 
**local_timezone** | **str** | Contains the name of the local timezone of the message, expressed in IANA Time Zone database format.  For example, America/Los_Angeles. | [optional] 
**caller_id** | **str** | A string containing an IRI identifying the caller of a bot. This field is not intended to be transmitted  over the wire, but is instead populated by bots and clients based on cryptographically verifiable data  that asserts the identity of the callers (e.g. tokens). | [optional] 
**service_url** | **str** | Contains the URL that specifies the channel&#39;s service endpoint. Set by the channel. | [optional] 
**channel_id** | **str** | Contains an ID that uniquely identifies the channel. Set by the channel. | [optional] 
**var_from** | [**ChannelAccount**](ChannelAccount.md) |  | [optional] 
**conversation** | [**ConversationAccount**](ConversationAccount.md) |  | [optional] 
**recipient** | [**ChannelAccount**](ChannelAccount.md) |  | [optional] 
**text_format** | [**TextFormatTypes**](TextFormatTypes.md) |  | [optional] 
**attachment_layout** | [**AttachmentLayoutTypes**](AttachmentLayoutTypes.md) |  | [optional] 
**members_added** | [**List[ChannelAccount]**](ChannelAccount.md) | The collection of members added to the conversation. | [optional] 
**members_removed** | [**List[ChannelAccount]**](ChannelAccount.md) | The collection of members removed from the conversation. | [optional] 
**reactions_added** | [**List[MessageReaction]**](MessageReaction.md) | The collection of reactions added to the conversation. | [optional] 
**reactions_removed** | [**List[MessageReaction]**](MessageReaction.md) | The collection of reactions removed from the conversation. | [optional] 
**topic_name** | **str** | The updated topic name of the conversation. | [optional] 
**history_disclosed** | **bool** | Indicates whether the prior history of the channel is disclosed. | [optional] 
**locale** | **str** | A locale name for the contents of the text field.  The locale name is a combination of an ISO 639 two- or three-letter culture code associated with a language  and an ISO 3166 two-letter subculture code associated with a country or region.  The locale name can also correspond to a valid BCP-47 language tag. | [optional] 
**text** | **str** | The text content of the message. | [optional] 
**speak** | **str** | The text to speak. | [optional] 
**input_hint** | [**InputHints**](InputHints.md) |  | [optional] 
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
**code** | [**EndOfConversationCodes**](EndOfConversationCodes.md) |  | [optional] 
**expiration** | **datetime** | The time at which the activity should be considered to be \&quot;expired\&quot; and should not be presented to the recipient. | [optional] 
**importance** | [**ActivityImportance**](ActivityImportance.md) |  | [optional] 
**delivery_mode** | [**DeliveryModes**](DeliveryModes.md) |  | [optional] 
**listen_for** | **List[str]** | List of phrases and references that speech and language priming systems should listen for | [optional] 
**text_highlights** | [**List[TextHighlight]**](TextHighlight.md) | The collection of text fragments to highlight when the activity contains a ReplyToId value. | [optional] 
**semantic_action** | [**SemanticAction**](SemanticAction.md) |  | [optional] 

## Example

```python
from bot_connector.models.activity import Activity

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


