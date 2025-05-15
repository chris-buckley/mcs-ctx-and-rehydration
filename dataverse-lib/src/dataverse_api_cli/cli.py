"""Command-line interface for Dataverse API CLI."""

import sys
import json
import click
from typing import Optional, List, Dict, Any
import yaml

from dataverse_api_cli.utils.console import console, create_table
from dataverse_api_cli.clients.auth import get_access_token
from dataverse_api_cli.clients.dataverse import DataverseClient
from dataverse_api_cli.models.entities import EntityManager
from dataverse_api_cli.config import config
from dataverse_api_cli.constants import ComponentType

@click.group()
@click.version_option()
def cli():
    """Dataverse API CLI - A command-line tool for interacting with Microsoft Dataverse."""
    pass

# Entity Commands

@cli.group()
def entity():
    """Commands for working with Dataverse entities."""
    pass

@entity.command(name="list")
@click.argument("entity_name")
@click.option("--select", help="Comma-separated list of fields to select")
@click.option("--filter", help="OData filter expression")
@click.option("--top", type=int, help="Maximum number of records to return")
@click.option("--order-by", help="Field to order results by")
@click.option("--format", type=click.Choice(["table", "json"]), default="table", help="Output format")
def list_entities(entity_name, select, filter, top, order_by, format):
    """
    List entities from Dataverse.
    
    Examples:
    
        dataverse-api entity list contacts --select=fullname,emailaddress1 --filter="contains(emailaddress1, 'example.com')"
        
        dataverse-api entity list bots --filter="contains(name, 'MyBot')" --format=json
    """
    try:
        access_token = get_access_token()
        client = DataverseClient(config["dataverse_endpoint"], access_token)
        
        # Process select option
        select_fields = select.split(",") if select else None
        
        # Get entities
        entities = client.get_entities(
            entity_name=entity_name,
            select=select_fields,
            filter=filter,
            top=top,
            order_by=order_by
        )
        
        if format == "json":
            console.print_json(json.dumps(entities))
            return
        
        # Display as table
        if not entities:
            console.print(f"No {entity_name} found matching the criteria.")
            return
            
        # Get fields to display
        if select_fields:
            display_fields = select_fields
        else:
            # Get fields from first entity
            display_fields = list(entities[0].keys())
            # Remove some common fields that are not useful for display
            for field in ["@odata.etag", "versionnumber", "createdon", "modifiedon"]:
                if field in display_fields:
                    display_fields.remove(field)
            # Limit to a reasonable number of fields
            display_fields = display_fields[:5]
        
        # Create table
        table = create_table(f"{entity_name.title()} ({len(entities)})", display_fields)
        
        # Add rows
        for entity in entities:
            row = []
            for field in display_fields:
                value = entity.get(field, "")
                # Truncate long values
                if isinstance(value, str) and len(value) > 50:
                    value = value[:47] + "..."
                row.append(str(value))
            table.add_row(*row)
        
        console.print(table)
        
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)
    finally:
        if 'client' in locals():
            client.close()

@entity.command(name="get")
@click.argument("entity_name")
@click.argument("entity_id")
@click.option("--select", help="Comma-separated list of fields to select")
@click.option("--expand", help="Comma-separated list of relationships to expand")
@click.option("--format", type=click.Choice(["table", "json"]), default="table", help="Output format")
def get_entity(entity_name, entity_id, select, expand, format):
    """
    Get a specific entity by ID.
    
    Examples:
    
        dataverse-api entity get contacts 00000000-0000-0000-0000-000000000001
        
        dataverse-api entity get bots 00000000-0000-0000-0000-000000000001 --format=json
    """
    try:
        access_token = get_access_token()
        client = DataverseClient(config["dataverse_endpoint"], access_token)
        
        entity = client.get_entity_by_id(
            entity_name=entity_name,
            entity_id=entity_id,
            select=select,
            expand=expand
        )
        
        if format == "json":
            console.print_json(json.dumps(entity))
            return
        
        # Display as table
        if not entity:
            console.print(f"No {entity_name} found with ID {entity_id}.")
            return
            
        # Create table
        table = create_table(f"{entity_name.title()} Details", ["Field", "Value"])
        
        # Add rows
        for field, value in entity.items():
            # Skip @odata fields
            if field.startswith("@odata"):
                continue
            
            # Format value
            if isinstance(value, dict) or isinstance(value, list):
                formatted_value = json.dumps(value, indent=2)
            else:
                formatted_value = str(value)
                
            # Truncate long values
            if len(formatted_value) > 80:
                formatted_value = formatted_value[:77] + "..."
                
            table.add_row(field, formatted_value)
        
        console.print(table)
        
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)
    finally:
        if 'client' in locals():
            client.close()

@entity.command(name="create")
@click.argument("entity_name")
@click.argument("data_file", type=click.Path(exists=True, readable=True))
def create_entity(entity_name, data_file):
    """
    Create a new entity.
    
    DATA_FILE should be a JSON file containing the entity data.
    
    Examples:
    
        dataverse-api entity create contacts contact_data.json
        
        dataverse-api entity create bots bot_data.json
    """
    try:
        # Load data from file
        with open(data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        access_token = get_access_token()
        client = DataverseClient(config["dataverse_endpoint"], access_token)
        
        # Create entity
        result = client.create_entity(entity_name, data)
        
        console.print(f"[bold green]✓[/bold green] Successfully created {entity_name} entity")
        console.print(f"Entity ID: {result.get('id', 'Unknown')}")
        
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)
    finally:
        if 'client' in locals():
            client.close()

@entity.command(name="update")
@click.argument("entity_name")
@click.argument("entity_id")
@click.argument("data_file", type=click.Path(exists=True, readable=True))
def update_entity(entity_name, entity_id, data_file):
    """
    Update an existing entity.
    
    DATA_FILE should be a JSON file containing the entity data to update.
    
    Examples:
    
        dataverse-api entity update contacts 00000000-0000-0000-0000-000000000001 contact_updates.json
        
        dataverse-api entity update bots 00000000-0000-0000-0000-000000000001 bot_updates.json
    """
    try:
        # Load data from file
        with open(data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        access_token = get_access_token()
        client = DataverseClient(config["dataverse_endpoint"], access_token)
        
        # Update entity
        client.update_entity(entity_name, entity_id, data)
        
        console.print(f"[bold green]✓[/bold green] Successfully updated {entity_name} entity with ID {entity_id}")
        
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)
    finally:
        if 'client' in locals():
            client.close()

@entity.command(name="delete")
@click.argument("entity_name")
@click.argument("entity_id")
@click.option("--confirm/--no-confirm", default=True, help="Confirm before deleting")
def delete_entity(entity_name, entity_id, confirm):
    """
    Delete an entity.
    
    Examples:
    
        dataverse-api entity delete contacts 00000000-0000-0000-0000-000000000001
        
        dataverse-api entity delete bots 00000000-0000-0000-0000-000000000001 --no-confirm
    """
    try:
        if confirm and not click.confirm(f"Are you sure you want to delete the {entity_name} entity with ID {entity_id}?"):
            console.print("Deletion cancelled.")
            return
        
        access_token = get_access_token()
        client = DataverseClient(config["dataverse_endpoint"], access_token)
        
        # Delete entity
        client.delete_entity(entity_name, entity_id)
        
        console.print(f"[bold green]✓[/bold green] Successfully deleted {entity_name} entity with ID {entity_id}")
        
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)
    finally:
        if 'client' in locals():
            client.close()

# Bot Commands

@cli.group()
def bot():
    """Commands for working with Dataverse bots."""
    pass

@bot.command(name="list")
@click.option("--filter", help="OData filter expression")
@click.option("--format", type=click.Choice(["table", "json"]), default="table", help="Output format")
def list_bots(filter, format):
    """
    List bots from Dataverse.
    
    Examples:
    
        dataverse-api bot list
        
        dataverse-api bot list --filter="contains(name, 'MyBot')" --format=json
    """
    try:
        access_token = get_access_token()
        client = DataverseClient(config["dataverse_endpoint"], access_token)
        
        # Get bots
        bots = client.get_entities(
            entity_name="bots",
            select=["botid", "name", "statecode"],
            filter=filter
        )
        
        if format == "json":
            console.print_json(json.dumps(bots))
            return
        
        # Display as table
        if not bots:
            console.print("No bots found matching the criteria.")
            return
            
        # Create table
        table = create_table(f"Bots ({len(bots)})", ["Bot ID", "Name", "State"])
        
        # Add rows
        for bot in bots:
                
            state = "Active" if bot.get("statecode") == 0 else "Inactive"
            
            table.add_row(
                bot.get("botid", ""),
                bot.get("name", ""),
                state
            )
        
        console.print(table)
        
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)
    finally:
        if 'client' in locals():
            client.close()

@bot.command(name="get")
@click.argument("bot_name_or_id")
@click.option("--format", type=click.Choice(["table", "json"]), default="table", help="Output format")
def get_bot(bot_name_or_id, format):
    """
    Get a specific bot by name or ID.
    
    Examples:
    
        dataverse-api bot get "My Bot"
        
        dataverse-api bot get 00000000-0000-0000-0000-000000000001 --format=json
    """
    try:
        access_token = get_access_token()
        client = DataverseClient(config["dataverse_endpoint"], access_token)
        entity_manager = EntityManager(client)
        
        # Check if bot_name_or_id is a GUID
        is_guid = len(bot_name_or_id) == 36 and bot_name_or_id.count('-') == 4
        
        if is_guid:
            bot = entity_manager.get_by_id("bots", bot_name_or_id)
        else:
            # Get bot by name
            bot = entity_manager.get_by_name("bots", bot_name_or_id)
        
        if not bot:
            console.print(f"No bot found with name or ID '{bot_name_or_id}'.")
            return
        
        if format == "json":
            console.print_json(json.dumps(bot))
            return
        
        # Display as table
        table = create_table(f"Bot: {bot.get('name', 'Unknown')}", ["Field", "Value"])
        
        # Add rows for important fields
        for field in ["botid", "name", "description", "statecode"]:
            value = bot.get(field, "")
            if field == "statecode":
                value = "Active" if value == 0 else "Inactive"
            table.add_row(field, str(value))
        
        console.print(table)
        
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)
    finally:
        if 'client' in locals():
            client.close()

@bot.command(name="components")
@click.argument("bot_name_or_id")
@click.option("--component-type", type=int, help="Filter by component type (e.g., 9 for TOPIC_V2)")
@click.option("--filter", help="Additional OData filter expression")
@click.option("--format", type=click.Choice(["table", "json"]), default="table", help="Output format")
def list_bot_components(bot_name_or_id, component_type, filter, format):
    """
    List components for a specific bot.
    
    Component types:
    0=Topic, 1=Skill, 2=Bot Variable, 3=Bot Entity, 4=Dialog, 5=Trigger,
    6=Language Understanding, 7=Language Generation, 8=Dialog Schema,
    9=Topic V2, 10=Bot Translations V2, 11=Bot Entity V2, 12=Bot Variable V2,
    13=Skill V2, 14=Bot File Attachment, 15=Custom GPT, 16=Knowledge Source,
    17=External Trigger, 18=Copilot Settings
    
    Examples:
    
        dataverse-api bot components "My Bot"
        
        dataverse-api bot components "My Bot" --component-type=9 --format=json
    """
    try:
        access_token = get_access_token()
        client = DataverseClient(config["dataverse_endpoint"], access_token)
        entity_manager = EntityManager(client)
        
        # Check if bot_name_or_id is a GUID
        is_guid = len(bot_name_or_id) == 36 and bot_name_or_id.count('-') == 4
        
        if is_guid:
            bot_id = bot_name_or_id
            # Get bot name for display
            bot = entity_manager.get_by_id("bots", bot_id)
            bot_name = bot["name"] if bot else "Unknown Bot"
        else:
            # Get bot by name
            bot = entity_manager.get_by_name("bots", bot_name_or_id)
            
            if not bot:
                console.print(f"No bot found with name or ID '{bot_name_or_id}'.")
                return
                
            bot_id = bot["botid"]
            bot_name = bot["name"]
        
        # Build filter for components
        filters = [f"_parentbotid_value eq '{bot_id}'"]
        
        if component_type is not None:
            filters.append(f"componenttype eq {component_type}")
            
        if filter:
            filters.append(filter)
            
        filter_expr = " and ".join(filters)
        
        # Get bot components
        components = client.get_entities(
            entity_name="botcomponents",
            filter=filter_expr
        )
        
        if format == "json":
            console.print_json(json.dumps(components))
            return
        
        # Display as table
        if not components:
            console.print(f"No components found for bot '{bot_name}' matching the criteria.")
            return
            
        # Create table
        table = create_table(
            f"Components for Bot: {bot_name} ({len(components)})", 
            ["Component ID", "Name", "Type", "Description"]
        )
        
        # Add rows
        for component in components:
            component_type_value = component.get("componenttype")
            component_type_name = (
                ComponentType.get_name(component_type_value) 
                if component_type_value is not None 
                else "Unknown"
            )
            
            description = ""
            # Try to extract description from data field if available
            if "data" in component:
                try:
                    yaml_data = yaml.safe_load(component["data"])
                    description = yaml_data.get("modelDescription", "")
                except:
                    pass
                    
            # Truncate long description
            if description and len(description) > 50:
                description = description[:47] + "..."
            
            table.add_row(
                component.get("botcomponentid", ""),
                component.get("name", ""),
                component_type_name,
                description
            )
        
        console.print(table)
        
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)
    finally:
        if 'client' in locals():
            client.close()

@bot.command(name="get-component-field")
@click.argument("bot_name_or_id")
@click.argument("component_name_or_id")
@click.argument("field_name")
def get_bot_component_field(bot_name_or_id, component_name_or_id, field_name):
    """
    Get a field from a bot component's YAML data.
    
    Examples:
    
        dataverse-api bot get-component-field "My Bot" "My Topic" modelDescription
    """
    try:
        access_token = get_access_token()
        client = DataverseClient(config["dataverse_endpoint"], access_token)
        entity_manager = EntityManager(client)
        
        # Get the bot
        bot_id = bot_name_or_id
        if not (len(bot_name_or_id) == 36 and bot_name_or_id.count('-') == 4):
            # Get bot by name
            bot = entity_manager.get_by_name("bots", bot_name_or_id)
            if not bot:
                console.print(f"[bold red]Error:[/bold red] Bot '{bot_name_or_id}' not found")
                sys.exit(1)
            bot_id = bot["botid"]
        
        # Get the component
        component_id = component_name_or_id
        if not (len(component_name_or_id) == 36 and component_name_or_id.count('-') == 4):
            # Get component by name
            components = client.get_entities(
                entity_name="botcomponents",
                filter=f"_parentbotid_value eq '{bot_id}' and name eq '{component_name_or_id}'"
            )
            if not components:
                console.print(f"[bold red]Error:[/bold red] Component '{component_name_or_id}' not found for bot '{bot_name_or_id}'")
                sys.exit(1)
            component_id = components[0]["botcomponentid"]
        
        # Get the field value
        field_value = entity_manager.get_yaml_field("botcomponents", component_id, field_name)
        
        # Print the field value
        console.print(field_value)
        
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)
    finally:
        if 'client' in locals():
            client.close()


@bot.command(name="update-component-field")
@click.argument("bot_name_or_id")
@click.argument("component_name_or_id")
@click.argument("field_name")
@click.argument("field_value")
def update_yaml_field(self, entity_name, entity_id, field_name, field_value):
    """
    Update a specific field in a YAML document within an entity record.
    Ensures proper formatting compatible with PowerApps YAML renderer.
    """
    # First, get the current entity data
    entity_data = self.client.get_entity(entity_name, entity_id)
    
    if not entity_data:
        raise Exception(f"Entity {entity_name} with ID {entity_id} not found")
    
    # Find the property containing YAML (likely 'serializeddata' or similar)
    yaml_property = None
    for prop in entity_data:
        if prop.lower().endswith('data') and isinstance(entity_data[prop], str):
            try:
                # Try to parse as YAML to see if this is the right field
                yaml_data = yaml.safe_load(entity_data[prop])
                if isinstance(yaml_data, dict):  # YAML should parse to a dictionary
                    yaml_property = prop
                    break
            except:
                continue
    
    if not yaml_property:
        raise Exception(f"Could not find YAML data property in entity {entity_name}")
    
    # Parse the YAML
    try:
        yaml_content = yaml.safe_load(entity_data[yaml_property])
    except Exception as e:
        raise Exception(f"Failed to parse YAML data: {e}")
    
    # Update the field - support for nested fields using dot notation
    if '.' in field_name:
        # Handle nested fields like 'parent.child.property'
        parts = field_name.split('.')
        current = yaml_content
        for part in parts[:-1]:
            if part not in current:
                current[part] = {}
            current = current[part]
        current[parts[-1]] = field_value
    else:
        # Direct field update
        yaml_content[field_name] = field_value
    
    # Convert back to YAML with consistent formatting
    # Note: Using literal style (|) for multiline strings 
    # and ensuring unix-style line endings
    yaml_str = yaml.dump(
        yaml_content, 
        default_flow_style=False,  # Use block style, not JSON-like flow style
        allow_unicode=True,        # Support unicode characters
        sort_keys=False,           # Preserve key ordering
        width=80,                  # Set reasonable line width
        indent=2                   # Use 2 spaces for indentation
    )
    
    # Ensure LF line endings (unix style) even if on Windows
    yaml_str = yaml_str.replace('\r\n', '\n')
    
    # Update entity
    self.client.update_entity(
        entity_name=entity_name,
        entity_id=entity_id,
        data={
            yaml_property: yaml_str
        }
    )
    
    return True


@bot.command(name="update-component-field")
@click.argument("bot_name_or_id")
@click.argument("component_name_or_id")
@click.argument("field_name")
@click.argument("field_value")
def update_bot_component_field(bot_name_or_id, component_name_or_id, field_name, field_value):
    """
    Update a field in a bot component's YAML data.
    
    Examples:
    
        dataverse-api bot update-component-field "My Bot" "My Topic" modelDescription "New description"
    """
    try:
        access_token = get_access_token()
        client = DataverseClient(config["dataverse_endpoint"], access_token)
        entity_manager = EntityManager(client)
        
        # Get the bot
        bot_id = bot_name_or_id
        if not (len(bot_name_or_id) == 36 and bot_name_or_id.count('-') == 4):
            # Get bot by name
            bot = entity_manager.get_by_name("bots", bot_name_or_id)
            if not bot:
                console.print(f"[bold red]Error:[/bold red] Bot '{bot_name_or_id}' not found")
                sys.exit(1)
            bot_id = bot["botid"]
        
        # Get the component
        component_id = component_name_or_id
        if not (len(component_name_or_id) == 36 and component_name_or_id.count('-') == 4):
            # Get component by name
            components = client.get_entities(
                entity_name="botcomponents",
                filter=f"_parentbotid_value eq '{bot_id}' and name eq '{component_name_or_id}'"
            )
            if not components:
                console.print(f"[bold red]Error:[/bold red] Component '{component_name_or_id}' not found for bot '{bot_name_or_id}'")
                sys.exit(1)
            component_id = components[0]["botcomponentid"]
        
        # Get current component data
        component = entity_manager.get_by_id("botcomponents", component_id)
        
        if not component or "data" not in component:
            console.print(f"[bold red]Error:[/bold red] Component does not contain YAML data")
            sys.exit(1)
            
        # Parse YAML data
        try:
            yaml_data = yaml.safe_load(component["data"])
        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] Failed to parse YAML data: {e}")
            sys.exit(1)
        
        # Update the field (support for nested fields using dot notation)
        if '.' in field_name:
            parts = field_name.split('.')
            current = yaml_data
            for i, part in enumerate(parts):
                if i == len(parts) - 1:
                    current[part] = field_value
                else:
                    if part not in current:
                        current[part] = {}
                    current = current[part]
        else:
            yaml_data[field_name] = field_value
        
        # Convert YAML to string with Windows line endings
        dumped_yaml = yaml.dump(
            yaml_data, 
            default_flow_style=False,  # Use block style formatting
            sort_keys=False,           # Preserve key order
            width=80,                  # Standard line width
            allow_unicode=True,        # Support unicode characters
            indent=2                   # 2-space indentation
        )
        
        # Always use Windows-style line endings as expected by Power Apps
        updated_yaml = dumped_yaml.replace('\n', '\r\n')
        
        # Update the component
        client.update_entity(
            entity_name="botcomponents",
            entity_id=component_id,
            data={"data": updated_yaml}
        )
        
        console.print(f"[bold green]✓[/bold green] Successfully updated field '{field_name}' for component '{component_name_or_id}'")
        
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)
    finally:
        if 'client' in locals():
            client.close()

# Entity Definition Commands

@cli.group(name="entity-definition")
def entity_definition():
    """Commands for working with Dataverse entity definitions."""
    pass

@entity_definition.command(name="list")
@click.option("--filter", help="OData filter expression")
@click.option("--format", type=click.Choice(["table", "json"]), default="table", help="Output format")
def list_entity_definitions(filter, format):
    """
    List entity definitions from Dataverse.
    
    Examples:
    
        dataverse-api entity-definition list
        
        dataverse-api entity-definition list --filter="contains(LogicalName, 'account')" --format=json
    """
    try:
        access_token = get_access_token()
        client = DataverseClient(config["dataverse_endpoint"], access_token)
        
        # Get entity definitions
        entity_defs = client.get_entities(
            entity_name="EntityDefinitions",
            select=["LogicalName", "DisplayName", "Description", "IsCustomEntity"],
            filter=filter,
            order_by="LogicalName"
        )
        
        if format == "json":
            console.print_json(json.dumps(entity_defs))
            return
        
        # Display as table
        if not entity_defs:
            console.print("No entity definitions found matching the criteria.")
            return
            
        # Create table
        table = create_table(
            f"Entity Definitions ({len(entity_defs)})", 
            ["Logical Name", "Display Name", "Custom Entity", "Description"]
        )
        
        # Add rows
        for entity_def in entity_defs:
            display_name = ""
            if "DisplayName" in entity_def:
                display_name = entity_def["DisplayName"].get("UserLocalizedLabel", {}).get("Label", "")
                
            description = ""
            if "Description" in entity_def:
                description = entity_def["Description"].get("UserLocalizedLabel", {}).get("Label", "")
                
            # Truncate long description
            if description and len(description) > 50:
                description = description[:47] + "..."
                
            is_custom = "Yes" if entity_def.get("IsCustomEntity") else "No"
            
            table.add_row(
                entity_def.get("LogicalName", ""),
                display_name,
                is_custom,
                description
            )
        
        console.print(table)
        
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)
    finally:
        if 'client' in locals():
            client.close()

@entity_definition.command(name="get")
@click.argument("entity_logical_name")
@click.option("--format", type=click.Choice(["table", "json"]), default="table", help="Output format")
def get_entity_definition(entity_logical_name, format):
    """
    Get a specific entity definition.
    
    Examples:
    
        dataverse-api entity-definition get account
        
        dataverse-api entity-definition get contact --format=json
    """
    try:
        access_token = get_access_token()
        client = DataverseClient(config["dataverse_endpoint"], access_token)
        
        # Get entity definitions by filter
        entity_defs = client.get_entities(
            entity_name="EntityDefinitions",
            filter=f"LogicalName eq '{entity_logical_name}'",
            expand="Attributes($select=LogicalName,DisplayName,AttributeType,Description)"
        )
        
        if not entity_defs:
            console.print(f"No entity definition found with logical name '{entity_logical_name}'.")
            return
            
        entity_def = entity_defs[0]
        
        if format == "json":
            console.print_json(json.dumps(entity_def))
            return
        
        # Display as table
        display_name = ""
        if "DisplayName" in entity_def:
            display_name = entity_def["DisplayName"].get("UserLocalizedLabel", {}).get("Label", "")
            
        description = ""
        if "Description" in entity_def:
            description = entity_def["Description"].get("UserLocalizedLabel", {}).get("Label", "")
            
        # Create table for entity info
        entity_table = create_table(
            f"Entity Definition: {entity_logical_name}", 
            ["Property", "Value"]
        )
        
        entity_table.add_row("Logical Name", entity_def.get("LogicalName", ""))
        entity_table.add_row("Display Name", display_name)
        entity_table.add_row("Description", description)
        entity_table.add_row("Custom Entity", "Yes" if entity_def.get("IsCustomEntity") else "No")
        
        console.print(entity_table)
        
        # Create table for attributes
        if "Attributes" in entity_def:
            attributes = entity_def["Attributes"]
            
            attr_table = create_table(
                f"Attributes ({len(attributes)})", 
                ["Logical Name", "Display Name", "Type", "Description"]
            )
            
            for attr in attributes:
                attr_display_name = ""
                if "DisplayName" in attr:
                    attr_display_name = attr["DisplayName"].get("UserLocalizedLabel", {}).get("Label", "")
                    
                attr_description = ""
                if "Description" in attr:
                    attr_description = attr["Description"].get("UserLocalizedLabel", {}).get("Label", "")
                    
                # Truncate long description
                if attr_description and len(attr_description) > 50:
                    attr_description = attr_description[:47] + "..."
                    
                attr_table.add_row(
                    attr.get("LogicalName", ""),
                    attr_display_name,
                    attr.get("AttributeType", ""),
                    attr_description
                )
                
            console.print(attr_table)
        
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)
    finally:
        if 'client' in locals():
            client.close()

# Keep the original command for backward compatibility
@cli.command(name="update-model-description")
@click.argument("bot_name")
@click.option("--component-id", help="Specific component ID to update")
@click.option("--component-type", type=int, default=ComponentType.TOPIC_V2, 
              help="Component type to filter by (default: 9 - TOPIC_V2)")
@click.option("--description", help="New model description (interactive prompt if not provided)")
def update_model_description(
    bot_name: str, 
    component_id: Optional[str] = None, 
    component_type: int = ComponentType.TOPIC_V2,
    description: Optional[str] = None
):
    """
    Update model description for a bot component.
    
    Examples:
    
        dataverse-api update-model-description "MyBot"
        
        dataverse-api update-model-description "MyBot" --component-type=9 --description="New description"
    """
    try:
        access_token = get_access_token()
        client = DataverseClient(config["dataverse_endpoint"], access_token)
        entity_manager = EntityManager(client)
        
        # Get the bot
        bot = entity_manager.get_by_name("bots", bot_name)
        
        if not bot:
            console.print(f"[bold red]Error:[/bold red] Bot '{bot_name}' not found")
            sys.exit(1)
            
        # If component_id is not provided, find components by filter
        if not component_id:
            # Build filter for components
            filters = [f"_parentbotid_value eq '{bot['botid']}'"]
            filters.append(f"componenttype eq {component_type}")
            filters.append("contains(data, 'modelDescription')")
            
            filter_expr = " and ".join(filters)
            
            # Get bot components
            components = client.get_entities(
                entity_name="botcomponents",
                filter=filter_expr
            )
            
            if not components:
                console.print(
                    f"[bold red]Error:[/bold red] No components found for bot '{bot_name}' "
                    f"with component type {component_type}"
                )
                sys.exit(1)
                
            component = components[0]
            component_id = component["botcomponentid"]
        else:
            # Get the component directly
            component = client.get_entity_by_id("botcomponents", component_id)
            if not component:
                console.print(f"[bold red]Error:[/bold red] Component with ID {component_id} not found")
                sys.exit(1)
            
        # If description not provided, prompt for it
        if not description:
            # Display current description if available
            try:
                yaml_data = yaml.safe_load(component["data"])
                current_desc = yaml_data.get("modelDescription", "None")
                console.print(f"Current model description: [italic]{current_desc}[/italic]")
            except Exception:
                console.print("[yellow]Could not parse current model description[/yellow]")
            
            description = click.prompt("Enter new model description")
        
        # Parse YAML data
        yaml_data = yaml.safe_load(component["data"])
        
        # Update model description
        yaml_data["modelDescription"] = description
        
        # Dump YAML data with Windows line endings (CRLF)
        dumped_yaml = yaml.dump(yaml_data, default_flow_style=False)
        updated_yaml = dumped_yaml.replace('\n', '\r\n')
        
        # Update the component
        client.update_entity(
            entity_name="botcomponents",
            entity_id=component_id,
            data={"data": updated_yaml}
        )
        
        console.print(f"[bold green]✓[/bold green] Successfully updated model description for component {component_id}")
        
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)
    finally:
        if 'client' in locals():
            client.close()

def main():
    """Entry point for the CLI."""
    cli()

if __name__ == "____main__":
    main()