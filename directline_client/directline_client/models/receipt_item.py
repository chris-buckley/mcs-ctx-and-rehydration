from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.card_action import CardAction
    from ..models.card_image import CardImage


T = TypeVar("T", bound="ReceiptItem")


@_attrs_define
class ReceiptItem:
    """An item on a receipt card

    Attributes:
        title (Union[Unset, str]): Title of the Card
        subtitle (Union[Unset, str]): Subtitle appears just below Title field, differs from Title in font styling only
        text (Union[Unset, str]): Text field appears just below subtitle, differs from Subtitle in font styling only
        image (Union[Unset, CardImage]): An image on a card
        price (Union[Unset, str]): Amount with currency
        quantity (Union[Unset, str]): Number of items of given kind
        tap (Union[Unset, CardAction]): A clickable action
    """

    title: Union[Unset, str] = UNSET
    subtitle: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    image: Union[Unset, "CardImage"] = UNSET
    price: Union[Unset, str] = UNSET
    quantity: Union[Unset, str] = UNSET
    tap: Union[Unset, "CardAction"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        subtitle = self.subtitle

        text = self.text

        image: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        price = self.price

        quantity = self.quantity

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
        if image is not UNSET:
            field_dict["image"] = image
        if price is not UNSET:
            field_dict["price"] = price
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
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

        _image = d.pop("image", UNSET)
        image: Union[Unset, CardImage]
        if isinstance(_image, Unset):
            image = UNSET
        else:
            image = CardImage.from_dict(_image)

        price = d.pop("price", UNSET)

        quantity = d.pop("quantity", UNSET)

        _tap = d.pop("tap", UNSET)
        tap: Union[Unset, CardAction]
        if isinstance(_tap, Unset):
            tap = UNSET
        else:
            tap = CardAction.from_dict(_tap)

        receipt_item = cls(
            title=title,
            subtitle=subtitle,
            text=text,
            image=image,
            price=price,
            quantity=quantity,
            tap=tap,
        )

        receipt_item.additional_properties = d
        return receipt_item

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
