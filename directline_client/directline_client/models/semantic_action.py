from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.semantic_action_entities import SemanticActionEntities


T = TypeVar("T", bound="SemanticAction")


@_attrs_define
class SemanticAction:
    """Represents a reference to a programmatic action

    Attributes:
        state (Union[Unset, str]): State of this action. Allowed values: `start`, `continue`, `done`
        id (Union[Unset, str]): ID of this action
        entities (Union[Unset, SemanticActionEntities]): Entities associated with this action
    """

    state: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    entities: Union[Unset, "SemanticActionEntities"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state

        id = self.id

        entities: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.entities, Unset):
            entities = self.entities.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if id is not UNSET:
            field_dict["id"] = id
        if entities is not UNSET:
            field_dict["entities"] = entities

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.semantic_action_entities import SemanticActionEntities

        d = dict(src_dict)
        state = d.pop("state", UNSET)

        id = d.pop("id", UNSET)

        _entities = d.pop("entities", UNSET)
        entities: Union[Unset, SemanticActionEntities]
        if isinstance(_entities, Unset):
            entities = UNSET
        else:
            entities = SemanticActionEntities.from_dict(_entities)

        semantic_action = cls(
            state=state,
            id=id,
            entities=entities,
        )

        semantic_action.additional_properties = d
        return semantic_action

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
