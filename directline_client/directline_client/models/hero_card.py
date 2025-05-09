from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.card_action import CardAction
    from ..models.card_image import CardImage


T = TypeVar("T", bound="HeroCard")


@_attrs_define
class HeroCard:
    """A Hero card (card with a single, large image)

    Attributes:
        title (Union[Unset, str]): Title of the card
        subtitle (Union[Unset, str]): Subtitle of the card
        text (Union[Unset, str]): Text for the card
        images (Union[Unset, list['CardImage']]): Array of images for the card
        buttons (Union[Unset, list['CardAction']]): Set of actions applicable to the current card
        tap (Union[Unset, CardAction]): A clickable action
    """

    title: Union[Unset, str] = UNSET
    subtitle: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    images: Union[Unset, list["CardImage"]] = UNSET
    buttons: Union[Unset, list["CardAction"]] = UNSET
    tap: Union[Unset, "CardAction"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        subtitle = self.subtitle

        text = self.text

        images: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        buttons: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.buttons, Unset):
            buttons = []
            for buttons_item_data in self.buttons:
                buttons_item = buttons_item_data.to_dict()
                buttons.append(buttons_item)

        tap: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tap, Unset):
            tap = self.tap.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if text is not UNSET:
            field_dict["text"] = text
        if images is not UNSET:
            field_dict["images"] = images
        if buttons is not UNSET:
            field_dict["buttons"] = buttons
        if tap is not UNSET:
            field_dict["tap"] = tap

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.card_action import CardAction
        from ..models.card_image import CardImage

        d = dict(src_dict)
        title = d.pop("title", UNSET)

        subtitle = d.pop("subtitle", UNSET)

        text = d.pop("text", UNSET)

        images = []
        _images = d.pop("images", UNSET)
        for images_item_data in _images or []:
            images_item = CardImage.from_dict(images_item_data)

            images.append(images_item)

        buttons = []
        _buttons = d.pop("buttons", UNSET)
        for buttons_item_data in _buttons or []:
            buttons_item = CardAction.from_dict(buttons_item_data)

            buttons.append(buttons_item)

        _tap = d.pop("tap", UNSET)
        tap: Union[Unset, CardAction]
        if isinstance(_tap, Unset):
            tap = UNSET
        else:
            tap = CardAction.from_dict(_tap)

        hero_card = cls(
            title=title,
            subtitle=subtitle,
            text=text,
            images=images,
            buttons=buttons,
            tap=tap,
        )

        hero_card.additional_properties = d
        return hero_card

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
