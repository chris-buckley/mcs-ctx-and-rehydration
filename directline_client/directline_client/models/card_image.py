from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.card_action import CardAction


T = TypeVar("T", bound="CardImage")


@_attrs_define
class CardImage:
    """An image on a card

    Attributes:
        url (Union[Unset, str]): URL thumbnail image for major content property
        alt (Union[Unset, str]): Image description intended for screen readers
        tap (Union[Unset, CardAction]): A clickable action
    """

    url: Union[Unset, str] = UNSET
    alt: Union[Unset, str] = UNSET
    tap: Union[Unset, "CardAction"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        alt = self.alt

        tap: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tap, Unset):
            tap = self.tap.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if alt is not UNSET:
            field_dict["alt"] = alt
        if tap is not UNSET:
            field_dict["tap"] = tap

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.card_action import CardAction

        d = dict(src_dict)
        url = d.pop("url", UNSET)

        alt = d.pop("alt", UNSET)

        _tap = d.pop("tap", UNSET)
        tap: Union[Unset, CardAction]
        if isinstance(_tap, Unset):
            tap = UNSET
        else:
            tap = CardAction.from_dict(_tap)

        card_image = cls(
            url=url,
            alt=alt,
            tap=tap,
        )

        card_image.additional_properties = d
        return card_image

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
