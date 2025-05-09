from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.token_request_settings import TokenRequestSettings


T = TypeVar("T", bound="TokenRequest")


@_attrs_define
class TokenRequest:
    """A request to receive a user token

    Attributes:
        provider (Union[Unset, str]): The provider to request a user token from
        settings (Union[Unset, TokenRequestSettings]): A collection of settings for the specific provider for this
            request
    """

    provider: Union[Unset, str] = UNSET
    settings: Union[Unset, "TokenRequestSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider

        settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if provider is not UNSET:
            field_dict["provider"] = provider
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.token_request_settings import TokenRequestSettings

        d = dict(src_dict)
        provider = d.pop("provider", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: Union[Unset, TokenRequestSettings]
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = TokenRequestSettings.from_dict(_settings)

        token_request = cls(
            provider=provider,
            settings=settings,
        )

        token_request.additional_properties = d
        return token_request

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
