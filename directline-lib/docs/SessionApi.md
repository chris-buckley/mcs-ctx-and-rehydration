# direct_line.SessionApi

All URIs are relative to *https://directline.botframework.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**session_get_session_id**](SessionApi.md#session_get_session_id) | **GET** /v3/directline/session/getsessionid | 


# **session_get_session_id**
> object session_get_session_id()

### Example


```python
import direct_line
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
    api_instance = direct_line.SessionApi(api_client)

    try:
        api_response = api_instance.session_get_session_id()
        print("The response of SessionApi->session_get_session_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionApi->session_get_session_id: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

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

