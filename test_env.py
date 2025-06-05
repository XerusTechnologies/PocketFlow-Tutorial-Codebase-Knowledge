import os
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()

# Get the API key from environment
api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    # Mask the API key for security (show only first 4 and last 4 characters)
    masked_key = f"{api_key[:4]}...{api_key[-4:]}" if len(api_key) > 8 else "***"
    print(f"✅ GEMINI_API_KEY is set: {masked_key}")
else:
    print("❌ GEMINI_API_KEY is not set")
    print("\nPlease make sure you have:")
    print("1. Created a .env file in your project root")
    print("2. Added this line to your .env file:")
    print("   GEMINI_API_KEY=your-api-key-here") 