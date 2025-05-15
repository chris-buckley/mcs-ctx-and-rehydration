"""Dataverse API client."""

from typing import Dict, Any, List, Optional, Union
import httpx

from dataverse_api_cli.utils.console import console

class DataverseClient:
    """Client for interacting with Microsoft Dataverse API"""
    
    def __init__(self, base_url: str, access_token: str, timeout: float = 30.0):
        """
        Initialize the Dataverse client
        
        Args:
            base_url (str): The base URL for the Dataverse API
            access_token (str): The access token for authentication
            timeout (float): Request timeout in seconds
        """
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/json",
            "OData-MaxVersion": "4.0",
            "OData-Version": "4.0",
            "Content-Type": "application/json"
        }
        # Create a client with default timeout
        self.client = httpx.Client(timeout=timeout)
    
    def request(
        self, 
        endpoint: str, 
        method: str = "GET", 
        data: Optional[Dict[str, Any]] = None, 
        params: Optional[Dict[str, str]] = None
    ) -> Optional[Dict[str, Any]]:
        """
        Make a request to the Dataverse API
        
        Args:
            endpoint (str): The API endpoint to call
            method (str): The HTTP method to use
            data (dict, optional): The data to send in the request body
            params (dict, optional): The query parameters to include
            
        Returns:
            dict: The JSON response from the API
            
        Raises:
            httpx.HTTPStatusError: If the request fails
        """
        url = f"{self.base_url}/{endpoint}"
        
        try:
            response = self.client.request(
                method, 
                url, 
                json=data, 
                params=params,
                headers=self.headers
            )
            response.raise_for_status()
                
            # Return None for empty responses (like 204 No Content)
            if not response.content:
                return None
                
            # Parse JSON only when there's content
            return response.json()
            
        except httpx.HTTPStatusError as e:
            console.print(f"[bold red]HTTP Error:[/bold red] {e}")
            # Try to extract more information from the response
            if e.response.content:
                try:
                    error_details = e.response.json()
                    console.print(f"Error details: {error_details}")
                except Exception:
                    console.print(f"Response content: {e.response.content.decode('utf-8')}")
            raise
        
        except httpx.RequestError as e:
            console.print(f"[bold red]Request Error:[/bold red] {e}")
            raise
    
    def get_entities(
        self, 
        entity_name: str, 
        select: Optional[Union[List[str], str]] = None, 
        filter: Optional[str] = None, 
        expand: Optional[Union[Dict[str, List[str]], str]] = None, 
        top: Optional[int] = None, 
        order_by: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Get entities from Dataverse with support for OData query parameters
        
        Args:
            entity_name (str): The name of the entity to query
            select (list or str, optional): Fields to select
            filter (str, optional): OData filter expression
            expand (dict or str, optional): Related entities to expand
            top (int, optional): Maximum number of records to return
            order_by (str, optional): Field to order results by
            
        Returns:
            list: List of entities matching the query
        """
        params = {}
        
        # Handle select parameter - convert list to comma-separated string
        if select:
            if isinstance(select, list):
                params["$select"] = ",".join(select)
            else:
                params["$select"] = select
        
        if filter:
            params["$filter"] = filter
        
        # Handle expand parameter - convert dict to OData format
        if expand:
            if isinstance(expand, dict):
                expand_parts = []
                for relationship, fields in expand.items():
                    if fields:
                        expand_parts.append(f"{relationship}($select={','.join(fields)})")
                    else:
                        expand_parts.append(relationship)
                params["$expand"] = ",".join(expand_parts)
            else:
                params["$expand"] = expand
        
        if top:
            params["$top"] = str(top)
        
        if order_by:
            params["$orderby"] = order_by
        
        response = self.request(entity_name, params=params)
        return response.get("value", []) if response else []
    
    def get_entity_by_id(
        self, 
        entity_name: str, 
        entity_id: str, 
        select: Optional[str] = None, 
        expand: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Get a specific entity by ID
        
        Args:
            entity_name (str): The name of the entity
            entity_id (str): The ID of the entity
            select (str, optional): The $select query parameter
            expand (str, optional): The $expand query parameter
            
        Returns:
            dict: The entity data
        """
        params = {}
        if select:
            params["$select"] = select
        if expand:
            params["$expand"] = expand
            
        return self.request(f"{entity_name}({entity_id})", params=params)
    
    def create_entity(self, entity_name: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new entity
        
        Args:
            entity_name (str): The name of the entity to create
            data (dict): The entity data
            
        Returns:
            dict: The created entity
        """
        return self.request(entity_name, method="POST", data=data)
    
    def update_entity(self, entity_name: str, entity_id: str, data: Dict[str, Any]) -> None:
        """
        Update an existing entity
        
        Args:
            entity_name (str): The name of the entity to update
            entity_id (str): The ID of the entity to update
            data (dict): The updated entity data
        """
        self.request(f"{entity_name}({entity_id})", method="PATCH", data=data)
    
    def delete_entity(self, entity_name: str, entity_id: str) -> None:
        """
        Delete an entity
        
        Args:
            entity_name (str): The name of the entity to delete
            entity_id (str): The ID of the entity to delete
        """
        self.request(f"{entity_name}({entity_id})", method="DELETE")

    def close(self) -> None:
        """Close the httpx client"""
        self.client.close()