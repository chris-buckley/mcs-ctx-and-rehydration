# bot_connector.ConversationsApi

All URIs are relative to *https://api.botframework.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**conversations_create_conversation**](ConversationsApi.md#conversations_create_conversation) | **POST** /v3/conversations | CreateConversation
[**conversations_delete_activity**](ConversationsApi.md#conversations_delete_activity) | **DELETE** /v3/conversations/{conversationId}/activities/{activityId} | DeleteActivity
[**conversations_delete_conversation_member**](ConversationsApi.md#conversations_delete_conversation_member) | **DELETE** /v3/conversations/{conversationId}/members/{memberId} | DeleteConversationMember
[**conversations_get_activity_members**](ConversationsApi.md#conversations_get_activity_members) | **GET** /v3/conversations/{conversationId}/activities/{activityId}/members | GetActivityMembers
[**conversations_get_conversation_members**](ConversationsApi.md#conversations_get_conversation_members) | **GET** /v3/conversations/{conversationId}/members | GetConversationMembers
[**conversations_get_conversation_paged_members**](ConversationsApi.md#conversations_get_conversation_paged_members) | **GET** /v3/conversations/{conversationId}/pagedmembers | GetConversationPagedMembers
[**conversations_get_conversations**](ConversationsApi.md#conversations_get_conversations) | **GET** /v3/conversations | GetConversations
[**conversations_reply_to_activity**](ConversationsApi.md#conversations_reply_to_activity) | **POST** /v3/conversations/{conversationId}/activities/{activityId} | ReplyToActivity
[**conversations_send_conversation_history**](ConversationsApi.md#conversations_send_conversation_history) | **POST** /v3/conversations/{conversationId}/activities/history | SendConversationHistory
[**conversations_send_to_conversation**](ConversationsApi.md#conversations_send_to_conversation) | **POST** /v3/conversations/{conversationId}/activities | SendToConversation
[**conversations_update_activity**](ConversationsApi.md#conversations_update_activity) | **PUT** /v3/conversations/{conversationId}/activities/{activityId} | UpdateActivity
[**conversations_upload_attachment**](ConversationsApi.md#conversations_upload_attachment) | **POST** /v3/conversations/{conversationId}/attachments | UploadAttachment


# **conversations_create_conversation**
> ConversationResourceResponse conversations_create_conversation(parameters)

CreateConversation

Create a new Conversation.

POST to this method with a
* Bot being the bot creating the conversation
* IsGroup set to true if this is not a direct message (default is false)
* Array containing the members to include in the conversation

The return value is a ResourceResponse which contains a conversation id which is suitable for use
in the message payload and REST API uris.

Most channels only support the semantics of bots initiating a direct message conversation.  An example of how to do that would be:

```
var resource = await connector.conversations.CreateConversation(new ConversationParameters(){ Bot = bot, members = new ChannelAccount[] { new ChannelAccount("user1") } );
await connect.Conversations.SendToConversationAsync(resource.Id, new Activity() ... ) ;

```

### Example


```python
import bot_connector
from bot_connector.models.conversation_parameters import ConversationParameters
from bot_connector.models.conversation_resource_response import ConversationResourceResponse
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
    api_instance = bot_connector.ConversationsApi(api_client)
    parameters = bot_connector.ConversationParameters() # ConversationParameters | Parameters to create the conversation from

    try:
        # CreateConversation
        api_response = api_instance.conversations_create_conversation(parameters)
        print("The response of ConversationsApi->conversations_create_conversation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_create_conversation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameters** | [**ConversationParameters**](ConversationParameters.md)| Parameters to create the conversation from | 

### Return type

[**ConversationResourceResponse**](ConversationResourceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object will be returned containing   * the ID for the conversation  * ActivityId for the activity if provided.  If ActivityId is null then the channel doesn&#39;t support returning resource id&#39;s for activity. |  -  |
**201** | An object will be returned containing   * the ID for the conversation  * ActivityId for the activity if provided.  If ActivityId is null then the channel doesn&#39;t support returning resource id&#39;s for activity. |  -  |
**202** | An object will be returned containing   * the ID for the conversation  * ActivityId for the activity if provided.  If ActivityId is null then the channel doesn&#39;t support returning resource id&#39;s for activity. |  -  |
**0** | The operation failed and the response is an error object describing the status code and failure. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_delete_activity**
> conversations_delete_activity(conversation_id, activity_id)

DeleteActivity

Delete an existing activity.

Some channels allow you to delete an existing activity, and if successful this method will remove the specified activity.

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
    api_instance = bot_connector.ConversationsApi(api_client)
    conversation_id = 'conversation_id_example' # str | Conversation ID
    activity_id = 'activity_id_example' # str | activityId to delete

    try:
        # DeleteActivity
        api_instance.conversations_delete_activity(conversation_id, activity_id)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_delete_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**| Conversation ID | 
 **activity_id** | **str**| activityId to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The operation succeeded, there is no response. |  -  |
**202** | The request has been accepted for processing, but the processing has not been completed |  -  |
**0** | The operation failed and the response is an error object describing the status code and failure. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_delete_conversation_member**
> conversations_delete_conversation_member(conversation_id, member_id)

DeleteConversationMember

Deletes a member from a conversation. 

This REST API takes a ConversationId and a memberId (of type string) and removes that member from the conversation. If that member was the last member
of the conversation, the conversation will also be deleted.

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
    api_instance = bot_connector.ConversationsApi(api_client)
    conversation_id = 'conversation_id_example' # str | Conversation ID
    member_id = 'member_id_example' # str | ID of the member to delete from this conversation

    try:
        # DeleteConversationMember
        api_instance.conversations_delete_conversation_member(conversation_id, member_id)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_delete_conversation_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**| Conversation ID | 
 **member_id** | **str**| ID of the member to delete from this conversation | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The operation succeeded, there is no response. |  -  |
**204** | The operation succeeded but no content was returned. |  -  |
**0** | The operation failed and the response is an error object describing the status code and failure. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_get_activity_members**
> List[ChannelAccount] conversations_get_activity_members(conversation_id, activity_id)

GetActivityMembers

Enumerate the members of an activity. 

This REST API takes a ConversationId and a ActivityId, returning an array of ChannelAccount objects representing the members of the particular activity in the conversation.

### Example


```python
import bot_connector
from bot_connector.models.channel_account import ChannelAccount
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
    api_instance = bot_connector.ConversationsApi(api_client)
    conversation_id = 'conversation_id_example' # str | Conversation ID
    activity_id = 'activity_id_example' # str | Activity ID

    try:
        # GetActivityMembers
        api_response = api_instance.conversations_get_activity_members(conversation_id, activity_id)
        print("The response of ConversationsApi->conversations_get_activity_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_get_activity_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**| Conversation ID | 
 **activity_id** | **str**| Activity ID | 

### Return type

[**List[ChannelAccount]**](ChannelAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of ChannelAccount objects |  -  |
**0** | The operation failed and the response is an error object describing the status code and failure. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_get_conversation_members**
> List[ChannelAccount] conversations_get_conversation_members(conversation_id)

GetConversationMembers

Enumerate the members of a conversation. 

This REST API takes a ConversationId and returns an array of ChannelAccount objects representing the members of the conversation.

### Example


```python
import bot_connector
from bot_connector.models.channel_account import ChannelAccount
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
    api_instance = bot_connector.ConversationsApi(api_client)
    conversation_id = 'conversation_id_example' # str | Conversation ID

    try:
        # GetConversationMembers
        api_response = api_instance.conversations_get_conversation_members(conversation_id)
        print("The response of ConversationsApi->conversations_get_conversation_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_get_conversation_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**| Conversation ID | 

### Return type

[**List[ChannelAccount]**](ChannelAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of ChannelAccount objects |  -  |
**0** | The operation failed and the response is an error object describing the status code and failure. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_get_conversation_paged_members**
> PagedMembersResult conversations_get_conversation_paged_members(conversation_id, page_size=page_size, continuation_token=continuation_token)

GetConversationPagedMembers

Enumerate the members of a conversation one page at a time.

This REST API takes a ConversationId. Optionally a pageSize and/or continuationToken can be provided. It returns a PagedMembersResult, which contains an array
of ChannelAccounts representing the members of the conversation and a continuation token that can be used to get more values.

One page of ChannelAccounts records are returned with each call. The number of records in a page may vary between channels and calls. The pageSize parameter can be used as 
a suggestion. If there are no additional results the response will not contain a continuation token. If there are no members in the conversation the Members will be empty or not present in the response.

A response to a request that has a continuation token from a prior request may rarely return members from a previous request.

### Example


```python
import bot_connector
from bot_connector.models.paged_members_result import PagedMembersResult
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
    api_instance = bot_connector.ConversationsApi(api_client)
    conversation_id = 'conversation_id_example' # str | Conversation ID
    page_size = 56 # int | Suggested page size (optional)
    continuation_token = 'continuation_token_example' # str | Continuation Token (optional)

    try:
        # GetConversationPagedMembers
        api_response = api_instance.conversations_get_conversation_paged_members(conversation_id, page_size=page_size, continuation_token=continuation_token)
        print("The response of ConversationsApi->conversations_get_conversation_paged_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_get_conversation_paged_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**| Conversation ID | 
 **page_size** | **int**| Suggested page size | [optional] 
 **continuation_token** | **str**| Continuation Token | [optional] 

### Return type

[**PagedMembersResult**](PagedMembersResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_get_conversations**
> ConversationsResult conversations_get_conversations(continuation_token=continuation_token)

GetConversations

List the Conversations in which this bot has participated.

GET from this method with a skip token

The return value is a ConversationsResult, which contains an array of ConversationMembers and a skip token.  If the skip token is not empty, then 
there are further values to be returned. Call this method again with the returned token to get more values.

Each ConversationMembers object contains the ID of the conversation and an array of ChannelAccounts that describe the members of the conversation.

### Example


```python
import bot_connector
from bot_connector.models.conversations_result import ConversationsResult
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
    api_instance = bot_connector.ConversationsApi(api_client)
    continuation_token = 'continuation_token_example' # str | skip or continuation token (optional)

    try:
        # GetConversations
        api_response = api_instance.conversations_get_conversations(continuation_token=continuation_token)
        print("The response of ConversationsApi->conversations_get_conversations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_get_conversations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **continuation_token** | **str**| skip or continuation token | [optional] 

### Return type

[**ConversationsResult**](ConversationsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object will be returned containing   * an array (Conversations) of ConversationMembers objects  * a continuation token    Each ConversationMembers object contains:  * the Id of the conversation  * an array (Members) of ChannelAccount objects |  -  |
**0** | The operation failed and the response is an error object describing the status code and failure. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_reply_to_activity**
> ResourceResponse conversations_reply_to_activity(conversation_id, activity_id, activity)

ReplyToActivity

This method allows you to reply to an activity.

This is slightly different from SendToConversation().
* SendToConversation(conversationId) - will append the activity to the end of the conversation according to the timestamp or semantics of the channel.
* ReplyToActivity(conversationId,ActivityId) - adds the activity as a reply to another activity, if the channel supports it. If the channel does not support nested replies, ReplyToActivity falls back to SendToConversation.

Use ReplyToActivity when replying to a specific activity in the conversation.

Use SendToConversation in all other cases.

### Example


```python
import bot_connector
from bot_connector.models.activity import Activity
from bot_connector.models.resource_response import ResourceResponse
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
    api_instance = bot_connector.ConversationsApi(api_client)
    conversation_id = 'conversation_id_example' # str | Conversation ID
    activity_id = 'activity_id_example' # str | activityId the reply is to (OPTIONAL)
    activity = bot_connector.Activity() # Activity | Activity to send

    try:
        # ReplyToActivity
        api_response = api_instance.conversations_reply_to_activity(conversation_id, activity_id, activity)
        print("The response of ConversationsApi->conversations_reply_to_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_reply_to_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**| Conversation ID | 
 **activity_id** | **str**| activityId the reply is to (OPTIONAL) | 
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
**200** | An object will be returned containing the ID for the resource. |  -  |
**201** | A ResourceResponse object will be returned containing the ID for the resource. |  -  |
**202** | An object will be returned containing the ID for the resource. |  -  |
**0** | The operation failed and the response is an error object describing the status code and failure. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_send_conversation_history**
> ResourceResponse conversations_send_conversation_history(conversation_id, history)

SendConversationHistory

This method allows you to upload the historic activities to the conversation.

Sender must ensure that the historic activities have unique ids and appropriate timestamps. The ids are used by the client to deal with duplicate activities and the timestamps are used by the client to render the activities in the right order.

### Example


```python
import bot_connector
from bot_connector.models.resource_response import ResourceResponse
from bot_connector.models.transcript import Transcript
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
    api_instance = bot_connector.ConversationsApi(api_client)
    conversation_id = 'conversation_id_example' # str | Conversation ID
    history = bot_connector.Transcript() # Transcript | Historic activities

    try:
        # SendConversationHistory
        api_response = api_instance.conversations_send_conversation_history(conversation_id, history)
        print("The response of ConversationsApi->conversations_send_conversation_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_send_conversation_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**| Conversation ID | 
 **history** | [**Transcript**](Transcript.md)| Historic activities | 

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
**200** | An object will be returned containing the ID for the resource. |  -  |
**201** | A ResourceResponse object will be returned containing the ID for the resource. |  -  |
**202** | An object will be returned containing the ID for the resource. |  -  |
**0** | The operation failed and the response is an error object describing the status code and failure. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_send_to_conversation**
> ResourceResponse conversations_send_to_conversation(conversation_id, activity)

SendToConversation

This method allows you to send an activity to the end of a conversation.

This is slightly different from ReplyToActivity().
* SendToConversation(conversationId) - will append the activity to the end of the conversation according to the timestamp or semantics of the channel.
* ReplyToActivity(conversationId,ActivityId) - adds the activity as a reply to another activity, if the channel supports it. If the channel does not support nested replies, ReplyToActivity falls back to SendToConversation.

Use ReplyToActivity when replying to a specific activity in the conversation.

Use SendToConversation in all other cases.

### Example


```python
import bot_connector
from bot_connector.models.activity import Activity
from bot_connector.models.resource_response import ResourceResponse
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
    api_instance = bot_connector.ConversationsApi(api_client)
    conversation_id = 'conversation_id_example' # str | Conversation ID
    activity = bot_connector.Activity() # Activity | Activity to send

    try:
        # SendToConversation
        api_response = api_instance.conversations_send_to_conversation(conversation_id, activity)
        print("The response of ConversationsApi->conversations_send_to_conversation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_send_to_conversation: %s\n" % e)
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
**200** | An object will be returned containing the ID for the resource. |  -  |
**201** | A ResourceResponse object will be returned containing the ID for the resource. |  -  |
**202** | An object will be returned containing the ID for the resource. |  -  |
**0** | The operation failed and the response is an error object describing the status code and failure. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_update_activity**
> ResourceResponse conversations_update_activity(conversation_id, activity_id, activity)

UpdateActivity

Edit an existing activity.

Some channels allow you to edit an existing activity to reflect the new state of a bot conversation.

For example, you can remove buttons after someone has clicked "Approve" button.

### Example


```python
import bot_connector
from bot_connector.models.activity import Activity
from bot_connector.models.resource_response import ResourceResponse
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
    api_instance = bot_connector.ConversationsApi(api_client)
    conversation_id = 'conversation_id_example' # str | Conversation ID
    activity_id = 'activity_id_example' # str | activityId to update
    activity = bot_connector.Activity() # Activity | replacement Activity

    try:
        # UpdateActivity
        api_response = api_instance.conversations_update_activity(conversation_id, activity_id, activity)
        print("The response of ConversationsApi->conversations_update_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_update_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**| Conversation ID | 
 **activity_id** | **str**| activityId to update | 
 **activity** | [**Activity**](Activity.md)| replacement Activity | 

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
**200** | An object will be returned containing the ID for the resource. |  -  |
**201** | A ResourceResponse object will be returned containing the ID for the resource. |  -  |
**202** | An object will be returned containing the ID for the resource. |  -  |
**0** | The operation failed and the response is an error object describing the status code and failure. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_upload_attachment**
> ResourceResponse conversations_upload_attachment(conversation_id, attachment_upload)

UploadAttachment

Upload an attachment directly into a channel's blob storage.

This is useful because it allows you to store data in a compliant store when dealing with enterprises.

The response is a ResourceResponse which contains an AttachmentId which is suitable for using with the attachments API.

### Example


```python
import bot_connector
from bot_connector.models.attachment_data import AttachmentData
from bot_connector.models.resource_response import ResourceResponse
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
    api_instance = bot_connector.ConversationsApi(api_client)
    conversation_id = 'conversation_id_example' # str | Conversation ID
    attachment_upload = bot_connector.AttachmentData() # AttachmentData | Attachment data

    try:
        # UploadAttachment
        api_response = api_instance.conversations_upload_attachment(conversation_id, attachment_upload)
        print("The response of ConversationsApi->conversations_upload_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_upload_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**| Conversation ID | 
 **attachment_upload** | [**AttachmentData**](AttachmentData.md)| Attachment data | 

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
**200** | An object will be returned containing the ID for the resource. |  -  |
**201** | A ResourceResponse object will be returned containing the ID for the resource. |  -  |
**202** | An object will be returned containing the ID for the resource. |  -  |
**0** | The operation failed and the response is an error object describing the status code and failure. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

