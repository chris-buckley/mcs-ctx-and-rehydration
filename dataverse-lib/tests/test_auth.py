"""Tests for the authentication client."""
import unittest
from unittest.mock import patch, MagicMock

class TestAuth(unittest.TestCase):
    
    @patch('dataverse_api_cli.clients.auth.msal.ConfidentialClientApplication')
    def test_get_access_token_success(self, mock_app):
        # Setup mock
        mock_instance = mock_app.return_value
        mock_instance.acquire_token_for_client.return_value = {
            'access_token': 'dummy_token'
        }
        
        # Import after mocking
        from dataverse_api_cli.clients.auth import get_access_token
        
        # Test
        token = get_access_token()
        
        # Assertions
        self.assertEqual(token, 'dummy_token')
        mock_instance.acquire_token_for_client.assert_called_once()

    @patch('dataverse_api_cli.clients.auth.msal.ConfidentialClientApplication')
    def test_get_access_token_failure(self, mock_app):
        # Setup mock
        mock_instance = mock_app.return_value
        mock_instance.acquire_token_for_client.return_value = {
            'error': 'access_denied',
            'error_description': 'Authentication failed'
        }
        
        # Import after mocking
        from dataverse_api_cli.clients.auth import get_access_token
        
        # Test and assert exception
        with self.assertRaises(Exception) as context:
            get_access_token()
            
        self.assertTrue('Authentication failed' in str(context.exception))

if __name__ == '__main__':
    unittest.main()