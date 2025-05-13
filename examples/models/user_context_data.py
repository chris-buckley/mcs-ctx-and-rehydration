"""
Context payload sent from the web-app to the chatbot so it can tailor replies.

This is how you set the topic in the Microsoft Copilot Studio:
kind: AdaptiveDialog
beginDialog:
  kind: OnEventActivity
  id: main
  eventName: setConversationContext
  actions:
    - kind: SetVariable
      id: set_user_first_name
      variable: Global.ConversationContextData.user_first_name
      value: =System.Activity.Value.user_first_name

    - kind: SetVariable
      id: set_user_last_name
      variable: Global.ConversationContextData.user_last_name
      value: =System.Activity.Value.user_last_name

    - kind: SetVariable
      id: set_user_email
      variable: Global.ConversationContextData.user_email
      value: =System.Activity.Value.user_email

    - kind: SetVariable
      id: set_current_page_url
      variable: Global.ConversationContextData.current_page_url
      value: =System.Activity.Value.current_page_url

    - kind: SetVariable
      id: set_page_title
      variable: Global.ConversationContextData.page_title
      value: =System.Activity.Value.page_title

    - kind: SetVariable
      id: set_element_clicked
      variable: Global.ConversationContextData.element_clicked_to_initiate_chat
      value: =System.Activity.Value.element_clicked_to_initiate_chat

    - kind: SetVariable
      id: set_device_type
      variable: Global.ConversationContextData.device_type
      value: =System.Activity.Value.device_type

    - kind: SetVariable
      id: set_device
      variable: Global.ConversationContextData.device
      value: =System.Activity.Value.device

    - kind: SetVariable
      id: set_viewport_width
      variable: Global.ConversationContextData.viewport_width
      value: =System.Activity.Value.viewport_width

    - kind: SetVariable
      id: set_viewport_height
      variable: Global.ConversationContextData.viewport_height
      value: =System.Activity.Value.viewport_height

    - kind: SetVariable
      id: set_connection_type
      variable: Global.ConversationContextData.connection_type
      value: =System.Activity.Value.connection_type

    - kind: SetVariable
      id: set_visit_start_time
      variable: Global.ConversationContextData.visit_start_time
      value: =System.Activity.Value.visit_start_time

    - kind: SetVariable
      id: set_last_conversation_time
      variable: Global.ConversationContextData.last_conversation_time
      value: =System.Activity.Value.last_conversation_time

    - kind: SetVariable
      id: set_user_id
      variable: Global.ConversationContextData.user_id
      value: =System.Activity.Value.user_id

    - kind: SetVariable
      id: set_is_authenticated
      variable: Global.ConversationContextData.is_authenticated
      value: =System.Activity.Value.is_authenticated

    - kind: SetVariable
      id: set_language
      variable: Global.ConversationContextData.language
      value: =System.Activity.Value.language

    - kind: SetVariable
      id: set_timezone
      variable: Global.ConversationContextData.timezone
      value: =System.Activity.Value.timezone

    - kind: SetVariable
      id: set_local_time
      variable: Global.ConversationContextData.local_time
      value: =System.Activity.Value.local_time

    - kind: SetVariable
      id: set_location
      variable: Global.ConversationContextData.location
      value: =System.Activity.Value.location

    - kind: SetVariable
      id: set_marketing_opt_in
      variable: Global.ConversationContextData.marketing_opt_in
      value: =System.Activity.Value.marketing_opt_in

    - kind: SetVariable
      id: set_app_version
      variable: Global.ConversationContextData.app_version
      value: =System.Activity.Value.app_version

    - kind: SetVariable
      id: set_widget_version
      variable: Global.ConversationContextData.widget_version
      value: =System.Activity.Value.widget_version

    - kind: SetVariable
      id: set_navigation_history
      variable: Global.ConversationContextData.navigation_history
      value: =System.Activity.Value.navigation_history

    - kind: SendActivity
      id: echo_context
      activity: Context received ➜ {Global.ConversationContextData}
"""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, List, Optional
import uuid

from pydantic import BaseModel, Field


class Location(BaseModel):
    country: str = Field(..., description="ISO country name resolved from the visitor’s IP/GPS")
    region: str = Field(..., description="State / province / region")
    city: str = Field(..., description="City or locality")
    latitude: float = Field(..., description="Latitude in decimal degrees")
    longitude: float = Field(..., description="Longitude in decimal degrees")


class NavigationClick(BaseModel):
    order: int = Field(..., description="1 = most recent click, 20 = oldest")
    element: str = Field(..., description="DOM selector, button ID, or short label of the element clicked")


class ConversationContextData(BaseModel):
    user_first_name: Optional[str] = Field(None, description="User’s first name")
    user_last_name: Optional[str] = Field(None, description="User’s last name")
    user_email: Optional[str] = Field(None, description="User’s email address")
    current_page_url: str = Field(..., description="Full URL where chat was opened")
    page_title: str = Field(..., description="Document.title at the moment of chat open")
    element_clicked_to_initiate_chat: str = Field(..., description="Widget ID / selector the user clicked to start the chat")
    device_type: str = Field(..., description="High-level category: desktop, mobile, or tablet")
    device: str = Field(..., description="User-agent details (OS + browser or handset model)")
    viewport_width: int = Field(..., description="CSS pixels – window.innerWidth")
    viewport_height: int = Field(..., description="CSS pixels – window.innerHeight")
    connection_type: str = Field(..., description="Network type: wifi, 4g, etc.")
    visit_start_time: str = Field(..., description="ISO-8601 timestamp when the visit began")
    last_conversation_time: Optional[str] = Field(None, description="ISO-8601 of previous message in this convo, or null")
    user_id: str = Field(..., description="Hashed internal user identifier")
    language: str = Field(..., description="UI language code (e.g. en, fr)")
    timezone: str = Field(..., description="IANA TZ string (e.g. Australia/Brisbane)")
    local_time: str = Field(..., description="User’s local ISO-8601 timestamp")
    location: Location = Field(..., description="Resolved geographic location")
    marketing_opt_in: bool = Field(..., description="True if user opted into marketing")
    app_version: str = Field(..., description="Frontend build or git version")
    widget_version: str = Field(..., description="Chat widget package version")
    navigation_history: List[NavigationClick] = Field(
        ...,
        description="Last 1–20 clicks before chat open (most recent first)",
    )


def use_default_conversation_data() -> ConversationContextData:
    now_utc = datetime.now(timezone.utc).isoformat()

    return ConversationContextData(
        user_first_name="John",
        user_last_name="Doe",
        user_email="John.doe@hotmail.com",
        current_page_url="https://examplebank.com/credit-cards/fees-and-charges",
        page_title="Compare Credit Cards – Example Bank",
        element_clicked_to_initiate_chat="#cc-help-chat",
        device_type="desktop",
        device="macOS 14 / Safari 17.0",
        viewport_width=1440,
        viewport_height=900,
        connection_type="wifi",
        visit_start_time=now_utc,
        last_conversation_time=None,
        user_id=str(uuid.uuid4()),
        language="en",
        timezone="Australia/Brisbane",
        local_time=now_utc,
        location=Location(
            country="Australia",
            region="Queensland",
            city="Brisbane",
            latitude=-27.4679,
            longitude=153.0281,
        ),
        marketing_opt_in=True,
        app_version="web-2.19.7",
        widget_version="chat-1.4.2",
        navigation_history=[
            NavigationClick(order=1, element="#cc-fee-details"),
            NavigationClick(order=2, element="#cc-interest-rate-tab"),
            NavigationClick(order=3, element="#cc-faq-interest-free"),
            NavigationClick(order=4, element="#cc-faq-annual-fee"),
            NavigationClick(order=5, element="#cc-compare-nav"),
            NavigationClick(order=6, element="#cc-terms-download"),
            NavigationClick(order=7, element="#filter-balance-transfer"),
            NavigationClick(order=8, element="#cc-rewards-explainer"),
            NavigationClick(order=9, element="#cc-signup-bonus"),
            NavigationClick(order=10, element="#cc-recalculate-limit"),
            NavigationClick(order=11, element="#main-nav-creditcards"),
            NavigationClick(order=12, element="#hero-cta-learn-more"),
        ],
    )


def main() -> None:
    ctx: ConversationContextData = use_default_conversation_data()
    print(ctx.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
