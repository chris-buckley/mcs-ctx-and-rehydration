from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConversationAccount")


@_attrs_define
class ConversationAccount:
    """Conversation account represents the identity of the conversation within a channel

    Attributes:
        is_group (Union[Unset, bool]): Indicates whether the conversation contains more than two participants at the
            time the activity was generated
        conversation_type (Union[Unset, str]): Indicates the type of the conversation in channels that distinguish
            between conversation types
        tenant_id (Union[Unset, str]): This conversation's tenant ID
        id (Union[Unset, str]): Channel id for the user or bot on this channel (Example: joe@smith.com, or @joesmith or
            123456)
        name (Union[Unset, str]): Display friendly name
        aad_object_id (Union[Unset, str]): This account's object ID within Azure Active Directory (AAD)
        role (Union[Unset, str]): Role of the entity behind the account (Example: User, Bot, etc.)
    """

    is_group: Union[Unset, bool] = UNSET
    conversation_type: Union[Unset, str] = UNSET
    tenant_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    aad_object_id: Union[Unset, str] = UNSET
    role: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_group = self.is_group

        conversation_type = self.conversation_type

        tenant_id = self.tenant_id

        id = self.id

        name = self.name

        aad_object_id = self.aad_object_id

        role = self.role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_group is not UNSET:
            field_dict["isGroup"] = is_group
        if conversation_type is not UNSET:
            field_dict["conversationType"] = conversation_type
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if aad_object_id is not UNSET:
            field_dict["aadObjectId"] = aad_object_id
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_group = d.pop("isGroup", UNSET)

        conversation_type = d.pop("conversationType", UNSET)

        tenant_id = d.pop("tenantId", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        aad_object_id = d.pop("aadObjectId", UNSET)

        role = d.pop("role", UNSET)

        conversation_account = cls(
            is_group=is_group,
            conversation_type=conversation_type,
            tenant_id=tenant_id,
            id=id,
            name=name,
            aad_object_id=aad_object_id,
            role=role,
        )

        conversation_account.additional_properties = d
        return conversation_account

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
