"""
FastCaptcha Exceptions
~~~~~~~~~~~~~~~~~~~~~~

Custom exceptions for FastCaptcha library.
"""


class FastCaptchaException(Exception):
    """Base exception for all FastCaptcha errors."""
    pass


class APIKeyError(FastCaptchaException):
    """Raised when API key is invalid or missing."""
    pass


class InvalidImageError(FastCaptchaException):
    """Raised when image is invalid or cannot be processed."""
    pass


class APIError(FastCaptchaException):
    """Raised when API request fails."""
    pass


class TimeoutError(FastCaptchaException):
    """Raised when API request times out."""
    pass
