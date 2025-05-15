"""Authentication client for Microsoft services."""

import msal

from dataverse_api_cli.utils.console import console
from dataverse_api_cli.config import config

def get_access_token() -> str:
    """
    Acquire an access token for the Microsoft Dataverse API.
    
    Returns:
        str: The access token
        
    Raises:
        Exception: If token acquisition fails
    """
    with console.status("[bold green]Acquiring access token...[/bold green]"):
        app = msal.ConfidentialClientApplication(
            config["client_id"],
            authority=config["authority"],
            client_credential=config["client_secret"],
        )
        
        result = app.acquire_token_for_client(scopes=config["scope"])
        
        if "access_token" in result:
            console.print("[bold green]✓[/bold green] Successfully acquired access token")
            return result["access_token"]
        else:
            error_msg = f"Error acquiring token: {result.get('error_description')}"
            console.print(f"[bold red]Error:[/bold red] {error_msg}")
            raise Exception(error_msg)