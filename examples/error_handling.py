"""
Example: Proper Error Handling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example demonstrates how to handle different types of errors
that may occur when using FastCaptcha.
"""

from fastcaptcha import (
    FastCaptcha,
    FastCaptchaException,
    APIKeyError,
    InvalidImageError,
    APIError,
    TimeoutError
)

def basic_error_handling():
    """
    Basic error handling example.
    """
    print("Example 1: Basic Error Handling")
    print("-" * 50)
    
    try:
        solver = FastCaptcha(api_key="your-api-key-here")
        result = solver.solve("captcha.jpg")
        print(f"✓ Success: {result}")
        
    except APIKeyError:
        print("✗ Error: Invalid API key. Please check your API key.")
        
    except InvalidImageError as e:
        print(f"✗ Error: Invalid image - {e}")
        print("  Make sure the image file exists and is a valid image format.")
        
    except APIError as e:
        print(f"✗ Error: API request failed - {e}")
        print("  Please try again later or contact support.")
        
    except TimeoutError:
        print("✗ Error: Request timed out.")
        print("  Try increasing the timeout parameter or check your internet connection.")
        
    except FastCaptchaException as e:
        print(f"✗ FastCaptcha Error: {e}")
        
    except Exception as e:
        print(f"✗ Unexpected Error: {e}")


def advanced_error_handling_with_retry():
    """
    Advanced error handling with retry logic.
    """
    print("\n\nExample 2: Error Handling with Retry Logic")
    print("-" * 50)
    
    max_retries = 3
    retry_delay = 2  # seconds
    
    solver = FastCaptcha(api_key="your-api-key-here")
    
    for attempt in range(1, max_retries + 1):
        try:
            print(f"Attempt {attempt}/{max_retries}...", end=" ")
            result = solver.solve("captcha.jpg")
            print(f"✓ Success: {result}")
            break
            
        except APIKeyError:
            print("✗ Invalid API key - stopping retries")
            break
            
        except InvalidImageError as e:
            print(f"✗ Invalid image - stopping retries: {e}")
            break
            
        except (APIError, TimeoutError) as e:
            print(f"✗ Failed: {e}")
            if attempt < max_retries:
                import time
                print(f"  Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                print("  Max retries reached. Please try again later.")
                
        except Exception as e:
            print(f"✗ Unexpected error: {e}")
            break
    
    solver.close()


def validate_before_solving():
    """
    Validate inputs before attempting to solve.
    """
    print("\n\nExample 3: Input Validation")
    print("-" * 50)
    
    import os
    
    api_key = "your-api-key-here"
    image_path = "captcha.jpg"
    
    # Validate API key
    if not api_key or api_key == "your-api-key-here":
        print("✗ Error: Please set a valid API key")
        return
    
    # Validate image file
    if not os.path.exists(image_path):
        print(f"✗ Error: Image file not found: {image_path}")
        return
    
    if not os.path.isfile(image_path):
        print(f"✗ Error: Path is not a file: {image_path}")
        return
    
    # Check file size (API may have limits)
    file_size = os.path.getsize(image_path)
    max_size = 5 * 1024 * 1024  # 5 MB
    
    if file_size > max_size:
        print(f"✗ Error: Image file too large ({file_size} bytes)")
        return
    
    # All validations passed
    try:
        solver = FastCaptcha(api_key=api_key)
        result = solver.solve(image_path)
        print(f"✓ Success: {result}")
        solver.close()
        
    except Exception as e:
        print(f"✗ Error: {e}")


def graceful_degradation():
    """
    Example of graceful degradation when CAPTCHA solving fails.
    """
    print("\n\nExample 4: Graceful Degradation")
    print("-" * 50)
    
    solver = FastCaptcha(api_key="your-api-key-here")
    
    try:
        result = solver.solve("captcha.jpg")
        print(f"✓ Automatic CAPTCHA solving succeeded: {result}")
        # Continue with automation
        
    except Exception as e:
        print(f"⚠ Automatic CAPTCHA solving failed: {e}")
        print("→ Falling back to manual input...")
        
        # Fallback: Ask user to solve manually
        result = input("Please enter the CAPTCHA text manually: ")
        print(f"✓ Using manual input: {result}")
        # Continue with manual solution
    
    finally:
        solver.close()


if __name__ == "__main__":
    # Run all examples
    basic_error_handling()
    advanced_error_handling_with_retry()
    validate_before_solving()
    graceful_degradation()
