from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TokenResponse")


@_attrs_define
class TokenResponse:
    """A response that includes a user token

    Attributes:
        channel_id (Union[Unset, str]): The channelId of the TokenResponse
        connection_name (Union[Unset, str]): The connection name
        token (Union[Unset, str]): The user token
        expiration (Union[Unset, str]): Expiration for the token, in ISO 8601 format (e.g. "2007-04-05T14:30Z")
    """

    channel_id: Union[Unset, str] = UNSET
    connection_name: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    expiration: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_id = self.channel_id

        connection_name = self.connection_name

        token = self.token

        expiration = self.expiration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if connection_name is not UNSET:
            field_dict["connectionName"] = connection_name
        if token is not UNSET:
            field_dict["token"] = token
        if expiration is not UNSET:
            field_dict["expiration"] = expiration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channel_id = d.pop("channelId", UNSET)

        connection_name = d.pop("connectionName", UNSET)

        token = d.pop("token", UNSET)

        expiration = d.pop("expiration", UNSET)

        token_response = cls(
            channel_id=channel_id,
            connection_name=connection_name,
            token=token,
            expiration=expiration,
        )

        token_response.additional_properties = d
        return token_response

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
