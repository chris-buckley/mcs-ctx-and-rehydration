from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GeoCoordinates")


@_attrs_define
class GeoCoordinates:
    """GeoCoordinates (entity type: "https://schema.org/GeoCoordinates")

    Attributes:
        elevation (Union[Unset, float]): Elevation of the location [WGS
            84](https://en.wikipedia.org/wiki/World_Geodetic_System)
        latitude (Union[Unset, float]): Latitude of the location [WGS
            84](https://en.wikipedia.org/wiki/World_Geodetic_System)
        longitude (Union[Unset, float]): Longitude of the location [WGS
            84](https://en.wikipedia.org/wiki/World_Geodetic_System)
        type_ (Union[Unset, str]): The type of the thing
        name (Union[Unset, str]): The name of the thing
    """

    elevation: Union[Unset, float] = UNSET
    latitude: Union[Unset, float] = UNSET
    longitude: Union[Unset, float] = UNSET
    type_: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        elevation = self.elevation

        latitude = self.latitude

        longitude = self.longitude

        type_ = self.type_

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if elevation is not UNSET:
            field_dict["elevation"] = elevation
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        elevation = d.pop("elevation", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        type_ = d.pop("type", UNSET)

        name = d.pop("name", UNSET)

        geo_coordinates = cls(
            elevation=elevation,
            latitude=latitude,
            longitude=longitude,
            type_=type_,
            name=name,
        )

        geo_coordinates.additional_properties = d
        return geo_coordinates

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
