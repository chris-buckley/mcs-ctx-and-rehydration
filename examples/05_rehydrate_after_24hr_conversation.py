import os
from dotenv import load_dotenv
import msal


# Load environment variables
load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
TENANT_ID = os.getenv("TENANT_ID")
CLIENT_SECRET = os.getenv("SECRET")
WEB_API_ENDPOINT = os.getenv("WEB_API_ENDPOINT", "").rstrip("/")

# Check env vars
if not all([CLIENT_ID, TENANT_ID, CLIENT_SECRET, WEB_API_ENDPOINT]):
    print("[bold red]Error:[/bold red] Missing required environment variables. Please check your .env file.")
    missing = []
    if not CLIENT_ID: missing.append("CLIENT_ID")
    if not TENANT_ID: missing.append("TENANT_ID")
    if not CLIENT_SECRET: missing.append("SECRET")
    if not WEB_API_ENDPOINT: missing.append("WEB_API_ENDPOINT")
    print(f"Missing variables: {', '.join(missing)}")
    exit(1)

DATAVERSE_ENDPOINT_WITH_API_VERSION = f"{WEB_API_ENDPOINT}/api/data/v9.2"

# Acquire access token
def get_access_token():
    """
    Acquire an access token for the Microsoft Dataverse API.
    Returns:
        str: The access token
    """
    with console.status("[bold green]Acquiring access token...[/bold green]"):
        authority = f"https://login.microsoftonline.com/{TENANT_ID}"
        scope = [f"{WEB_API_ENDPOINT}/.default"]
        app = msal.ConfidentialClientApplication(
            CLIENT_ID, authority=authority, client_credential=CLIENT_SECRET,
        )
        result = app.acquire_token_for_client(scopes=scope)
        if "access_token" in result:
            console.print("[bold green]✓[/bold green] Successfully acquired access token")
            return result["access_token"]
        else:
            console.print(f"[bold red]Error acquiring token:[/bold red] {result.get('error_description')}")
            raise Exception(f"Error acquiring token: {result.get('error_description')}")