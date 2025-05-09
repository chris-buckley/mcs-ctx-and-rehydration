from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audio_card_value import AudioCardValue
    from ..models.card_action import CardAction
    from ..models.media_url import MediaUrl
    from ..models.thumbnail_url import ThumbnailUrl


T = TypeVar("T", bound="AudioCard")


@_attrs_define
class AudioCard:
    """Audio card

    Attributes:
        title (Union[Unset, str]): Title of this card
        subtitle (Union[Unset, str]): Subtitle of this card
        text (Union[Unset, str]): Text of this card
        image (Union[Unset, ThumbnailUrl]): Thumbnail URL
        media (Union[Unset, list['MediaUrl']]): Media URLs for this card. When this field contains more than one URL,
            each URL is an alternative format of the same content.
        buttons (Union[Unset, list['CardAction']]): Actions on this card
        shareable (Union[Unset, bool]): This content may be shared with others (default:true)
        autoloop (Union[Unset, bool]): Should the client loop playback at end of content (default:true)
        autostart (Union[Unset, bool]): Should the client automatically start playback of media in this card
            (default:true)
        aspect (Union[Unset, str]): Aspect ratio of thumbnail/media placeholder. Allowed values are "16:9" and "4:3"
        duration (Union[Unset, str]): Describes the length of the media content without requiring a receiver to open the
            content. Formatted as an ISO 8601 Duration field.
        value (Union[Unset, AudioCardValue]): Supplementary parameter for this card
    """

    title: Union[Unset, str] = UNSET
    subtitle: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    image: Union[Unset, "ThumbnailUrl"] = UNSET
    media: Union[Unset, list["MediaUrl"]] = UNSET
    buttons: Union[Unset, list["CardAction"]] = UNSET
    shareable: Union[Unset, bool] = UNSET
    autoloop: Union[Unset, bool] = UNSET
    autostart: Union[Unset, bool] = UNSET
    aspect: Union[Unset, str] = UNSET
    duration: Union[Unset, str] = UNSET
    value: Union[Unset, "AudioCardValue"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        subtitle = self.subtitle

        text = self.text

        image: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        media: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.media, Unset):
            media = []
            for media_item_data in self.media:
                media_item = media_item_data.to_dict()
                media.append(media_item)

        buttons: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.buttons, Unset):
            buttons = []
            for buttons_item_data in self.buttons:
                buttons_item = buttons_item_data.to_dict()
                buttons.append(buttons_item)

        shareable = self.shareable

        autoloop = self.autoloop

        autostart = self.autostart

        aspect = self.aspect

        duration = self.duration

        value: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if text is not UNSET:
            field_dict["text"] = text
        if image is not UNSET:
            field_dict["image"] = image
        if media is not UNSET:
            field_dict["media"] = media
        if buttons is not UNSET:
            field_dict["buttons"] = buttons
        if shareable is not UNSET:
            field_dict["shareable"] = shareable
        if autoloop is not UNSET:
            field_dict["autoloop"] = autoloop
        if autostart is not UNSET:
            field_dict["autostart"] = autostart
        if aspect is not UNSET:
            field_dict["aspect"] = aspect
        if duration is not UNSET:
            field_dict["duration"] = duration
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audio_card_value import AudioCardValue
        from ..models.card_action import CardAction
        from ..models.media_url import MediaUrl
        from ..models.thumbnail_url import ThumbnailUrl

        d = dict(src_dict)
        title = d.pop("title", UNSET)

        subtitle = d.pop("subtitle", UNSET)

        text = d.pop("text", UNSET)

        _image = d.pop("image", UNSET)
        image: Union[Unset, ThumbnailUrl]
        if isinstance(_image, Unset):
            image = UNSET
        else:
            image = ThumbnailUrl.from_dict(_image)

        media = []
        _media = d.pop("media", UNSET)
        for media_item_data in _media or []:
            media_item = MediaUrl.from_dict(media_item_data)

            media.append(media_item)

        buttons = []
        _buttons = d.pop("buttons", UNSET)
        for buttons_item_data in _buttons or []:
            buttons_item = CardAction.from_dict(buttons_item_data)

            buttons.append(buttons_item)

        shareable = d.pop("shareable", UNSET)

        autoloop = d.pop("autoloop", UNSET)

        autostart = d.pop("autostart", UNSET)

        aspect = d.pop("aspect", UNSET)

        duration = d.pop("duration", UNSET)

        _value = d.pop("value", UNSET)
        value: Union[Unset, AudioCardValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = AudioCardValue.from_dict(_value)

        audio_card = cls(
            title=title,
            subtitle=subtitle,
            text=text,
            image=image,
            media=media,
            buttons=buttons,
            shareable=shareable,
            autoloop=autoloop,
            autostart=autostart,
            aspect=aspect,
            duration=duration,
            value=value,
        )

        audio_card.additional_properties = d
        return audio_card

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
