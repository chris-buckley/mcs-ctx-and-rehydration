# coding: utf-8

"""
    Bot Connector - Direct Line API - v3.0

    Direct Line 3.0  ===============      The Direct Line API is a simple REST API for connecting directly to a single bot. This API is intended for developers  writing their own client applications, web chat controls, mobile apps, or service-to-service applications that will  talk to their bot.    Within the Direct Line API, you will find:    * An **authentication mechanism** using standard secret/token patterns  * The ability to **send** messages from your client to your bot via an HTTP POST message  * The ability to **receive** messages by **WebSocket** stream, if you choose  * The ability to **receive** messages by **polling HTTP GET**, if you choose  * A stable **schema**, even if your bot changes its protocol version    Direct Line 1.1 and 3.0 are both available and supported. This document describes Direct Line 3.0. For information  on Direct Line 1.1, visit the [Direct Line 1.1 reference documentation](/en-us/restapi/directline/).    # Authentication: Secrets and Tokens    Direct Line allows you to authenticate all calls with either a secret (retrieved from the Direct Line channel  configuration page) or a token (which you may get at runtime by converting your secret).    A Direct Line **secret** is a master key that can access any conversation, and create tokens. Secrets do not expire.    A Direct Line **token** is a key for a single conversation. It expires but can be refreshed.    If you're writing a service-to-service application, using the secret may be simplest. If you're writing an application  where the client runs in a web browser or mobile app, you may want to exchange your secret for a token, which only  works for a single conversation and will expire unless refreshed. You choose which security model works best for you.    Your secret or token is communicated in the ```Authorization``` header of every call, with the Bearer scheme.  Example below.    ```  -- connect to directline.botframework.com --  POST /v3/directline/conversations/abc123/activities HTTP/1.1  Authorization: Bearer RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0  [other HTTP headers, omitted]  ```    You may notice that your Direct Line client credentials are different from your bot's credentials. This is  intentional, and it allows you to revise your keys independently and lets you share client tokens without  disclosing your bot's password.     ## Exchanging a secret for a token    This operation is optional. Use this step if you want to prevent clients from accessing conversations they aren't  participating in.    To exchange a secret for a token, POST to /v3/directline/tokens/generate with your secret in the auth header  and no HTTP body.    ```  -- connect to directline.botframework.com --  POST /v3/directline/tokens/generate HTTP/1.1  Authorization: Bearer RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0  [other headers]    -- response from directline.botframework.com --  HTTP/1.1 200 OK  [other headers]    {    \"conversationId\": \"abc123\",    \"token\": \"RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0y8qbOF5xPGfiCpg4Fv0y8qqbOF5x8qbOF5xn\",    \"expires_in\": 1800  }  ```    If successful, the response is a token suitable for one conversation. The token expires in the seconds  indicated in the ```expires_in``` field (30 minutes in the example above) and must be refreshed before then to  remain useful.    This call is similar to ```/v3/directline/conversations```. The difference is that the call to  ```/v3/directline/tokens/generate``` does not start the conversation, does not contact the bot, and does not  create a streaming WebSocket URL.  * Call ```/v3/directline/conversations``` if you will distribute the token to client(s) and want them to     initiate the conversation.  * Call ```/v3/directline/conversations``` if you intend to start the conversation immediately.      ## Refreshing a token    A token may be refreshed an unlimited number of times unless it is expired.    To refresh a token, POST to /v3/directline/tokens/refresh. This method is valid only for unexpired tokens.    ```  -- connect to directline.botframework.com --  POST /v3/directline/tokens/refresh HTTP/1.1  Authorization: Bearer RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0y8qbOF5xPGfiCpg4Fv0y8qqbOF5x8qbOF5xn  [other headers]    -- response from directline.botframework.com --  HTTP/1.1 200 OK  [other headers]    {    \"conversationId\": \"abc123\",    \"token\": \"RCurR_XV9ZA.cwA.BKA.y8qbOF5xPGfiCpg4Fv0y8qqbOF5x8qbOF5xniaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0\",    \"expires_in\": 1800  }  ```       # REST calls for a Direct Line conversation    Direct Line conversations are explicitly opened by clients and may run as long as the bot and client participate  (and have valid credentials). While the conversation is open, the bot and client may both send messages. More than  one client may connect to a given conversation and each client may participate on behalf of multiple users.    ## Starting a conversation    Clients begin by explicitly starting a conversation. If successful, the Direct Line service replies with a  JSON object containing a conversation ID, a token, and a WebSocket URL that may be used later.    ```  -- connect to directline.botframework.com --  POST /v3/directline/conversations HTTP/1.1  Authorization: Bearer RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0y8qbOF5xPGfiCpg4Fv0y8qqbOF5x8qbOF5xn  [other headers]    -- response from directline.botframework.com --  HTTP/1.1 201 Created  [other headers]    {    \"conversationId\": \"abc123\",    \"token\": \"RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0y8qbOF5xPGfiCpg4Fv0y8qqbOF5x8qbOF5xn\",    \"expires_in\": 1800,    \"streamUrl\": \"https://directline.botframework.com/v3/directline/conversations/abc123/stream?t=RCurR_XV9ZA.cwA...\"  }  ```    If the conversation was started, an HTTP 201 status code is returned. HTTP 201 is the code that clients  will receive under most circumstances, as the typical use case is for a client to start a new conversation.  Under certain conditions -- specifically, when the client has a token scoped to a single conversation AND  when that conversation was started with a prior call to this URL -- this method will return HTTP 200 to signify  the request was acceptable but that no conversation was created (as it already existed).    You have 60 seconds to connect to the WebSocket URL. If the connection cannot be established during this time,  use the reconnect method below to generate a new stream URL.    This call is similar to ```/v3/directline/tokens/generate```. The difference is that the call to  ```/v3/directline/conversations``` starts the conversation, contacts the bot, and creates a streaming WebSocket  URL, none of which occur when generating a token.  * Call ```/v3/directline/conversations``` if you will distribute the token to client(s) and want them to    initiate the conversation.  * Call ```/v3/directline/conversations``` if you intend to start the conversation immediately.    ## Reconnecting to a conversation    If a client is using the WebSocket interface to receive messages but loses its connection, it may need to reconnect.  Reconnecting requires generating a new WebSocket stream URL, and this can be accomplished by sending a GET request  to the ```/v3/directline/conversations/{id}``` endpoint.    The ```watermark``` parameter is optional. If supplied, the conversation replays from the watermark,  guaranteeing no messages are lost. If ```watermark``` is omitted, only messages received after the reconnection  call (```GET /v3/directline/conversations/abc123```) are replayed.    ```  -- connect to directline.botframework.com --  GET /v3/directline/conversations/abc123?watermark=0000a-42 HTTP/1.1  Authorization: Bearer RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0y8qbOF5xPGfiCpg4Fv0y8qqbOF5x8qbOF5xn  [other headers]    -- response from directline.botframework.com --  HTTP/1.1 200 OK  [other headers]    {    \"conversationId\": \"abc123\",    \"token\": \"RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0y8qbOF5xPGfiCpg4Fv0y8qqbOF5x8qbOF5xn\",    \"streamUrl\": \"https://directline.botframework.com/v3/directline/conversations/abc123/stream?watermark=000a-4&t=RCurR_XV9ZA.cwA...\"  }  ```    You have 60 seconds to connect to the WebSocket stream URL. If the connection cannot be established during this  time, issue another reconnect request to get an updated stream URL.    ## Sending an Activity to the bot    Using the Direct Line 3.0 protocol, clients and bots may exchange many different Bot Framework v3 Activities,  including Message Activities, Typing Activities, and custom activities that the bot supports.    To send any one of these activities to the bot,    1. the client formulates the Activity according to the Activity schema (see below)  2. the client issues a POST message to ```/v3/directline/conversations/{id}/activities```  3. the service returns when the activity was delivered to the bot, with an HTTP status code reflecting the     bot's status code. If the POST was successful, the service returns a JSON payload containing the ID of the     Activity that was sent.    Example follows.    ```  -- connect to directline.botframework.com --  POST /v3/directline/conversations/abc123/activities HTTP/1.1  Authorization: Bearer RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0  [other headers]    {    \"type\": \"message\",    \"from\": {      \"id\": \"user1\"    },    \"text\": \"hello\"  }    -- response from directline.botframework.com --  HTTP/1.1 200 OK  [other headers]    {    \"id\": \"0001\"  }  ```    The client's Activity is available in the message retrieval path (either polling GET or WebSocket) and is not  returned inline.    The total time to POST a message to a Direct Line conversation is:    * Transit time to the Direct Line service,  * Internal processing time within Direct Line (typically less than 120ms)  * Transit time to the bot  * Processing time within the bot  * Transit time for HTTP responses to travel back to the client.    If the bot generates an error, that error will trigger an HTTP 502 error (\"Bad Gateway\") in  the ```POST /v3/directline/conversations/{id}/activities``` call.    ### Sending one or more attachments by URL    Clients may optionally send attachments, such as images or documents. If the client already has a URL for the  attachment, the simplest way to send it is to include the URL in the ```contentUrl``` field of an Activity  attachment object. This applies to HTTP, HTTPS, and ```data:``` URIs.    ### Sending a single attachment by upload    Often, clients have an image or document on a device but no URL that can be included in the activity.    To upload an attachment, POST a single attachment to  the ```/v3/directline/conversations/{conversationId}/upload``` endpoint. The ```Content-Type```  and ```Content-Disposition``` headers control the attachment's type and filename, respectively.    A user ID is required. Supply the ID of the user sending the attachment as a ```userId``` parameter in the URL.    If uploading a single attachment, a message activity is sent to the bot when the upload completes.    On completion, the service returns the ID of the activity that was sent.    ```  -- connect to directline.botframework.com --  POST /v3/directline/conversations/abc123/upload?userId=user1 HTTP/1.1  Authorization: Bearer RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0  Content-Type: image/jpeg  Content-Disposition: name=\"file\"; filename=\"badjokeeel.jpg\"  [other headers]    [JPEG content]    -- response from directline.botframework.com --  HTTP/1.1 200 OK  [other headers]    {    \"id\": \"0003\"  }  ```    ### Sending multiple attachments by upload    If uploading multiple attachments, use ```multipart/form-data``` as the content type and include each  attachment as a separate part. Each attachment's type and filename may be included in the ```Content-Type```  and ```Content-Disposition``` headers in each part.    An activity may be included by adding a part with content type of ```application/vnd.microsoft.activity```.  Other parts in the payload are attached to this activity before it is sent. If an Activity is not included,  an empty Activity is created as a wrapper for the attachments.    ```  -- connect to directline.botframework.com --  POST /v3/directline/conversations/abc123/upload?userId=user1 HTTP/1.1  Authorization: Bearer RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0  Content-Type: multipart/form-data; boundary=----DD4E5147-E865-4652-B662-F223701A8A89  [other headers]    ----DD4E5147-E865-4652-B662-F223701A8A89  Content-Type: image/jpeg  Content-Disposition: form-data; name=\"file\"; filename=\"badjokeeel.jpg\"  [other headers]    [JPEG content]    ----DD4E5147-E865-4652-B662-F223701A8A89  Content-Type: application/vnd.microsoft.activity  [other headers]    {    \"type\": \"message\",    \"from\": {      \"id\": \"user1\"    },    \"text\": \"Hey I just IM'd you\\n\\nand this is crazy\\n\\nbut here's my webhook\\n\\nso POST me maybe\"  }    ----DD4E5147-E865-4652-B662-F223701A8A89            -- response from directline.botframework.com --  HTTP/1.1 200 OK  [other headers]    {    \"id\": \"0004\"  }  ```    ## Receiving Activities from the bot    Direct Line 3.0 clients may choose from two different mechanisms for retrieving messages:    1. A **streaming WebSocket**, which pushes messages efficiently to clients.  2. A **polling GET** interface, which is available for clients unable to use WebSockets or for clients     retrieving the conversation history.    **Not all activities are available via the polling GET interface.** A table of activity availability follows.    |Activity type|Availability|  |-------------|--------|  |Message|Polling GET and WebSocket|  |Typing|WebSocket only|  |ConversationUpdate|Not sent/received via client|  |ContactRelationUpdate|Not supported in Direct Line|  |EndOfConversation|Polling GET and WebSocket|  |All other activity types|Polling GET and WebSocket|    ### Receiving Activities by WebSocket    To connect via WebSocket, a client uses the StreamUrl when starting a conversation. The stream URL is  preauthorized and does NOT require an Authorization header containing the client's secret or token.    ```  -- connect to wss://directline.botframework.com --  GET /v3/directline/conversations/abc123/stream?t=RCurR_XV9ZA.cwA...\" HTTP/1.1  Upgrade: websocket  Connection: upgrade  [other headers]    -- response from directline.botframework.com --  HTTP/1.1 101 Switching Protocols  [other headers]  ```    The Direct Line service sends the following messages:    * An **ActivitySet**, which contains one or more activities and a watermark (described below)  * An empty message, which the Direct Line service uses to ensure the connection is still valid  * Additional types, to be defined later. These types are identified by the properties in the JSON root.    ActivitySets contain messages sent by the bot and by all users. Example ActivitySet:    ```  {    \"activities\": [{      \"type\": \"message\",      \"channelId\": \"directline\",      \"conversation\": {        \"id\": \"abc123\"      },      \"id\": \"abc123|0000\",      \"from\": {        \"id\": \"user1\"      },      \"text\": \"hello\"    }],    \"watermark\": \"0000a-42\"  }  ```    Clients should keep track of the \"watermark\" value from each ActivitySet so they can use it on reconnect.  **Note** that a ```null``` or missing watermark should be ignored and should not overwrite a prior watermark  in the client.    Clients should ignore empty messages.    Clients may send their own empty messages to verify connectivity. The Direct Line service will ignore these.    The service may forcibly close the connection under certain conditions. If the client has not received an  EndOfConversation activity, it may reconnect by issuing a GET request to the conversation endpoint to get a  new stream URL (see above).    The WebSocket stream contains live updates and very recent messages (since the call to get the WebSocket call  was issued) but it does not include messages sent prior to the most recent POST  to ```/v3/directline/conversations/{id}```. To retrieve messages sent earlier in the conversation, use the  GET mechanism below.    ### Receiving Activities by GET    The GET mechanism is useful for clients who are unable to use the WebSocket, or for clients wishing to retrieve  the conversation history.    To retrieve messages, issue a GET call to the conversation endpoint. Optionally supply a watermark, indicating  the most recent message seen. The watermark field accompanies all GET/WebSocket messages as a property in the  ActivitySet.    ```  -- connect to directline.botframework.com --  GET /v3/directline/conversations/abc123/activities?watermark=0001a-94 HTTP/1.1  Authorization: Bearer RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0  [other headers]    -- response from directline.botframework.com --  HTTP/1.1 200 OK  [other headers]    {    \"activities\": [{      \"type\": \"message\",      \"channelId\": \"directline\",      \"conversation\": {        \"id\": \"abc123\"      },      \"id\": \"abc123|0000\",      \"from\": {        \"id\": \"user1\"      },      \"text\": \"hello\"    }, {      \"type\": \"message\",      \"channelId\": \"directline\",      \"conversation\": {        \"id\": \"abc123\"      },      \"id\": \"abc123|0001\",      \"from\": {        \"id\": \"bot1\"      },      \"text\": \"Nice to see you, user1!\"    }],    \"watermark\": \"0001a-95\"  }  ```    Clients should page through the available activities by advancing the ```watermark``` value until no activities  are returned.      ### Timing considerations     Most clients wish to retain a complete message history. Even though Direct Line is a multi-part protocol with  potential timing gaps, the protocol and service is designed to make it easy to build a reliable client.    1. The ```watermark``` field sent in the WebSocket stream and GET response is reliable. You will not miss     messages as long as you replay the watermark verbatim.  2. When starting a conversation and connecting to the WebSocket stream, any Activities sent after the POST but     before the socket is opened are replayed before new messages.  3. When refreshing history by GET call while connected to the WebSocket, Activities may be duplicated across both     channels. Keeping a list of all known Activity IDs will allow you to reject duplicate messages should they occur.    Clients using the polling GET interface should choose a polling interval that matches their intended use.    * Service-to-service applications often use a polling interval of 5s or 10s.  * Client-facing applications often use a polling interval of 1s, and fire an additional request ~300ms after    every message the client sends to rapidly pick up a bot's response. This 300ms delay should be adjusted    based on the bot's speed and transit time.    ## Ending a conversation    Either a client or a bot may signal the end of a DirectLine conversation. This operation halts communication  and prevents the bot and the client from sending messages. Messages may still be retrieved via the GET mechanism.  Sending this messages is as simple as POSTing an EndOfConversation activity.    ```  -- connect to directline.botframework.com --  POST /v3/directline/conversations/abc123/activities HTTP/1.1  Authorization: Bearer RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0  [other headers]    {    \"type\": \"endOfConversation\",    \"from\": {      \"id\": \"user1\"    }  }    -- response from directline.botframework.com --  HTTP/1.1 200 OK  [other headers]    {    \"id\": \"0004\"  }  ```    ## REST API errors    HTTP calls to the Direct Line service follow standard HTTP error conventions:    * 2xx status codes indicate success. (Direct Line 3.0 uses 200 and 201.)  * 4xx status codes indicate an error in your request.    * 401 indicates a missing or malformed Authorization header (or URL token, in calls where a token parameter      is allowed).    * 403 indicates an unauthorized client.      * If calling with a valid but expired token, the ```code``` field is set to ```TokenExpired```.    * 404 indicates a missing path, site, conversation, etc.  * 5xx status codes indicate a service-side error.    * 500 indicates an error inside the Direct Line service.    * 502 indicates an error was returned by the bot. **This is a common error code.**  * 101 is used in the WebSocket connection path, although this is likely handled by your WebSocket client.    When an error message is returned, error detail may be present in a JSON response. Look for an ```error```  property with ```code``` and ```message``` fields.    ```  -- connect to directline.botframework.com --  POST /v3/directline/conversations/abc123/activities HTTP/1.1  [detail omitted]    -- response from directline.botframework.com --  HTTP/1.1 502 Bad Gateway  [other headers]    {    \"error\": {      \"code\": \"BotRejectedActivity\",      \"message\": \"Failed to send activity: bot returned an error\"    }  }  ```    The contents of the ```message``` field may change. The HTTP status code and values in the ```code```  property are stable.    # Schema    The Direct Line 3.0 schema is identical to the Bot Framework v3 schema.    When a bot sends an Activity to a client through Direct Line:    * attachment cards are preserved,  * URLs for uploaded attachments are hidden with a private link, and  * the ```channelData``` property is preserved without modification.    When a client sends an Activity to a bot through Direct Line:    * the ```type``` property contains the kind of activity you are sending (typically ```message```),  * the ```from``` property must be populated with a user ID, chosen by your client,  * attachments may contain URLs to existing resources or URLs uploaded through the Direct Line attachment    endpoint, and  * the ```channelData``` property is preserved without modification.    Clients and bots may send Activities of any type, including Message Activities, Typing Activities, and  custom Activity types.    Clients may send a single Activity at a time.    ```  {    \"type\": \"message\",    \"channelId\": \"directline\",    \"from\": {      \"id\": \"user1\"    },    \"text\": \"hello\"  }  ```    Clients receive multiple Activities as part of an ActivitySet. The ActivitySet has an array of activities  and a watermark field.    ```  {    \"activities\": [{      \"type\": \"message\",      \"channelId\": \"directline\",      \"conversation\": {        \"id\": \"abc123\"      },      \"id\": \"abc123|0000\",      \"from\": {        \"id\": \"user1\"      },      \"text\": \"hello\"    }],    \"watermark\": \"0000a-42\"  }  ```    # Libraries for the Direct Line API    The Direct Line API is designed to be coded directly, but the Bot Framework includes libraries and controls that  help you to embed Direct-Line-powered bots into your application.    * The [Bot Framework Web Chat control](https://github.com/Microsoft/BotFramework-WebChat) is an easy way to embed    the Direct Line protocol into a webpage.  * [Direct Line Nuget package](https://www.nuget.org/packages/Microsoft.Bot.Connector.DirectLine) with libraries for    .Net 4.5, UWP, and .Net Standard.  * [DirectLineJs](https://github.com/Microsoft/BotFramework-DirectLineJs), also available on    [NPM](https://www.npmjs.com/package/botframework-directlinejs)  * You may generate your own from the [Direct Line Swagger file](swagger.json)    Our [BotBuilder-Samples GitHub repo](https://github.com/Microsoft/BotBuilder-Samples) also contains samples for    [C#](https://github.com/Microsoft/BotBuilder-Samples/tree/master/CSharp/core-DirectLine) and    [JavaScript](https://github.com/Microsoft/BotBuilder-Samples/tree/master/Node/core-DirectLine).

    The version of the OpenAPI document: v3
    Contact: botframework@microsoft.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from direct_line.models.attachment import Attachment
from direct_line.models.channel_account import ChannelAccount
from direct_line.models.conversation_account import ConversationAccount
from direct_line.models.conversation_reference import ConversationReference
from direct_line.models.entity import Entity
from direct_line.models.message_reaction import MessageReaction
from direct_line.models.semantic_action import SemanticAction
from direct_line.models.suggested_actions import SuggestedActions
from direct_line.models.text_highlight import TextHighlight
from typing import Optional, Set
from typing_extensions import Self

class Activity(BaseModel):
    """
    An Activity is the basic communication type for the Bot Framework 3.0 protocol.
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="Contains the activity type.")
    id: Optional[StrictStr] = Field(default=None, description="Contains an ID that uniquely identifies the activity on the channel.")
    timestamp: Optional[datetime] = Field(default=None, description="Contains the date and time that the message was sent, in UTC, expressed in ISO-8601 format.")
    local_timestamp: Optional[datetime] = Field(default=None, description="Contains the local date and time of the message, expressed in ISO-8601 format.  For example, 2016-09-23T13:07:49.4714686-07:00.", alias="localTimestamp")
    local_timezone: Optional[StrictStr] = Field(default=None, description="Contains the name of the local timezone of the message, expressed in IANA Time Zone database format.  For example, America/Los_Angeles.", alias="localTimezone")
    service_url: Optional[StrictStr] = Field(default=None, description="Contains the URL that specifies the channel's service endpoint. Set by the channel.", alias="serviceUrl")
    channel_id: Optional[StrictStr] = Field(default=None, description="Contains an ID that uniquely identifies the channel. Set by the channel.", alias="channelId")
    var_from: Optional[ChannelAccount] = Field(default=None, alias="from")
    conversation: Optional[ConversationAccount] = None
    recipient: Optional[ChannelAccount] = None
    text_format: Optional[StrictStr] = Field(default=None, description="Format of text fields Default:markdown", alias="textFormat")
    attachment_layout: Optional[StrictStr] = Field(default=None, description="The layout hint for multiple attachments. Default: list.", alias="attachmentLayout")
    members_added: Optional[List[ChannelAccount]] = Field(default=None, description="The collection of members added to the conversation.", alias="membersAdded")
    members_removed: Optional[List[ChannelAccount]] = Field(default=None, description="The collection of members removed from the conversation.", alias="membersRemoved")
    reactions_added: Optional[List[MessageReaction]] = Field(default=None, description="The collection of reactions added to the conversation.", alias="reactionsAdded")
    reactions_removed: Optional[List[MessageReaction]] = Field(default=None, description="The collection of reactions removed from the conversation.", alias="reactionsRemoved")
    topic_name: Optional[StrictStr] = Field(default=None, description="The updated topic name of the conversation.", alias="topicName")
    history_disclosed: Optional[StrictBool] = Field(default=None, description="Indicates whether the prior history of the channel is disclosed.", alias="historyDisclosed")
    locale: Optional[StrictStr] = Field(default=None, description="A locale name for the contents of the text field.  The locale name is a combination of an ISO 639 two- or three-letter culture code associated with a language  and an ISO 3166 two-letter subculture code associated with a country or region.  The locale name can also correspond to a valid BCP-47 language tag.")
    text: Optional[StrictStr] = Field(default=None, description="The text content of the message.")
    speak: Optional[StrictStr] = Field(default=None, description="The text to speak.")
    input_hint: Optional[StrictStr] = Field(default=None, description="Indicates whether your bot is accepting,  expecting, or ignoring user input after the message is delivered to the client.", alias="inputHint")
    summary: Optional[StrictStr] = Field(default=None, description="The text to display if the channel cannot render cards.")
    suggested_actions: Optional[SuggestedActions] = Field(default=None, alias="suggestedActions")
    attachments: Optional[List[Attachment]] = Field(default=None, description="Attachments")
    entities: Optional[List[Entity]] = Field(default=None, description="Represents the entities that were mentioned in the message.")
    channel_data: Optional[Dict[str, Any]] = Field(default=None, description="Contains channel-specific content.", alias="channelData")
    action: Optional[StrictStr] = Field(default=None, description="Indicates whether the recipient of a contactRelationUpdate was added or removed from the sender's contact list.")
    reply_to_id: Optional[StrictStr] = Field(default=None, description="Contains the ID of the message to which this message is a reply.", alias="replyToId")
    label: Optional[StrictStr] = Field(default=None, description="A descriptive label for the activity.")
    value_type: Optional[StrictStr] = Field(default=None, description="The type of the activity's value object.", alias="valueType")
    value: Optional[Dict[str, Any]] = Field(default=None, description="A value that is associated with the activity.")
    name: Optional[StrictStr] = Field(default=None, description="The name of the operation associated with an invoke or event activity.")
    relates_to: Optional[ConversationReference] = Field(default=None, alias="relatesTo")
    code: Optional[StrictStr] = Field(default=None, description="The a code for endOfConversation activities that indicates why the conversation ended.")
    expiration: Optional[datetime] = Field(default=None, description="The time at which the activity should be considered to be \"expired\" and should not be presented to the recipient.")
    importance: Optional[StrictStr] = Field(default=None, description="The importance of the activity.")
    delivery_mode: Optional[StrictStr] = Field(default=None, description="A delivery hint to signal to the recipient alternate delivery paths for the activity.  The default delivery mode is \"default\".", alias="deliveryMode")
    listen_for: Optional[List[StrictStr]] = Field(default=None, description="List of phrases and references that speech and language priming systems should listen for", alias="listenFor")
    text_highlights: Optional[List[TextHighlight]] = Field(default=None, description="The collection of text fragments to highlight when the activity contains a ReplyToId value.", alias="textHighlights")
    semantic_action: Optional[SemanticAction] = Field(default=None, alias="semanticAction")
    __properties: ClassVar[List[str]] = ["type", "id", "timestamp", "localTimestamp", "localTimezone", "serviceUrl", "channelId", "from", "conversation", "recipient", "textFormat", "attachmentLayout", "membersAdded", "membersRemoved", "reactionsAdded", "reactionsRemoved", "topicName", "historyDisclosed", "locale", "text", "speak", "inputHint", "summary", "suggestedActions", "attachments", "entities", "channelData", "action", "replyToId", "label", "valueType", "value", "name", "relatesTo", "code", "expiration", "importance", "deliveryMode", "listenFor", "textHighlights", "semanticAction"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Activity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of var_from
        if self.var_from:
            _dict['from'] = self.var_from.to_dict()
        # override the default output from pydantic by calling `to_dict()` of conversation
        if self.conversation:
            _dict['conversation'] = self.conversation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recipient
        if self.recipient:
            _dict['recipient'] = self.recipient.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in members_added (list)
        _items = []
        if self.members_added:
            for _item_members_added in self.members_added:
                if _item_members_added:
                    _items.append(_item_members_added.to_dict())
            _dict['membersAdded'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in members_removed (list)
        _items = []
        if self.members_removed:
            for _item_members_removed in self.members_removed:
                if _item_members_removed:
                    _items.append(_item_members_removed.to_dict())
            _dict['membersRemoved'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in reactions_added (list)
        _items = []
        if self.reactions_added:
            for _item_reactions_added in self.reactions_added:
                if _item_reactions_added:
                    _items.append(_item_reactions_added.to_dict())
            _dict['reactionsAdded'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in reactions_removed (list)
        _items = []
        if self.reactions_removed:
            for _item_reactions_removed in self.reactions_removed:
                if _item_reactions_removed:
                    _items.append(_item_reactions_removed.to_dict())
            _dict['reactionsRemoved'] = _items
        # override the default output from pydantic by calling `to_dict()` of suggested_actions
        if self.suggested_actions:
            _dict['suggestedActions'] = self.suggested_actions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item_attachments in self.attachments:
                if _item_attachments:
                    _items.append(_item_attachments.to_dict())
            _dict['attachments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in entities (list)
        _items = []
        if self.entities:
            for _item_entities in self.entities:
                if _item_entities:
                    _items.append(_item_entities.to_dict())
            _dict['entities'] = _items
        # override the default output from pydantic by calling `to_dict()` of relates_to
        if self.relates_to:
            _dict['relatesTo'] = self.relates_to.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in text_highlights (list)
        _items = []
        if self.text_highlights:
            for _item_text_highlights in self.text_highlights:
                if _item_text_highlights:
                    _items.append(_item_text_highlights.to_dict())
            _dict['textHighlights'] = _items
        # override the default output from pydantic by calling `to_dict()` of semantic_action
        if self.semantic_action:
            _dict['semanticAction'] = self.semantic_action.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Activity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "id": obj.get("id"),
            "timestamp": obj.get("timestamp"),
            "localTimestamp": obj.get("localTimestamp"),
            "localTimezone": obj.get("localTimezone"),
            "serviceUrl": obj.get("serviceUrl"),
            "channelId": obj.get("channelId"),
            "from": ChannelAccount.from_dict(obj["from"]) if obj.get("from") is not None else None,
            "conversation": ConversationAccount.from_dict(obj["conversation"]) if obj.get("conversation") is not None else None,
            "recipient": ChannelAccount.from_dict(obj["recipient"]) if obj.get("recipient") is not None else None,
            "textFormat": obj.get("textFormat"),
            "attachmentLayout": obj.get("attachmentLayout"),
            "membersAdded": [ChannelAccount.from_dict(_item) for _item in obj["membersAdded"]] if obj.get("membersAdded") is not None else None,
            "membersRemoved": [ChannelAccount.from_dict(_item) for _item in obj["membersRemoved"]] if obj.get("membersRemoved") is not None else None,
            "reactionsAdded": [MessageReaction.from_dict(_item) for _item in obj["reactionsAdded"]] if obj.get("reactionsAdded") is not None else None,
            "reactionsRemoved": [MessageReaction.from_dict(_item) for _item in obj["reactionsRemoved"]] if obj.get("reactionsRemoved") is not None else None,
            "topicName": obj.get("topicName"),
            "historyDisclosed": obj.get("historyDisclosed"),
            "locale": obj.get("locale"),
            "text": obj.get("text"),
            "speak": obj.get("speak"),
            "inputHint": obj.get("inputHint"),
            "summary": obj.get("summary"),
            "suggestedActions": SuggestedActions.from_dict(obj["suggestedActions"]) if obj.get("suggestedActions") is not None else None,
            "attachments": [Attachment.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None,
            "entities": [Entity.from_dict(_item) for _item in obj["entities"]] if obj.get("entities") is not None else None,
            "channelData": obj.get("channelData"),
            "action": obj.get("action"),
            "replyToId": obj.get("replyToId"),
            "label": obj.get("label"),
            "valueType": obj.get("valueType"),
            "value": obj.get("value"),
            "name": obj.get("name"),
            "relatesTo": ConversationReference.from_dict(obj["relatesTo"]) if obj.get("relatesTo") is not None else None,
            "code": obj.get("code"),
            "expiration": obj.get("expiration"),
            "importance": obj.get("importance"),
            "deliveryMode": obj.get("deliveryMode"),
            "listenFor": obj.get("listenFor"),
            "textHighlights": [TextHighlight.from_dict(_item) for _item in obj["textHighlights"]] if obj.get("textHighlights") is not None else None,
            "semanticAction": SemanticAction.from_dict(obj["semanticAction"]) if obj.get("semanticAction") is not None else None
        })
        return _obj


