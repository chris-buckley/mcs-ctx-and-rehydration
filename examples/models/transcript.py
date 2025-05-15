from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class Message(BaseModel):
    timestamp: str = Field(
        ...,
        description="ISO-8601 UTC timestamp when the message was sent",
    )
    from_id: str = Field(
        ...,
        description="Unique identifier (user, agent, or system) that authored the message",
    )
    message: str = Field(
        ...,
        description="Raw message content in plain text",
    )


class Transcript(BaseModel):
    conversation_id: str = Field(
        ...,
        description="Globally unique identifier for this conversation",
    )
    messages: List[Message] = Field(
        ...,
        description="Chronologically ordered list of messages (oldest first)",
    )
