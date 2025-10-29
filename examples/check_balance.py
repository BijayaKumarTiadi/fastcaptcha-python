"""
Example: Check Account Balance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example demonstrates how to check your FastCaptcha account balance
and credit information.
"""

from fastcaptcha import FastCaptcha, APIKeyError, APIError

def main():
    # Initialize with your API key
    api_key = "your-api-key-here"  # Replace with your actual API key
    
    try:
        solver = FastCaptcha(api_key=api_key)
        
        # Get balance information
        print("Fetching account balance...")
        balance = solver.get_balance()
        
        # Display balance information
        print("\n" + "="*50)
        print("Account Balance Information")
        print("="*50)
        print(f"Credits Remaining: {balance.get('credits', 'N/A')}")
        print(f"Total Used: {balance.get('total_used', 'N/A')}")
        print(f"Account Status: {balance.get('status', 'N/A')}")
        print("="*50)
        
        # Warning if credits are low
        credits = balance.get('credits', 0)
        if credits < 100:
            print("\n⚠ Warning: Low credits! Consider purchasing more credits.")
            print("   Visit: https://fastcaptcha.org/pricing/")
        elif credits < 500:
            print("\n⚠ Your credits are running low.")
        else:
            print("\n✓ You have sufficient credits.")
        
        solver.close()
        
    except APIKeyError:
        print("✗ Error: Invalid API key")
        print("  Please check your API key at https://fastcaptcha.org/dashboard/")
        
    except APIError as e:
        print(f"✗ Error: Failed to get balance - {e}")
        
    except Exception as e:
        print(f"✗ Unexpected error: {e}")


if __name__ == "__main__":
    main()
