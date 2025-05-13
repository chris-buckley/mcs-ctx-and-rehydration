# GeoCoordinates

GeoCoordinates (entity type: \"https://schema.org/GeoCoordinates\")

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elevation** | **float** | Elevation of the location [WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System) | [optional] 
**latitude** | **float** | Latitude of the location [WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System) | [optional] 
**longitude** | **float** | Longitude of the location [WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System) | [optional] 
**type** | **str** | The type of the thing | [optional] 
**name** | **str** | The name of the thing | [optional] 

## Example

```python
from direct_line.models.geo_coordinates import GeoCoordinates

# TODO update the JSON string below
json = "{}"
# create an instance of GeoCoordinates from a JSON string
geo_coordinates_instance = GeoCoordinates.from_json(json)
# print the JSON string representation of the object
print(GeoCoordinates.to_json())

# convert the object into a dict
geo_coordinates_dict = geo_coordinates_instance.to_dict()
# create an instance of GeoCoordinates from a dict
geo_coordinates_from_dict = GeoCoordinates.from_dict(geo_coordinates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


