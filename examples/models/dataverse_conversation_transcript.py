import datetime
import uuid
from enum import Enum
from typing import Optional, Literal
from pydantic import BaseModel, Field

# Enums for Dataverse Choice/Option sets
class ConversationTranscriptState(Enum):
    """
    Status of the conversationtranscript
    """
    ACTIVE = 0
    INACTIVE = 1

class ConversationTranscriptStatus(Enum):
    """
    Reason for the status of the conversationtranscript
    """
    ACTIVE = 1 # Corresponds to State.ACTIVE
    INACTIVE = 2 # Corresponds to State.INACTIVE

class ConversationTranscript(BaseModel):
    """
    Contains the transcripts of conversations between participants such as customers, Virtual Agents or Human agents.
    
    Dataverse Table: conversationtranscript
    Primary ID Attribute: conversationtranscriptid
    Primary Name Attribute: name
    """

    # --- Writable columns/attributes ---

    # Logical Name: bot_conversationtranscriptid
    # Display Name: bot_conversationtranscript
    # Description: Conversation Transcripts related to customer interactions with a Bot
    # Type: Lookup (Targets: bot)
    # Required Level: None
    bot_conversationtranscript_id: Optional[uuid.UUID] = Field(
        None,
        alias="bot_conversationtranscriptid",
        description="Unique identifier of the bot conversation transcript related to customer interactions with a Bot."
    )

    # Logical Name: content
    # Display Name: Content
    # Description: Content of the conversation
    # Type: Memo
    # Required Level: ApplicationRequired
    content: str = Field(
        ..., # Required
        alias="content",
        description="Content of the conversation."
    )

    # Logical Name: conversationstarttime
    # Display Name: ConversationStartTime
    # Description: The actual start time of the conversation (not the time it was written to the data store)
    # Type: DateTime
    # Required Level: ApplicationRequired
    conversation_start_time: datetime.datetime = Field(
        ..., # Required
        alias="conversationstarttime",
        description="The actual start time of the conversation (not the time it was written to the data store)."
    )

    # Logical Name: conversationtranscriptid
    # Display Name: conversationtranscript
    # Description: Unique identifier for entity instances
    # Type: Uniqueidentifier
    # Required Level: SystemRequired (but typically system-generated on creation)
    conversationtranscript_id: Optional[uuid.UUID] = Field(
        None,
        alias="conversationtranscriptid",
        description="Unique identifier for conversation transcript entity instances."
    )

    # Logical Name: importsequencenumber
    # Display Name: Import Sequence Number
    # Description: Sequence number of the import that created this record.
    # Type: Integer
    # Required Level: None
    import_sequence_number: Optional[int] = Field(
        None,
        alias="importsequencenumber",
        description="Sequence number of the import that created this record."
    )

    # Logical Name: metadata
    # Display Name: Metadata
    # Description: Any metadata about the conversation being captured such as the schema version, state, agents, participants, etc if applicable.
    # Type: Memo
    # Required Level: None
    metadata: Optional[str] = Field(
        None,
        alias="metadata",
        description="Any metadata about the conversation being captured (e.g., schema version, state, agents, participants)."
    )

    # Logical Name: name
    # Display Name: Name
    # Description: The name of the custom entity. (PrimaryNameAttribute)
    # Type: String
    # Required Level: None
    name: Optional[str] = Field(
        None,
        alias="name",
        description="The name of the custom entity."
    )

    # Logical Name: overriddencreatedon
    # Display Name: Record Created On
    # Description: Date and time that the record was migrated.
    # Type: DateTime
    # Required Level: None
    overridden_created_on: Optional[datetime.datetime] = Field(
        None,
        alias="overriddencreatedon",
        description="Date and time that the record was migrated."
    )

    # Logical Name: ownerid
    # Display Name: Owner
    # Description: Owner Id
    # Type: Owner (Targets: systemuser, team)
    # Required Level: SystemRequired (often defaults if not explicitly set)
    owner_id: Optional[uuid.UUID] = Field(
        None,
        alias="ownerid",
        description="Unique identifier of the owner (user or team)."
    )

    # Logical Name: owneridtype
    # Display Name: (empty)
    # Description: Owner Id Type
    # Type: EntityName
    # Required Level: SystemRequired (derived from owner_id)
    owner_id_type: Optional[Literal["systemuser", "team"]] = Field(
        None,
        alias="owneridtype",
        description="Type of the owner (systemuser or team)."
    )

    # Logical Name: schematype
    # Display Name: SchemaType
    # Description: This defines the type of schema used for the conversation based on format used by the application writing this conversation (PVA, Omni-Channel, OBI, etc)
    # Type: String
    # Required Level: None
    schema_type: Optional[str] = Field(
        None,
        alias="schematype",
        description="Defines the type of schema used for the conversation based on the writing application's format (e.g., PVA, Omni-Channel)."
    )

    # Logical Name: schemaversion
    # Display Name: ContentSchemaVersion
    # Description: The version of the conversation transcript content schema that is used.
    # Type: String
    # Required Level: None
    schema_version: Optional[str] = Field(
        None,
        alias="schemaversion",
        description="The version of the conversation transcript content schema that is used."
    )

    # Logical Name: statecode
    # Display Name: Status
    # Description: Status of the conversationtranscript
    # Type: State
    # Required Level: SystemRequired
    state_code: ConversationTranscriptState = Field(
        ..., # Required
        alias="statecode",
        description="Status of the conversation transcript."
    )

    # Logical Name: statuscode
    # Display Name: Status Reason
    # Description: Reason for the status of the conversationtranscript
    # Type: Status
    # Required Level: None
    status_code: Optional[ConversationTranscriptStatus] = Field(
        None,
        alias="statuscode",
        description="Reason for the status of the conversation transcript."
    )

    # Logical Name: timezoneruleversionnumber
    # Display Name: Time Zone Rule Version Number
    # Description: For internal use only.
    # Type: Integer
    # Required Level: None
    time_zone_rule_version_number: Optional[int] = Field(
        None,
        alias="timezoneruleversionnumber",
        description="For internal use only."
    )

    # Logical Name: utcconversiontimezonecode
    # Display Name: UTC Conversion Time Zone Code
    # Description: Time zone code that was in use when the record was created.
    # Type: Integer
    # Required Level: None
    utc_conversion_time_zone_code: Optional[int] = Field(
        None,
        alias="utcconversiontimezonecode",
        description="Time zone code that was in use when the record was created."
    )

    # --- Read-only columns/attributes ---

    # Logical Name: createdby
    # Display Name: Created By
    # Description: Unique identifier of the user who created the record.
    # Type: Lookup (Targets: systemuser)
    # Required Level: None
    created_by: Optional[uuid.UUID] = Field(
        None,
        alias="createdby",
        description="Unique identifier of the user who created the record."
    )

    # Logical Name: createdon
    # Display Name: Created On
    # Description: Date and time when the record was created.
    # Type: DateTime
    # Required Level: None
    created_on: Optional[datetime.datetime] = Field(
        None,
        alias="createdon",
        description="Date and time when the record was created."
    )

    # Logical Name: createdonbehalfby
    # Display Name: Created By (Delegate)
    # Description: Unique identifier of the delegate user who created the record.
    # Type: Lookup (Targets: systemuser)
    # Required Level: None
    created_on_behalf_by: Optional[uuid.UUID] = Field(
        None,
        alias="createdonbehalfby",
        description="Unique identifier of the delegate user who created the record."
    )

    # Logical Name: modifiedby
    # Display Name: Modified By
    # Description: Unique identifier of the user who modified the record.
    # Type: Lookup (Targets: systemuser)
    # Required Level: None
    modified_by: Optional[uuid.UUID] = Field(
        None,
        alias="modifiedby",
        description="Unique identifier of the user who modified the record."
    )

    # Logical Name: modifiedon
    # Display Name: Modified On
    # Description: Date and time when the record was modified.
    # Type: DateTime
    # Required Level: None
    modified_on: Optional[datetime.datetime] = Field(
        None,
        alias="modifiedon",
        description="Date and time when the record was modified."
    )

    # Logical Name: modifiedonbehalfby
    # Display Name: Modified By (Delegate)
    # Description: Unique identifier of the delegate user who modified the record.
    # Type: Lookup (Targets: systemuser)
    # Required Level: None
    modified_on_behalf_by: Optional[uuid.UUID] = Field(
        None,
        alias="modifiedonbehalfby",
        description="Unique identifier of the delegate user who modified the record."
    )

    # Logical Name: owneridname
    # Display Name: (empty)
    # Description: Name of the owner
    # Type: String
    # Required Level: SystemRequired (derived, read-only)
    owner_id_name: Optional[str] = Field(
        None,
        alias="owneridname",
        description="Name of the owner."
    )

    # Logical Name: owneridyominame
    # Display Name: (empty)
    # Description: Yomi name of the owner
    # Type: String
    # Required Level: SystemRequired (derived, read-only)
    owner_id_yomi_name: Optional[str] = Field(
        None,
        alias="owneridyominame",
        description="Yomi name of the owner."
    )

    # Logical Name: owningbusinessunit
    # Display Name: Owning Business Unit
    # Description: Unique identifier for the business unit that owns the record
    # Type: Lookup (Targets: businessunit)
    # Required Level: None
    owning_business_unit: Optional[uuid.UUID] = Field(
        None,
        alias="owningbusinessunit",
        description="Unique identifier for the business unit that owns the record."
    )

    # Logical Name: owningteam
    # Display Name: Owning Team
    # Description: Unique identifier for the team that owns the record.
    # Type: Lookup (Targets: team)
    # Required Level: None
    owning_team: Optional[uuid.UUID] = Field(
        None,
        alias="owningteam",
        description="Unique identifier for the team that owns the record."
    )

    # Logical Name: owninguser
    # Display Name: Owning User
    # Description: Unique identifier for the user that owns the record.
    # Type: Lookup (Targets: systemuser)
    # Required Level: None
    owning_user: Optional[uuid.UUID] = Field(
        None,
        alias="owninguser",
        description="Unique identifier for the user that owns the record."
    )

    # Logical Name: versionnumber
    # Display Name: Version Number
    # Description: Version Number
    # Type: BigInt
    # Required Level: None
    version_number: Optional[int] = Field(
        None,
        alias="versionnumber",
        description="Version Number of the record."
    )

    class Config:
        populate_by_name = True # Allows instantiation using either field name or alias
        use_enum_values = True  # Use enum values (int) instead of enum members for serialization

# Example Usage (optional, for demonstration)
if __name__ == "__main__":
    # Example of creating a new conversation transcript (minimum required fields)
    new_transcript = ConversationTranscript(
        content="Hello, how can I help you today?",
        conversation_start_time=datetime.datetime.now(),
        state_code=ConversationTranscriptState.ACTIVE,
        name="Customer Service Chat 123"
    )
    print("New Transcript (minimum fields):")
    print(new_transcript.model_dump_json(indent=2))

    # Example of a fully populated transcript (simulating a retrieved record)
    retrieved_transcript = ConversationTranscript(
        conversationtranscript_id=uuid.uuid4(),
        bot_conversationtranscript_id=uuid.uuid4(),
        content="Agent: How can I assist you further? Customer: I have another question.",
        conversation_start_time=datetime.datetime(2023, 10, 26, 10, 0, 0),
        import_sequence_number=1,
        metadata='{"schema_version": "1.0", "participants": ["customer", "agent"]}',
        name="Online Support Chat Session",
        overridden_created_on=datetime.datetime(2023, 10, 25),
        owner_id=uuid.uuid4(),
        owner_id_type="systemuser",
        schema_type="Omni-Channel",
        schema_version="1.0",
        state_code=ConversationTranscriptState.ACTIVE,
        status_code=ConversationTranscriptStatus.ACTIVE,
        time_zone_rule_version_number=42,
        utc_conversion_time_zone_code=252,
        created_by=uuid.uuid4(),
        created_on=datetime.datetime(2023, 10, 26, 9, 58, 0),
        modified_by=uuid.uuid4(),
        modified_on=datetime.datetime(2023, 10, 26, 10, 30, 0),
        owner_id_name="John Doe",
        owning_business_unit=uuid.uuid4(),
        version_number=123456789
    )
    print("\nRetrieved Transcript (full fields):")
    print(retrieved_transcript.model_dump_json(indent=2))

    # Accessing fields using Pythonic names
    print(f"\nTranscript content: {retrieved_transcript.content}")
    print(f"Transcript ID: {retrieved_transcript.conversationtranscript_id}")
    print(f"Transcript State: {retrieved_transcript.state_code.name} (Value: {retrieved_transcript.state_code.value})")

    # Accessing fields using Dataverse alias (requires populate_by_name=True)
    retrieved_from_alias = ConversationTranscript.model_validate({"content": "Test alias", "conversationstarttime": "2023-01-01T12:00:00", "statecode": 0})
    print(f"\nContent from alias: {retrieved_from_alias.content}")