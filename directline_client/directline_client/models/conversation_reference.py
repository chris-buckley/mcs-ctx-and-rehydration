from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.channel_account import ChannelAccount
    from ..models.conversation_account import ConversationAccount


T = TypeVar("T", bound="ConversationReference")


@_attrs_define
class ConversationReference:
    """An object relating to a particular point in a conversation

    Attributes:
        activity_id (Union[Unset, str]): (Optional) ID of the activity to refer to
        user (Union[Unset, ChannelAccount]): Channel account information needed to route a message
        bot (Union[Unset, ChannelAccount]): Channel account information needed to route a message
        conversation (Union[Unset, ConversationAccount]): Conversation account represents the identity of the
            conversation within a channel
        channel_id (Union[Unset, str]): Channel ID
        service_url (Union[Unset, str]): Service endpoint where operations concerning the referenced conversation may be
            performed
    """

    activity_id: Union[Unset, str] = UNSET
    user: Union[Unset, "ChannelAccount"] = UNSET
    bot: Union[Unset, "ChannelAccount"] = UNSET
    conversation: Union[Unset, "ConversationAccount"] = UNSET
    channel_id: Union[Unset, str] = UNSET
    service_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity_id = self.activity_id

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        bot: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bot, Unset):
            bot = self.bot.to_dict()

        conversation: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.conversation, Unset):
            conversation = self.conversation.to_dict()

        channel_id = self.channel_id

        service_url = self.service_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activity_id is not UNSET:
            field_dict["activityId"] = activity_id
        if user is not UNSET:
            field_dict["user"] = user
        if bot is not UNSET:
            field_dict["bot"] = bot
        if conversation is not UNSET:
            field_dict["conversation"] = conversation
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if service_url is not UNSET:
            field_dict["serviceUrl"] = service_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.channel_account import ChannelAccount
        from ..models.conversation_account import ConversationAccount

        d = dict(src_dict)
        activity_id = d.pop("activityId", UNSET)

        _user = d.pop("user", UNSET)
        user: Union[Unset, ChannelAccount]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = ChannelAccount.from_dict(_user)

        _bot = d.pop("bot", UNSET)
        bot: Union[Unset, ChannelAccount]
        if isinstance(_bot, Unset):
            bot = UNSET
        else:
            bot = ChannelAccount.from_dict(_bot)

        _conversation = d.pop("conversation", UNSET)
        conversation: Union[Unset, ConversationAccount]
        if isinstance(_conversation, Unset):
            conversation = UNSET
        else:
            conversation = ConversationAccount.from_dict(_conversation)

        channel_id = d.pop("channelId", UNSET)

        service_url = d.pop("serviceUrl", UNSET)

        conversation_reference = cls(
            activity_id=activity_id,
            user=user,
            bot=bot,
            conversation=conversation,
            channel_id=channel_id,
            service_url=service_url,
        )

        conversation_reference.additional_properties = d
        return conversation_reference

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
