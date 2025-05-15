"""Configuration module for Dataverse API CLI."""

import os
from typing import Dict, Any
from dotenv import load_dotenv

from dataverse_api_cli.utils.console import console
from dataverse_api_cli.constants import API_VERSION

# Load environment variables
load_dotenv()

# Required environment variables
REQUIRED_ENV_VARS = ["CLIENT_ID", "TENANT_ID", "CLIENT_SECRET", "WEB_API_ENDPOINT"]

def load_config() -> Dict[str, Any]:
    """
    Load configuration from environment variables.
    
    Returns:
        Dict[str, Any]: Configuration dictionary
    
    Raises:
        SystemExit: If any required environment variables are missing
    """
    # Check for required env vars
    missing = [var for var in REQUIRED_ENV_VARS if not os.getenv(var)]
    
    if missing:
        console.print("[bold red]Error:[/bold red] Missing required environment variables.")
        console.print(f"Missing variables: {', '.join(missing)}")
        console.print("Please check your .env file.")
        raise SystemExit(1)
    
    # Create configuration dictionary
    config = {
        "client_id": os.getenv("CLIENT_ID"),
        "tenant_id": os.getenv("TENANT_ID"),
        "client_secret": os.getenv("CLIENT_SECRET"),
        "web_api_endpoint": os.getenv("WEB_API_ENDPOINT", "").rstrip("/"),
    }
    
    # Add derived configuration
    config["dataverse_endpoint"] = f"{config['web_api_endpoint']}/api/data/{API_VERSION}"
    config["authority"] = f"https://login.microsoftonline.com/{config['tenant_id']}"
    config["scope"] = [f"{config['web_api_endpoint']}/.default"]
    
    return config

# Export the config
config = load_config()