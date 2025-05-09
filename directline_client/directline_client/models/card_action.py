from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.card_action_channel_data import CardActionChannelData
    from ..models.card_action_value import CardActionValue


T = TypeVar("T", bound="CardAction")


@_attrs_define
class CardAction:
    """A clickable action

    Attributes:
        type_ (Union[Unset, str]): The type of action implemented by this button
        title (Union[Unset, str]): Text description which appears on the button
        image (Union[Unset, str]): Image URL which will appear on the button, next to text label
        text (Union[Unset, str]): Text for this action
        display_text (Union[Unset, str]): (Optional) text to display in the chat feed if the button is clicked
        value (Union[Unset, CardActionValue]): Supplementary parameter for action. Content of this property depends on
            the ActionType
        channel_data (Union[Unset, CardActionChannelData]): Channel-specific data associated with this action
    """

    type_: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    image: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    display_text: Union[Unset, str] = UNSET
    value: Union[Unset, "CardActionValue"] = UNSET
    channel_data: Union[Unset, "CardActionChannelData"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        title = self.title

        image = self.image

        text = self.text

        display_text = self.display_text

        value: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        channel_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.channel_data, Unset):
            channel_data = self.channel_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if title is not UNSET:
            field_dict["title"] = title
        if image is not UNSET:
            field_dict["image"] = image
        if text is not UNSET:
            field_dict["text"] = text
        if display_text is not UNSET:
            field_dict["displayText"] = display_text
        if value is not UNSET:
            field_dict["value"] = value
        if channel_data is not UNSET:
            field_dict["channelData"] = channel_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.card_action_channel_data import CardActionChannelData
        from ..models.card_action_value import CardActionValue

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        title = d.pop("title", UNSET)

        image = d.pop("image", UNSET)

        text = d.pop("text", UNSET)

        display_text = d.pop("displayText", UNSET)

        _value = d.pop("value", UNSET)
        value: Union[Unset, CardActionValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = CardActionValue.from_dict(_value)

        _channel_data = d.pop("channelData", UNSET)
        channel_data: Union[Unset, CardActionChannelData]
        if isinstance(_channel_data, Unset):
            channel_data = UNSET
        else:
            channel_data = CardActionChannelData.from_dict(_channel_data)

        card_action = cls(
            type_=type_,
            title=title,
            image=image,
            text=text,
            display_text=display_text,
            value=value,
            channel_data=channel_data,
        )

        card_action.additional_properties = d
        return card_action

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
