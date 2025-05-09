from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inner_http_error import InnerHttpError


T = TypeVar("T", bound="Error")


@_attrs_define
class Error:
    """Object representing error information

    Attributes:
        code (Union[Unset, str]): Error code
        message (Union[Unset, str]): Error message
        inner_http_error (Union[Unset, InnerHttpError]): Object representing inner http error
    """

    code: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    inner_http_error: Union[Unset, "InnerHttpError"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        inner_http_error: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.inner_http_error, Unset):
            inner_http_error = self.inner_http_error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message
        if inner_http_error is not UNSET:
            field_dict["innerHttpError"] = inner_http_error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inner_http_error import InnerHttpError

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        message = d.pop("message", UNSET)

        _inner_http_error = d.pop("innerHttpError", UNSET)
        inner_http_error: Union[Unset, InnerHttpError]
        if isinstance(_inner_http_error, Unset):
            inner_http_error = UNSET
        else:
            inner_http_error = InnerHttpError.from_dict(_inner_http_error)

        error = cls(
            code=code,
            message=message,
            inner_http_error=inner_http_error,
        )

        error.additional_properties = d
        return error

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
