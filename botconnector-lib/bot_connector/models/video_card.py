# coding: utf-8

"""
    Microsoft Bot Connector API - v3.0

    The Bot Connector REST API allows your bot to send and receive messages to channels configured in the  [Bot Framework Developer Portal](https://dev.botframework.com). The Connector service uses industry-standard REST  and JSON over HTTPS.    Client libraries for this REST API are available. See below for a list.    Many bots will use both the Bot Connector REST API and the associated [Bot State REST API](/en-us/restapi/state). The  Bot State REST API allows a bot to store and retrieve state associated with users and conversations.    Authentication for both the Bot Connector and Bot State REST APIs is accomplished with JWT Bearer tokens, and is  described in detail in the [Connector Authentication](/en-us/restapi/authentication) document.    # Client Libraries for the Bot Connector REST API    * [Bot Builder for C#](/en-us/csharp/builder/sdkreference/)  * [Bot Builder for Node.js](/en-us/node/builder/overview/)  * Generate your own from the [Connector API Swagger file](https://raw.githubusercontent.com/Microsoft/BotBuilder/master/CSharp/Library/Microsoft.Bot.Connector.Shared/Swagger/ConnectorAPI.json)    © 2016 Microsoft

    The version of the OpenAPI document: v3
    Contact: botframework@microsoft.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from bot_connector.models.card_action import CardAction
from bot_connector.models.media_url import MediaUrl
from bot_connector.models.thumbnail_url import ThumbnailUrl
from typing import Optional, Set
from typing_extensions import Self

class VideoCard(BaseModel):
    """
    Video card
    """ # noqa: E501
    title: Optional[StrictStr] = Field(default=None, description="Title of this card")
    subtitle: Optional[StrictStr] = Field(default=None, description="Subtitle of this card")
    text: Optional[StrictStr] = Field(default=None, description="Text of this card")
    image: Optional[ThumbnailUrl] = None
    media: Optional[List[MediaUrl]] = Field(default=None, description="Media URLs for this card. When this field contains more than one URL, each URL is an alternative format of the same content.")
    buttons: Optional[List[CardAction]] = Field(default=None, description="Actions on this card")
    shareable: Optional[StrictBool] = Field(default=None, description="This content may be shared with others (default:true)")
    autoloop: Optional[StrictBool] = Field(default=None, description="Should the client loop playback at end of content (default:true)")
    autostart: Optional[StrictBool] = Field(default=None, description="Should the client automatically start playback of media in this card (default:true)")
    aspect: Optional[StrictStr] = Field(default=None, description="Aspect ratio of thumbnail/media placeholder. Allowed values are \"16:9\" and \"4:3\"")
    duration: Optional[StrictStr] = Field(default=None, description="Describes the length of the media content without requiring a receiver to open the content. Formatted as an ISO 8601 Duration field.")
    value: Optional[Dict[str, Any]] = Field(default=None, description="Supplementary parameter for this card")
    __properties: ClassVar[List[str]] = ["title", "subtitle", "text", "image", "media", "buttons", "shareable", "autoloop", "autostart", "aspect", "duration", "value"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of VideoCard from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of image
        if self.image:
            _dict['image'] = self.image.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in media (list)
        _items = []
        if self.media:
            for _item_media in self.media:
                if _item_media:
                    _items.append(_item_media.to_dict())
            _dict['media'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in buttons (list)
        _items = []
        if self.buttons:
            for _item_buttons in self.buttons:
                if _item_buttons:
                    _items.append(_item_buttons.to_dict())
            _dict['buttons'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VideoCard from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "subtitle": obj.get("subtitle"),
            "text": obj.get("text"),
            "image": ThumbnailUrl.from_dict(obj["image"]) if obj.get("image") is not None else None,
            "media": [MediaUrl.from_dict(_item) for _item in obj["media"]] if obj.get("media") is not None else None,
            "buttons": [CardAction.from_dict(_item) for _item in obj["buttons"]] if obj.get("buttons") is not None else None,
            "shareable": obj.get("shareable"),
            "autoloop": obj.get("autoloop"),
            "autostart": obj.get("autostart"),
            "aspect": obj.get("aspect"),
            "duration": obj.get("duration"),
            "value": obj.get("value")
        })
        return _obj


