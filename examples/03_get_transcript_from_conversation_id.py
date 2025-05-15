# This import is specified by the user.
from logging import Logger
from typing import Optional
from dotenv import load_dotenv

from models.transcript import Transcript
from utilities.custom_rich_logger import setup_logger
from utilities.get_transcript_from_conversation_id import get_transcript_from_conversation_id

logger: Logger = setup_logger()

# Load environment variables from .env file
load_dotenv()

if __name__ == "__main__":
    # Ask input for the conversation ID
    conversation_id: str = input("Enter the conversation ID: ")
    
    # Fetch the transcript
    transcript: Optional[Transcript] = get_transcript_from_conversation_id(
        conversation_id=conversation_id
    )
    for msg in transcript.messages:
        logger.info("\nMessage ID: %s", msg.timestamp)
        logger.info("From: %s", msg.from_id)
        logger.info("Text: %s", msg.message)
    
    logger.info("Transcript fetched successfully.")
