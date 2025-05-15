"""Models for entity management."""

from typing import Dict, Any, List, Optional
import yaml

from dataverse_api_cli.clients.dataverse import DataverseClient

class EntityManager:
    """
    Manager class for Dataverse entity operations.
    """
    
    def __init__(self, client: DataverseClient):
        """
        Initialize the entity manager.
        
        Args:
            client (DataverseClient): The Dataverse client
        """
        self.client = client
        
    def get_by_name(self, entity_type: str, name: str) -> Optional[Dict[str, Any]]:
        """
        Get an entity by name.
        
        Args:
            entity_type (str): The type of entity (e.g., "bots", "contacts")
            name (str): The name of the entity
            
        Returns:
            Optional[Dict[str, Any]]: The entity object, or None if not found
        """
        entities = self.client.get_entities(entity_name=entity_type, filter=f"contains(name, '{name}')")
        return entities[0] if entities else None
    
    def get_by_id(self, entity_type: str, entity_id: str) -> Optional[Dict[str, Any]]:
        """
        Get an entity by ID.
        
        Args:
            entity_type (str): The type of entity (e.g., "bots", "contacts")
            entity_id (str): The ID of the entity
            
        Returns:
            Optional[Dict[str, Any]]: The entity object, or None if not found
        """
        return self.client.get_entity_by_id(entity_name=entity_type, entity_id=entity_id)
    
    def get_related_entities(
        self, 
        entity_type: str, 
        entity_id: str, 
        relationship_name: str,
        filter: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Get entities related to the specified entity.
        
        Args:
            entity_type (str): The type of entity (e.g., "bots", "contacts")
            entity_id (str): The ID of the entity
            relationship_name (str): The name of the relationship
            filter (str, optional): Additional filter expression
            
        Returns:
            List[Dict[str, Any]]: List of related entities
        """
        # Build filter for related entities
        filters = [f"_parentid_value eq '{entity_id}'"]
        
        if filter:
            filters.append(filter)
            
        filter_expr = " and ".join(filters)
            
        return self.client.get_entities(entity_name=relationship_name, filter=filter_expr)
    
    def update_yaml_field(self, entity_type: str, entity_id: str, field_name: str, field_value: str) -> None:
        """
        Update a YAML field in an entity's data.
        
        Args:
            entity_type (str): The type of entity (e.g., "botcomponents")
            entity_id (str): The ID of the entity
            field_name (str): The name of the field to update in the YAML data
            field_value (str): The new value for the field
        """
        # Get current entity data
        entity = self.client.get_entity_by_id(entity_name=entity_type, entity_id=entity_id)
        
        if not entity or "data" not in entity:
            raise ValueError(f"Entity {entity_type} with ID {entity_id} not found or has no data field")
            
        # Parse YAML data
        yaml_data = yaml.safe_load(entity["data"])
        
        # Update field
        yaml_data[field_name] = field_value
        
        # Dump YAML data with Windows line endings (CRLF)
        dumped_yaml = yaml.dump(yaml_data, default_flow_style=False)
        updated_yaml = dumped_yaml.replace('\n', '\r\n')
        
        # Update the entity
        self.client.update_entity(
            entity_name=entity_type,
            entity_id=entity_id,
            data={"data": updated_yaml}
        )
    
    def get_yaml_field(self, entity_type: str, entity_id: str, field_name: str) -> Optional[str]:
        """
        Get a YAML field from an entity's data.
        
        Args:
            entity_type (str): The type of entity (e.g., "botcomponents")
            entity_id (str): The ID of the entity
            field_name (str): The name of the field to get from the YAML data
            
        Returns:
            Optional[str]: The value of the field, or None if not found
        """
        # Get current entity data
        entity = self.client.get_entity_by_id(entity_name=entity_type, entity_id=entity_id)
        
        if not entity or "data" not in entity:
            raise ValueError(f"Entity {entity_type} with ID {entity_id} not found or has no data field")
            
        # Parse YAML data
        yaml_data = yaml.safe_load(entity["data"])
        
        # Return field value
        return yaml_data.get(field_name)