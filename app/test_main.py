from unittest.mock import patch
from app.main import can_access_google_page
class TestCanAccessGooglePage:
    
    @patch('app.main.valid_google_url')
    @patch('app.main.has_internet_connection')
    def test_accessible_when_url_valid_and_has_internet(self, mock_internet, mock_url):
        # Arrange
        mock_url.return_value = True
        mock_internet.return_value = True
        
        # Act
        result = can_access_google_page("https://www.google.com")
        
        # Assert
        assert result == "Accessible"
