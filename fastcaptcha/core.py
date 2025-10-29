"""
FastCaptcha Core Module
~~~~~~~~~~~~~~~~~~~~~~~

This module contains the main FastCaptcha class for solving image CAPTCHAs.
"""

import base64
import requests
from typing import Optional, Union
from pathlib import Path

from .exceptions import APIKeyError, InvalidImageError, APIError, TimeoutError
from .utils import validate_image_path, is_valid_url, download_image


class FastCaptcha:
    """
    FastCaptcha solver class for solving text-based image CAPTCHAs.
    
    This class provides methods to solve CAPTCHAs from local files, URLs,
    or base64-encoded images using the FastCaptcha API.
    
    Args:
        api_key (str): Your FastCaptcha API key
        base_url (str, optional): Custom API endpoint. Defaults to production API.
        timeout (int, optional): Request timeout in seconds. Defaults to 30.
    
    Example:
        >>> solver = FastCaptcha(api_key='your-api-key')
        >>> result = solver.solve('captcha.jpg')
        >>> print(result)
        'ABC123'
    """
    
    DEFAULT_API_URL = "https://fastcaptcha.org/api/v1/ocr/"
    
    def __init__(
        self,
        api_key: str,
        base_url: Optional[str] = None,
        timeout: int = 30
    ):
        """
        Initialize FastCaptcha solver.
        
        Args:
            api_key: Your FastCaptcha API key
            base_url: Custom API endpoint (optional)
            timeout: Request timeout in seconds (default: 30)
        
        Raises:
            APIKeyError: If API key is invalid or missing
        """
        if not api_key or not isinstance(api_key, str):
            raise APIKeyError("API key must be a non-empty string")
        
        self.api_key = api_key.strip()
        self.base_url = base_url or self.DEFAULT_API_URL
        self.timeout = timeout
        self._session = requests.Session()
        self._session.headers.update({
            'User-Agent': f'FastCaptcha-Python/{self.__class__.__module__}'
        })
    
    def solve(self, image: Union[str, Path], **kwargs) -> str:
        """
        Solve a CAPTCHA from a file path or URL.
        
        Args:
            image: Path to image file or image URL
            **kwargs: Additional parameters to pass to the API
        
        Returns:
            str: Solved CAPTCHA text
        
        Raises:
            InvalidImageError: If image is invalid or cannot be read
            APIError: If API request fails
            TimeoutError: If request times out
        
        Example:
            >>> solver = FastCaptcha(api_key='your-api-key')
            >>> # From file
            >>> result = solver.solve('captcha.jpg')
            >>> # From URL
            >>> result = solver.solve('https://example.com/captcha.png')
        """
        image_str = str(image)
        
        # Handle URL
        if is_valid_url(image_str):
            return self.solve_url(image_str, **kwargs)
        
        # Handle file path
        if not validate_image_path(image_str):
            raise InvalidImageError(f"Invalid image path: {image_str}")
        
        with open(image_str, 'rb') as f:
            image_data = f.read()
        
        return self._solve_image_data(image_data, **kwargs)
    
    def solve_url(self, url: str, **kwargs) -> str:
        """
        Solve a CAPTCHA from a URL.
        
        Args:
            url: URL of the CAPTCHA image
            **kwargs: Additional parameters to pass to the API
        
        Returns:
            str: Solved CAPTCHA text
        
        Raises:
            InvalidImageError: If URL is invalid or image cannot be downloaded
            APIError: If API request fails
        
        Example:
            >>> solver = FastCaptcha(api_key='your-api-key')
            >>> result = solver.solve_url('https://example.com/captcha.png')
        """
        if not is_valid_url(url):
            raise InvalidImageError(f"Invalid URL: {url}")
        
        try:
            image_data = download_image(url, timeout=self.timeout)
        except Exception as e:
            raise InvalidImageError(f"Failed to download image from URL: {str(e)}")
        
        return self._solve_image_data(image_data, **kwargs)
    
    def solve_base64(self, base64_string: str, **kwargs) -> str:
        """
        Solve a CAPTCHA from a base64-encoded image.
        
        Args:
            base64_string: Base64-encoded image string
            **kwargs: Additional parameters to pass to the API
        
        Returns:
            str: Solved CAPTCHA text
        
        Raises:
            InvalidImageError: If base64 string is invalid
            APIError: If API request fails
        
        Example:
            >>> solver = FastCaptcha(api_key='your-api-key')
            >>> b64_image = "iVBORw0KGgoAAAANSUhEUgAA..."
            >>> result = solver.solve_base64(b64_image)
        """
        try:
            # Remove data URI prefix if present
            if ',' in base64_string:
                base64_string = base64_string.split(',')[1]
            
            image_data = base64.b64decode(base64_string)
        except Exception as e:
            raise InvalidImageError(f"Invalid base64 string: {str(e)}")
        
        return self._solve_image_data(image_data, **kwargs)
    
    def _solve_image_data(self, image_data: bytes, **kwargs) -> str:
        """
        Internal method to solve CAPTCHA from raw image bytes.
        
        Args:
            image_data: Raw image bytes
            **kwargs: Additional parameters to pass to the API
        
        Returns:
            str: Solved CAPTCHA text
        
        Raises:
            APIError: If API request fails
            TimeoutError: If request times out
        """
        # Encode image to base64
        image_base64 = base64.b64encode(image_data).decode('utf-8')
        
        # Prepare request payload
        payload = {
            'image': image_base64,
            **kwargs
        }
        
        headers = {
            'X-API-Key': self.api_key,
            'Content-Type': 'application/json'
        }
        
        try:
            response = self._session.post(
                self.base_url,
                json=payload,
                headers=headers,
                timeout=self.timeout
            )
            
            # Handle API errors
            if response.status_code == 401:
                raise APIKeyError("Invalid API key")
            elif response.status_code == 400:
                error_msg = response.json().get('error', 'Bad request')
                raise InvalidImageError(f"API returned error: {error_msg}")
            elif response.status_code != 200:
                raise APIError(
                    f"API request failed with status {response.status_code}: "
                    f"{response.text}"
                )
            
            # Parse response
            result = response.json()
            
            if 'text' not in result:
                raise APIError("Invalid API response format")
            
            return result['text']
            
        except requests.exceptions.Timeout:
            raise TimeoutError(
                f"Request timed out after {self.timeout} seconds"
            )
        except requests.exceptions.RequestException as e:
            raise APIError(f"Network error: {str(e)}")
    
    def get_balance(self) -> dict:
        """
        Get account balance and credit information.
        
        Returns:
            dict: Account balance information
        
        Raises:
            APIError: If API request fails
        
        Example:
            >>> solver = FastCaptcha(api_key='your-api-key')
            >>> balance = solver.get_balance()
            >>> print(f"Credits remaining: {balance['credits']}")
        """
        headers = {
            'X-API-Key': self.api_key
        }
        
        try:
            response = self._session.get(
                self.base_url.replace('/ocr/', '/balance/'),
                headers=headers,
                timeout=self.timeout
            )
            
            if response.status_code == 401:
                raise APIKeyError("Invalid API key")
            elif response.status_code != 200:
                raise APIError(
                    f"Failed to get balance. Status: {response.status_code}"
                )
            
            return response.json()
            
        except requests.exceptions.RequestException as e:
            raise APIError(f"Network error: {str(e)}")
    
    def close(self):
        """Close the HTTP session."""
        self._session.close()
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()
    
    def __repr__(self):
        return f"<FastCaptcha(api_key='***{self.api_key[-4:]}')>"
