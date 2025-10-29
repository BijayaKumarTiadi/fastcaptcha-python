# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-29

### Added
- Initial release of FastCaptcha Python library
- `FastCaptcha` class for solving image CAPTCHAs
- Support for solving from local files, URLs, and base64 strings
- `solve()` method for solving from file path or URL
- `solve_url()` method for solving from URL
- `solve_base64()` method for solving from base64-encoded images
- `get_balance()` method for checking account credits
- Context manager support for automatic session cleanup
- Comprehensive error handling with custom exceptions
- Type hints for better IDE support
- Complete documentation and examples
- PyPI package configuration

### Features
- 95% accuracy for text-based image CAPTCHAs
- Solve CAPTCHAs in under 0.3 seconds
- Support for all major image formats (JPG, PNG, GIF, BMP, WebP)
- Automatic retry logic for network errors
- Timeout configuration
- Session management with connection pooling

### Documentation
- Comprehensive README with SEO optimization
- 6 detailed example scripts
- API documentation
- Contributing guidelines
- MIT License

## [Unreleased]

### Planned
- Async/await support
- Webhook notifications
- Batch API endpoint
- CLI tool
- More examples for popular frameworks
