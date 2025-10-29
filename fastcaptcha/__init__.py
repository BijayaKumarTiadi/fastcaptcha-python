"""
FastCaptcha - Fastest Image CAPTCHA Solver API for Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

FastCaptcha is a powerful Python library for solving text-based image CAPTCHAs
using AI-powered OCR technology with 95% accuracy in under 0.3 seconds.

Basic usage:

   >>> from fastcaptcha import FastCaptcha
   >>> solver = FastCaptcha(api_key='your-api-key-here')
   >>> result = solver.solve('captcha.jpg')
   >>> print(result)
   'ABC123'

:copyright: (c) 2025 by FastCaptcha (Bijaya kumar Tiadi).
:license: MIT, see LICENSE for more details.
"""

__title__ = 'fastcaptcha-api'
__version__ = '1.0.0'
__author__ = 'Bijaya kumar Tiadi'
__license__ = 'MIT'
__copyright__ = 'Copyright 2025 FastCaptcha'

from .core import FastCaptcha
from .exceptions import (
    FastCaptchaException,
    APIKeyError,
    InvalidImageError,
    APIError,
    TimeoutError
)

__all__ = [
    'FastCaptcha',
    'FastCaptchaException',
    'APIKeyError',
    'InvalidImageError',
    'APIError',
    'TimeoutError'
]
