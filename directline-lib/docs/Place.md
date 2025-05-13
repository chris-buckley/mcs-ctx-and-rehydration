# Place

Place (entity type: \"https://schema.org/Place\")

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **object** | Address of the place (may be &#x60;string&#x60; or complex object of type &#x60;PostalAddress&#x60;) | [optional] 
**geo** | **object** | Geo coordinates of the place (may be complex object of type &#x60;GeoCoordinates&#x60; or &#x60;GeoShape&#x60;) | [optional] 
**has_map** | **object** | Map to the place (may be &#x60;string&#x60; (URL) or complex object of type &#x60;Map&#x60;) | [optional] 
**type** | **str** | The type of the thing | [optional] 
**name** | **str** | The name of the thing | [optional] 

## Example

```python
from direct_line.models.place import Place

# TODO update the JSON string below
json = "{}"
# create an instance of Place from a JSON string
place_instance = Place.from_json(json)
# print the JSON string representation of the object
print(Place.to_json())

# convert the object into a dict
place_dict = place_instance.to_dict()
# create an instance of Place from a dict
place_from_dict = Place.from_dict(place_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


