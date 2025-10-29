# Contributing to FastCaptcha Python

Thank you for your interest in contributing to FastCaptcha! We welcome contributions from the community.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue on GitHub with:
- A clear description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Your Python version and OS

### Suggesting Features

We love new ideas! Open an issue with:
- Clear description of the feature
- Use case and benefits
- Example code showing how it would work

### Pull Requests

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests if applicable
5. Ensure code follows PEP 8 style guide
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to your branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

### Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions small and focused

### Testing

Before submitting a PR, ensure:
- All existing tests pass
- New features have tests
- Code coverage doesn't decrease

## Development Setup

```bash
# Clone the repository
git clone https://github.com/fastcaptcha/fastcaptcha.git
cd fastcaptcha

# Install in development mode
pip install -e .[dev]

# Run tests
pytest

# Check code style
flake8 fastcaptcha/
black --check fastcaptcha/
```

## Questions?

Feel free to reach out:
- Email: contact@fastcaptcha.org
- GitHub Issues: [Open an issue](https://github.com/fastcaptcha/fastcaptcha/issues)

Thank you for contributing! 🎉
