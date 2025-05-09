from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.channel_account import ChannelAccount


T = TypeVar("T", bound="Mention")


@_attrs_define
class Mention:
    """Mention information (entity type: "mention")

    Attributes:
        mentioned (Union[Unset, ChannelAccount]): Channel account information needed to route a message
        text (Union[Unset, str]): Sub Text which represents the mention (can be null or empty)
        type_ (Union[Unset, str]): Type of this entity (RFC 3987 IRI)
    """

    mentioned: Union[Unset, "ChannelAccount"] = UNSET
    text: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mentioned: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.mentioned, Unset):
            mentioned = self.mentioned.to_dict()

        text = self.text

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mentioned is not UNSET:
            field_dict["mentioned"] = mentioned
        if text is not UNSET:
            field_dict["text"] = text
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.channel_account import ChannelAccount

        d = dict(src_dict)
        _mentioned = d.pop("mentioned", UNSET)
        mentioned: Union[Unset, ChannelAccount]
        if isinstance(_mentioned, Unset):
            mentioned = UNSET
        else:
            mentioned = ChannelAccount.from_dict(_mentioned)

        text = d.pop("text", UNSET)

        type_ = d.pop("type", UNSET)

        mention = cls(
            mentioned=mentioned,
            text=text,
            type_=type_,
        )

        mention.additional_properties = d
        return mention

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
