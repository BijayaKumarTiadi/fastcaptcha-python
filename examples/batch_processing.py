"""
Example: Batch Process Multiple CAPTCHAs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to solve multiple CAPTCHA images in batch.
"""

from fastcaptcha import FastCaptcha
import glob
import time

def main():
    # Initialize the solver
    api_key = "your-api-key-here"  # Replace with your actual API key
    
    # Use context manager for automatic session cleanup
    with FastCaptcha(api_key=api_key) as solver:
        # Find all CAPTCHA images in a directory
        captcha_files = glob.glob("captchas/*.jpg")
        
        if not captcha_files:
            print("No CAPTCHA images found in 'captchas/' directory")
            return
        
        print(f"Found {len(captcha_files)} CAPTCHAs to solve\n")
        
        # Track statistics
        successful = 0
        failed = 0
        start_time = time.time()
        
        # Process each CAPTCHA
        for i, captcha_file in enumerate(captcha_files, 1):
            try:
                print(f"[{i}/{len(captcha_files)}] Solving {captcha_file}...", end=" ")
                result = solver.solve(captcha_file)
                print(f"✓ Result: {result}")
                successful += 1
                
            except Exception as e:
                print(f"✗ Error: {e}")
                failed += 1
        
        # Print statistics
        elapsed = time.time() - start_time
        print(f"\n{'='*50}")
        print(f"Batch Processing Complete")
        print(f"{'='*50}")
        print(f"Total: {len(captcha_files)}")
        print(f"Successful: {successful}")
        print(f"Failed: {failed}")
        print(f"Time elapsed: {elapsed:.2f} seconds")
        print(f"Average time per CAPTCHA: {elapsed/len(captcha_files):.2f} seconds")
        print(f"{'='*50}")


if __name__ == "__main__":
    main()
