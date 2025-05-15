# ReceiptItem

An item on a receipt card

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title of the Card | [optional] 
**subtitle** | **str** | Subtitle appears just below Title field, differs from Title in font styling only | [optional] 
**text** | **str** | Text field appears just below subtitle, differs from Subtitle in font styling only | [optional] 
**image** | [**CardImage**](CardImage.md) |  | [optional] 
**price** | **str** | Amount with currency | [optional] 
**quantity** | **str** | Number of items of given kind | [optional] 
**tap** | [**CardAction**](CardAction.md) |  | [optional] 

## Example

```python
from bot_connector.models.receipt_item import ReceiptItem

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiptItem from a JSON string
receipt_item_instance = ReceiptItem.from_json(json)
# print the JSON string representation of the object
print(ReceiptItem.to_json())

# convert the object into a dict
receipt_item_dict = receipt_item_instance.to_dict()
# create an instance of ReceiptItem from a dict
receipt_item_from_dict = ReceiptItem.from_dict(receipt_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


