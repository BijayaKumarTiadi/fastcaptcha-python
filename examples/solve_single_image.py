"""
Example: Solve a Single CAPTCHA Image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example demonstrates how to solve a single CAPTCHA image from a local file.
"""

from fastcaptcha import FastCaptcha

def main():
    # Initialize the solver with your API key
    api_key = "your-api-key-here"  # Replace with your actual API key
    solver = FastCaptcha(api_key=api_key)
    
    # Path to your CAPTCHA image
    image_path = "captcha.jpg"  # Replace with your image path
    
    try:
        # Solve the CAPTCHA
        print(f"Solving CAPTCHA from: {image_path}")
        result = solver.solve(image_path)
        
        # Print the result
        print(f"✓ Solved! CAPTCHA text: {result}")
        
    except Exception as e:
        print(f"✗ Error: {e}")
    
    finally:
        # Close the session
        solver.close()


if __name__ == "__main__":
    main()
