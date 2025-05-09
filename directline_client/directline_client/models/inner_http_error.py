from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inner_http_error_body import InnerHttpErrorBody


T = TypeVar("T", bound="InnerHttpError")


@_attrs_define
class InnerHttpError:
    """Object representing inner http error

    Attributes:
        status_code (Union[Unset, int]): HttpStatusCode from failed request
        body (Union[Unset, InnerHttpErrorBody]): Body from failed request
    """

    status_code: Union[Unset, int] = UNSET
    body: Union[Unset, "InnerHttpErrorBody"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status_code = self.status_code

        body: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code
        if body is not UNSET:
            field_dict["body"] = body

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inner_http_error_body import InnerHttpErrorBody

        d = dict(src_dict)
        status_code = d.pop("statusCode", UNSET)

        _body = d.pop("body", UNSET)
        body: Union[Unset, InnerHttpErrorBody]
        if isinstance(_body, Unset):
            body = UNSET
        else:
            body = InnerHttpErrorBody.from_dict(_body)

        inner_http_error = cls(
            status_code=status_code,
            body=body,
        )

        inner_http_error.additional_properties = d
        return inner_http_error

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
