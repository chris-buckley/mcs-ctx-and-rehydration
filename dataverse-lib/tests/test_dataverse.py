"""Tests for the Dataverse client."""
import unittest
from unittest.mock import patch, MagicMock

class TestDataverseClient(unittest.TestCase):
    
    def setUp(self):
        self.base_url = "https://test-instance.api.crm.dynamics.com/api/data/v9.2"
        self.access_token = "dummy_token"
        
        # Import the client
        from dataverse_api_cli.clients.dataverse import DataverseClient
        
        # Initialize the client with patched httpx.Client
        with patch('httpx.Client') as mock_client:
            self.client_instance = mock_client.return_value
            self.dataverse_client = DataverseClient(self.base_url, self.access_token)
    
    def test_request(self):
        # Setup mock response
        mock_response = MagicMock()
        mock_response.content = b'{"value": "test"}'
        mock_response.json.return_value = {"value": "test"}
        self.client_instance.request.return_value = mock_response
        
        # Test the request method
        result = self.dataverse_client.request("contacts")
        
        # Assertions
        self.assertEqual(result, {"value": "test"})
        self.client_instance.request.assert_called_with(
            "GET", 
            f"{self.base_url}/contacts", 
            json=None, 
            params=None, 
            headers=self.dataverse_client.headers
        )

    def test_get_entities(self):
        # Setup mock response
        mock_response = MagicMock()
        mock_response.json.return_value = {"value": [{"id": "1", "name": "Test"}]}
        self.client_instance.request.return_value = mock_response
        
        # Test get_entities method
        result = self.dataverse_client.get_entities(
            "contacts",
            select=["fullname", "emailaddress1"],
            filter="contains(emailaddress1, 'example.com')"
        )
        
        # Assertions
        self.assertEqual(result, [{"id": "1", "name": "Test"}])
        
    def tearDown(self):
        # Clean up
        self.dataverse_client.close()

if __name__ == '__main__':
    unittest.main()