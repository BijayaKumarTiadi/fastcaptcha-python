# PyPI Publishing Guide for FastCaptcha

This guide explains how to publish the FastCaptcha package to PyPI.

## Prerequisites

1. **Create PyPI account**: https://pypi.org/account/register/
2. **Create TestPyPI account**: https://test.pypi.org/account/register/ (for testing)
3. **Install build tools**:
   ```bash
   pip install build twine
   ```

## Step 1: Build the Package

```bash
cd fastcaptcha-python

# Clean previous builds
rm -rf build/ dist/ *.egg-info

# Build the package
python -m build
```

This creates:
- `dist/fastcaptcha-api-1.0.0.tar.gz` (source distribution)
- `dist/fastcaptcha_api-1.0.0-py3-none-any.whl` (wheel distribution)

## Step 2: Test on TestPyPI (Recommended)

```bash
# Upload to TestPyPI first
python -m twine upload --repository testpypi dist/*

# Test installation from TestPyPI
pip install --index-url https://test.pypi.org/simple/ fastcaptcha-api
```

## Step 3: Upload to PyPI

```bash
# Upload to real PyPI
python -m twine upload dist/*
```

You'll be prompted for:
- Username: Your PyPI username
- Password: Your PyPI password (or API token)

## Step 4: Verify Installation

```bash
# Install from PyPI
pip install fastcaptcha-api

# Test it works
python -c "from fastcaptcha import FastCaptcha; print(FastCaptcha.__version__)"
```

## Using API Tokens (Recommended)

Instead of using your password, create an API token:

1. Go to https://pypi.org/manage/account/
2. Scroll to "API tokens"
3. Click "Add API token"
4. Name: "fastcaptcha-api-upload"
5. Scope: "Project: fastcaptcha-api"
6. Copy the token

Create `~/.pypirc`:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-YOUR-API-TOKEN-HERE

[testpypi]
username = __token__
password = pypi-YOUR-TEST-API-TOKEN-HERE
```

Now you can upload without entering credentials:

```bash
python -m twine upload dist/*
```

## Publishing Updates

1. Update version in:
   - `fastcaptcha/__init__.py` (`__version__`)
   - `setup.py` (`version`)
   - `pyproject.toml` (`version`)

2. Update `CHANGELOG.md` with changes

3. Build and upload:
   ```bash
   rm -rf dist/
   python -m build
   python -m twine upload dist/*
   ```

## Verification Checklist

Before publishing, verify:

- ✅ Version number is correct and incremented
- ✅ `README.md` is up to date
- ✅ `CHANGELOG.md` is updated
- ✅ All tests pass (if you have tests)
- ✅ Package builds without errors
- ✅ Installation works from TestPyPI
- ✅ Example code runs correctly
- ✅ Documentation links are correct
- ✅ License file is included
- ✅ `.gitignore` excludes build artifacts

## After Publishing

1. **Verify on PyPI**: https://pypi.org/project/fastcaptcha-api/
2. **Test installation**: `pip install fastcaptcha-api`
3. **Update GitHub**: Tag the release
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```
4. **Create GitHub Release**: Add release notes from CHANGELOG

## Troubleshooting

### Error: "File already exists"
- You already uploaded this version
- Increment version number and rebuild

### Error: "Invalid credentials"
- Check your PyPI username/password
- Use API token instead

### Error: "README rendering failed"
- Check `README.md` markdown syntax
- Validate with: `python -m readme_renderer README.md`

## SEO Tips for PyPI

Your package listing will appear in:
- Google search results
- PyPI search
- GitHub search

Make sure:
- ✅ Package name includes "captcha" keyword
- ✅ Description is keyword-rich (already done)
- ✅ Keywords list is comprehensive (already done)
- ✅ README has good structure with headers
- ✅ Links back to your website (backlinks for SEO)

## Resources

- PyPI: https://pypi.org
- Packaging Guide: https://packaging.python.org
- Twine Docs: https://twine.readthedocs.io
- Build Docs: https://build.pypa.io

---

**Good luck with your PyPI publication!** 🚀

If you have questions, contact: contact@fastcaptcha.org
