from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.card_action import CardAction
    from ..models.fact import Fact
    from ..models.receipt_item import ReceiptItem


T = TypeVar("T", bound="ReceiptCard")


@_attrs_define
class ReceiptCard:
    """A receipt card

    Attributes:
        title (Union[Unset, str]): Title of the card
        facts (Union[Unset, list['Fact']]): Array of Fact objects
        items (Union[Unset, list['ReceiptItem']]): Array of Receipt Items
        tap (Union[Unset, CardAction]): A clickable action
        total (Union[Unset, str]): Total amount of money paid (or to be paid)
        tax (Union[Unset, str]): Total amount of tax paid (or to be paid)
        vat (Union[Unset, str]): Total amount of VAT paid (or to be paid)
        buttons (Union[Unset, list['CardAction']]): Set of actions applicable to the current card
    """

    title: Union[Unset, str] = UNSET
    facts: Union[Unset, list["Fact"]] = UNSET
    items: Union[Unset, list["ReceiptItem"]] = UNSET
    tap: Union[Unset, "CardAction"] = UNSET
    total: Union[Unset, str] = UNSET
    tax: Union[Unset, str] = UNSET
    vat: Union[Unset, str] = UNSET
    buttons: Union[Unset, list["CardAction"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        facts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.facts, Unset):
            facts = []
            for facts_item_data in self.facts:
                facts_item = facts_item_data.to_dict()
                facts.append(facts_item)

        items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        tap: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tap, Unset):
            tap = self.tap.to_dict()

        total = self.total

        tax = self.tax

        vat = self.vat

        buttons: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.buttons, Unset):
            buttons = []
            for buttons_item_data in self.buttons:
                buttons_item = buttons_item_data.to_dict()
                buttons.append(buttons_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if facts is not UNSET:
            field_dict["facts"] = facts
        if items is not UNSET:
            field_dict["items"] = items
        if tap is not UNSET:
            field_dict["tap"] = tap
        if total is not UNSET:
            field_dict["total"] = total
        if tax is not UNSET:
            field_dict["tax"] = tax
        if vat is not UNSET:
            field_dict["vat"] = vat
        if buttons is not UNSET:
            field_dict["buttons"] = buttons

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.card_action import CardAction
        from ..models.fact import Fact
        from ..models.receipt_item import ReceiptItem

        d = dict(src_dict)
        title = d.pop("title", UNSET)

        facts = []
        _facts = d.pop("facts", UNSET)
        for facts_item_data in _facts or []:
            facts_item = Fact.from_dict(facts_item_data)

            facts.append(facts_item)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = ReceiptItem.from_dict(items_item_data)

            items.append(items_item)

        _tap = d.pop("tap", UNSET)
        tap: Union[Unset, CardAction]
        if isinstance(_tap, Unset):
            tap = UNSET
        else:
            tap = CardAction.from_dict(_tap)

        total = d.pop("total", UNSET)

        tax = d.pop("tax", UNSET)

        vat = d.pop("vat", UNSET)

        buttons = []
        _buttons = d.pop("buttons", UNSET)
        for buttons_item_data in _buttons or []:
            buttons_item = CardAction.from_dict(buttons_item_data)

            buttons.append(buttons_item)

        receipt_card = cls(
            title=title,
            facts=facts,
            items=items,
            tap=tap,
            total=total,
            tax=tax,
            vat=vat,
            buttons=buttons,
        )

        receipt_card.additional_properties = d
        return receipt_card

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
