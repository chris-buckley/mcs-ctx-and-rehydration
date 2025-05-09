from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Conversation")


@_attrs_define
class Conversation:
    """An object representing a conversation or a conversation token

    Attributes:
        conversation_id (Union[Unset, str]): ID for this conversation
        token (Union[Unset, str]): Token scoped to this conversation
        expires_in (Union[Unset, int]): Expiration for token
        stream_url (Union[Unset, str]): URL for this conversation's message stream
        reference_grammar_id (Union[Unset, str]): ID for the reference grammar for this bot
        e_tag (Union[Unset, str]):
    """

    conversation_id: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    expires_in: Union[Unset, int] = UNSET
    stream_url: Union[Unset, str] = UNSET
    reference_grammar_id: Union[Unset, str] = UNSET
    e_tag: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conversation_id = self.conversation_id

        token = self.token

        expires_in = self.expires_in

        stream_url = self.stream_url

        reference_grammar_id = self.reference_grammar_id

        e_tag = self.e_tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conversation_id is not UNSET:
            field_dict["conversationId"] = conversation_id
        if token is not UNSET:
            field_dict["token"] = token
        if expires_in is not UNSET:
            field_dict["expires_in"] = expires_in
        if stream_url is not UNSET:
            field_dict["streamUrl"] = stream_url
        if reference_grammar_id is not UNSET:
            field_dict["referenceGrammarId"] = reference_grammar_id
        if e_tag is not UNSET:
            field_dict["eTag"] = e_tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        conversation_id = d.pop("conversationId", UNSET)

        token = d.pop("token", UNSET)

        expires_in = d.pop("expires_in", UNSET)

        stream_url = d.pop("streamUrl", UNSET)

        reference_grammar_id = d.pop("referenceGrammarId", UNSET)

        e_tag = d.pop("eTag", UNSET)

        conversation = cls(
            conversation_id=conversation_id,
            token=token,
            expires_in=expires_in,
            stream_url=stream_url,
            reference_grammar_id=reference_grammar_id,
            e_tag=e_tag,
        )

        conversation.additional_properties = d
        return conversation

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
