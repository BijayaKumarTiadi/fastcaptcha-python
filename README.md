# FastCaptcha - Fastest Image CAPTCHA Solver API for Python 🚀

[![PyPI version](https://badge.fury.io/py/fastcaptcha-api.svg)](https://badge.fury.io/py/fastcaptcha-api)
[![Python Versions](https://img.shields.io/pypi/pyversions/fastcaptcha-api.svg)](https://pypi.org/project/fastcaptcha-api/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://pepy.tech/badge/fastcaptcha-api)](https://pepy.tech/project/fastcaptcha-api)

**FastCaptcha** is the fastest AI-powered image CAPTCHA solver API for Python with **95% accuracy** in under **0.3 seconds**. Perfect for web scraping, automation, bot development, and testing.

---

## 🚀 What is FastCaptcha?

FastCaptcha is a powerful Python library that solves text-based image CAPTCHAs using advanced AI and OCR technology. Unlike traditional CAPTCHA solvers, FastCaptcha provides:

- ⚡ **Lightning-Fast** - Solve CAPTCHAs in under 0.3 seconds
- 🎯 **95% Accuracy** - Industry-leading accuracy for image CAPTCHAs
- 💰 **Affordable** - Starting at $1 for 3000 CAPTCHA solves
- 🔌 **Easy Integration** - Simple Python API with one-line installation
- 🌐 **RESTful API** - Works with any programming language
- 🔒 **Secure** - Your data is encrypted and never stored

### Supported CAPTCHA Types

FastCaptcha supports all text-based image CAPTCHAs including:
- Alphanumeric CAPTCHAs
- Numeric only CAPTCHAs
- Mixed case text CAPTCHAs
- Distorted text CAPTCHAs
- Noisy background CAPTCHAs
- High contrast CAPTCHAs
- Multi-line CAPTCHAs
- Complex pattern CAPTCHAs

---

## 🔧 Installation

Install FastCaptcha using pip:

```bash
pip install fastcaptcha-api
```

That's it! No complex setup, no dependencies issues.

### Requirements
- Python 3.7 or higher
- `requests` library (auto-installed)

---

## 🧩 Quick Start Example

Get started in just 3 lines of code:

```python
from fastcaptcha import FastCaptcha

# Initialize with your API key
solver = FastCaptcha(api_key="your-api-key-here")

# Solve a CAPTCHA
result = solver.solve("captcha.jpg")
print(result)  # Output: "ABC123"
```

### Get Your Free API Key

1. Visit [FastCaptcha.org](https://fastcaptcha.org)
2. Sign up for free
3. Get **100 free credits** to start
4. Copy your API key from the dashboard

---

## 💡 Why FastCaptcha?

### Compare FastCaptcha vs Other CAPTCHA Solvers

| Feature | FastCaptcha | 2Captcha | AntiCaptcha | TrueCaptcha |
|---------|-------------|----------|-------------|-------------|
| **Speed** | **0.3s** | 10-30s | 5-20s | 3-10s |
| **Accuracy** | **95%** | 80-85% | 75-80% | 70-75% |
| **Price per 1000** | **$0.33** | $1.00 | $1.50 | $2.00 |
| **Python Library** | ✅ | ❌ | ❌ | ❌ |
| **API Quality** | ✅ | ⚠️ | ⚠️ | ❌ |
| **Free Credits** | 100 | 0 | 0 | 50 |

### Key Advantages

✅ **10x Faster** - Solve CAPTCHAs in 0.3 seconds vs 10-30 seconds with competitors  
✅ **3x Cheaper** - $0.33 per 1000 solves vs $1-$2 with other services  
✅ **Higher Accuracy** - 95% accuracy vs 70-85% industry average  
✅ **Better Developer Experience** - Native Python library, not just API wrapper  
✅ **No Hidden Costs** - Pay only for what you use, credits never expire  

---

## 🌐 Direct REST API Usage (Without Python Package)

Don't want to install the Python package? Use our RESTful API directly from any programming language!

### API Endpoint

```
POST https://fastcaptcha.org/api/v1/ocr/
```

### cURL Example

```bash
curl -X POST https://fastcaptcha.org/api/v1/ocr/ \
  -H "Content-Type: application/json" \
  -d '{
    "api_key": "your-api-key-here",
    "image": "base64_encoded_image_here"
  }'
```

### Response Format

```json
{
  "success": true,
  "text": "ABC123",
  "credits_remaining": 2850,
  "processing_time": 0.28
}
```

### Error Response

```json
{
  "success": false,
  "error": "Invalid API key",
  "error_code": "INVALID_API_KEY"
}
```

### Using with JavaScript/Node.js

```javascript
const axios = require('axios');
const fs = require('fs');

async function solveCaptcha(imagePath) {
  const imageBase64 = fs.readFileSync(imagePath, { encoding: 'base64' });
  
  const response = await axios.post('https://fastcaptcha.org/api/v1/ocr/', {
    api_key: 'your-api-key-here',
    image: imageBase64
  });
  
  return response.data.text;
}

solveCaptcha('captcha.jpg').then(result => {
  console.log('Solved:', result);
});
```

### Using with PHP

```php
<?php
$image = base64_encode(file_get_contents('captcha.jpg'));

$data = json_encode([
    'api_key' => 'your-api-key-here',
    'image' => $image
]);

$ch = curl_init('https://fastcaptcha.org/api/v1/ocr/');
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/json']);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = json_decode(curl_exec($ch), true);
curl_close($ch);

echo "Solved: " . $response['text'];
?>
```

### Using with Java

```java
import java.net.http.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Base64;

public class FastCaptcha {
    public static void main(String[] args) throws Exception {
        byte[] imageBytes = Files.readAllBytes(Paths.get("captcha.jpg"));
        String base64Image = Base64.getEncoder().encodeToString(imageBytes);
        
        String json = String.format(
            "{\"api_key\":\"your-api-key\",\"image\":\"%s\"}", 
            base64Image
        );
        
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("https://fastcaptcha.org/api/v1/ocr/"))
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(json))
            .build();
            
        HttpResponse<String> response = client.send(request, 
            HttpResponse.BodyHandlers.ofString());
            
        System.out.println(response.body());
    }
}
```

### API Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `api_key` | string | Yes | Your FastCaptcha API key |
| `image` | string | Yes | Base64-encoded image OR image URL |
| `timeout` | integer | No | Max processing time in seconds (default: 30) |

### Rate Limits

- **Free Plan**: 10 requests/minute
- **Basic Plan**: 60 requests/minute
- **Pro Plan**: 300 requests/minute
- **Enterprise**: Unlimited

---

## 📦 Complete Usage Guide

### Basic Usage

#### Solve from Local File

```python
from fastcaptcha import FastCaptcha

solver = FastCaptcha(api_key="your-api-key")
result = solver.solve("path/to/captcha.jpg")
print(f"Solved: {result}")
```

#### Solve from URL

```python
from fastcaptcha import FastCaptcha

solver = FastCaptcha(api_key="your-api-key")
result = solver.solve_url("https://example.com/captcha.png")
print(f"Solved: {result}")
```

#### Solve from Base64

```python
from fastcaptcha import FastCaptcha

solver = FastCaptcha(api_key="your-api-key")
base64_image = "iVBORw0KGgoAAAANSUhEUgAA..."
result = solver.solve_base64(base64_image)
print(f"Solved: {result}")
```

### Advanced Usage

#### Context Manager (Recommended)

```python
from fastcaptcha import FastCaptcha

with FastCaptcha(api_key="your-api-key") as solver:
    result = solver.solve("captcha.jpg")
    print(f"Solved: {result}")
# Session automatically closed
```

#### Check Account Balance

```python
from fastcaptcha import FastCaptcha

solver = FastCaptcha(api_key="your-api-key")
balance = solver.get_balance()
print(f"Credits remaining: {balance['credits']}")
```

#### Error Handling

```python
from fastcaptcha import FastCaptcha, APIKeyError, InvalidImageError, APIError

try:
    solver = FastCaptcha(api_key="your-api-key")
    result = solver.solve("captcha.jpg")
    print(f"Solved: {result}")
except APIKeyError:
    print("Invalid API key")
except InvalidImageError as e:
    print(f"Invalid image: {e}")
except APIError as e:
    print(f"API error: {e}")
```

#### Batch Processing

```python
from fastcaptcha import FastCaptcha
import glob

solver = FastCaptcha(api_key="your-api-key")

# Solve multiple CAPTCHAs
captcha_files = glob.glob("captchas/*.jpg")
for captcha_file in captcha_files:
    try:
        result = solver.solve(captcha_file)
        print(f"{captcha_file}: {result}")
    except Exception as e:
        print(f"{captcha_file}: Error - {e}")
```

#### Custom Timeout

```python
from fastcaptcha import FastCaptcha

# Set custom timeout (default is 30 seconds)
solver = FastCaptcha(api_key="your-api-key", timeout=60)
result = solver.solve("captcha.jpg")
```

---

## 🌐 Integration Examples

### Web Scraping with Selenium

```python
from selenium import webdriver
from fastcaptcha import FastCaptcha
import base64

driver = webdriver.Chrome()
solver = FastCaptcha(api_key="your-api-key")

# Navigate to page with CAPTCHA
driver.get("https://example.com/login")

# Get CAPTCHA image
captcha_element = driver.find_element_by_id("captcha-image")
captcha_base64 = captcha_element.screenshot_as_base64

# Solve CAPTCHA
result = solver.solve_base64(captcha_base64)

# Enter solution
input_field = driver.find_element_by_id("captcha-input")
input_field.send_keys(result)
```

### Requests Library

```python
import requests
from fastcaptcha import FastCaptcha

# Download CAPTCHA image
response = requests.get("https://example.com/captcha")
with open("captcha.jpg", "wb") as f:
    f.write(response.content)

# Solve CAPTCHA
solver = FastCaptcha(api_key="your-api-key")
result = solver.solve("captcha.jpg")

# Submit form with solution
data = {"captcha": result, "username": "user"}
requests.post("https://example.com/submit", data=data)
```

### Flask API Integration

```python
from flask import Flask, request, jsonify
from fastcaptcha import FastCaptcha
import base64

app = Flask(__name__)
solver = FastCaptcha(api_key="your-api-key")

@app.route('/solve', methods=['POST'])
def solve_captcha():
    data = request.json
    image_base64 = data.get('image')
    
    try:
        result = solver.solve_base64(image_base64)
        return jsonify({"success": True, "text": result})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run()
```

---

## 📊 Pricing

FastCaptcha offers the most competitive pricing in the industry:

| Package | Credits | Price | Price per 1000 |
|---------|---------|-------|----------------|
| **Starter** | 500 | FREE | $0.00 |
| **Budget** | 3000 | $1 | $0.33 |
| **Basic** | 10000 | $3 | $0.30 |
| **Pro** | 50000 | $12 | $0.24 |
| **Business** | 200000 | $40 | $0.20 |

- ✅ No monthly subscriptions
- ✅ Pay only for what you use
- ✅ Credits never expire
- ✅ Volume discounts available
- ✅ Free 100 credits on signup

[View All Pricing Plans →](https://fastcaptcha.org/pricing/)

---

## 🏆 Use Cases

FastCaptcha is perfect for:

- 🕷️ **Web Scraping** - Bypass CAPTCHAs while collecting data
- 🤖 **Automation** - Automate form submissions and testing
- 🧪 **QA Testing** - Test CAPTCHA-protected features
- 📊 **Data Collection** - Gather data from protected websites
- 🔄 **API Integration** - Add CAPTCHA solving to your API
- 🎮 **Bot Development** - Build bots that can solve CAPTCHAs
- 🌐 **Multi-Account Management** - Manage multiple accounts efficiently

---

## 📈 SEO Keywords

This library is optimized for developers searching for:

**Primary Keywords:**
- Fast CAPTCHA solver Python
- Best CAPTCHA solver API
- CAPTCHA OCR Python
- AI CAPTCHA solver
- Python CAPTCHA recognition
- Automated CAPTCHA solver
- Image CAPTCHA solver

**Alternative to:**
- 2Captcha Python
- AntiCaptcha Python
- TrueCaptcha alternative
- DeathByCaptcha alternative
- ImageTyperz alternative

**Use Cases:**
- CAPTCHA bypass Python
- Web scraping CAPTCHA solver
- Selenium CAPTCHA solver
- Automation CAPTCHA solver
- Bot CAPTCHA solver

---

## 📚 Examples Repository

Check out our [examples directory](./examples/) for more code samples:

- `solve_single_image.py` - Basic CAPTCHA solving
- `solve_from_url.py` - Solve CAPTCHAs from URLs
- `batch_processing.py` - Process multiple CAPTCHAs
- `selenium_integration.py` - Integrate with Selenium
- `error_handling.py` - Proper error handling

---

## 🔒 Security & Privacy

- 🔐 All API requests are encrypted with HTTPS
- 🗑️ Images are deleted immediately after processing
- 🚫 We never store or log your CAPTCHA images
- ✅ GDPR and CCPA compliant
- 🛡️ Enterprise-grade security

---

## 🤝 Support

Need help? We're here for you:

- 📧 **Email**: [contact@fastcaptcha.org](mailto:contact@fastcaptcha.org)
- 📖 **Documentation**: [fastcaptcha.org/api-docs/](https://fastcaptcha.org/api-docs/)
- 💬 **GitHub Issues**: [Report a bug](https://github.com/fastcaptcha/fastcaptcha/issues)
- 🌐 **Website**: [fastcaptcha.org](https://fastcaptcha.org)
- ❓ **FAQ**: [fastcaptcha.org/faq/](https://fastcaptcha.org/faq/)

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🌟 Why Developers Love FastCaptcha

> "Switched from 2Captcha to FastCaptcha and my scraping scripts are now 10x faster. Best decision ever!" - *John D., Data Engineer*

> "The Python library is so easy to use. Integrated it in 5 minutes. Accuracy is incredible!" - *Sarah M., Full Stack Developer*

> "Finally, a CAPTCHA solver that's actually fast and affordable. Saved my company $500/month!" - *Mike R., DevOps Engineer*

---

## 🚀 Get Started Now

1. **Install**: `pip install fastcaptcha-api`
2. **Sign Up**: [Get your free API key](https://fastcaptcha.org)
3. **Solve**: Start solving CAPTCHAs in seconds!

```python
from fastcaptcha import FastCaptcha

solver = FastCaptcha(api_key="your-api-key")
print(solver.solve("captcha.jpg"))
```

---

## 🔗 Links

- 🌐 **Website**: [fastcaptcha.org](https://fastcaptcha.org)
- 📖 **API Docs**: [fastcaptcha.org/api-docs/](https://fastcaptcha.org/api-docs/)
- 💰 **Pricing**: [fastcaptcha.org/pricing/](https://fastcaptcha.org/pricing/)
- 🎮 **Live Demo**: [fastcaptcha.org/demo/](https://fastcaptcha.org/demo/)
- 📧 **Contact**: [contact@fastcaptcha.org](mailto:contact@fastcaptcha.org)

---

**Made with ❤️ by FastCaptcha Team**

*Copyright © 2025 FastCaptcha - All rights reserved*
