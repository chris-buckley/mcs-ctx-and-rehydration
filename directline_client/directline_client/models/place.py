from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.place_address import PlaceAddress
    from ..models.place_geo import PlaceGeo
    from ..models.place_has_map import PlaceHasMap


T = TypeVar("T", bound="Place")


@_attrs_define
class Place:
    """Place (entity type: "https://schema.org/Place")

    Attributes:
        address (Union[Unset, PlaceAddress]): Address of the place (may be `string` or complex object of type
            `PostalAddress`)
        geo (Union[Unset, PlaceGeo]): Geo coordinates of the place (may be complex object of type `GeoCoordinates` or
            `GeoShape`)
        has_map (Union[Unset, PlaceHasMap]): Map to the place (may be `string` (URL) or complex object of type `Map`)
        type_ (Union[Unset, str]): The type of the thing
        name (Union[Unset, str]): The name of the thing
    """

    address: Union[Unset, "PlaceAddress"] = UNSET
    geo: Union[Unset, "PlaceGeo"] = UNSET
    has_map: Union[Unset, "PlaceHasMap"] = UNSET
    type_: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        geo: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.geo, Unset):
            geo = self.geo.to_dict()

        has_map: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.has_map, Unset):
            has_map = self.has_map.to_dict()

        type_ = self.type_

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if geo is not UNSET:
            field_dict["geo"] = geo
        if has_map is not UNSET:
            field_dict["hasMap"] = has_map
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.place_address import PlaceAddress
        from ..models.place_geo import PlaceGeo
        from ..models.place_has_map import PlaceHasMap

        d = dict(src_dict)
        _address = d.pop("address", UNSET)
        address: Union[Unset, PlaceAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = PlaceAddress.from_dict(_address)

        _geo = d.pop("geo", UNSET)
        geo: Union[Unset, PlaceGeo]
        if isinstance(_geo, Unset):
            geo = UNSET
        else:
            geo = PlaceGeo.from_dict(_geo)

        _has_map = d.pop("hasMap", UNSET)
        has_map: Union[Unset, PlaceHasMap]
        if isinstance(_has_map, Unset):
            has_map = UNSET
        else:
            has_map = PlaceHasMap.from_dict(_has_map)

        type_ = d.pop("type", UNSET)

        name = d.pop("name", UNSET)

        place = cls(
            address=address,
            geo=geo,
            has_map=has_map,
            type_=type_,
            name=name,
        )

        place.additional_properties = d
        return place

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
