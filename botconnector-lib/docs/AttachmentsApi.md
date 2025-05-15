# bot_connector.AttachmentsApi

All URIs are relative to *https://api.botframework.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attachments_get_attachment**](AttachmentsApi.md#attachments_get_attachment) | **GET** /v3/attachments/{attachmentId}/views/{viewId} | GetAttachment
[**attachments_get_attachment_info**](AttachmentsApi.md#attachments_get_attachment_info) | **GET** /v3/attachments/{attachmentId} | GetAttachmentInfo


# **attachments_get_attachment**
> bytearray attachments_get_attachment(attachment_id, view_id)

GetAttachment

Get the named view as binary content

### Example


```python
import bot_connector
from bot_connector.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.botframework.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bot_connector.Configuration(
    host = "https://api.botframework.com"
)


# Enter a context with an instance of the API client
with bot_connector.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bot_connector.AttachmentsApi(api_client)
    attachment_id = 'attachment_id_example' # str | attachment id
    view_id = 'view_id_example' # str | View id from attachmentInfo

    try:
        # GetAttachment
        api_response = api_instance.attachments_get_attachment(attachment_id, view_id)
        print("The response of AttachmentsApi->attachments_get_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentsApi->attachments_get_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**| attachment id | 
 **view_id** | **str**| View id from attachmentInfo | 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attachment stream |  -  |
**301** | The Location header describes where the content is now. |  -  |
**302** | The Location header describes where the content is now. |  -  |
**0** | The operation failed and the response is an error object describing the status code and failure. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attachments_get_attachment_info**
> AttachmentInfo attachments_get_attachment_info(attachment_id)

GetAttachmentInfo

Get AttachmentInfo structure describing the attachment views

### Example


```python
import bot_connector
from bot_connector.models.attachment_info import AttachmentInfo
from bot_connector.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.botframework.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bot_connector.Configuration(
    host = "https://api.botframework.com"
)


# Enter a context with an instance of the API client
with bot_connector.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bot_connector.AttachmentsApi(api_client)
    attachment_id = 'attachment_id_example' # str | attachment id

    try:
        # GetAttachmentInfo
        api_response = api_instance.attachments_get_attachment_info(attachment_id)
        print("The response of AttachmentsApi->attachments_get_attachment_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentsApi->attachments_get_attachment_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**| attachment id | 

### Return type

[**AttachmentInfo**](AttachmentInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An attachmentInfo object is returned which describes the:  * type of the attachment  * name of the attachment      and an array of views:  * Size - size of the object  * ViewId - View Id which can be used to fetch a variation on the content (ex: original or thumbnail) |  -  |
**0** | The operation failed and the response is an error object describing the status code and failure. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

