"""
Example: Solve CAPTCHA from URL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example demonstrates how to solve a CAPTCHA image directly from a URL.
"""

from fastcaptcha import FastCaptcha

def main():
    # Initialize the solver
    api_key = "your-api-key-here"  # Replace with your actual API key
    solver = FastCaptcha(api_key=api_key)
    
    # CAPTCHA image URL
    captcha_url = "https://example.com/captcha.png"  # Replace with actual URL
    
    try:
        # Solve CAPTCHA from URL
        print(f"Solving CAPTCHA from URL: {captcha_url}")
        result = solver.solve_url(captcha_url)
        
        # Print result
        print(f"✓ Solved! CAPTCHA text: {result}")
        
    except Exception as e:
        print(f"✗ Error: {e}")
    
    finally:
        solver.close()


if __name__ == "__main__":
    main()
