# direct_line.ConversationsApi

All URIs are relative to *https://directline.botframework.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**conversations_get_activities**](ConversationsApi.md#conversations_get_activities) | **GET** /v3/directline/conversations/{conversationId}/activities | Get activities in this conversation. This method is paged with the &#39;watermark&#39; parameter.
[**conversations_post_activity**](ConversationsApi.md#conversations_post_activity) | **POST** /v3/directline/conversations/{conversationId}/activities | Send an activity
[**conversations_reconnect_to_conversation**](ConversationsApi.md#conversations_reconnect_to_conversation) | **GET** /v3/directline/conversations/{conversationId} | Get information about an existing conversation
[**conversations_start_conversation**](ConversationsApi.md#conversations_start_conversation) | **POST** /v3/directline/conversations | Start a new conversation
[**conversations_upload**](ConversationsApi.md#conversations_upload) | **POST** /v3/directline/conversations/{conversationId}/upload | Upload file(s) and send as attachment(s)


# **conversations_get_activities**
> ActivitySet conversations_get_activities(conversation_id, watermark=watermark)

Get activities in this conversation. This method is paged with the 'watermark' parameter.

### Example


```python
import direct_line
from direct_line.models.activity_set import ActivitySet
from direct_line.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://directline.botframework.com
# See configuration.py for a list of all supported configuration parameters.
configuration = direct_line.Configuration(
    host = "https://directline.botframework.com"
)


# Enter a context with an instance of the API client
with direct_line.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = direct_line.ConversationsApi(api_client)
    conversation_id = 'conversation_id_example' # str | Conversation ID
    watermark = 'watermark_example' # str | (Optional) only returns activities newer than this watermark (optional)

    try:
        # Get activities in this conversation. This method is paged with the 'watermark' parameter.
        api_response = api_instance.conversations_get_activities(conversation_id, watermark=watermark)
        print("The response of ConversationsApi->conversations_get_activities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_get_activities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**| Conversation ID | 
 **watermark** | **str**| (Optional) only returns activities newer than this watermark | [optional] 

### Return type

[**ActivitySet**](ActivitySet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A set of activities and a watermark are returned. |  -  |
**400** | The URL, body, or headers in the request are malformed or invalid. |  -  |
**401** | The operation included an invalid or missing Authorization header. |  -  |
**403** | You are forbidden from performing this action because your token or secret is invalid. |  -  |
**404** | The requested resource was not found. |  -  |
**429** | Too many requests have been submitted to this API. This error may be accompanied by a Retry-After header, which includes the suggested retry interval. |  -  |
**500** | An internal server error has occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_post_activity**
> ResourceResponse conversations_post_activity(conversation_id, activity)

Send an activity

### Example


```python
import direct_line
from direct_line.models.activity import Activity
from direct_line.models.resource_response import ResourceResponse
from direct_line.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://directline.botframework.com
# See configuration.py for a list of all supported configuration parameters.
configuration = direct_line.Configuration(
    host = "https://directline.botframework.com"
)


# Enter a context with an instance of the API client
with direct_line.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = direct_line.ConversationsApi(api_client)
    conversation_id = 'conversation_id_example' # str | Conversation ID
    activity = direct_line.Activity() # Activity | Activity to send

    try:
        # Send an activity
        api_response = api_instance.conversations_post_activity(conversation_id, activity)
        print("The response of ConversationsApi->conversations_post_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_post_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**| Conversation ID | 
 **activity** | [**Activity**](Activity.md)| Activity to send | 

### Return type

[**ResourceResponse**](ResourceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The operation succeeded. |  -  |
**204** | The operation succeeded. No content was returned. |  -  |
**400** | The URL, body, or headers in the request are malformed or invalid. |  -  |
**401** | The operation included an invalid or missing Authorization header. |  -  |
**403** | You are forbidden from performing this action because your token or secret is invalid. |  -  |
**404** | The requested resource was not found. |  -  |
**429** | Too many requests have been submitted to this API. This error may be accompanied by a Retry-After header, which includes the suggested retry interval. |  -  |
**500** | An internal server error has occurred. |  -  |
**502** | The bot is unavailable or returned an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_reconnect_to_conversation**
> Conversation conversations_reconnect_to_conversation(conversation_id, watermark=watermark)

Get information about an existing conversation

### Example


```python
import direct_line
from direct_line.models.conversation import Conversation
from direct_line.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://directline.botframework.com
# See configuration.py for a list of all supported configuration parameters.
configuration = direct_line.Configuration(
    host = "https://directline.botframework.com"
)


# Enter a context with an instance of the API client
with direct_line.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = direct_line.ConversationsApi(api_client)
    conversation_id = 'conversation_id_example' # str | 
    watermark = 'watermark_example' # str |  (optional)

    try:
        # Get information about an existing conversation
        api_response = api_instance.conversations_reconnect_to_conversation(conversation_id, watermark=watermark)
        print("The response of ConversationsApi->conversations_reconnect_to_conversation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_reconnect_to_conversation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**|  | 
 **watermark** | **str**|  | [optional] 

### Return type

[**Conversation**](Conversation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The conversation was successfully created, updated, or retrieved. |  -  |
**400** | The URL, body, or headers in the request are malformed or invalid. |  -  |
**401** | The operation included an invalid or missing Authorization header. |  -  |
**403** | You are forbidden from performing this action because your token or secret is invalid. |  -  |
**404** | The requested resource was not found. |  -  |
**429** | Too many requests have been submitted to this API. This error may be accompanied by a Retry-After header, which includes the suggested retry interval. |  -  |
**500** | An internal server error has occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_start_conversation**
> Conversation conversations_start_conversation(token_parameters=token_parameters)

Start a new conversation

### Example


```python
import direct_line
from direct_line.models.conversation import Conversation
from direct_line.models.token_parameters import TokenParameters
from direct_line.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://directline.botframework.com
# See configuration.py for a list of all supported configuration parameters.
configuration = direct_line.Configuration(
    host = "https://directline.botframework.com"
)


# Enter a context with an instance of the API client
with direct_line.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = direct_line.ConversationsApi(api_client)
    token_parameters = direct_line.TokenParameters() # TokenParameters |  (optional)

    try:
        # Start a new conversation
        api_response = api_instance.conversations_start_conversation(token_parameters=token_parameters)
        print("The response of ConversationsApi->conversations_start_conversation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_start_conversation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_parameters** | [**TokenParameters**](TokenParameters.md)|  | [optional] 

### Return type

[**Conversation**](Conversation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The conversation was successfully created, updated, or retrieved. |  -  |
**201** | The conversation was successfully created. |  -  |
**400** | The URL, body, or headers in the request are malformed or invalid. |  -  |
**401** | The operation included an invalid or missing Authorization header. |  -  |
**403** | You are forbidden from performing this action because your token or secret is invalid. |  -  |
**404** | The requested resource was not found. |  -  |
**409** | The object you are trying to create already exists. |  -  |
**429** | Too many requests have been submitted to this API. This error may be accompanied by a Retry-After header, which includes the suggested retry interval. |  -  |
**500** | An internal server error has occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_upload**
> ResourceResponse conversations_upload(conversation_id, file, user_id=user_id)

Upload file(s) and send as attachment(s)

### Example


```python
import direct_line
from direct_line.models.resource_response import ResourceResponse
from direct_line.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://directline.botframework.com
# See configuration.py for a list of all supported configuration parameters.
configuration = direct_line.Configuration(
    host = "https://directline.botframework.com"
)


# Enter a context with an instance of the API client
with direct_line.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = direct_line.ConversationsApi(api_client)
    conversation_id = 'conversation_id_example' # str | 
    file = None # bytearray | 
    user_id = 'user_id_example' # str |  (optional)

    try:
        # Upload file(s) and send as attachment(s)
        api_response = api_instance.conversations_upload(conversation_id, file, user_id=user_id)
        print("The response of ConversationsApi->conversations_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**|  | 
 **file** | **bytearray**|  | 
 **user_id** | **str**|  | [optional] 

### Return type

[**ResourceResponse**](ResourceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The operation succeeded. |  -  |
**202** | The request was accepted for processing. |  -  |
**204** | The operation succeeded. No content was returned. |  -  |
**400** | The URL, body, or headers in the request are malformed or invalid. |  -  |
**401** | The operation included an invalid or missing Authorization header. |  -  |
**403** | You are forbidden from performing this action because your token or secret is invalid. |  -  |
**404** | The requested resource was not found. |  -  |
**429** | Too many requests have been submitted to this API. This error may be accompanied by a Retry-After header, which includes the suggested retry interval. |  -  |
**500** | An internal server error has occurred. |  -  |
**502** | The bot is unavailable or returned an error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

