# coding: utf-8

"""
    Bot Connector - Direct Line API - v3.0

    Direct Line 3.0  ===============      The Direct Line API is a simple REST API for connecting directly to a single bot. This API is intended for developers  writing their own client applications, web chat controls, mobile apps, or service-to-service applications that will  talk to their bot.    Within the Direct Line API, you will find:    * An **authentication mechanism** using standard secret/token patterns  * The ability to **send** messages from your client to your bot via an HTTP POST message  * The ability to **receive** messages by **WebSocket** stream, if you choose  * The ability to **receive** messages by **polling HTTP GET**, if you choose  * A stable **schema**, even if your bot changes its protocol version    Direct Line 1.1 and 3.0 are both available and supported. This document describes Direct Line 3.0. For information  on Direct Line 1.1, visit the [Direct Line 1.1 reference documentation](/en-us/restapi/directline/).    # Authentication: Secrets and Tokens    Direct Line allows you to authenticate all calls with either a secret (retrieved from the Direct Line channel  configuration page) or a token (which you may get at runtime by converting your secret).    A Direct Line **secret** is a master key that can access any conversation, and create tokens. Secrets do not expire.    A Direct Line **token** is a key for a single conversation. It expires but can be refreshed.    If you're writing a service-to-service application, using the secret may be simplest. If you're writing an application  where the client runs in a web browser or mobile app, you may want to exchange your secret for a token, which only  works for a single conversation and will expire unless refreshed. You choose which security model works best for you.    Your secret or token is communicated in the ```Authorization``` header of every call, with the Bearer scheme.  Example below.    ```  -- connect to directline.botframework.com --  POST /v3/directline/conversations/abc123/activities HTTP/1.1  Authorization: Bearer RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0  [other HTTP headers, omitted]  ```    You may notice that your Direct Line client credentials are different from your bot's credentials. This is  intentional, and it allows you to revise your keys independently and lets you share client tokens without  disclosing your bot's password.     ## Exchanging a secret for a token    This operation is optional. Use this step if you want to prevent clients from accessing conversations they aren't  participating in.    To exchange a secret for a token, POST to /v3/directline/tokens/generate with your secret in the auth header  and no HTTP body.    ```  -- connect to directline.botframework.com --  POST /v3/directline/tokens/generate HTTP/1.1  Authorization: Bearer RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0  [other headers]    -- response from directline.botframework.com --  HTTP/1.1 200 OK  [other headers]    {    \"conversationId\": \"abc123\",    \"token\": \"RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0y8qbOF5xPGfiCpg4Fv0y8qqbOF5x8qbOF5xn\",    \"expires_in\": 1800  }  ```    If successful, the response is a token suitable for one conversation. The token expires in the seconds  indicated in the ```expires_in``` field (30 minutes in the example above) and must be refreshed before then to  remain useful.    This call is similar to ```/v3/directline/conversations```. The difference is that the call to  ```/v3/directline/tokens/generate``` does not start the conversation, does not contact the bot, and does not  create a streaming WebSocket URL.  * Call ```/v3/directline/conversations``` if you will distribute the token to client(s) and want them to     initiate the conversation.  * Call ```/v3/directline/conversations``` if you intend to start the conversation immediately.      ## Refreshing a token    A token may be refreshed an unlimited number of times unless it is expired.    To refresh a token, POST to /v3/directline/tokens/refresh. This method is valid only for unexpired tokens.    ```  -- connect to directline.botframework.com --  POST /v3/directline/tokens/refresh HTTP/1.1  Authorization: Bearer RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0y8qbOF5xPGfiCpg4Fv0y8qqbOF5x8qbOF5xn  [other headers]    -- response from directline.botframework.com --  HTTP/1.1 200 OK  [other headers]    {    \"conversationId\": \"abc123\",    \"token\": \"RCurR_XV9ZA.cwA.BKA.y8qbOF5xPGfiCpg4Fv0y8qqbOF5x8qbOF5xniaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0\",    \"expires_in\": 1800  }  ```       # REST calls for a Direct Line conversation    Direct Line conversations are explicitly opened by clients and may run as long as the bot and client participate  (and have valid credentials). While the conversation is open, the bot and client may both send messages. More than  one client may connect to a given conversation and each client may participate on behalf of multiple users.    ## Starting a conversation    Clients begin by explicitly starting a conversation. If successful, the Direct Line service replies with a  JSON object containing a conversation ID, a token, and a WebSocket URL that may be used later.    ```  -- connect to directline.botframework.com --  POST /v3/directline/conversations HTTP/1.1  Authorization: Bearer RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0y8qbOF5xPGfiCpg4Fv0y8qqbOF5x8qbOF5xn  [other headers]    -- response from directline.botframework.com --  HTTP/1.1 201 Created  [other headers]    {    \"conversationId\": \"abc123\",    \"token\": \"RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0y8qbOF5xPGfiCpg4Fv0y8qqbOF5x8qbOF5xn\",    \"expires_in\": 1800,    \"streamUrl\": \"https://directline.botframework.com/v3/directline/conversations/abc123/stream?t=RCurR_XV9ZA.cwA...\"  }  ```    If the conversation was started, an HTTP 201 status code is returned. HTTP 201 is the code that clients  will receive under most circumstances, as the typical use case is for a client to start a new conversation.  Under certain conditions -- specifically, when the client has a token scoped to a single conversation AND  when that conversation was started with a prior call to this URL -- this method will return HTTP 200 to signify  the request was acceptable but that no conversation was created (as it already existed).    You have 60 seconds to connect to the WebSocket URL. If the connection cannot be established during this time,  use the reconnect method below to generate a new stream URL.    This call is similar to ```/v3/directline/tokens/generate```. The difference is that the call to  ```/v3/directline/conversations``` starts the conversation, contacts the bot, and creates a streaming WebSocket  URL, none of which occur when generating a token.  * Call ```/v3/directline/conversations``` if you will distribute the token to client(s) and want them to    initiate the conversation.  * Call ```/v3/directline/conversations``` if you intend to start the conversation immediately.    ## Reconnecting to a conversation    If a client is using the WebSocket interface to receive messages but loses its connection, it may need to reconnect.  Reconnecting requires generating a new WebSocket stream URL, and this can be accomplished by sending a GET request  to the ```/v3/directline/conversations/{id}``` endpoint.    The ```watermark``` parameter is optional. If supplied, the conversation replays from the watermark,  guaranteeing no messages are lost. If ```watermark``` is omitted, only messages received after the reconnection  call (```GET /v3/directline/conversations/abc123```) are replayed.    ```  -- connect to directline.botframework.com --  GET /v3/directline/conversations/abc123?watermark=0000a-42 HTTP/1.1  Authorization: Bearer RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0y8qbOF5xPGfiCpg4Fv0y8qqbOF5x8qbOF5xn  [other headers]    -- response from directline.botframework.com --  HTTP/1.1 200 OK  [other headers]    {    \"conversationId\": \"abc123\",    \"token\": \"RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0y8qbOF5xPGfiCpg4Fv0y8qqbOF5x8qbOF5xn\",    \"streamUrl\": \"https://directline.botframework.com/v3/directline/conversations/abc123/stream?watermark=000a-4&t=RCurR_XV9ZA.cwA...\"  }  ```    You have 60 seconds to connect to the WebSocket stream URL. If the connection cannot be established during this  time, issue another reconnect request to get an updated stream URL.    ## Sending an Activity to the bot    Using the Direct Line 3.0 protocol, clients and bots may exchange many different Bot Framework v3 Activities,  including Message Activities, Typing Activities, and custom activities that the bot supports.    To send any one of these activities to the bot,    1. the client formulates the Activity according to the Activity schema (see below)  2. the client issues a POST message to ```/v3/directline/conversations/{id}/activities```  3. the service returns when the activity was delivered to the bot, with an HTTP status code reflecting the     bot's status code. If the POST was successful, the service returns a JSON payload containing the ID of the     Activity that was sent.    Example follows.    ```  -- connect to directline.botframework.com --  POST /v3/directline/conversations/abc123/activities HTTP/1.1  Authorization: Bearer RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0  [other headers]    {    \"type\": \"message\",    \"from\": {      \"id\": \"user1\"    },    \"text\": \"hello\"  }    -- response from directline.botframework.com --  HTTP/1.1 200 OK  [other headers]    {    \"id\": \"0001\"  }  ```    The client's Activity is available in the message retrieval path (either polling GET or WebSocket) and is not  returned inline.    The total time to POST a message to a Direct Line conversation is:    * Transit time to the Direct Line service,  * Internal processing time within Direct Line (typically less than 120ms)  * Transit time to the bot  * Processing time within the bot  * Transit time for HTTP responses to travel back to the client.    If the bot generates an error, that error will trigger an HTTP 502 error (\"Bad Gateway\") in  the ```POST /v3/directline/conversations/{id}/activities``` call.    ### Sending one or more attachments by URL    Clients may optionally send attachments, such as images or documents. If the client already has a URL for the  attachment, the simplest way to send it is to include the URL in the ```contentUrl``` field of an Activity  attachment object. This applies to HTTP, HTTPS, and ```data:``` URIs.    ### Sending a single attachment by upload    Often, clients have an image or document on a device but no URL that can be included in the activity.    To upload an attachment, POST a single attachment to  the ```/v3/directline/conversations/{conversationId}/upload``` endpoint. The ```Content-Type```  and ```Content-Disposition``` headers control the attachment's type and filename, respectively.    A user ID is required. Supply the ID of the user sending the attachment as a ```userId``` parameter in the URL.    If uploading a single attachment, a message activity is sent to the bot when the upload completes.    On completion, the service returns the ID of the activity that was sent.    ```  -- connect to directline.botframework.com --  POST /v3/directline/conversations/abc123/upload?userId=user1 HTTP/1.1  Authorization: Bearer RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0  Content-Type: image/jpeg  Content-Disposition: name=\"file\"; filename=\"badjokeeel.jpg\"  [other headers]    [JPEG content]    -- response from directline.botframework.com --  HTTP/1.1 200 OK  [other headers]    {    \"id\": \"0003\"  }  ```    ### Sending multiple attachments by upload    If uploading multiple attachments, use ```multipart/form-data``` as the content type and include each  attachment as a separate part. Each attachment's type and filename may be included in the ```Content-Type```  and ```Content-Disposition``` headers in each part.    An activity may be included by adding a part with content type of ```application/vnd.microsoft.activity```.  Other parts in the payload are attached to this activity before it is sent. If an Activity is not included,  an empty Activity is created as a wrapper for the attachments.    ```  -- connect to directline.botframework.com --  POST /v3/directline/conversations/abc123/upload?userId=user1 HTTP/1.1  Authorization: Bearer RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0  Content-Type: multipart/form-data; boundary=----DD4E5147-E865-4652-B662-F223701A8A89  [other headers]    ----DD4E5147-E865-4652-B662-F223701A8A89  Content-Type: image/jpeg  Content-Disposition: form-data; name=\"file\"; filename=\"badjokeeel.jpg\"  [other headers]    [JPEG content]    ----DD4E5147-E865-4652-B662-F223701A8A89  Content-Type: application/vnd.microsoft.activity  [other headers]    {    \"type\": \"message\",    \"from\": {      \"id\": \"user1\"    },    \"text\": \"Hey I just IM'd you\\n\\nand this is crazy\\n\\nbut here's my webhook\\n\\nso POST me maybe\"  }    ----DD4E5147-E865-4652-B662-F223701A8A89            -- response from directline.botframework.com --  HTTP/1.1 200 OK  [other headers]    {    \"id\": \"0004\"  }  ```    ## Receiving Activities from the bot    Direct Line 3.0 clients may choose from two different mechanisms for retrieving messages:    1. A **streaming WebSocket**, which pushes messages efficiently to clients.  2. A **polling GET** interface, which is available for clients unable to use WebSockets or for clients     retrieving the conversation history.    **Not all activities are available via the polling GET interface.** A table of activity availability follows.    |Activity type|Availability|  |-------------|--------|  |Message|Polling GET and WebSocket|  |Typing|WebSocket only|  |ConversationUpdate|Not sent/received via client|  |ContactRelationUpdate|Not supported in Direct Line|  |EndOfConversation|Polling GET and WebSocket|  |All other activity types|Polling GET and WebSocket|    ### Receiving Activities by WebSocket    To connect via WebSocket, a client uses the StreamUrl when starting a conversation. The stream URL is  preauthorized and does NOT require an Authorization header containing the client's secret or token.    ```  -- connect to wss://directline.botframework.com --  GET /v3/directline/conversations/abc123/stream?t=RCurR_XV9ZA.cwA...\" HTTP/1.1  Upgrade: websocket  Connection: upgrade  [other headers]    -- response from directline.botframework.com --  HTTP/1.1 101 Switching Protocols  [other headers]  ```    The Direct Line service sends the following messages:    * An **ActivitySet**, which contains one or more activities and a watermark (described below)  * An empty message, which the Direct Line service uses to ensure the connection is still valid  * Additional types, to be defined later. These types are identified by the properties in the JSON root.    ActivitySets contain messages sent by the bot and by all users. Example ActivitySet:    ```  {    \"activities\": [{      \"type\": \"message\",      \"channelId\": \"directline\",      \"conversation\": {        \"id\": \"abc123\"      },      \"id\": \"abc123|0000\",      \"from\": {        \"id\": \"user1\"      },      \"text\": \"hello\"    }],    \"watermark\": \"0000a-42\"  }  ```    Clients should keep track of the \"watermark\" value from each ActivitySet so they can use it on reconnect.  **Note** that a ```null``` or missing watermark should be ignored and should not overwrite a prior watermark  in the client.    Clients should ignore empty messages.    Clients may send their own empty messages to verify connectivity. The Direct Line service will ignore these.    The service may forcibly close the connection under certain conditions. If the client has not received an  EndOfConversation activity, it may reconnect by issuing a GET request to the conversation endpoint to get a  new stream URL (see above).    The WebSocket stream contains live updates and very recent messages (since the call to get the WebSocket call  was issued) but it does not include messages sent prior to the most recent POST  to ```/v3/directline/conversations/{id}```. To retrieve messages sent earlier in the conversation, use the  GET mechanism below.    ### Receiving Activities by GET    The GET mechanism is useful for clients who are unable to use the WebSocket, or for clients wishing to retrieve  the conversation history.    To retrieve messages, issue a GET call to the conversation endpoint. Optionally supply a watermark, indicating  the most recent message seen. The watermark field accompanies all GET/WebSocket messages as a property in the  ActivitySet.    ```  -- connect to directline.botframework.com --  GET /v3/directline/conversations/abc123/activities?watermark=0001a-94 HTTP/1.1  Authorization: Bearer RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0  [other headers]    -- response from directline.botframework.com --  HTTP/1.1 200 OK  [other headers]    {    \"activities\": [{      \"type\": \"message\",      \"channelId\": \"directline\",      \"conversation\": {        \"id\": \"abc123\"      },      \"id\": \"abc123|0000\",      \"from\": {        \"id\": \"user1\"      },      \"text\": \"hello\"    }, {      \"type\": \"message\",      \"channelId\": \"directline\",      \"conversation\": {        \"id\": \"abc123\"      },      \"id\": \"abc123|0001\",      \"from\": {        \"id\": \"bot1\"      },      \"text\": \"Nice to see you, user1!\"    }],    \"watermark\": \"0001a-95\"  }  ```    Clients should page through the available activities by advancing the ```watermark``` value until no activities  are returned.      ### Timing considerations     Most clients wish to retain a complete message history. Even though Direct Line is a multi-part protocol with  potential timing gaps, the protocol and service is designed to make it easy to build a reliable client.    1. The ```watermark``` field sent in the WebSocket stream and GET response is reliable. You will not miss     messages as long as you replay the watermark verbatim.  2. When starting a conversation and connecting to the WebSocket stream, any Activities sent after the POST but     before the socket is opened are replayed before new messages.  3. When refreshing history by GET call while connected to the WebSocket, Activities may be duplicated across both     channels. Keeping a list of all known Activity IDs will allow you to reject duplicate messages should they occur.    Clients using the polling GET interface should choose a polling interval that matches their intended use.    * Service-to-service applications often use a polling interval of 5s or 10s.  * Client-facing applications often use a polling interval of 1s, and fire an additional request ~300ms after    every message the client sends to rapidly pick up a bot's response. This 300ms delay should be adjusted    based on the bot's speed and transit time.    ## Ending a conversation    Either a client or a bot may signal the end of a DirectLine conversation. This operation halts communication  and prevents the bot and the client from sending messages. Messages may still be retrieved via the GET mechanism.  Sending this messages is as simple as POSTing an EndOfConversation activity.    ```  -- connect to directline.botframework.com --  POST /v3/directline/conversations/abc123/activities HTTP/1.1  Authorization: Bearer RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0  [other headers]    {    \"type\": \"endOfConversation\",    \"from\": {      \"id\": \"user1\"    }  }    -- response from directline.botframework.com --  HTTP/1.1 200 OK  [other headers]    {    \"id\": \"0004\"  }  ```    ## REST API errors    HTTP calls to the Direct Line service follow standard HTTP error conventions:    * 2xx status codes indicate success. (Direct Line 3.0 uses 200 and 201.)  * 4xx status codes indicate an error in your request.    * 401 indicates a missing or malformed Authorization header (or URL token, in calls where a token parameter      is allowed).    * 403 indicates an unauthorized client.      * If calling with a valid but expired token, the ```code``` field is set to ```TokenExpired```.    * 404 indicates a missing path, site, conversation, etc.  * 5xx status codes indicate a service-side error.    * 500 indicates an error inside the Direct Line service.    * 502 indicates an error was returned by the bot. **This is a common error code.**  * 101 is used in the WebSocket connection path, although this is likely handled by your WebSocket client.    When an error message is returned, error detail may be present in a JSON response. Look for an ```error```  property with ```code``` and ```message``` fields.    ```  -- connect to directline.botframework.com --  POST /v3/directline/conversations/abc123/activities HTTP/1.1  [detail omitted]    -- response from directline.botframework.com --  HTTP/1.1 502 Bad Gateway  [other headers]    {    \"error\": {      \"code\": \"BotRejectedActivity\",      \"message\": \"Failed to send activity: bot returned an error\"    }  }  ```    The contents of the ```message``` field may change. The HTTP status code and values in the ```code```  property are stable.    # Schema    The Direct Line 3.0 schema is identical to the Bot Framework v3 schema.    When a bot sends an Activity to a client through Direct Line:    * attachment cards are preserved,  * URLs for uploaded attachments are hidden with a private link, and  * the ```channelData``` property is preserved without modification.    When a client sends an Activity to a bot through Direct Line:    * the ```type``` property contains the kind of activity you are sending (typically ```message```),  * the ```from``` property must be populated with a user ID, chosen by your client,  * attachments may contain URLs to existing resources or URLs uploaded through the Direct Line attachment    endpoint, and  * the ```channelData``` property is preserved without modification.    Clients and bots may send Activities of any type, including Message Activities, Typing Activities, and  custom Activity types.    Clients may send a single Activity at a time.    ```  {    \"type\": \"message\",    \"channelId\": \"directline\",    \"from\": {      \"id\": \"user1\"    },    \"text\": \"hello\"  }  ```    Clients receive multiple Activities as part of an ActivitySet. The ActivitySet has an array of activities  and a watermark field.    ```  {    \"activities\": [{      \"type\": \"message\",      \"channelId\": \"directline\",      \"conversation\": {        \"id\": \"abc123\"      },      \"id\": \"abc123|0000\",      \"from\": {        \"id\": \"user1\"      },      \"text\": \"hello\"    }],    \"watermark\": \"0000a-42\"  }  ```    # Libraries for the Direct Line API    The Direct Line API is designed to be coded directly, but the Bot Framework includes libraries and controls that  help you to embed Direct-Line-powered bots into your application.    * The [Bot Framework Web Chat control](https://github.com/Microsoft/BotFramework-WebChat) is an easy way to embed    the Direct Line protocol into a webpage.  * [Direct Line Nuget package](https://www.nuget.org/packages/Microsoft.Bot.Connector.DirectLine) with libraries for    .Net 4.5, UWP, and .Net Standard.  * [DirectLineJs](https://github.com/Microsoft/BotFramework-DirectLineJs), also available on    [NPM](https://www.npmjs.com/package/botframework-directlinejs)  * You may generate your own from the [Direct Line Swagger file](swagger.json)    Our [BotBuilder-Samples GitHub repo](https://github.com/Microsoft/BotBuilder-Samples) also contains samples for    [C#](https://github.com/Microsoft/BotBuilder-Samples/tree/master/CSharp/core-DirectLine) and    [JavaScript](https://github.com/Microsoft/BotBuilder-Samples/tree/master/Node/core-DirectLine).

    The version of the OpenAPI document: v3
    Contact: botframework@microsoft.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import datetime
from dateutil.parser import parse
from enum import Enum
import decimal
import json
import mimetypes
import os
import re
import tempfile

from urllib.parse import quote
from typing import Tuple, Optional, List, Dict, Union
from pydantic import SecretStr

from direct_line.configuration import Configuration
from direct_line.api_response import ApiResponse, T as ApiResponseT
import direct_line.models
from direct_line import rest
from direct_line.exceptions import (
    ApiValueError,
    ApiException,
    BadRequestException,
    UnauthorizedException,
    ForbiddenException,
    NotFoundException,
    ServiceException
)

RequestSerialized = Tuple[str, str, Dict[str, str], Optional[str], List[str]]

class ApiClient:
    """Generic API client for OpenAPI client library builds.

    OpenAPI generic API client. This client handles the client-
    server communication, and is invariant across implementations. Specifics of
    the methods and models for each application are generated from the OpenAPI
    templates.

    :param configuration: .Configuration object for this client
    :param header_name: a header to pass when making calls to the API.
    :param header_value: a header value to pass when making calls to
        the API.
    :param cookie: a cookie to include in the header when making calls
        to the API
    """

    PRIMITIVE_TYPES = (float, bool, bytes, str, int)
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int, # TODO remove as only py3 is supported?
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'decimal': decimal.Decimal,
        'object': object,
    }
    _pool = None

    def __init__(
        self,
        configuration=None,
        header_name=None,
        header_value=None,
        cookie=None
    ) -> None:
        # use default configuration if none is provided
        if configuration is None:
            configuration = Configuration.get_default()
        self.configuration = configuration

        self.rest_client = rest.RESTClientObject(configuration)
        self.default_headers = {}
        if header_name is not None:
            self.default_headers[header_name] = header_value
        self.cookie = cookie
        # Set default User-Agent.
        self.user_agent = 'OpenAPI-Generator/1.0.0/python'
        self.client_side_validation = configuration.client_side_validation

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    @property
    def user_agent(self):
        """User agent for this API client"""
        return self.default_headers['User-Agent']

    @user_agent.setter
    def user_agent(self, value):
        self.default_headers['User-Agent'] = value

    def set_default_header(self, header_name, header_value):
        self.default_headers[header_name] = header_value


    _default = None

    @classmethod
    def get_default(cls):
        """Return new instance of ApiClient.

        This method returns newly created, based on default constructor,
        object of ApiClient class or returns a copy of default
        ApiClient.

        :return: The ApiClient object.
        """
        if cls._default is None:
            cls._default = ApiClient()
        return cls._default

    @classmethod
    def set_default(cls, default):
        """Set default instance of ApiClient.

        It stores default ApiClient.

        :param default: object of ApiClient.
        """
        cls._default = default

    def param_serialize(
        self,
        method,
        resource_path,
        path_params=None,
        query_params=None,
        header_params=None,
        body=None,
        post_params=None,
        files=None, auth_settings=None,
        collection_formats=None,
        _host=None,
        _request_auth=None
    ) -> RequestSerialized:

        """Builds the HTTP request params needed by the request.
        :param method: Method to call.
        :param resource_path: Path to method endpoint.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param files dict: key -> filename, value -> filepath,
            for `multipart/form-data`.
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :return: tuple of form (path, http_method, query_params, header_params,
            body, post_params, files)
        """

        config = self.configuration

        # header parameters
        header_params = header_params or {}
        header_params.update(self.default_headers)
        if self.cookie:
            header_params['Cookie'] = self.cookie
        if header_params:
            header_params = self.sanitize_for_serialization(header_params)
            header_params = dict(
                self.parameters_to_tuples(header_params,collection_formats)
            )

        # path parameters
        if path_params:
            path_params = self.sanitize_for_serialization(path_params)
            path_params = self.parameters_to_tuples(
                path_params,
                collection_formats
            )
            for k, v in path_params:
                # specified safe chars, encode everything
                resource_path = resource_path.replace(
                    '{%s}' % k,
                    quote(str(v), safe=config.safe_chars_for_path_param)
                )

        # post parameters
        if post_params or files:
            post_params = post_params if post_params else []
            post_params = self.sanitize_for_serialization(post_params)
            post_params = self.parameters_to_tuples(
                post_params,
                collection_formats
            )
            if files:
                post_params.extend(self.files_parameters(files))

        # auth setting
        self.update_params_for_auth(
            header_params,
            query_params,
            auth_settings,
            resource_path,
            method,
            body,
            request_auth=_request_auth
        )

        # body
        if body:
            body = self.sanitize_for_serialization(body)

        # request url
        if _host is None or self.configuration.ignore_operation_servers:
            url = self.configuration.host + resource_path
        else:
            # use server/host defined in path or operation instead
            url = _host + resource_path

        # query parameters
        if query_params:
            query_params = self.sanitize_for_serialization(query_params)
            url_query = self.parameters_to_url_query(
                query_params,
                collection_formats
            )
            url += "?" + url_query

        return method, url, header_params, body, post_params


    def call_api(
        self,
        method,
        url,
        header_params=None,
        body=None,
        post_params=None,
        _request_timeout=None
    ) -> rest.RESTResponse:
        """Makes the HTTP request (synchronous)
        :param method: Method to call.
        :param url: Path to method endpoint.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param _request_timeout: timeout setting for this request.
        :return: RESTResponse
        """

        try:
            # perform request and return response
            response_data = self.rest_client.request(
                method, url,
                headers=header_params,
                body=body, post_params=post_params,
                _request_timeout=_request_timeout
            )

        except ApiException as e:
            raise e

        return response_data

    def response_deserialize(
        self,
        response_data: rest.RESTResponse,
        response_types_map: Optional[Dict[str, ApiResponseT]]=None
    ) -> ApiResponse[ApiResponseT]:
        """Deserializes response into an object.
        :param response_data: RESTResponse object to be deserialized.
        :param response_types_map: dict of response types.
        :return: ApiResponse
        """

        msg = "RESTResponse.read() must be called before passing it to response_deserialize()"
        assert response_data.data is not None, msg

        response_type = response_types_map.get(str(response_data.status), None)
        if not response_type and isinstance(response_data.status, int) and 100 <= response_data.status <= 599:
            # if not found, look for '1XX', '2XX', etc.
            response_type = response_types_map.get(str(response_data.status)[0] + "XX", None)

        # deserialize response data
        response_text = None
        return_data = None
        try:
            if response_type == "bytearray":
                return_data = response_data.data
            elif response_type == "file":
                return_data = self.__deserialize_file(response_data)
            elif response_type is not None:
                match = None
                content_type = response_data.getheader('content-type')
                if content_type is not None:
                    match = re.search(r"charset=([a-zA-Z\-\d]+)[\s;]?", content_type)
                encoding = match.group(1) if match else "utf-8"
                response_text = response_data.data.decode(encoding)
                return_data = self.deserialize(response_text, response_type, content_type)
        finally:
            if not 200 <= response_data.status <= 299:
                raise ApiException.from_response(
                    http_resp=response_data,
                    body=response_text,
                    data=return_data,
                )

        return ApiResponse(
            status_code = response_data.status,
            data = return_data,
            headers = response_data.getheaders(),
            raw_data = response_data.data
        )

    def sanitize_for_serialization(self, obj):
        """Builds a JSON POST object.

        If obj is None, return None.
        If obj is SecretStr, return obj.get_secret_value()
        If obj is str, int, long, float, bool, return directly.
        If obj is datetime.datetime, datetime.date
            convert to string in iso8601 format.
        If obj is decimal.Decimal return string representation.
        If obj is list, sanitize each element in the list.
        If obj is dict, return the dict.
        If obj is OpenAPI model, return the properties dict.

        :param obj: The data to serialize.
        :return: The serialized form of data.
        """
        if obj is None:
            return None
        elif isinstance(obj, Enum):
            return obj.value
        elif isinstance(obj, SecretStr):
            return obj.get_secret_value()
        elif isinstance(obj, self.PRIMITIVE_TYPES):
            return obj
        elif isinstance(obj, list):
            return [
                self.sanitize_for_serialization(sub_obj) for sub_obj in obj
            ]
        elif isinstance(obj, tuple):
            return tuple(
                self.sanitize_for_serialization(sub_obj) for sub_obj in obj
            )
        elif isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        elif isinstance(obj, decimal.Decimal):
            return str(obj)

        elif isinstance(obj, dict):
            obj_dict = obj
        else:
            # Convert model obj to dict except
            # attributes `openapi_types`, `attribute_map`
            # and attributes which value is not None.
            # Convert attribute name to json key in
            # model definition for request.
            if hasattr(obj, 'to_dict') and callable(getattr(obj, 'to_dict')):
                obj_dict = obj.to_dict()
            else:
                obj_dict = obj.__dict__

        return {
            key: self.sanitize_for_serialization(val)
            for key, val in obj_dict.items()
        }

    def deserialize(self, response_text: str, response_type: str, content_type: Optional[str]):
        """Deserializes response into an object.

        :param response: RESTResponse object to be deserialized.
        :param response_type: class literal for
            deserialized object, or string of class name.
        :param content_type: content type of response.

        :return: deserialized object.
        """

        # fetch data from response object
        if content_type is None:
            try:
                data = json.loads(response_text)
            except ValueError:
                data = response_text
        elif re.match(r'^application/(json|[\w!#$&.+-^_]+\+json)\s*(;|$)', content_type, re.IGNORECASE):
            if response_text == "":
                data = ""
            else:
                data = json.loads(response_text)
        elif re.match(r'^text\/[a-z.+-]+\s*(;|$)', content_type, re.IGNORECASE):
            data = response_text
        else:
            raise ApiException(
                status=0,
                reason="Unsupported content type: {0}".format(content_type)
            )

        return self.__deserialize(data, response_type)

    def __deserialize(self, data, klass):
        """Deserializes dict, list, str into an object.

        :param data: dict, list or str.
        :param klass: class literal, or string of class name.

        :return: object.
        """
        if data is None:
            return None

        if isinstance(klass, str):
            if klass.startswith('List['):
                m = re.match(r'List\[(.*)]', klass)
                assert m is not None, "Malformed List type definition"
                sub_kls = m.group(1)
                return [self.__deserialize(sub_data, sub_kls)
                        for sub_data in data]

            if klass.startswith('Dict['):
                m = re.match(r'Dict\[([^,]*), (.*)]', klass)
                assert m is not None, "Malformed Dict type definition"
                sub_kls = m.group(2)
                return {k: self.__deserialize(v, sub_kls)
                        for k, v in data.items()}

            # convert str to class
            if klass in self.NATIVE_TYPES_MAPPING:
                klass = self.NATIVE_TYPES_MAPPING[klass]
            else:
                klass = getattr(direct_line.models, klass)

        if klass in self.PRIMITIVE_TYPES:
            return self.__deserialize_primitive(data, klass)
        elif klass == object:
            return self.__deserialize_object(data)
        elif klass == datetime.date:
            return self.__deserialize_date(data)
        elif klass == datetime.datetime:
            return self.__deserialize_datetime(data)
        elif klass == decimal.Decimal:
            return decimal.Decimal(data)
        elif issubclass(klass, Enum):
            return self.__deserialize_enum(data, klass)
        else:
            return self.__deserialize_model(data, klass)

    def parameters_to_tuples(self, params, collection_formats):
        """Get parameters as list of tuples, formatting collections.

        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: Parameters as list of tuples, collections formatted
        """
        new_params: List[Tuple[str, str]] = []
        if collection_formats is None:
            collection_formats = {}
        for k, v in params.items() if isinstance(params, dict) else params:
            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == 'multi':
                    new_params.extend((k, value) for value in v)
                else:
                    if collection_format == 'ssv':
                        delimiter = ' '
                    elif collection_format == 'tsv':
                        delimiter = '\t'
                    elif collection_format == 'pipes':
                        delimiter = '|'
                    else:  # csv is the default
                        delimiter = ','
                    new_params.append(
                        (k, delimiter.join(str(value) for value in v)))
            else:
                new_params.append((k, v))
        return new_params

    def parameters_to_url_query(self, params, collection_formats):
        """Get parameters as list of tuples, formatting collections.

        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: URL query string (e.g. a=Hello%20World&b=123)
        """
        new_params: List[Tuple[str, str]] = []
        if collection_formats is None:
            collection_formats = {}
        for k, v in params.items() if isinstance(params, dict) else params:
            if isinstance(v, bool):
                v = str(v).lower()
            if isinstance(v, (int, float)):
                v = str(v)
            if isinstance(v, dict):
                v = json.dumps(v)

            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == 'multi':
                    new_params.extend((k, quote(str(value))) for value in v)
                else:
                    if collection_format == 'ssv':
                        delimiter = ' '
                    elif collection_format == 'tsv':
                        delimiter = '\t'
                    elif collection_format == 'pipes':
                        delimiter = '|'
                    else:  # csv is the default
                        delimiter = ','
                    new_params.append(
                        (k, delimiter.join(quote(str(value)) for value in v))
                    )
            else:
                new_params.append((k, quote(str(v))))

        return "&".join(["=".join(map(str, item)) for item in new_params])

    def files_parameters(
        self,
        files: Dict[str, Union[str, bytes, List[str], List[bytes], Tuple[str, bytes]]],
    ):
        """Builds form parameters.

        :param files: File parameters.
        :return: Form parameters with files.
        """
        params = []
        for k, v in files.items():
            if isinstance(v, str):
                with open(v, 'rb') as f:
                    filename = os.path.basename(f.name)
                    filedata = f.read()
            elif isinstance(v, bytes):
                filename = k
                filedata = v
            elif isinstance(v, tuple):
                filename, filedata = v
            elif isinstance(v, list):
                for file_param in v:
                    params.extend(self.files_parameters({k: file_param}))
                continue
            else:
                raise ValueError("Unsupported file value")
            mimetype = (
                mimetypes.guess_type(filename)[0]
                or 'application/octet-stream'
            )
            params.append(
                tuple([k, tuple([filename, filedata, mimetype])])
            )
        return params

    def select_header_accept(self, accepts: List[str]) -> Optional[str]:
        """Returns `Accept` based on an array of accepts provided.

        :param accepts: List of headers.
        :return: Accept (e.g. application/json).
        """
        if not accepts:
            return None

        for accept in accepts:
            if re.search('json', accept, re.IGNORECASE):
                return accept

        return accepts[0]

    def select_header_content_type(self, content_types):
        """Returns `Content-Type` based on an array of content_types provided.

        :param content_types: List of content-types.
        :return: Content-Type (e.g. application/json).
        """
        if not content_types:
            return None

        for content_type in content_types:
            if re.search('json', content_type, re.IGNORECASE):
                return content_type

        return content_types[0]

    def update_params_for_auth(
        self,
        headers,
        queries,
        auth_settings,
        resource_path,
        method,
        body,
        request_auth=None
    ) -> None:
        """Updates header and query params based on authentication setting.

        :param headers: Header parameters dict to be updated.
        :param queries: Query parameters tuple list to be updated.
        :param auth_settings: Authentication setting identifiers list.
        :resource_path: A string representation of the HTTP request resource path.
        :method: A string representation of the HTTP request method.
        :body: A object representing the body of the HTTP request.
        The object type is the return value of sanitize_for_serialization().
        :param request_auth: if set, the provided settings will
                             override the token in the configuration.
        """
        if not auth_settings:
            return

        if request_auth:
            self._apply_auth_params(
                headers,
                queries,
                resource_path,
                method,
                body,
                request_auth
            )
        else:
            for auth in auth_settings:
                auth_setting = self.configuration.auth_settings().get(auth)
                if auth_setting:
                    self._apply_auth_params(
                        headers,
                        queries,
                        resource_path,
                        method,
                        body,
                        auth_setting
                    )

    def _apply_auth_params(
        self,
        headers,
        queries,
        resource_path,
        method,
        body,
        auth_setting
    ) -> None:
        """Updates the request parameters based on a single auth_setting

        :param headers: Header parameters dict to be updated.
        :param queries: Query parameters tuple list to be updated.
        :resource_path: A string representation of the HTTP request resource path.
        :method: A string representation of the HTTP request method.
        :body: A object representing the body of the HTTP request.
        The object type is the return value of sanitize_for_serialization().
        :param auth_setting: auth settings for the endpoint
        """
        if auth_setting['in'] == 'cookie':
            headers['Cookie'] = auth_setting['value']
        elif auth_setting['in'] == 'header':
            if auth_setting['type'] != 'http-signature':
                headers[auth_setting['key']] = auth_setting['value']
        elif auth_setting['in'] == 'query':
            queries.append((auth_setting['key'], auth_setting['value']))
        else:
            raise ApiValueError(
                'Authentication token must be in `query` or `header`'
            )

    def __deserialize_file(self, response):
        """Deserializes body to file

        Saves response body into a file in a temporary folder,
        using the filename from the `Content-Disposition` header if provided.

        handle file downloading
        save response body into a tmp file and return the instance

        :param response:  RESTResponse.
        :return: file path.
        """
        fd, path = tempfile.mkstemp(dir=self.configuration.temp_folder_path)
        os.close(fd)
        os.remove(path)

        content_disposition = response.getheader("Content-Disposition")
        if content_disposition:
            m = re.search(
                r'filename=[\'"]?([^\'"\s]+)[\'"]?',
                content_disposition
            )
            assert m is not None, "Unexpected 'content-disposition' header value"
            filename = m.group(1)
            path = os.path.join(os.path.dirname(path), filename)

        with open(path, "wb") as f:
            f.write(response.data)

        return path

    def __deserialize_primitive(self, data, klass):
        """Deserializes string to primitive type.

        :param data: str.
        :param klass: class literal.

        :return: int, long, float, str, bool.
        """
        try:
            return klass(data)
        except UnicodeEncodeError:
            return str(data)
        except TypeError:
            return data

    def __deserialize_object(self, value):
        """Return an original value.

        :return: object.
        """
        return value

    def __deserialize_date(self, string):
        """Deserializes string to date.

        :param string: str.
        :return: date.
        """
        try:
            return parse(string).date()
        except ImportError:
            return string
        except ValueError:
            raise rest.ApiException(
                status=0,
                reason="Failed to parse `{0}` as date object".format(string)
            )

    def __deserialize_datetime(self, string):
        """Deserializes string to datetime.

        The string should be in iso8601 datetime format.

        :param string: str.
        :return: datetime.
        """
        try:
            return parse(string)
        except ImportError:
            return string
        except ValueError:
            raise rest.ApiException(
                status=0,
                reason=(
                    "Failed to parse `{0}` as datetime object"
                    .format(string)
                )
            )

    def __deserialize_enum(self, data, klass):
        """Deserializes primitive type to enum.

        :param data: primitive type.
        :param klass: class literal.
        :return: enum value.
        """
        try:
            return klass(data)
        except ValueError:
            raise rest.ApiException(
                status=0,
                reason=(
                    "Failed to parse `{0}` as `{1}`"
                    .format(data, klass)
                )
            )

    def __deserialize_model(self, data, klass):
        """Deserializes list or dict to model.

        :param data: dict, list.
        :param klass: class literal.
        :return: model object.
        """

        return klass.from_dict(data)
