"""
Generates a Direct Line v3 token and associated conversation ID.

This script demonstrates how to obtain a short-lived Direct Line token
using a Direct Line Secret. This token can then be used by client applications
(like web chat controls or custom clients) to communicate with a bot.

The process involves making a POST request to the Direct Line token generation
endpoint (e.g., https://directline.botframework.com/v3/directline/tokens/generate)
with the Direct Line Secret included in the Authorization header.

The script requires the `python-dotenv` and `httpx` libraries.
It expects the `DIRECT_LINE_SECRET` to be set in a .env file or as an
environment variable.

Example Usage:
    The script, when run directly, will attempt to generate a token using
    the `DIRECT_LINE_SECRET` from the environment and print the
    conversation ID, a truncated token, and its expiry time. It also shows
    a basic example of how this token could be used with the `AuthenticatedClient`
    from a `directline_client` library (if available).

Note:
    The 'conversationId' returned here is an ID associated with the token.
    If you also pass a 'User.Id' in the request payload (commented out in
    the `generate_direct_line_token` function), this token will be bound
    to that user. This is different from starting a new conversation via
    the `/v3/directline/conversations` endpoint, which returns a full
    Conversation object including a stream URL.
"""
import httpx
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration
DIRECT_LINE_SECRET: str | None = os.getenv("DIRECT_LINE_SECRET")
# Standard global endpoint. Can be overridden by DL_BASE_URL if needed for regional instances.
BASE_URL: str = os.getenv("DL_BASE_URL", "https://directline.botframework.com")
TOKEN_GENERATE_PATH: str = "/v3/directline/tokens/generate"


def generate_direct_line_token(secret: str, base_url: str = BASE_URL) -> tuple[str, str, int]:
    """
    Generates a Direct Line token and conversation ID using the provided secret.

    Args:
        secret: The Direct Line Secret for your bot.
        base_url: The base URL for the Direct Line service.
                  Defaults to "https://directline.botframework.com".

    Returns:
        A tuple containing:
            - conversationId (str): The ID of the conversation associated with the token.
            - token (str): The generated Direct Line token.
            - expires_in (int): The validity duration of the token in seconds.

    Raises:
        httpx.HTTPStatusError: If the token generation request fails.
    """
    headers = {"Authorization": f"Bearer {secret}"}
    url = f"{base_url.rstrip('/')}{TOKEN_GENERATE_PATH}"

    # Optional: To associate a user ID with this token from the start:
    # user_payload = {"User": {"Id": "dl_your_specific_user_id"}}
    # response = httpx.post(url, headers=headers, json=user_payload)
    #
    # Or, for a token not pre-associated with a specific user ID (a user ID
    # will be assigned by Direct Line or can be set in the first activity):
    response = httpx.post(url, headers=headers)

    response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
    data = response.json()
    return data["conversationId"], data["token"], data["expires_in"]


if __name__ == "__main__":
    if DIRECT_LINE_SECRET:
        print(f"Attempting to generate token using base URL: {BASE_URL}")
        try:
            conversation_id, conversation_token, expires_in = generate_direct_line_token(
                DIRECT_LINE_SECRET, BASE_URL
            )
            print(
                f"Successfully generated token for Conversation ID: {conversation_id}")
            # IMPORTANT: Do not log the full token in production environments.
            # The truncated token is for demonstration purposes only.
            print(
                f"Generated Token (first 15 chars): {conversation_token[:15]}...")
            print(
                f"Token expires in: {expires_in} seconds (approx. {expires_in / 60:.1f} minutes)")
            print("-" * 30)

            # Example: Using the generated token with an AuthenticatedClient
            # This part assumes you have a 'directline_client' library available.
            print("\nExample: How to use this token with a Direct Line client:")
            try:
                from directline_client import AuthenticatedClient
                print(
                    f"Initializing AuthenticatedClient with token for conversation: {conversation_id}")
                client = AuthenticatedClient(
                    base_url=BASE_URL,  # Or your specific regional endpoint
                    token=conversation_token
                )
                print("AuthenticatedClient initialized successfully.")
                print("You can now use this 'client' instance to:")
                print("  - Post activities to the conversation (e.g., send messages).")
                print(
                    "  - Start a WebSocket stream to receive activities (if the client supports it or you use the stream URL).")
                print(
                    "  - Reconnect to the conversation using this token until it expires.")
                # Example: You might post an initial activity or connect to a stream.
                # This requires further implementation based on client library capabilities.
                # e.g., client.conversations.conversations_post_activity(conversation_id=conversation_id, ...)
            except ImportError:
                print(
                    "\nNote: 'directline_client' library not found. "
                    "The above is an example of how the token would be used."
                )
            except Exception as client_ex:
                print(f"Error during client example: {client_ex}")

        except httpx.HTTPStatusError as e:
            print(f"Error generating token: HTTP {e.response.status_code}")
            print(f"Response content: {e.response.text}")
        except httpx.RequestError as e:
            print(f"Request error generating token: {e}")
            print(f"Attempted to connect to: {e.request.url}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    else:
        print("Error: DIRECT_LINE_SECRET not found.")
        print("Please set it as an environment variable or in a .env file.")
