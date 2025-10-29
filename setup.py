"""
FastCaptcha Python Package Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Setup configuration for PyPI distribution.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read long description from README
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name='fastcaptcha-api',
    version='1.0.0',
    author='Bijaya kumar Tiadi',
    author_email='contact@fastcaptcha.org',
    description='Fastest AI-powered image CAPTCHA solver API for Python with 95% accuracy',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/fastcaptcha/fastcaptcha',
    project_urls={
        'Documentation': 'https://fastcaptcha.org/api-docs/',
        'Source': 'https://github.com/fastcaptcha/fastcaptcha',
        'Website': 'https://fastcaptcha.org',
        'Bug Reports': 'https://github.com/fastcaptcha/fastcaptcha/issues',
    },
    packages=find_packages(exclude=['tests', 'tests.*', 'examples']),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Operating System :: OS Independent',
    ],
    keywords=[
        'captcha',
        'captcha solver',
        'fast captcha',
        'python captcha api',
        'captcha ocr',
        'ai captcha solver',
        'image captcha',
        'captcha recognition',
        'automated captcha solver',
        'captcha bypass',
        'ocr api',
        'image to text',
        'web scraping',
        'automation',
        'bot development',
        '2captcha alternative',
        'anticaptcha alternative',
    ],
    python_requires='>=3.7',
    install_requires=[
        'requests>=2.25.0',
    ],
    extras_require={
        'dev': [
            'pytest>=6.0',
            'pytest-cov>=2.0',
            'black>=21.0',
            'flake8>=3.9',
            'mypy>=0.900',
        ],
    },
    include_package_data=True,
    zip_safe=False,
    license='MIT',
)
