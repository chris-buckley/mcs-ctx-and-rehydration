## 1. Introduction: Understanding Microsoft Copilot Studio

*Research carried out by Christopher Buckley - Microsoft ISE*

## Table of Contents
1.  [Introduction: Understanding Microsoft Copilot Studio](#introduction-understanding-microsoft-copilot-studio)
2.  [Core Architecture and Key Components](#core-architecture-and-key-components)
3.  [API Ecosystem for Communication and Extensibility](#api-ecosystem-for-communication-and-extensibility)

    *   [Key Direct Line API Information](#key-direct-line-api-information)

        *   [Secrets and tokens](#secrets-and-tokens)
        *   [Refreshing a Token](#refreshing-a-token)
        *   [Starting a Conversation](#starting-a-conversation)
        *   [Conversation History Timeframes](#conversation-history-timeframes)

    *   [Detailed Overview of Direct Line API 3.0](#detailed-overview-of-direct-line-api-30)

        *   [Authentication: Secrets and Tokens](#authentication-secrets-and-tokens)
        *   [REST calls for a Direct Line conversation](#rest-calls-for-a-direct-line-conversation)
        *   [REST API errors](#rest-api-errors)
        *   [Schema](#schema)
        *   [Libraries for the Direct Line API](#libraries-for-the-direct-line-api)

4.  [The Intelligence Engine: AI Models, NLU, and Orchestration](#the-intelligence-engine-ai-models-nlu-and-orchestration)

    4.1. [Natural Language Understanding (NLU)](#41-natural-language-understanding-nlu)

    4.2. [Generative AI and Azure OpenAI GPT Models](#42-generative-ai-and-azure-openai-gpt-models)

    4.3. [Dialog Management and Orchestration](#43-dialog-management-and-orchestration)
    
5.  [Data Flow and Channel Communication](#data-flow-and-channel-communication)
    *   Channel Communication Flow Comparison
    *   Context Passing
6.  [Microsoft Dataverse: The Operational Backbone](#microsoft-dataverse-the-operational-backbone)
    *   Illustrative Dataverse Tables for Copilot Studio Components
7.  [Data Storage, Retention, and Security](#data-storage-retention-and-security)

    7.1. [Storage Locations and Data Types](#71-storage-locations-and-data-types)

    7.2. [Data Retention Policies](#72-data-retention-policies)

    7.3. [Transient vs. Persistent Data Summary](#73-transient-vs-persistent-data-summary)

    7.4. [Security of Data](#74-security-of-data)
    
8.  [Conclusion: A Synthesized View of Copilot Studio Operations](#conclusion-a-synthesized-view-of-copilot-studio-operations)

Microsoft Copilot Studio, formerly known as Power Virtual Agents, is an enterprise-grade, cloud-based conversational AI platform that empowers organizations to design, build, and deploy sophisticated AI agents (also referred to as copilots or bots) [Copilot Studio architecture key concepts and solution ideas - Power Platform](https://learn.microsoft.com/en-us/power-platform/architecture/products/copilot-studio). It operates as a sophisticated orchestrator, harmonizing a complex ecosystem of Microsoft services, including the Power Platform, Azure AI, and Azure Bot Services, to deliver its comprehensive capabilities [Copilot Studio architecture key concepts and solution ideas - Power Platform](https://learn.microsoft.com/en-us/power-platform/architecture/products/copilot-studio). While presented as a graphical, low-code environment for creating custom agents and extending Microsoft 365 Copilot [Copilot Studio architecture key concepts and solution ideas - Power Platform](https://learn.microsoft.com/en-us/power-platform/architecture/products/copilot-studio), its enterprise strength is unlocked through deep integration points that allow for pro-code extensions, catering to both citizen developers and seasoned programmers [Copilot Studio architecture key concepts and solution ideas - Power Platform](https://learn.microsoft.com/en-us/power-platform/architecture/products/copilot-studio).

This report provides a fused analysis of Copilot Studio's data flow, communication architecture, API interactions, underlying AI models, channel communication pathways, Microsoft Dataverse integration, and data storage mechanisms, based on the findings of the provided research papers.

## 2. Core Architecture and Key Components

Microsoft Copilot Studio is delivered as a Software-as-a-Service (SaaS) offering, deeply embedded within the Microsoft Power Platform and intricately connected with Azure AI and Azure Bot Services [Microsoft Copilot Studio on Azure | Microsoft Azure](https://azure.microsoft.com/en-us/products/copilot-studio). Its architecture comprises several key elements:

*   An **authoring environment** for designing conversational logic and user interactions [Copilot Studio architecture key concepts and solution ideas - Power Platform](https://learn.microsoft.com/en-us/power-platform/architecture/products/copilot-studio).
*   A **runtime environment** responsible for executing the deployed agents [Copilot Studio architecture key concepts and solution ideas - Power Platform](https://learn.microsoft.com/en-us/power-platform/architecture/products/copilot-studio). This runtime is essentially a hosted Bot Framework runtime, managed by Microsoft [Microsoft Docs – Bot Framework Connector API and Azure Bot Service](https://learn.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-connector-api-reference?view=azure-bot-service-4.0).
*   An **AI engine** that provides Natural Language Understanding (NLU) and generative AI capabilities [Copilot Studio architecture key concepts and solution ideas - Power Platform](https://learn.microsoft.com/en-us/power-platform/architecture/products/copilot-studio).
*   Robust integration with **Microsoft Dataverse** for data management, solution packaging, and as a knowledge source [Copilot Studio architecture key concepts and solution ideas - Power Platform](https://learn.microsoft.com/en-us/power-platform/architecture/products/copilot-studio).
*   Connections to **Microsoft Graph** for accessing enterprise data [Copilot Studio architecture key concepts and solution ideas - Power Platform](https://learn.microsoft.com/en-us/power-platform/architecture/products/copilot-studio).

The interaction with **Azure Bot Service** and the broader **Bot Framework** is fundamental. Azure Bot Service provides the foundational infrastructure for managing bot resources and connecting agents to numerous communication channels [Microsoft Copilot Studio on Azure | Microsoft Azure](https://azure.microsoft.com/en-us/products/copilot-studio). Agents created in Copilot Studio are, in essence, sophisticated manifestations of Bot Framework bots [Microsoft Copilot Studio on Azure | Microsoft Azure](https://azure.microsoft.com/en-us/products/copilot-studio).

Central to multi-channel communication is the **Bot Framework Connector Service**. This service acts as the primary messaging pipeline, facilitating information exchange between a Copilot Studio agent and various channels (e.g., Microsoft Teams, web chat) [Bot Framework Connector service REST API reference - Azure documentation](https://docs.azure.cn/en-us/bot-service/rest-api/bot-framework-rest-connector-api-reference?view=azure-bot-service-4.0). It uses industry-standard REST and JSON over HTTPS, employing a standardized **Activity object** to encapsulate messages and conversational events [Bot Framework Connector service REST API reference - Azure documentation](https://docs.azure.cn/en-us/bot-service/rest-api/bot-framework-rest-connector-api-reference?view=azure-bot-service-4.0). The Connector Service translates protocols between the agent and channel-specific APIs [Bot Framework Connector service REST API reference - Azure documentation](https://docs.azure.cn/en-us/bot-service/rest-api/bot-framework-rest-connector-api-reference?view=azure-bot-service-4.0).

The general flow involves:
1.  A user interacting through a client interface (e.g., Teams, web chat).
2.  The channel connector sending the user's message as an Activity object to the Azure Bot Service.
3.  Azure Bot Service forwarding the activity to the bot's messaging endpoint.
4.  The Copilot Studio agent's logic (Bot Framework Runtime) processing the message, utilizing NLU and potentially generative AI.
5.  The agent crafting a response Activity, sent back via Azure Bot Service to the user's channel.

Copilot Studio abstracts much of this complexity, providing a scalable, enterprise-grade bot hosting environment automatically [Microsoft Copilot Studio on Azure | Microsoft Azure](https://azure.microsoft.com/en-us/products/copilot-studio).

## 3. API Ecosystem for Communication and Extensibility

Copilot Studio utilizes a sophisticated ecosystem of APIs for communication, external service integration, and custom client interactions.

| API Name                                 | Core Function in Copilot Studio                                                                                                | Key Communication Protocols/Formats | Authentication Methods Supported                                                                                             | Typical Use Cases in Copilot Studio                                                                                                                              |
| :--------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------- | :---------------------------------- | :--------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Direct Line API**                      | Enables direct, stateful communication between custom clients (web, mobile) and the Copilot Studio agent.                      | REST/JSON, Activity objects, WebSockets | Secret-based, Token-based (generated from secret), User-specific tokens via external IdP (e.g., Microsoft Entra ID OAuth) [Connecting to agents in Copilot Studio through Direct Line channel](https://community.powerplatform.com/forums/thread/details/?threadid=4d0f9b82-80cf-ef11-b8e8-6045bdd9204f) | Building custom user interfaces, embedding agents in mobile apps, scenarios requiring fine-grained control over conversation UX.                                 |
| **Bot Framework Connector Service API**  | Relays messages and activities between Copilot Studio agents and configured standard channels (e.g., Teams, Web Chat, Slack).    | REST/JSON, Activity objects         | Channel-specific authentication, often integrated with the channel's identity system (e.g., Entra ID for Teams) [Bot Framework Connector service REST API reference - Azure documentation](https://docs.azure.cn/en-us/bot-service/rest-api/bot-framework-rest-connector-api-reference?view=azure-bot-service-4.0)      | Standard channel integrations where Copilot Studio manages the channel connection.                                                                               |
| **Azure Bot Service API**                | Management API for Azure Bot resources. Leveraged by Copilot Studio for provisioning and managing underlying bot infrastructure. | Azure Resource Manager (ARM) APIs   | Microsoft Entra ID (for management operations)                                                                               | Underlying infrastructure management by the Copilot Studio service; not directly used by agent authors for message exchange.                                   |
| **Bot Framework SDK**                    | Libraries for building the core logic of bots, including skills that can extend Copilot Studio agents.                         | Language-specific (e.g., C#, JS) [Bot Framework SDK documentation - Bot Service | Microsoft Learn](https://learn.microsoft.com/en-us/azure/bot-service/index-bf-sdk?view=azure-bot-service-4.0)    | Depends on the skill's implementation; can integrate with OAuth providers.                                                       | Developing Bot Framework Skills for complex custom logic, extending agent capabilities beyond no-code/low-code authoring [Bot Framework SDK documentation - Bot Service | Microsoft Learn](https://learn.microsoft.com/en-us/azure/bot-service/index-bf-sdk?view=azure-bot-service-4.0). |
| **Power Automate Connector for Copilot Studio** | Enables Copilot Studio agents to invoke Power Automate flows as actions.                                                       | Proprietary (within Power Platform) | Uses Power Platform connections, which can be user-based or service principal-based.                                         | Automating backend processes, integrating with LOB systems, performing complex data manipulations via flows [Create a Power Automate flow - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-flow-create).        |

*   **Direct Line API:** This RESTful API provides a direct, stateful communication channel to a Copilot Studio agent [Connecting to agents in Copilot Studio through Direct Line channel](https://community.powerplatform.com/forums/thread/details/?threadid=4d0f9b82-80cf-ef11-b8e8-6045bdd9204f). It's key for custom UIs, allowing granular control. Authentication typically involves obtaining a token by exchanging a Direct Line secret [Configure web and Direct Line channel security - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configure-web-security). For security, it's vital to protect the Direct Line secret by using a backend service for token generation [Configure web and Direct Line channel security - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configure-web-security).

    The Direct Line API facilitates direct communication between custom client applications (e.g., web, mobile, desktop) and a bot. It is specifically designed for integrating bots into bespoke user interfaces, distinct from standard channel integrations handled by the Connector API. Direct Line establishes a dedicated channel using REST and JSON over HTTPS, with its own unique endpoints, authentication, and communication patterns. Version 3.0 is recommended for new projects.

    Its primary use case involves scenarios requiring custom UIs, offering complete control over the user experience, or integrating bot capabilities into proprietary applications (e.g., embedded web chat, mobile app features, voice interfaces for kiosks). The Bot Framework Web Chat control is a notable client built using Direct Line.

    Communication via Direct Line involves the client initiating a conversation (often obtaining a token and `conversationId`), sending activities to the bot via HTTPS POST, and receiving activities from the bot. For receiving, Direct Line 3.0 offers efficient WebSocket streaming (preferred for real-time updates) or traditional HTTP GET polling. The Direct Line service routes these activities between the client and the bot, with the bot processing activities as it would from any other channel.

    Authentication in Direct Line is client-focused, verifying the client application's authorization. It primarily uses a **Direct Line Secret** (a static master key for the Direct Line channel configuration) or a **Direct Line Token** (a short-lived credential for a single conversation, obtained by exchanging the Secret). Using tokens is highly recommended for client-side applications to enhance security by limiting credential scope and lifetime, though it requires backend logic for token generation and refresh. Direct Line also supports Enhanced Authentication, restricting token generation to trusted origins. This model decouples client access from the bot's core Azure AD identity, improving security for custom integrations.

    Key capabilities of Direct Line API 3.0 include starting conversations, sending/receiving standard Bot Framework Activity objects, managing authentication tokens, and handling file uploads. It ensures that rich content like cards and `channelData` are passed through, with the custom client responsible for rendering. Clients should be aware of potential service limitations like payload size and rate limits.

### Key Direct Line API Information
    <!-- This section incorporates the provided extra content about Direct Line -->

#### Secrets and tokens

##### DIRECT_LINE_SECRET
    (source)[https://learn.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-direct-line-3-0-authentication?view=azure-bot-service-4.0]
    A DIRECT_LINE_SECRET is a master key that can be used to access any conversation that belongs to the associated bot.
    A DIRECT_LINE_SECRET can also be used to obtain a token.
    A DIRECT_LINE_SECRET does not expire.

    A Direct Line token is a key that can be used to access a single conversation.
    A token expires but can be refreshed.

##### DIRECT_LINE_CONVERSATION_TOKEN
    (source)[https://learn.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-direct-line-3-0-authentication?view=azure-bot-service-4.0]

    Obtaining a token:
    REQUEST
    ```
    POST https://directline.botframework.com/v3/directline/tokens/generate
    Authorization: Bearer DIRECT_LINE_SECRET
    ```

    RESPONSE
    ```json
    {
      "conversationId": "abc123",
      "token": "RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0y8qbOF5xPGfiCpg4Fv0y8qqbOF5x8qbOF5xn",
      "expires_in": 1800
    }
    ```

#### Refreshing a Token
    A Direct Line token can be refreshed an unlimited number of times as long as it hasn't expired.
    An expired token can't be refreshed.
    To refresh a Direct Line token, issue this request:

    REQUEST
    ```
    POST https://directline.botframework.com/v3/directline/tokens/refresh
    Authorization: Bearer TOKEN_TO_BE_REFRESHED
    ```

#### Starting a Conversation
    Whenever you start a conversation you can also get a token.
    The difference is essentially the Generate Token operation doesn't start the conversation, doesn't contact the bot, and doesn't create a streaming WebSocket URL.

    REQUEST
    ```
    POST https://directline.botframework.com/v3/directline/conversations
    Authorization: Bearer SECRET_OR_TOKEN
    ```

    RESPONSE
    ```json
    {
      "conversationId": "abc123",
      "token": "RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0y8qbOF5xPGfiCpg4Fv0y8qqbOF5x8qbOF5xn",
      "expires_in": 1800,
      "streamUrl": "https://directline.botframework.com/v3/directline/conversations/abc123/stream?t=RCurR_XV9ZA.cwA..."
    }
    ```

#### Conversation History Timeframes
    <!-- This sub-section details the storage duration for Direct Line conversation data. -->
    For the standard Direct Line channel, individual messages are stored for up to 24 hours, and the record of the conversation (conversation metadata) is stored for up to 21 days after the last message in the conversation.

### Detailed Overview of Direct Line API 3.0
    The Direct Line API is a simple REST API for connecting directly to a single bot. This API is intended for developers writing their own client applications, web chat controls, mobile apps, or service-to-service applications that will talk to their bot.

    Within the Direct Line API, you will find:

    * An **authentication mechanism** using standard secret/token patterns
    * The ability to **send** messages from your client to your bot via an HTTP POST message
    * The ability to **receive** messages by **WebSocket** stream, if you choose
    * The ability to **receive** messages by **polling HTTP GET**, if you choose
    * A stable **schema**, even if your bot changes its protocol version

    Direct Line 1.1 and 3.0 are both available and supported. This document describes Direct Line 3.0. For information on Direct Line 1.1, visit the [Direct Line 1.1 reference documentation](/en-us/restapi/directline/).

#### Authentication: Secrets and Tokens

    Direct Line allows you to authenticate all calls with either a secret (retrieved from the Direct Line channel configuration page) or a token (which you may get at runtime by converting your secret).

    A Direct Line **secret** is a master key that can access any conversation, and create tokens. Secrets do not expire.

    A Direct Line **token** is a key for a single conversation. It expires but can be refreshed.

    If you're writing a service-to-service application, using the secret may be simplest. If you're writing an application where the client runs in a web browser or mobile app, you may want to exchange your secret for a token, which only works for a single conversation and will expire unless refreshed. You choose which security model works best for you.

    Your secret or token is communicated in the ```Authorization``` header of every call, with the Bearer scheme. Example below.

    ```
    -- connect to directline.botframework.com --
    POST /v3/directline/conversations/abc123/activities HTTP/1.1
    Authorization: Bearer RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0
    [other HTTP headers, omitted]
    ```

    You may notice that your Direct Line client credentials are different from your bot's credentials. This is intentional, and it allows you to revise your keys independently and lets you share client tokens without disclosing your bot's password.

##### Exchanging a secret for a token

    This operation is optional. Use this step if you want to prevent clients from accessing conversations they aren't participating in.

    To exchange a secret for a token, POST to /v3/directline/tokens/generate with your secret in the auth header and no HTTP body.

    ```
    -- connect to directline.botframework.com --
    POST /v3/directline/tokens/generate HTTP/1.1
    Authorization: Bearer RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0
    [other headers]

    -- response from directline.botframework.com --
    HTTP/1.1 200 OK
    [other headers]

    {
      "conversationId": "abc123",
      "token": "RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0y8qbOF5xPGfiCpg4Fv0y8qqbOF5x8qbOF5xn",
      "expires_in": 1800
    }
    ```

    If successful, the response is a token suitable for one conversation. The token expires in the seconds indicated in the ```expires_in``` field (30 minutes in the example above) and must be refreshed before then to remain useful.

    This call is similar to ```/v3/directline/conversations```. The difference is that the call to ```/v3/directline/tokens/generate``` does not start the conversation, does not contact the bot, and does not create a streaming WebSocket URL.
    * Call ```/v3/directline/conversations``` if you will distribute the token to client(s) and want them to
      initiate the conversation.
    * Call ```/v3/directline/conversations``` if you intend to start the conversation immediately.

##### Refreshing a token

    A token may be refreshed an unlimited number of times unless it is expired.

    To refresh a token, POST to /v3/directline/tokens/refresh. This method is valid only for unexpired tokens.

    ```
    -- connect to directline.botframework.com --
    POST /v3/directline/tokens/refresh HTTP/1.1
    Authorization: Bearer RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0y8qbOF5xPGfiCpg4Fv0y8qqbOF5x8qbOF5xn
    [other headers]

    -- response from directline.botframework.com --
    HTTP/1.1 200 OK
    [other headers]

    {
      "conversationId": "abc123",
      "token": "RCurR_XV9ZA.cwA.BKA.y8qbOF5xPGfiCpg4Fv0y8qqbOF5x8qbOF5xniaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0",
      "expires_in": 1800
    }
    ```

#### REST calls for a Direct Line conversation

    Direct Line conversations are explicitly opened by clients and may run as long as the bot and client participate (and have valid credentials). While the conversation is open, the bot and client may both send messages. More than one client may connect to a given conversation and each client may participate on behalf of multiple users.

##### Starting a conversation

    Clients begin by explicitly starting a conversation. If successful, the Direct Line service replies with a JSON object containing a conversation ID, a token, and a WebSocket URL that may be used later.

    ```
    -- connect to directline.botframework.com --
    POST /v3/directline/conversations HTTP/1.1
    Authorization: Bearer RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0y8qbOF5xPGfiCpg4Fv0y8qqbOF5x8qbOF5xn
    [other headers]

    -- response from directline.botframework.com --
    HTTP/1.1 201 Created
    [other headers]

    {
      "conversationId": "abc123",
      "token": "RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0y8qbOF5xPGfiCpg4Fv0y8qqbOF5x8qbOF5xn",
      "expires_in": 1800,
      "streamUrl": "https://directline.botframework.com/v3/directline/conversations/abc123/stream?t=RCurR_XV9ZA.cwA..."
    }
    ```

    If the conversation was started, an HTTP 201 status code is returned. HTTP 201 is the code that clients will receive under most circumstances, as the typical use case is for a client to start a new conversation.
    Under certain conditions -- specifically, when the client has a token scoped to a single conversation AND when that conversation was started with a prior call to this URL -- this method will return HTTP 200 to signify the request was acceptable but that no conversation was created (as it already existed).

    You have 60 seconds to connect to the WebSocket URL. If the connection cannot be established during this time, use the reconnect method below to generate a new stream URL.

    This call is similar to ```/v3/directline/tokens/generate```. The difference is that the call to ```/v3/directline/conversations``` starts the conversation, contacts the bot, and creates a streaming WebSocket URL, none of which occur when generating a token.
    * Call ```/v3/directline/conversations``` if you will distribute the token to client(s) and want them to
      initiate the conversation.
    * Call ```/v3/directline/conversations``` if you intend to start the conversation immediately.

##### Reconnecting to a conversation

    If a client is using the WebSocket interface to receive messages but loses its connection, it may need to reconnect. Reconnecting requires generating a new WebSocket stream URL, and this can be accomplished by sending a GET request to the ```/v3/directline/conversations/{id}``` endpoint.

    The ```watermark``` parameter is optional. If supplied, the conversation replays from the watermark, guaranteeing no messages are lost. If ```watermark``` is omitted, only messages received after the reconnection call (```GET /v3/directline/conversations/abc123```) are replayed.

    ```
    -- connect to directline.botframework.com --
    GET /v3/directline/conversations/abc123?watermark=0000a-42 HTTP/1.1
    Authorization: Bearer RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0y8qbOF5xPGfiCpg4Fv0y8qqbOF5x8qbOF5xn
    [other headers]

    -- response from directline.botframework.com --
    HTTP/1.1 200 OK
    [other headers]

    {
      "conversationId": "abc123",
      "token": "RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0y8qbOF5xPGfiCpg4Fv0y8qqbOF5x8qbOF5xn",
      "streamUrl": "https://directline.botframework.com/v3/directline/conversations/abc123/stream?watermark=000a-4&t=RCurR_XV9ZA.cwA..."
    }
    ```

    You have 60 seconds to connect to the WebSocket stream URL. If the connection cannot be established during this time, issue another reconnect request to get an updated stream URL.

##### Sending an Activity to the bot

    Using the Direct Line 3.0 protocol, clients and bots may exchange many different Bot Framework v3 Activities, including Message Activities, Typing Activities, and custom activities that the bot supports.

    To send any one of these activities to the bot,

    1. the client formulates the Activity according to the Activity schema (see below)
    2. the client issues a POST message to ```/v3/directline/conversations/{id}/activities```
    3. the service returns when the activity was delivered to the bot, with an HTTP status code reflecting the
       bot's status code. If the POST was successful, the service returns a JSON payload containing the ID of the
       Activity that was sent.

    Example follows.

    ```
    -- connect to directline.botframework.com --
    POST /v3/directline/conversations/abc123/activities HTTP/1.1
    Authorization: Bearer RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0
    [other headers]

    {
      "type": "message",
      "from": {
        "id": "user1"
      },
      "text": "hello"
    }

    -- response from directline.botframework.com --
    HTTP/1.1 200 OK
    [other headers]

    {
      "id": "0001"
    }
    ```

    The client's Activity is available in the message retrieval path (either polling GET or WebSocket) and is not returned inline.

    The total time to POST a message to a Direct Line conversation is:

    * Transit time to the Direct Line service,
    * Internal processing time within Direct Line (typically less than 120ms)
    * Transit time to the bot
    * Processing time within the bot
    * Transit time for HTTP responses to travel back to the client.

    If the bot generates an error, that error will trigger an HTTP 502 error ("Bad Gateway") in the ```POST /v3/directline/conversations/{id}/activities``` call.

###### Sending one or more attachments by URL

    Clients may optionally send attachments, such as images or documents. If the client already has a URL for the attachment, the simplest way to send it is to include the URL in the ```contentUrl``` field of an Activity attachment object. This applies to HTTP, HTTPS, and ```data:``` URIs.

###### Sending a single attachment by upload

    Often, clients have an image or document on a device but no URL that can be included in the activity.

    To upload an attachment, POST a single attachment to the ```/v3/directline/conversations/{conversationId}/upload``` endpoint. The ```Content-Type``` and ```Content-Disposition``` headers control the attachment's type and filename, respectively.

    A user ID is required. Supply the ID of the user sending the attachment as a ```userId``` parameter in the URL.

    If uploading a single attachment, a message activity is sent to the bot when the upload completes.

    On completion, the service returns the ID of the activity that was sent.

    ```
    -- connect to directline.botframework.com --
    POST /v3/directline/conversations/abc123/upload?userId=user1 HTTP/1.1
    Authorization: Bearer RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0
    Content-Type: image/jpeg
    Content-Disposition: name="file"; filename="badjokeeel.jpg"
    [other headers]

    [JPEG content]

    -- response from directline.botframework.com --
    HTTP/1.1 200 OK
    [other headers]

    {
      "id": "0003"
    }
    ```

###### Sending multiple attachments by upload

    If uploading multiple attachments, use ```multipart/form-data``` as the content type and include each attachment as a separate part. Each attachment's type and filename may be included in the ```Content-Type``` and ```Content-Disposition``` headers in each part.

    An activity may be included by adding a part with content type of ```application/vnd.microsoft.activity```. Other parts in the payload are attached to this activity before it is sent. If an Activity is not included, an empty Activity is created as a wrapper for the attachments.

    ```
    -- connect to directline.botframework.com --
    POST /v3/directline/conversations/abc123/upload?userId=user1 HTTP/1.1
    Authorization: Bearer RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0
    Content-Type: multipart/form-data; boundary=----DD4E5147-E865-4652-B662-F223701A8A89
    [other headers]

    ----DD4E5147-E865-4652-B662-F223701A8A89
    Content-Type: image/jpeg
    Content-Disposition: form-data; name="file"; filename="badjokeeel.jpg"
    [other headers]

    [JPEG content]

    ----DD4E5147-E865-4652-B662-F223701A8A89
    Content-Type: application/vnd.microsoft.activity
    [other headers]

    {
      "type": "message",
      "from": {
        "id": "user1"
      },
      "text": "Hey I just IM'd you\\n\\nand this is crazy\\n\\nbut here's my webhook\\n\\nso POST me maybe"
    }

    ----DD4E5147-E865-4652-B662-F223701A8A89


    -- response from directline.botframework.com --
    HTTP/1.1 200 OK
    [other headers]

    {
      "id": "0004"
    }
    ```

##### Receiving Activities from the bot

    Direct Line 3.0 clients may choose from two different mechanisms for retrieving messages:

    1. A **streaming WebSocket**, which pushes messages efficiently to clients.
    2. A **polling GET** interface, which is available for clients unable to use WebSockets or for clients retrieving the conversation history.

    **Not all activities are available via the polling GET interface.** A table of activity availability follows.

    |Activity type|Availability|
    |-------------|--------|
    |Message|Polling GET and WebSocket|
    |Typing|WebSocket only|
    |ConversationUpdate|Not sent/received via client|
    |ContactRelationUpdate|Not supported in Direct Line|
    |EndOfConversation|Polling GET and WebSocket|
    |All other activity types|Polling GET and WebSocket|

###### Receiving Activities by WebSocket

    To connect via WebSocket, a client uses the StreamUrl when starting a conversation. The stream URL is preauthorized and does NOT require an Authorization header containing the client's secret or token.

    ```
    -- connect to wss://directline.botframework.com --
    GET /v3/directline/conversations/abc123/stream?t=RCurR_XV9ZA.cwA...\" HTTP/1.1
    Upgrade: websocket
    Connection: upgrade
    [other headers]

    -- response from directline.botframework.com --
    HTTP/1.1 101 Switching Protocols
    [other headers]
    ```

    The Direct Line service sends the following messages:

    * An **ActivitySet**, which contains one or more activities and a watermark (described below)
    * An empty message, which the Direct Line service uses to ensure the connection is still valid
    * Additional types, to be defined later. These types are identified by the properties in the JSON root.

    ActivitySets contain messages sent by the bot and by all users. Example ActivitySet:

    ```
    {
      "activities": [{
        "type": "message",
        "channelId": "directline",
        "conversation": {
          "id": "abc123"
        },
        "id": "abc123|0000",
        "from": {
          "id": "user1"
        },
        "text": "hello"
      }],
      "watermark": "0000a-42"
    }
    ```

    Clients should keep track of the "watermark" value from each ActivitySet so they can use it on reconnect. **Note** that a ```null``` or missing watermark should be ignored and should not overwrite a prior watermark in the client.

    Clients should ignore empty messages.

    Clients may send their own empty messages to verify connectivity. The Direct Line service will ignore these.

    The service may forcibly close the connection under certain conditions. If the client has not received an EndOfConversation activity, it may reconnect by issuing a GET request to the conversation endpoint to get a new stream URL (see above).

    The WebSocket stream contains live updates and very recent messages (since the call to get the WebSocket call was issued) but it does not include messages sent prior to the most recent POST to ```/v3/directline/conversations/{id}```. To retrieve messages sent earlier in the conversation, use the GET mechanism below.

###### Receiving Activities by GET

    The GET mechanism is useful for clients who are unable to use the WebSocket, or for clients wishing to retrieve the conversation history.

    To retrieve messages, issue a GET call to the conversation endpoint. Optionally supply a watermark, indicating the most recent message seen. The watermark field accompanies all GET/WebSocket messages as a property in the ActivitySet.

    ```
    -- connect to directline.botframework.com --
    GET /v3/directline/conversations/abc123/activities?watermark=0001a-94 HTTP/1.1
    Authorization: Bearer RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0
    [other headers]

    -- response from directline.botframework.com --
    HTTP/1.1 200 OK
    [other headers]

    {
      "activities": [{
        "type": "message",
        "channelId": "directline",
        "conversation": {
          "id": "abc123"
        },
        "id": "abc123|0000",
        "from": {
          "id": "user1"
        },
        "text": "hello"
      }, {
        "type": "message",
        "channelId": "directline",
        "conversation": {
          "id": "abc123"
        },
        "id": "abc123|0001",
        "from": {
          "id": "bot1"
        },
        "text": "Nice to see you, user1!"
      }],
      "watermark": "0001a-95"
    }
    ```

    Clients should page through the available activities by advancing the ```watermark``` value until no activities are returned.

###### Timing considerations

    Most clients wish to retain a complete message history. Even though Direct Line is a multi-part protocol with potential timing gaps, the protocol and service is designed to make it easy to build a reliable client.

    1. The ```watermark``` field sent in the WebSocket stream and GET response is reliable. You will not miss messages as long as you replay the watermark verbatim.
    2. When starting a conversation and connecting to the WebSocket stream, any Activities sent after the POST but before the socket is opened are replayed before new messages.
    3. When refreshing history by GET call while connected to the WebSocket, Activities may be duplicated across both channels. Keeping a list of all known Activity IDs will allow you to reject duplicate messages should they occur.

    Clients using the polling GET interface should choose a polling interval that matches their intended use.

    * Service-to-service applications often use a polling interval of 5s or 10s.
    * Client-facing applications often use a polling interval of 1s, and fire an additional request ~300ms after every message the client sends to rapidly pick up a bot's response. This 300ms delay should be adjusted based on the bot's speed and transit time.

##### Ending a conversation

    Either a client or a bot may signal the end of a DirectLine conversation. This operation halts communication and prevents the bot and the client from sending messages. Messages may still be retrieved via the GET mechanism. Sending this messages is as simple as POSTing an EndOfConversation activity.

    ```
    -- connect to directline.botframework.com --
    POST /v3/directline/conversations/abc123/activities HTTP/1.1
    Authorization: Bearer RCurR_XV9ZA.cwA.BKA.iaJrC8xpy8qbOF5xnR2vtCX7CZj0LdjAPGfiCpg4Fv0
    [other headers]

    {
      "type": "endOfConversation",
      "from": {
        "id": "user1"
      }
    }

    -- response from directline.botframework.com --
    HTTP/1.1 200 OK
    [other headers]

    {
      "id": "0004"
    }
    ```

#### REST API errors

    HTTP calls to the Direct Line service follow standard HTTP error conventions:

    * 2xx status codes indicate success. (Direct Line 3.0 uses 200 and 201.)
    * 4xx status codes indicate an error in your request.
      * 401 indicates a missing or malformed Authorization header (or URL token, in calls where a token parameter is allowed).
      * 403 indicates an unauthorized client.
        * If calling with a valid but expired token, the ```code``` field is set to ```TokenExpired```.
      * 404 indicates a missing path, site, conversation, etc.
    * 5xx status codes indicate a service-side error.
      * 500 indicates an error inside the Direct Line service.
      * 502 indicates an error was returned by the bot. **This is a common error code.**
    * 101 is used in the WebSocket connection path, although this is likely handled by your WebSocket client.

    When an error message is returned, error detail may be present in a JSON response. Look for an ```error``` property with ```code``` and ```message``` fields.

    ```
    -- connect to directline.botframework.com --
    POST /v3/directline/conversations/abc123/activities HTTP/1.1
    [detail omitted]

    -- response from directline.botframework.com --
    HTTP/1.1 502 Bad Gateway
    [other headers]

    {
      "error": {
        "code": "BotRejectedActivity",
        "message": "Failed to send activity: bot returned an error"
      }
    }
    ```

    The contents of the ```message``` field may change. The HTTP status code and values in the ```code``` property are stable.

#### Schema

    The Direct Line 3.0 schema is identical to the Bot Framework v3 schema.

    When a bot sends an Activity to a client through Direct Line:

    * attachment cards are preserved,
    * URLs for uploaded attachments are hidden with a private link, and
    * the ```channelData``` property is preserved without modification.

    When a client sends an Activity to a bot through Direct Line:

    * the ```type``` property contains the kind of activity you are sending (typically ```message```),
    * the ```from``` property must be populated with a user ID, chosen by your client,
    * attachments may contain URLs to existing resources or URLs uploaded through the Direct Line attachment endpoint, and
    * the ```channelData``` property is preserved without modification.

    Clients and bots may send Activities of any type, including Message Activities, Typing Activities, and custom Activity types.

    Clients may send a single Activity at a time.

    ```
    {
      "type": "message",
      "channelId": "directline",
      "from": {
        "id": "user1"
      },
      "text": "hello"
    }
    ```

    Clients receive multiple Activities as part of an ActivitySet. The ActivitySet has an array of activities and a watermark field.

    ```
    {
      "activities": [{
        "type": "message",
        "channelId": "directline",
        "conversation": {
          "id": "abc123"
        },
        "id": "abc123|0000",
        "from": {
          "id": "user1"
        },
        "text": "hello"
      }],
      "watermark": "0000a-42"
    }
    ```

#### Libraries for the Direct Line API

    The Direct Line API is designed to be coded directly, but the Bot Framework includes libraries and controls that help you to embed Direct-Line-powered bots into your application.

    * The [Bot Framework Web Chat control](https://github.com/Microsoft/BotFramework-WebChat) is an easy way to embed the Direct Line protocol into a webpage.
    * [Direct Line Nuget package](https://www.nuget.org/packages/Microsoft.Bot.Connector.DirectLine) with libraries for .Net 4.5, UWP, and .Net Standard.
    * [DirectLineJs](https://github.com/Microsoft/BotFramework-DirectLineJs), also available on [NPM](https://www.npmjs.com/package/botframework-directlinejs)
    * You may generate your own from the [Direct Line Swagger file](swagger.json)

    Our [BotBuilder-Samples GitHub repo](https://github.com/Microsoft/BotBuilder-Samples) also contains samples for [C#](https://github.com/Microsoft/BotBuilder-Samples/tree/master/CSharp/core-DirectLine) and [JavaScript](https://github.com/Microsoft/BotBuilder-Samples/tree/master/Node/core-DirectLine).

*   **Bot Framework Connector Service API:** This is the primary mechanism for communication with standard channels like Microsoft Teams [Bot Framework Connector service REST API reference - Azure documentation](https://docs.azure.cn/en-us/bot-service/rest-api/bot-framework-rest-connector-api-reference?view=azure-bot-service-4.0). It normalizes messages into a common Activity schema.
*   **Azure Bot Service API:** Used by Copilot Studio for managing the underlying Azure Bot resources [Microsoft Copilot Studio on Azure | Microsoft Azure](https://azure.microsoft.com/en-us/products/copilot-studio).
*   **Bot Framework SDK:** Provides libraries (.NET, JavaScript) for building Bot Framework Skills, which are custom-coded bots that can extend Copilot Studio agents [Configure a Bot Framework skill - Microsoft Copilot Studio | Microsoft ...](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configuration-add-skills). Java and Python SDKs are being retired [Bot Framework SDK documentation - Bot Service | Microsoft Learn](https://learn.microsoft.com/en-us/azure/bot-service/index-bf-sdk?view=azure-bot-service-4.0).
*   **Power Automate flows:** Serve as a crucial extensibility point, allowing agents to perform actions by calling flows [Create a Power Automate flow - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-flow-create). These flows must have specific triggers and response actions for Copilot Studio and are subject to a timeout [Create a Power Automate flow - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-flow-create).

**Authentication** varies: standard channels often use integrated authentication (e.g., Microsoft Entra ID for Teams) [Key concepts - Publish and deploy your agent - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels). Direct Line relies on secrets or tokens [Configure web and Direct Line channel security - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configure-web-security). SSO can be configured for custom canvases using Direct Line and Microsoft Entra ID [Configure single sign-on with Microsoft Entra ID - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configure-sso).

## 4. The Intelligence Engine: AI Models, NLU, and Orchestration

Copilot Studio's intelligence combines customized Natural Language Understanding (NLU) models with advanced generative AI capabilities, primarily leveraging Azure OpenAI GPT models [Quickstart guide for building agents with generative AI - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/nlu-gpt-quickstart).

### 4.1. Natural Language Understanding (NLU)
Copilot Studio employs **customized NLU models** to interpret user input (text or speech) [Quickstart guide for building agents with generative AI - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/nlu-gpt-quickstart). These models aim to discern user *intent* and extract relevant *entities* (e.g., dates, locations) [What is Natural Language Understanding? | Microsoft Copilot](https://www.microsoft.com/en-us/microsoft-copilot/for-individuals/do-more-with-ai/general-ai/what-is-natural-language-understanding).
For classic chatbots, the NLU is described as transformer-based, utilizing an example-based approach powered by a deep neural network, effective even with a small number of training examples for new topics [AI features for Teams and Classic chatbots - Microsoft Copilot Studio ...](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-ai-features). This NLU is fundamental for matching user utterances to the most appropriate agent "topic."

### 4.2. Generative AI and Azure OpenAI GPT Models
The integration of **Azure OpenAI GPT models** (similar to those in Bing) significantly enhances Copilot Studio's intelligence [Quickstart guide for building agents with generative AI - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/nlu-gpt-quickstart). Key functions include:

*   **Generative Answers (Conversation Booster):** When a query doesn't match a pre-authored topic, generative AI can formulate an answer by drawing from configured knowledge sources like public websites, SharePoint sites, uploaded documents, or Dataverse tables [Quickstart guide for building agents with generative AI - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/nlu-gpt-quickstart). The LLM synthesizes information to provide a relevant, conversational response [Microsoft Copilot Studio Blog – Announcement of generative AI features](https://www.microsoft.com/en-us/microsoft-copilot/blog/).
*   **Topic Creation and Modification:** Developers can use generative AI to bootstrap new topics from natural language descriptions or modify existing ones [Quickstart guide for building agents with generative AI - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/nlu-gpt-quickstart). This is powered by an LLM like GPT-4 taking a prompt to create dialog content [Quickstart guide for building agents with generative AI - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/nlu-gpt-quickstart).
*   **Generative Actions & Orchestration:** This feature allows agents to dynamically create conversational flows by identifying and connecting appropriate plugins (Power Automate flows, connectors, Bot Framework skills) in real-time based on the user's request [Copilot and AI innovation - Learn Microsoft](https://learn.microsoft.com/en-us/power-platform/release-plan/2025wave1/microsoft-copilot-studio/copilot-ai-innovation). The LLM reasons about available tools and orchestrates their execution.
*   **Custom Prompts:** Authors can create prompts to instruct the GPT model on specific tasks like summarization or translation [What's new in Copilot Studio: March 2025 - Microsoft](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/whats-new-in-copilot-studio-march-2025/).

### 4.3. Dialog Management and Orchestration
The dialog management system incorporates these generative capabilities:

*   **Topic-Based Dialog:** Traditional structured conversational flows where NLU maps user intent to topics containing nodes (messages, questions, actions) [Quickstart guide for building agents with generative AI - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/nlu-gpt-quickstart).
*   **Generative Orchestration (AI Planner):** A more advanced mode where the agent dynamically selects the best combination of actions, topics, and knowledge sources [AI features for Teams and Classic chatbots - Microsoft Copilot Studio ...](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-ai-features). The system considers natural language *descriptions* of components and conversation history to formulate a response plan [Orchestrate agent behavior with generative AI - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-generative-actions). If needed inputs are missing, the orchestrator can dynamically generate questions [Add actions to custom agents - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-plugin-actions). This AI planner evaluates the user's request against available topics, knowledge, and actions, deciding among pre-built topics, knowledge sources, or invoking an Action/Plugin [Orchestrate agent behavior with generative AI - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-generative-actions).

This hybrid AI model balances control with flexibility, allowing precise definition of core paths while empowering agents to handle unanticipated queries through generative capabilities [FAQ for generative orchestration - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/faqs-generative-orchestration).

## 5. Data Flow and Channel Communication

The data exchange sequence when a user interacts with a Copilot Studio agent involves the user, channel client, intermediary services (Bot Framework Connector), Copilot Studio runtime/AI engine, and backend systems.

**End-to-End Data Flow (Generalized):**
1.  User sends a message via a channel interface.
2.  Channel client transmits this as an Activity object to the Bot Framework Connector Service (for standard channels) or Direct Line service (for custom clients) [Bot Framework Connector service REST API reference - Azure documentation](https://docs.azure.cn/en-us/bot-service/rest-api/bot-framework-rest-connector-api-reference?view=azure-bot-service-4.0).
3.  Connector/Direct Line service authenticates and forwards the Activity to the Copilot Studio agent's endpoint.
4.  Copilot Studio runtime receives the Activity; its AI engine processes the input (NLU, generative orchestration) [Quickstart guide for building agents with generative AI - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/nlu-gpt-quickstart).
5.  Agent might trigger a topic, invoke an action (Power Automate flow, Skill) [Create a Power Automate flow - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-flow-create), query knowledge sources (Dataverse, SharePoint) [Add a Dataverse knowledge source - Microsoft Copilot Studio ...](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-add-dataverse), or update conversation state [Work with global variables - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-variables-bot).
6.  Agent formulates a response Activity (text, cards, etc.).
7.  Response Activity is sent back through the Connector/Direct Line service to the originating channel.
8.  Channel client renders the response to the user. This flow is analogous to Microsoft 365 Copilot's prompt processing [Microsoft 365 Copilot architecture and how it works](https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-architecture).

**Channel Communication Flow Comparison:**

| Channel Type                             | Initial User Interaction Point | Primary Message Routing Path (Simplified)                                                              | Authentication Handling                                                                                                | Context Passing Mechanism                                                                                                             | Key Architectural Differences/Considerations                                                                                                                                                                 |
| :--------------------------------------- | :----------------------------- | :----------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Microsoft Teams**                      | Teams Client (Chat)            | User → Teams Client → Teams Services → Bot Framework Connector → Copilot Studio Agent                  | Integrated Microsoft Entra ID (typically automatic if configured) [Key concepts - Publish and deploy your agent - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels)             | Teams user context (ID, name), User.AccessToken if SSO configured. The bot receives Activities with `channelId` "msteams".         | Integrated experience; data shared with Teams service may flow outside compliance boundaries [Connect and configure an agent for Teams and Microsoft 365 Copilot](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-add-bot-to-microsoft-teams). Bot can use Teams-specific features. |
| **Custom Web Chat (Copilot Studio Snippet / Direct Line)** | Embedded Web Chat Control / Custom App UI | User → Web Chat JS / Custom App → Direct Line API / Bot Framework Connector → Copilot Studio Agent | None, Microsoft Entra ID, or Manual (OAuth 2.0 IdP) configured in Copilot Studio [Key concepts - Publish and deploy your agent - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels). Direct Line uses token-based auth. | JavaScript variables from host page as parameters [Copilot Studio architecture key concepts and solution ideas - Power Platform](https://learn.microsoft.com/en-us/power-platform/architecture/products/copilot-studio); session variables. Activity `channelId` is "directline" or "webchat". | Quick to deploy (snippet); limited UI customization. Direct Line offers maximum control over UI/UX but more developer responsibility for token management, security [Configure web and Direct Line channel security - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configure-web-security), and client-side state [webchat.js -> direct line API--> copilot studio, reset the chat bot messages - Stack Overflow](https://stackoverflow.com/questions/79487310/webchat-js-direct-line-api-copilot-studio-reset-the-chat-bot-messages). |

**Context Passing:**
*   **User Identity:** Available in authenticated channels like Teams [Key concepts - Publish and deploy your agent - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels). For Direct Line, it can be passed when generating the token [Connecting to agents in Copilot Studio through Direct Line channel](https://community.powerplatform.com/forums/thread/details/?threadid=4d0f9b82-80cf-ef11-b8e8-6045bdd9204f) or via SSO with Microsoft Entra ID (User.AccessToken variable) [Configure single sign-on with Microsoft Entra ID - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configure-sso).
*   **Session and Global Variables:** Copilot Studio uses variables (`bot.` prefix for global) to store data during a conversation, accessible across topics and initializable from external sources [Work with global variables - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-variables-bot).
*   **Conversation State:** Managed by the underlying Azure Bot Service framework, potentially persisted to Azure Blob Storage or Cosmos DB for custom code/skills [Save user and conversation data - Bot Service | Microsoft Learn](https://learn.microsoft.com/en-us/azure/bot-service/bot-builder-howto-v4-state?view=azure-bot-service-4.0). Copilot Studio sessions end due to inactivity (30+ min), duration (60+ min), or turn limits (100+ turns) [Manage sessions and capacity - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-sessions-management).

## 6. Microsoft Dataverse: The Operational Backbone

Microsoft Dataverse is critical for Copilot Studio, serving as a knowledge source, repository for bot definitions, storage for operational data (like transcripts), and central to Application Lifecycle Management (ALM).

*   **Enterprise Knowledge Source:** Dataverse tables can ground agents in structured business data (e.g., from Dynamics 365, Power Apps) [Add a Dataverse knowledge source - Microsoft Copilot Studio ...](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-add-dataverse). Retrieval Augmented Generation (RAG) techniques are used, where the agent retrieves relevant Dataverse information to formulate responses [Add Dataverse as enterprise knowledge in Copilot Studio - Learn Microsoft](https://learn.microsoft.com/en-us/power-platform/release-plan/2024wave2/data-platform/add-dataverse-as-enterprise-knowledge-copilot-studio). Copilot Studio respects Dataverse security models (table, row, column-level permissions) [Knowledge in Microsoft Copilot Studio - Microsoft Power Platform Blog](https://www.microsoft.com/en-us/power-platform/blog/it-pro/knowledge-in-microsoft-copilot-studio/).
*   **Storage for Bot Definitions and Components:**
    *   Core agent definitions are stored in the `bot` Dataverse table (logical name `bot`, schema `msdyn_bot`) [Exploring Copilot Agent data in Dataverse : r/PowerPlatform - Reddit](https://www.reddit.com/r/PowerPlatform/comments/1k1efra/exploring_copilot_agent_data_in_dataverse/).
    *   Components (topics, entities, variables, actions, knowledge configurations) are packaged within **Dataverse solutions** [Copilot Studio Dataverse Capacity : r/copilotstudio - Reddit](https://www.reddit.com/r/copilotstudio/comments/1jtfm96/copilot_studio_dataverse_capacity/). Actions are automatically saved into solutions [Use application lifecycle management in Copilot Studio - Learn Microsoft](https://learn.microsoft.com/en-us/power-platform/release-plan/2024wave2/data-platform/use-application-lifecycle-management-copilot-studio).
    *   Reusable component collections are managed in tables like `botcomponentcollection` [Copilot component collection (botcomponentcollection) table/entity reference (Microsoft Dataverse) - Power Apps](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/reference/entities/botcomponentcollection).
    *   The `botcomponent` table stores information related to knowledge sources [Exploring Copilot Agent data in Dataverse : r/PowerPlatform - Reddit](https://www.reddit.com/r/PowerPlatform/comments/1k1efra/exploring_copilot_agent_data_in_dataverse/).
*   **Conversation Transcripts and Interaction Data:** Stored in Dataverse tables like `msdyn_copilotinteraction`, `msdyn_copilotinteractiondata`, `msdyn_copilottranscript`, and `msdyn_copilottranscriptdata` [Download Copilot transcripts and interaction data - Learn Microsoft](https://learn.microsoft.com/en-us/dynamics365/customer-service/develop/download-copilot-transcript-data). These are used for analytics.
*   **Application Lifecycle Management (ALM):** Because agents and their components are solution-aware and stored in Dataverse, they can be managed using standard Power Platform ALM practices (export/import solutions) [Copilot Studio architecture key concepts and solution ideas - Power Platform](https://learn.microsoft.com/en-us/power-platform/architecture/products/copilot-studio), [Use application lifecycle management in Copilot Studio - Learn Microsoft](https://learn.microsoft.com/en-us/power-platform/release-plan/2024wave2/data-platform/use-application-lifecycle-management-copilot-studio).

**Illustrative Dataverse Tables for Copilot Studio Components:**

| Copilot Studio Component                 | Likely Dataverse Table(s) (Logical Name / Common Schema Name)                                    | Brief Description of Data Stored                                                                                                                               |
| :--------------------------------------- | :----------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent/Bot Definition                     | `bot` / `msdyn_bot` [Exploring Copilot Agent data in Dataverse : r/PowerPlatform - Reddit](https://www.reddit.com/r/PowerPlatform/comments/1k1efra/exploring_copilot_agent_data_in_dataverse/)                                                                 | Core metadata about the agent (name, ID, environment, owner, configuration settings).                                                                          |
| Topics, Entities, Variables, Agent Logic | Stored as components within Dataverse Solutions. Underlying tables include `botcomponent`.         | Detailed definitions of conversational flows, data types, memory units, and other agent configurations.                                                        |
| Knowledge Source Configurations          | `botcomponent` (for knowledge source type components) [Exploring Copilot Agent data in Dataverse : r/PowerPlatform - Reddit](https://www.reddit.com/r/PowerPlatform/comments/1k1efra/exploring_copilot_agent_data_in_dataverse/), other related entities. | Configuration details for connected knowledge sources (Dataverse tables, websites, files).                                                                     |
| Actions (e.g., Power Automate flows)     | Stored as components in Dataverse Solutions, referencing flow definitions (e.g., `workflow`). Solution-aware [Use application lifecycle management in Copilot Studio - Learn Microsoft](https://learn.microsoft.com/en-us/power-platform/release-plan/2024wave2/data-platform/use-application-lifecycle-management-copilot-studio).      | Definitions of actions the agent can perform, including mappings to Power Automate flows or Bot Framework Skills.                                              |
| Component Collections                    | `botcomponentcollection` [Copilot component collection (botcomponentcollection) table/entity reference (Microsoft Dataverse) - Power Apps](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/reference/entities/botcomponentcollection)                                           | Collections of reusable agent components (topics, knowledge, actions, entities).                                                                               |
| Conversation Transcripts                 | `msdyn_copilotinteraction`, `msdyn_copilotinteractiondata`, `msdyn_copilottranscript`, `msdyn_copilottranscriptdata` [Download Copilot transcripts and interaction data - Learn Microsoft](https://learn.microsoft.com/en-us/dynamics365/customer-service/develop/download-copilot-transcript-data) | Detailed logs of conversations including user inputs, agent responses, session IDs, outcomes, and metadata. Also referred to as `ConversationTranscript` in some contexts. |
| Agent Permissions                        | `principalobjectaccess` (general Dataverse table) [Exploring Copilot Agent data in Dataverse : r/PowerPlatform - Reddit](https://www.reddit.com/r/PowerPlatform/comments/1k1efra/exploring_copilot_agent_data_in_dataverse/)                                                 | Records indicating user/team access levels to the agent definition and components.                                                                             |

*Note on Dataverse for Teams:* Bots built in a Dataverse for Teams environment use a lightweight version of Dataverse, and conversation transcripts are not saved for these bots [Download conversation transcripts in Copilot Studio - Learn Microsoft](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-transcripts-studio).

## 7. Data Storage, Retention, and Security

Data storage in Copilot Studio involves a mix of transient (session-based) and persistent (long-term) data.

### 7.1. Storage Locations and Data Types
*   **Conversation Transcripts:** Primarily stored in Dataverse tables (e.g., `msdyn_copilottranscript`, `msdyn_copilotinteraction`) [Download Copilot transcripts and interaction data - Learn Microsoft](https://learn.microsoft.com/en-us/dynamics365/customer-service/develop/download-copilot-transcript-data). Accessible via Copilot Studio analytics [Download conversation transcripts in Copilot Studio - Learn Microsoft](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-transcripts-studio). Not written for Dataverse for Teams or developer environments [Download conversation transcripts in Copilot Studio - Learn Microsoft](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-transcripts-studio). For Microsoft 365 Copilot interactions, history may be in the user's Exchange Online mailbox (hidden folder) [Microsoft 365 Copilot architecture and how it works](https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-architecture).
*   **Bot Definitions (Topics, Entities, etc.):** Stored in Dataverse as solution components [Exploring Copilot Agent data in Dataverse : r/PowerPlatform - Reddit](https://www.reddit.com/r/PowerPlatform/comments/1k1efra/exploring_copilot_agent_data_in_dataverse/).
*   **User Context (Session/Global Variables):**
    *   **Transient (Session-based):** Active session state, including current values of session-scoped variables, is managed by the Copilot Studio runtime in-memory during an ongoing conversation [Manage sessions and capacity - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-sessions-management). This state is lost when the session ends.
    *   **Persistent (Global):** Global variables (prefixed with `bot.`) are persisted as part of the agent's definition within Dataverse [Work with global variables - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-variables-bot).
    *   Underlying Bot Framework state (if custom code/skills are used) might persist data to Azure Storage (Blob, Cosmos DB) [Managing state in Bot Framework SDK - Bot Service - Learn Microsoft](https://learn.microsoft.com/en-us/azure/bot-service/bot-builder-concept-state?view=azure-bot-service-4.0).
*   **Analytics Data:** Aggregated data in Copilot Studio analytics is available for up to 360 days (for events after Nov 22, 2024) [Analyze conversational agent effectiveness - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-improve-agent-effectiveness). Raw data largely resides in Dataverse.
*   **Uploaded Files for Knowledge:** Files uploaded directly to Copilot Studio as knowledge sources are semantically indexed and stored in a "built-in store for the agent," likely within the Power Platform environment (Dataverse file capacity or related Azure storage) [Knowledge in Microsoft Copilot Studio - Microsoft Power Platform Blog](https://www.microsoft.com/en-us/power-platform/blog/it-pro/knowledge-in-microsoft-copilot-studio/).

### 7.2. Data Retention Policies
*   **Copilot Studio Data in Dataverse (Transcripts, Definitions):** Subject to Dataverse environment lifecycle and retention policies. Trial environments are deleted after 30 days if not converted [Microsoft Copilot Studio on Azure | Microsoft Azure](https://azure.microsoft.com/en-us/products/copilot-studio). Conversation transcripts in Dataverse are typically retained for 30 days by default, but this can be configurable.
*   **Microsoft Purview Retention Policies:** Can be configured for "AI app interactions" (prompts/responses for Copilots, often stored in user's Exchange Online mailbox) [Learn about retention for Copilot and AI apps](https://learn.microsoft.com/en-us/purview/retention-policies-copilot). Policies define retention duration or deletion timing.
*   **General Copilot Prompts/Responses (e.g., M365 Copilot):** May be retained by Microsoft for up to 30 days for service improvement, then generally deleted unless legal/compliance obligations exist [Does Microsoft Copilot Store Your Data? | Nightfall AI](https://www.nightfall.ai/blog/does-microsoft-copilot-store-your-data).

### 7.3. Transient vs. Persistent Data Summary

| Data Type                                        | Storage Nature                                                                                                                                                                                                                           | Examples                                                                                                                                 |
| :----------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------- |
| **Session State & Variables**                    | **Transient (Short-Term):** In-memory during active conversation. Cleared when session ends [Manage sessions and capacity - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-sessions-management).                                                                                                                                                           | User's name provided in the current chat, current step in a dialog.                                                                      |
| **Live Adaptive Knowledge Results**              | **Transient (Short-Term):** Data fetched from knowledge sources (SharePoint, Dataverse) at query time. Used for response formulation and then discarded by the bot service.                                                                  | Text from a SharePoint policy document used to answer a specific question.                                                               |
| **Conversation Transcripts**                     | **Persistent (Long-Term):** Stored in Dataverse tables (e.g., `msdyn_copilottranscript`) [Download Copilot transcripts and interaction data - Learn Microsoft](https://learn.microsoft.com/en-us/dynamics365/customer-service/develop/download-copilot-transcript-data). Default retention ~30 days, configurable. | Log of a chat session from last week, used for analytics.                                                                                |
| **Bot Content & Configuration**                  | **Persistent (Long-Term):** Topics, entities, flows, knowledge connections stored in Dataverse [Exploring Copilot Agent data in Dataverse : r/PowerPlatform - Reddit](https://www.reddit.com/r/PowerPlatform/comments/1k1efra/exploring_copilot_agent_data_in_dataverse/). Persists until changed by the maker.                                                     | The "Store Hours" topic definition, trigger phrases for a specific intent.                                                               |
| **Integrated Business Data Records (via Actions)** | **Persistent (Long-Term):** Records created/updated in external systems (Dataverse, CRM, ITSM) via Power Automate flows or connectors.                                                                                                  | A support ticket logged in ServiceNow or Dataverse by the bot.                                                                           |
| **Global Variables (`bot.varName`)**             | **Persistent (Long-Term):** Stored as part of the bot's definition in Dataverse [Work with global variables - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-variables-bot).                                                                                                                                  | A global setting for the bot, like a default language or region, initialized from an external source.                                  |

### 7.4. Security of Data
*   Customer data generally remains within the Microsoft 365 service boundary (for M365 Copilot interactions) [Microsoft 365 Copilot architecture and how it works](https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-architecture) and customer-chosen Azure geographic location for Copilot Studio deployments [Data locations in Copilot Studio - Learn Microsoft](https://learn.microsoft.com/en-us/microsoft-copilot-studio/data-location), with exceptions for global services or external connectors [Data locations in Copilot Studio - Learn Microsoft](https://learn.microsoft.com/en-us/microsoft-copilot-studio/data-location).
*   Data is encrypted at rest and in transit using industry-standard protocols [Geographic data residency in Copilot Studio - Learn Microsoft](https://learn.microsoft.com/en-us/microsoft-copilot-studio/geo-data-residency).
*   Access is governed by organizational security policies, Microsoft Entra ID authentication, and Power Platform admin controls [Customize Copilot and Create Agents | Microsoft Copilot Studio](https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio).
*   Dataverse's native security model (table, row, column-level security) is enforced for Dataverse knowledge sources [Knowledge in Microsoft Copilot Studio - Microsoft Power Platform Blog](https://www.microsoft.com/en-us/power-platform/blog/it-pro/knowledge-in-microsoft-copilot-studio/).
*   Audit logs are viewable in Microsoft Purview; alerts can be configured via Microsoft Sentinel [Customize Copilot and Create Agents | Microsoft Copilot Studio](https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio).

## 8. Conclusion: A Synthesized View of Copilot Studio Operations

Microsoft Copilot Studio is not a monolithic application but an advanced orchestration layer, interweaving Azure AI, Azure Bot Services, and the Power Platform (especially Dataverse) [Copilot Studio architecture key concepts and solution ideas - Power Platform](https://learn.microsoft.com/en-us/power-platform/architecture/products/copilot-studio). A user's message journey involves APIs for connectivity (Direct Line, Bot Connector), AI models (NLU, GPT) for understanding and generation, Dataverse for persistence and knowledge, and channel integrations for delivery [What is Copilot Studio? The Architecture of a Copilot | Video - Quisitive](https://quisitive.com/what-is-copilot-studio-the-architecture-of-a-copilot/).

Key architectural considerations include:
*   **Strategic Integration Choices:** Selecting between standard channels (via Bot Framework Connector) and Direct Line API impacts development, control, and security [Configure web and Direct Line channel security - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configure-web-security). Similarly, choosing between Bot Framework Skills or Power Automate flows for extensions depends on complexity and skills [Microsoft Copilot Studio on Azure | Microsoft Azure](https://azure.microsoft.com/en-us/products/copilot-studio).
*   **Comprehensive Data Governance:** Multiple data storage locations and varying retention policies necessitate a holistic governance strategy, including data residency implications [Data locations in Copilot Studio - Learn Microsoft](https://learn.microsoft.com/en-us/microsoft-copilot-studio/data-location).
*   **Scalability and Performance:** Dependent on underlying Azure services (Azure Bot Service, Azure OpenAI, Dataverse).
*   **Robust ALM:** Leveraging Dataverse solutions is crucial for managing agents across environments [Use application lifecycle management in Copilot Studio - Learn Microsoft](https://learn.microsoft.com/en-us/power-platform/release-plan/2024wave2/data-platform/use-application-lifecycle-management-copilot-studio).
*   **Diverse Skillset Requirements:** While low-code, complex scenarios benefit from Power Platform, Azure development, and AI/LLM understanding [Microsoft Copilot Studio on Azure | Microsoft Azure](https://azure.microsoft.com/en-us/products/copilot-studio).

The increasing emphasis on generative AI (generative orchestration, answers, actions) [Copilot and AI innovation - Learn Microsoft](https://learn.microsoft.com/en-us/power-platform/release-plan/2025wave1/microsoft-copilot-studio/copilot-ai-innovation) and rich extensibility points signal a move towards more autonomous and intelligent copilots [What's new in Copilot Studio: March 2025 - Microsoft](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/whats-new-in-copilot-studio-march-2025/). This requires continuous learning to harness Copilot Studio's expanding potential.