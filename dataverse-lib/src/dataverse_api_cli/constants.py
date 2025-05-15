"""Constants used throughout the application."""

class ComponentType:
    TOPIC = 0
    SKILL = 1
    BOT_VARIABLE = 2
    BOT_ENTITY = 3
    DIALOG = 4
    TRIGGER = 5
    LANGUAGE_UNDERSTANDING = 6
    LANGUAGE_GENERATION = 7
    DIALOG_SCHEMA = 8
    TOPIC_V2 = 9
    BOT_TRANSLATIONS_V2 = 10
    BOT_ENTITY_V2 = 11
    BOT_VARIABLE_V2 = 12
    SKILL_V2 = 13
    BOT_FILE_ATTACHMENT = 14
    CUSTOM_GPT = 15
    KNOWLEDGE_SOURCE = 16
    EXTERNAL_TRIGGER = 17
    COPILOT_SETTINGS = 18

    @classmethod
    def get_name(cls, component_type: int) -> str:
        """Get the name of a component type."""
        for name, value in vars(cls).items():
            if not name.startswith("_") and isinstance(value, int) and value == component_type:
                return name.replace("_", " ").title()
        return f"Unknown Component Type ({component_type})"

# API Constants
API_VERSION = "v9.2"