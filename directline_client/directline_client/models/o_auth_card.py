from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.card_action import CardAction


T = TypeVar("T", bound="OAuthCard")


@_attrs_define
class OAuthCard:
    """A card representing a request to perform a sign in via OAuth

    Attributes:
        text (Union[Unset, str]): Text for signin request
        connection_name (Union[Unset, str]): The name of the registered connection
        buttons (Union[Unset, list['CardAction']]): Action to use to perform signin
    """

    text: Union[Unset, str] = UNSET
    connection_name: Union[Unset, str] = UNSET
    buttons: Union[Unset, list["CardAction"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        connection_name = self.connection_name

        buttons: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.buttons, Unset):
            buttons = []
            for buttons_item_data in self.buttons:
                buttons_item = buttons_item_data.to_dict()
                buttons.append(buttons_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if text is not UNSET:
            field_dict["text"] = text
        if connection_name is not UNSET:
            field_dict["connectionName"] = connection_name
        if buttons is not UNSET:
            field_dict["buttons"] = buttons

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.card_action import CardAction

        d = dict(src_dict)
        text = d.pop("text", UNSET)

        connection_name = d.pop("connectionName", UNSET)

        buttons = []
        _buttons = d.pop("buttons", UNSET)
        for buttons_item_data in _buttons or []:
            buttons_item = CardAction.from_dict(buttons_item_data)

            buttons.append(buttons_item)

        o_auth_card = cls(
            text=text,
            connection_name=connection_name,
            buttons=buttons,
        )

        o_auth_card.additional_properties = d
        return o_auth_card

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
