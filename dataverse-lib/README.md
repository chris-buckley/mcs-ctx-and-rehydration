# Dataverse API CLI

A command-line tool for interacting with the Microsoft Dataverse API.

## Installation

```bash
pip install dataverse-api-cli
```

## Configuration

Create a `.env` file in your project directory with the following variables:

```
CLIENT_ID=your_client_id_here
TENANT_ID=your_tenant_id_here
CLIENT_SECRET=your_client_secret_here
WEB_API_ENDPOINT=https://your-instance.crm.dynamics.com
```

## Usage

### Entity Operations

```bash
# List entities
dataverse-api entity list contacts --select=fullname,emailaddress1 --filter="contains(emailaddress1, 'example.com')"

# Get a specific entity
dataverse-api entity get contacts 00000000-0000-0000-0000-000000000001

# Create an entity
dataverse-api entity create contacts contact_data.json

# Update an entity
dataverse-api entity update contacts 00000000-0000-0000-0000-000000000001 contact_updates.json

# Delete an entity
dataverse-api entity delete contacts 00000000-0000-0000-0000-000000000001
```

### Bot Operations

```bash
# List bots
dataverse-api bot list
dataverse-api bot list --filter="contains(name, 'MyBot')"

# Get a specific bot
dataverse-api bot get "My Bot"

# List bot components
dataverse-api bot components "My Bot" --component-type=9

# Update a bot component
dataverse-api bot update-component 00000000-0000-0000-0000-000000000001 --description="New description"
```

### Entity Definition Operations

```bash
# List entity definitions
dataverse-api entity-definition list

# Get a specific entity definition
dataverse-api entity-definition get account
```

## Development

### Setup

1. Clone the repository
2. Install dependencies: `pip install -e .`
3. Create a `.env` file with your credentials
4. Run tests: `pytest`

## License

MIT