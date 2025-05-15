# ReceiptCard

A receipt card

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title of the card | [optional] 
**facts** | [**List[Fact]**](Fact.md) | Array of Fact objects | [optional] 
**items** | [**List[ReceiptItem]**](ReceiptItem.md) | Array of Receipt Items | [optional] 
**tap** | [**CardAction**](CardAction.md) |  | [optional] 
**total** | **str** | Total amount of money paid (or to be paid) | [optional] 
**tax** | **str** | Total amount of tax paid (or to be paid) | [optional] 
**vat** | **str** | Total amount of VAT paid (or to be paid) | [optional] 
**buttons** | [**List[CardAction]**](CardAction.md) | Set of actions applicable to the current card | [optional] 

## Example

```python
from bot_connector.models.receipt_card import ReceiptCard

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiptCard from a JSON string
receipt_card_instance = ReceiptCard.from_json(json)
# print the JSON string representation of the object
print(ReceiptCard.to_json())

# convert the object into a dict
receipt_card_dict = receipt_card_instance.to_dict()
# create an instance of ReceiptCard from a dict
receipt_card_from_dict = ReceiptCard.from_dict(receipt_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


