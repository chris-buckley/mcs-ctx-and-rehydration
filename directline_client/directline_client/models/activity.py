import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_channel_data import ActivityChannelData
    from ..models.activity_value import ActivityValue
    from ..models.attachment import Attachment
    from ..models.channel_account import ChannelAccount
    from ..models.conversation_account import ConversationAccount
    from ..models.conversation_reference import ConversationReference
    from ..models.entity import Entity
    from ..models.message_reaction import MessageReaction
    from ..models.semantic_action import SemanticAction
    from ..models.suggested_actions import SuggestedActions
    from ..models.text_highlight import TextHighlight


T = TypeVar("T", bound="Activity")


@_attrs_define
class Activity:
    """An Activity is the basic communication type for the Bot Framework 3.0 protocol.

    Attributes:
        type_ (Union[Unset, str]): Contains the activity type.
        id (Union[Unset, str]): Contains an ID that uniquely identifies the activity on the channel.
        timestamp (Union[Unset, datetime.datetime]): Contains the date and time that the message was sent, in UTC,
            expressed in ISO-8601 format.
        local_timestamp (Union[Unset, datetime.datetime]): Contains the local date and time of the message, expressed in
            ISO-8601 format.
            For example, 2016-09-23T13:07:49.4714686-07:00.
        local_timezone (Union[Unset, str]): Contains the name of the local timezone of the message, expressed in IANA
            Time Zone database format.
            For example, America/Los_Angeles.
        service_url (Union[Unset, str]): Contains the URL that specifies the channel's service endpoint. Set by the
            channel.
        channel_id (Union[Unset, str]): Contains an ID that uniquely identifies the channel. Set by the channel.
        from_ (Union[Unset, ChannelAccount]): Channel account information needed to route a message
        conversation (Union[Unset, ConversationAccount]): Conversation account represents the identity of the
            conversation within a channel
        recipient (Union[Unset, ChannelAccount]): Channel account information needed to route a message
        text_format (Union[Unset, str]): Format of text fields Default:markdown
        attachment_layout (Union[Unset, str]): The layout hint for multiple attachments. Default: list.
        members_added (Union[Unset, list['ChannelAccount']]): The collection of members added to the conversation.
        members_removed (Union[Unset, list['ChannelAccount']]): The collection of members removed from the conversation.
        reactions_added (Union[Unset, list['MessageReaction']]): The collection of reactions added to the conversation.
        reactions_removed (Union[Unset, list['MessageReaction']]): The collection of reactions removed from the
            conversation.
        topic_name (Union[Unset, str]): The updated topic name of the conversation.
        history_disclosed (Union[Unset, bool]): Indicates whether the prior history of the channel is disclosed.
        locale (Union[Unset, str]): A locale name for the contents of the text field.
            The locale name is a combination of an ISO 639 two- or three-letter culture code associated with a language
            and an ISO 3166 two-letter subculture code associated with a country or region.
            The locale name can also correspond to a valid BCP-47 language tag.
        text (Union[Unset, str]): The text content of the message.
        speak (Union[Unset, str]): The text to speak.
        input_hint (Union[Unset, str]): Indicates whether your bot is accepting,
            expecting, or ignoring user input after the message is delivered to the client.
        summary (Union[Unset, str]): The text to display if the channel cannot render cards.
        suggested_actions (Union[Unset, SuggestedActions]): SuggestedActions that can be performed
        attachments (Union[Unset, list['Attachment']]): Attachments
        entities (Union[Unset, list['Entity']]): Represents the entities that were mentioned in the message.
        channel_data (Union[Unset, ActivityChannelData]): Contains channel-specific content.
        action (Union[Unset, str]): Indicates whether the recipient of a contactRelationUpdate was added or removed from
            the sender's contact list.
        reply_to_id (Union[Unset, str]): Contains the ID of the message to which this message is a reply.
        label (Union[Unset, str]): A descriptive label for the activity.
        value_type (Union[Unset, str]): The type of the activity's value object.
        value (Union[Unset, ActivityValue]): A value that is associated with the activity.
        name (Union[Unset, str]): The name of the operation associated with an invoke or event activity.
        relates_to (Union[Unset, ConversationReference]): An object relating to a particular point in a conversation
        code (Union[Unset, str]): The a code for endOfConversation activities that indicates why the conversation ended.
        expiration (Union[Unset, datetime.datetime]): The time at which the activity should be considered to be
            "expired" and should not be presented to the recipient.
        importance (Union[Unset, str]): The importance of the activity.
        delivery_mode (Union[Unset, str]): A delivery hint to signal to the recipient alternate delivery paths for the
            activity.
            The default delivery mode is "default".
        listen_for (Union[Unset, list[str]]): List of phrases and references that speech and language priming systems
            should listen for
        text_highlights (Union[Unset, list['TextHighlight']]): The collection of text fragments to highlight when the
            activity contains a ReplyToId value.
        semantic_action (Union[Unset, SemanticAction]): Represents a reference to a programmatic action
    """

    type_: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET
    local_timestamp: Union[Unset, datetime.datetime] = UNSET
    local_timezone: Union[Unset, str] = UNSET
    service_url: Union[Unset, str] = UNSET
    channel_id: Union[Unset, str] = UNSET
    from_: Union[Unset, "ChannelAccount"] = UNSET
    conversation: Union[Unset, "ConversationAccount"] = UNSET
    recipient: Union[Unset, "ChannelAccount"] = UNSET
    text_format: Union[Unset, str] = UNSET
    attachment_layout: Union[Unset, str] = UNSET
    members_added: Union[Unset, list["ChannelAccount"]] = UNSET
    members_removed: Union[Unset, list["ChannelAccount"]] = UNSET
    reactions_added: Union[Unset, list["MessageReaction"]] = UNSET
    reactions_removed: Union[Unset, list["MessageReaction"]] = UNSET
    topic_name: Union[Unset, str] = UNSET
    history_disclosed: Union[Unset, bool] = UNSET
    locale: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    speak: Union[Unset, str] = UNSET
    input_hint: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    suggested_actions: Union[Unset, "SuggestedActions"] = UNSET
    attachments: Union[Unset, list["Attachment"]] = UNSET
    entities: Union[Unset, list["Entity"]] = UNSET
    channel_data: Union[Unset, "ActivityChannelData"] = UNSET
    action: Union[Unset, str] = UNSET
    reply_to_id: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    value_type: Union[Unset, str] = UNSET
    value: Union[Unset, "ActivityValue"] = UNSET
    name: Union[Unset, str] = UNSET
    relates_to: Union[Unset, "ConversationReference"] = UNSET
    code: Union[Unset, str] = UNSET
    expiration: Union[Unset, datetime.datetime] = UNSET
    importance: Union[Unset, str] = UNSET
    delivery_mode: Union[Unset, str] = UNSET
    listen_for: Union[Unset, list[str]] = UNSET
    text_highlights: Union[Unset, list["TextHighlight"]] = UNSET
    semantic_action: Union[Unset, "SemanticAction"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id = self.id

        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        local_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.local_timestamp, Unset):
            local_timestamp = self.local_timestamp.isoformat()

        local_timezone = self.local_timezone

        service_url = self.service_url

        channel_id = self.channel_id

        from_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        conversation: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.conversation, Unset):
            conversation = self.conversation.to_dict()

        recipient: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.recipient, Unset):
            recipient = self.recipient.to_dict()

        text_format = self.text_format

        attachment_layout = self.attachment_layout

        members_added: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.members_added, Unset):
            members_added = []
            for members_added_item_data in self.members_added:
                members_added_item = members_added_item_data.to_dict()
                members_added.append(members_added_item)

        members_removed: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.members_removed, Unset):
            members_removed = []
            for members_removed_item_data in self.members_removed:
                members_removed_item = members_removed_item_data.to_dict()
                members_removed.append(members_removed_item)

        reactions_added: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.reactions_added, Unset):
            reactions_added = []
            for reactions_added_item_data in self.reactions_added:
                reactions_added_item = reactions_added_item_data.to_dict()
                reactions_added.append(reactions_added_item)

        reactions_removed: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.reactions_removed, Unset):
            reactions_removed = []
            for reactions_removed_item_data in self.reactions_removed:
                reactions_removed_item = reactions_removed_item_data.to_dict()
                reactions_removed.append(reactions_removed_item)

        topic_name = self.topic_name

        history_disclosed = self.history_disclosed

        locale = self.locale

        text = self.text

        speak = self.speak

        input_hint = self.input_hint

        summary = self.summary

        suggested_actions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.suggested_actions, Unset):
            suggested_actions = self.suggested_actions.to_dict()

        attachments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        entities: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.entities, Unset):
            entities = []
            for entities_item_data in self.entities:
                entities_item = entities_item_data.to_dict()
                entities.append(entities_item)

        channel_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.channel_data, Unset):
            channel_data = self.channel_data.to_dict()

        action = self.action

        reply_to_id = self.reply_to_id

        label = self.label

        value_type = self.value_type

        value: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        name = self.name

        relates_to: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.relates_to, Unset):
            relates_to = self.relates_to.to_dict()

        code = self.code

        expiration: Union[Unset, str] = UNSET
        if not isinstance(self.expiration, Unset):
            expiration = self.expiration.isoformat()

        importance = self.importance

        delivery_mode = self.delivery_mode

        listen_for: Union[Unset, list[str]] = UNSET
        if not isinstance(self.listen_for, Unset):
            listen_for = self.listen_for

        text_highlights: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.text_highlights, Unset):
            text_highlights = []
            for text_highlights_item_data in self.text_highlights:
                text_highlights_item = text_highlights_item_data.to_dict()
                text_highlights.append(text_highlights_item)

        semantic_action: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.semantic_action, Unset):
            semantic_action = self.semantic_action.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if id is not UNSET:
            field_dict["id"] = id
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if local_timestamp is not UNSET:
            field_dict["localTimestamp"] = local_timestamp
        if local_timezone is not UNSET:
            field_dict["localTimezone"] = local_timezone
        if service_url is not UNSET:
            field_dict["serviceUrl"] = service_url
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if from_ is not UNSET:
            field_dict["from"] = from_
        if conversation is not UNSET:
            field_dict["conversation"] = conversation
        if recipient is not UNSET:
            field_dict["recipient"] = recipient
        if text_format is not UNSET:
            field_dict["textFormat"] = text_format
        if attachment_layout is not UNSET:
            field_dict["attachmentLayout"] = attachment_layout
        if members_added is not UNSET:
            field_dict["membersAdded"] = members_added
        if members_removed is not UNSET:
            field_dict["membersRemoved"] = members_removed
        if reactions_added is not UNSET:
            field_dict["reactionsAdded"] = reactions_added
        if reactions_removed is not UNSET:
            field_dict["reactionsRemoved"] = reactions_removed
        if topic_name is not UNSET:
            field_dict["topicName"] = topic_name
        if history_disclosed is not UNSET:
            field_dict["historyDisclosed"] = history_disclosed
        if locale is not UNSET:
            field_dict["locale"] = locale
        if text is not UNSET:
            field_dict["text"] = text
        if speak is not UNSET:
            field_dict["speak"] = speak
        if input_hint is not UNSET:
            field_dict["inputHint"] = input_hint
        if summary is not UNSET:
            field_dict["summary"] = summary
        if suggested_actions is not UNSET:
            field_dict["suggestedActions"] = suggested_actions
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if entities is not UNSET:
            field_dict["entities"] = entities
        if channel_data is not UNSET:
            field_dict["channelData"] = channel_data
        if action is not UNSET:
            field_dict["action"] = action
        if reply_to_id is not UNSET:
            field_dict["replyToId"] = reply_to_id
        if label is not UNSET:
            field_dict["label"] = label
        if value_type is not UNSET:
            field_dict["valueType"] = value_type
        if value is not UNSET:
            field_dict["value"] = value
        if name is not UNSET:
            field_dict["name"] = name
        if relates_to is not UNSET:
            field_dict["relatesTo"] = relates_to
        if code is not UNSET:
            field_dict["code"] = code
        if expiration is not UNSET:
            field_dict["expiration"] = expiration
        if importance is not UNSET:
            field_dict["importance"] = importance
        if delivery_mode is not UNSET:
            field_dict["deliveryMode"] = delivery_mode
        if listen_for is not UNSET:
            field_dict["listenFor"] = listen_for
        if text_highlights is not UNSET:
            field_dict["textHighlights"] = text_highlights
        if semantic_action is not UNSET:
            field_dict["semanticAction"] = semantic_action

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_channel_data import ActivityChannelData
        from ..models.activity_value import ActivityValue
        from ..models.attachment import Attachment
        from ..models.channel_account import ChannelAccount
        from ..models.conversation_account import ConversationAccount
        from ..models.conversation_reference import ConversationReference
        from ..models.entity import Entity
        from ..models.message_reaction import MessageReaction
        from ..models.semantic_action import SemanticAction
        from ..models.suggested_actions import SuggestedActions
        from ..models.text_highlight import TextHighlight

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        id = d.pop("id", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        _local_timestamp = d.pop("localTimestamp", UNSET)
        local_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_local_timestamp, Unset):
            local_timestamp = UNSET
        else:
            local_timestamp = isoparse(_local_timestamp)

        local_timezone = d.pop("localTimezone", UNSET)

        service_url = d.pop("serviceUrl", UNSET)

        channel_id = d.pop("channelId", UNSET)

        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, ChannelAccount]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = ChannelAccount.from_dict(_from_)

        _conversation = d.pop("conversation", UNSET)
        conversation: Union[Unset, ConversationAccount]
        if isinstance(_conversation, Unset):
            conversation = UNSET
        else:
            conversation = ConversationAccount.from_dict(_conversation)

        _recipient = d.pop("recipient", UNSET)
        recipient: Union[Unset, ChannelAccount]
        if isinstance(_recipient, Unset):
            recipient = UNSET
        else:
            recipient = ChannelAccount.from_dict(_recipient)

        text_format = d.pop("textFormat", UNSET)

        attachment_layout = d.pop("attachmentLayout", UNSET)

        members_added = []
        _members_added = d.pop("membersAdded", UNSET)
        for members_added_item_data in _members_added or []:
            members_added_item = ChannelAccount.from_dict(members_added_item_data)

            members_added.append(members_added_item)

        members_removed = []
        _members_removed = d.pop("membersRemoved", UNSET)
        for members_removed_item_data in _members_removed or []:
            members_removed_item = ChannelAccount.from_dict(members_removed_item_data)

            members_removed.append(members_removed_item)

        reactions_added = []
        _reactions_added = d.pop("reactionsAdded", UNSET)
        for reactions_added_item_data in _reactions_added or []:
            reactions_added_item = MessageReaction.from_dict(reactions_added_item_data)

            reactions_added.append(reactions_added_item)

        reactions_removed = []
        _reactions_removed = d.pop("reactionsRemoved", UNSET)
        for reactions_removed_item_data in _reactions_removed or []:
            reactions_removed_item = MessageReaction.from_dict(reactions_removed_item_data)

            reactions_removed.append(reactions_removed_item)

        topic_name = d.pop("topicName", UNSET)

        history_disclosed = d.pop("historyDisclosed", UNSET)

        locale = d.pop("locale", UNSET)

        text = d.pop("text", UNSET)

        speak = d.pop("speak", UNSET)

        input_hint = d.pop("inputHint", UNSET)

        summary = d.pop("summary", UNSET)

        _suggested_actions = d.pop("suggestedActions", UNSET)
        suggested_actions: Union[Unset, SuggestedActions]
        if isinstance(_suggested_actions, Unset):
            suggested_actions = UNSET
        else:
            suggested_actions = SuggestedActions.from_dict(_suggested_actions)

        attachments = []
        _attachments = d.pop("attachments", UNSET)
        for attachments_item_data in _attachments or []:
            attachments_item = Attachment.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        entities = []
        _entities = d.pop("entities", UNSET)
        for entities_item_data in _entities or []:
            entities_item = Entity.from_dict(entities_item_data)

            entities.append(entities_item)

        _channel_data = d.pop("channelData", UNSET)
        channel_data: Union[Unset, ActivityChannelData]
        if isinstance(_channel_data, Unset):
            channel_data = UNSET
        else:
            channel_data = ActivityChannelData.from_dict(_channel_data)

        action = d.pop("action", UNSET)

        reply_to_id = d.pop("replyToId", UNSET)

        label = d.pop("label", UNSET)

        value_type = d.pop("valueType", UNSET)

        _value = d.pop("value", UNSET)
        value: Union[Unset, ActivityValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = ActivityValue.from_dict(_value)

        name = d.pop("name", UNSET)

        _relates_to = d.pop("relatesTo", UNSET)
        relates_to: Union[Unset, ConversationReference]
        if isinstance(_relates_to, Unset):
            relates_to = UNSET
        else:
            relates_to = ConversationReference.from_dict(_relates_to)

        code = d.pop("code", UNSET)

        _expiration = d.pop("expiration", UNSET)
        expiration: Union[Unset, datetime.datetime]
        if isinstance(_expiration, Unset):
            expiration = UNSET
        else:
            expiration = isoparse(_expiration)

        importance = d.pop("importance", UNSET)

        delivery_mode = d.pop("deliveryMode", UNSET)

        listen_for = cast(list[str], d.pop("listenFor", UNSET))

        text_highlights = []
        _text_highlights = d.pop("textHighlights", UNSET)
        for text_highlights_item_data in _text_highlights or []:
            text_highlights_item = TextHighlight.from_dict(text_highlights_item_data)

            text_highlights.append(text_highlights_item)

        _semantic_action = d.pop("semanticAction", UNSET)
        semantic_action: Union[Unset, SemanticAction]
        if isinstance(_semantic_action, Unset):
            semantic_action = UNSET
        else:
            semantic_action = SemanticAction.from_dict(_semantic_action)

        activity = cls(
            type_=type_,
            id=id,
            timestamp=timestamp,
            local_timestamp=local_timestamp,
            local_timezone=local_timezone,
            service_url=service_url,
            channel_id=channel_id,
            from_=from_,
            conversation=conversation,
            recipient=recipient,
            text_format=text_format,
            attachment_layout=attachment_layout,
            members_added=members_added,
            members_removed=members_removed,
            reactions_added=reactions_added,
            reactions_removed=reactions_removed,
            topic_name=topic_name,
            history_disclosed=history_disclosed,
            locale=locale,
            text=text,
            speak=speak,
            input_hint=input_hint,
            summary=summary,
            suggested_actions=suggested_actions,
            attachments=attachments,
            entities=entities,
            channel_data=channel_data,
            action=action,
            reply_to_id=reply_to_id,
            label=label,
            value_type=value_type,
            value=value,
            name=name,
            relates_to=relates_to,
            code=code,
            expiration=expiration,
            importance=importance,
            delivery_mode=delivery_mode,
            listen_for=listen_for,
            text_highlights=text_highlights,
            semantic_action=semantic_action,
        )

        activity.additional_properties = d
        return activity

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
