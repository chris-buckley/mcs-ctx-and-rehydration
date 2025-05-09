from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.channel_account import ChannelAccount


T = TypeVar("T", bound="TokenParameters")


@_attrs_define
class TokenParameters:
    """Parameters for creating a token

    Attributes:
        user (Union[Unset, ChannelAccount]): Channel account information needed to route a message
        trusted_origins (Union[Unset, list[str]]): Trusted origins to embed within the token
        e_tag (Union[Unset, str]):
    """

    user: Union[Unset, "ChannelAccount"] = UNSET
    trusted_origins: Union[Unset, list[str]] = UNSET
    e_tag: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        trusted_origins: Union[Unset, list[str]] = UNSET
        if not isinstance(self.trusted_origins, Unset):
            trusted_origins = self.trusted_origins

        e_tag = self.e_tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if trusted_origins is not UNSET:
            field_dict["trustedOrigins"] = trusted_origins
        if e_tag is not UNSET:
            field_dict["eTag"] = e_tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.channel_account import ChannelAccount

        d = dict(src_dict)
        _user = d.pop("user", UNSET)
        user: Union[Unset, ChannelAccount]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = ChannelAccount.from_dict(_user)

        trusted_origins = cast(list[str], d.pop("trustedOrigins", UNSET))

        e_tag = d.pop("eTag", UNSET)

        token_parameters = cls(
            user=user,
            trusted_origins=trusted_origins,
            e_tag=e_tag,
        )

        token_parameters.additional_properties = d
        return token_parameters

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
