# direct_line.TokensApi

All URIs are relative to *https://directline.botframework.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tokens_generate_token_for_new_conversation**](TokensApi.md#tokens_generate_token_for_new_conversation) | **POST** /v3/directline/tokens/generate | Generate a token for a new conversation
[**tokens_refresh_token**](TokensApi.md#tokens_refresh_token) | **POST** /v3/directline/tokens/refresh | Refresh a token


# **tokens_generate_token_for_new_conversation**
> Conversation tokens_generate_token_for_new_conversation(token_parameters=token_parameters)

Generate a token for a new conversation

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
    api_instance = direct_line.TokensApi(api_client)
    token_parameters = direct_line.TokenParameters() # TokenParameters |  (optional)

    try:
        # Generate a token for a new conversation
        api_response = api_instance.tokens_generate_token_for_new_conversation(token_parameters=token_parameters)
        print("The response of TokensApi->tokens_generate_token_for_new_conversation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokensApi->tokens_generate_token_for_new_conversation: %s\n" % e)
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
**401** | The operation included an invalid or missing Authorization header. |  -  |
**403** | You are forbidden from performing this action because your token or secret is invalid. |  -  |
**404** | The requested resource was not found. |  -  |
**429** | Too many requests have been submitted to this API. This error may be accompanied by a Retry-After header, which includes the suggested retry interval. |  -  |
**500** | An internal server error has occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tokens_refresh_token**
> Conversation tokens_refresh_token()

Refresh a token

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
    api_instance = direct_line.TokensApi(api_client)

    try:
        # Refresh a token
        api_response = api_instance.tokens_refresh_token()
        print("The response of TokensApi->tokens_refresh_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokensApi->tokens_refresh_token: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**401** | The operation included an invalid or missing Authorization header. |  -  |
**403** | You are forbidden from performing this action because your token or secret is invalid. |  -  |
**404** | The requested resource was not found. |  -  |
**429** | Too many requests have been submitted to this API. This error may be accompanied by a Retry-After header, which includes the suggested retry interval. |  -  |
**500** | An internal server error has occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

