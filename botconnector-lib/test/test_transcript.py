# coding: utf-8

"""
    Microsoft Bot Connector API - v3.0

    The Bot Connector REST API allows your bot to send and receive messages to channels configured in the  [Bot Framework Developer Portal](https://dev.botframework.com). The Connector service uses industry-standard REST  and JSON over HTTPS.    Client libraries for this REST API are available. See below for a list.    Many bots will use both the Bot Connector REST API and the associated [Bot State REST API](/en-us/restapi/state). The  Bot State REST API allows a bot to store and retrieve state associated with users and conversations.    Authentication for both the Bot Connector and Bot State REST APIs is accomplished with JWT Bearer tokens, and is  described in detail in the [Connector Authentication](/en-us/restapi/authentication) document.    # Client Libraries for the Bot Connector REST API    * [Bot Builder for C#](/en-us/csharp/builder/sdkreference/)  * [Bot Builder for Node.js](/en-us/node/builder/overview/)  * Generate your own from the [Connector API Swagger file](https://raw.githubusercontent.com/Microsoft/BotBuilder/master/CSharp/Library/Microsoft.Bot.Connector.Shared/Swagger/ConnectorAPI.json)    © 2016 Microsoft

    The version of the OpenAPI document: v3
    Contact: botframework@microsoft.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from bot_connector.models.transcript import Transcript

class TestTranscript(unittest.TestCase):
    """Transcript unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Transcript:
        """Test Transcript
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Transcript`
        """
        model = Transcript()
        if include_optional:
            return Transcript(
                activities = [
                    bot_connector.models.activity.Activity(
                        type = 'message', 
                        id = '', 
                        timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        local_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        local_timezone = '', 
                        caller_id = '', 
                        service_url = '', 
                        channel_id = '', 
                        from = bot_connector.models.channel_account.ChannelAccount(
                            id = '', 
                            name = '', 
                            aad_object_id = '', 
                            role = 'user', ), 
                        conversation = bot_connector.models.conversation_account.ConversationAccount(
                            is_group = True, 
                            conversation_type = '', 
                            tenant_id = '', 
                            id = '', 
                            name = '', 
                            aad_object_id = '', ), 
                        recipient = bot_connector.models.channel_account.ChannelAccount(
                            id = '', 
                            name = '', 
                            aad_object_id = '', ), 
                        text_format = 'markdown', 
                        attachment_layout = 'list', 
                        members_added = [
                            
                            ], 
                        members_removed = [
                            
                            ], 
                        reactions_added = [
                            bot_connector.models.message_reaction.MessageReaction()
                            ], 
                        reactions_removed = [
                            bot_connector.models.message_reaction.MessageReaction()
                            ], 
                        topic_name = '', 
                        history_disclosed = True, 
                        locale = '', 
                        text = '', 
                        speak = '', 
                        input_hint = 'acceptingInput', 
                        summary = '', 
                        suggested_actions = bot_connector.models.suggested_actions.SuggestedActions(
                            to = [
                                ''
                                ], 
                            actions = [
                                bot_connector.models.card_action.CardAction(
                                    title = '', 
                                    image = '', 
                                    text = '', 
                                    display_text = '', 
                                    value = bot_connector.models.value.value(), 
                                    channel_data = bot_connector.models.channel_data.channelData(), )
                                ], ), 
                        attachments = [
                            bot_connector.models.attachment.Attachment(
                                content_type = '', 
                                content_url = '', 
                                content = bot_connector.models.content.content(), 
                                name = '', 
                                thumbnail_url = '', )
                            ], 
                        entities = [
                            bot_connector.models.entity.Entity()
                            ], 
                        channel_data = bot_connector.models.channel_data.channelData(), 
                        action = '', 
                        reply_to_id = '', 
                        label = '', 
                        value_type = '', 
                        value = bot_connector.models.value.value(), 
                        name = '', 
                        relates_to = bot_connector.models.conversation_reference.ConversationReference(
                            activity_id = '', 
                            user = , 
                            bot = , 
                            channel_id = '', 
                            service_url = '', ), 
                        code = 'unknown', 
                        expiration = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        importance = 'low', 
                        delivery_mode = 'normal', 
                        listen_for = [
                            ''
                            ], 
                        text_highlights = [
                            bot_connector.models.text_highlight.TextHighlight(
                                text = '', 
                                occurrence = 56, )
                            ], 
                        semantic_action = bot_connector.models.semantic_action.SemanticAction(
                            state = 'start', 
                            id = '', ), )
                    ]
            )
        else:
            return Transcript(
        )
        """

    def testTranscript(self):
        """Test Transcript"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
