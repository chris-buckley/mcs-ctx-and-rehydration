from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.card_action import CardAction


T = TypeVar("T", bound="SuggestedActions")


@_attrs_define
class SuggestedActions:
    """SuggestedActions that can be performed

    Attributes:
        to (Union[Unset, list[str]]): Ids of the recipients that the actions should be shown to.  These Ids are relative
            to the channelId and a subset of all recipients of the activity
        actions (Union[Unset, list['CardAction']]): Actions that can be shown to the user
    """

    to: Union[Unset, list[str]] = UNSET
    actions: Union[Unset, list["CardAction"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        to: Union[Unset, list[str]] = UNSET
        if not isinstance(self.to, Unset):
            to = self.to

        actions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.actions, Unset):
            actions = []
            for actions_item_data in self.actions:
                actions_item = actions_item_data.to_dict()
                actions.append(actions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if to is not UNSET:
            field_dict["to"] = to
        if actions is not UNSET:
            field_dict["actions"] = actions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.card_action import CardAction

        d = dict(src_dict)
        to = cast(list[str], d.pop("to", UNSET))

        actions = []
        _actions = d.pop("actions", UNSET)
        for actions_item_data in _actions or []:
            actions_item = CardAction.from_dict(actions_item_data)

            actions.append(actions_item)

        suggested_actions = cls(
            to=to,
            actions=actions,
        )

        suggested_actions.additional_properties = d
        return suggested_actions

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
