from google import genai
import os

os.environ["GOOGLE_API_KEY"] = ""

try:
    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    print("Testing API Key...")
    
    # If your key works, this will successfully print out the models
    for model in client.models.list():
        print(model.name)
        
except Exception as e:
    print(f"Auth Failed: {e}")