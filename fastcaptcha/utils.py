"""
FastCaptcha Utility Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Helper functions for image validation and processing.
"""

import os
import re
from pathlib import Path
from typing import Union
import requests


def validate_image_path(path: Union[str, Path]) -> bool:
    """
    Validate if the given path points to a valid image file.
    
    Args:
        path: Path to image file
    
    Returns:
        bool: True if valid image file exists, False otherwise
    """
    if not path:
        return False
    
    path_obj = Path(path)
    
    # Check if file exists
    if not path_obj.exists():
        return False
    
    # Check if it's a file (not directory)
    if not path_obj.is_file():
        return False
    
    # Check file extension
    valid_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'}
    if path_obj.suffix.lower() not in valid_extensions:
        return False
    
    return True


def is_valid_url(url: str) -> bool:
    """
    Check if the given string is a valid URL.
    
    Args:
        url: URL string to validate
    
    Returns:
        bool: True if valid URL, False otherwise
    """
    if not url or not isinstance(url, str):
        return False
    
    # Simple URL validation regex
    url_pattern = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain
        r'localhost|'  # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # IP
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE
    )
    
    return bool(url_pattern.match(url))


def download_image(url: str, timeout: int = 30) -> bytes:
    """
    Download image from URL.
    
    Args:
        url: Image URL
        timeout: Request timeout in seconds
    
    Returns:
        bytes: Image data
    
    Raises:
        Exception: If download fails
    """
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    
    # Verify content type
    content_type = response.headers.get('content-type', '').lower()
    if not content_type.startswith('image/'):
        raise ValueError(f"URL does not point to an image. Content-Type: {content_type}")
    
    return response.content


def format_file_size(size_bytes: int) -> str:
    """
    Format file size in human-readable format.
    
    Args:
        size_bytes: File size in bytes
    
    Returns:
        str: Formatted file size (e.g., "1.5 MB")
    """
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} TB"
