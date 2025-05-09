from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attachment_content import AttachmentContent


T = TypeVar("T", bound="Attachment")


@_attrs_define
class Attachment:
    """An attachment within an activity

    Attributes:
        content_type (Union[Unset, str]): mimetype/Contenttype for the file
        content_url (Union[Unset, str]): Content Url
        content (Union[Unset, AttachmentContent]): Embedded content
        name (Union[Unset, str]): (OPTIONAL) The name of the attachment
        thumbnail_url (Union[Unset, str]): (OPTIONAL) Thumbnail associated with attachment
    """

    content_type: Union[Unset, str] = UNSET
    content_url: Union[Unset, str] = UNSET
    content: Union[Unset, "AttachmentContent"] = UNSET
    name: Union[Unset, str] = UNSET
    thumbnail_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_type = self.content_type

        content_url = self.content_url

        content: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict()

        name = self.name

        thumbnail_url = self.thumbnail_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if content_url is not UNSET:
            field_dict["contentUrl"] = content_url
        if content is not UNSET:
            field_dict["content"] = content
        if name is not UNSET:
            field_dict["name"] = name
        if thumbnail_url is not UNSET:
            field_dict["thumbnailUrl"] = thumbnail_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attachment_content import AttachmentContent

        d = dict(src_dict)
        content_type = d.pop("contentType", UNSET)

        content_url = d.pop("contentUrl", UNSET)

        _content = d.pop("content", UNSET)
        content: Union[Unset, AttachmentContent]
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = AttachmentContent.from_dict(_content)

        name = d.pop("name", UNSET)

        thumbnail_url = d.pop("thumbnailUrl", UNSET)

        attachment = cls(
            content_type=content_type,
            content_url=content_url,
            content=content,
            name=name,
            thumbnail_url=thumbnail_url,
        )

        attachment.additional_properties = d
        return attachment

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
