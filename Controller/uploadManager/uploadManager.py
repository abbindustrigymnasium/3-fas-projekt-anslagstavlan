
from supabase import create_client, Client  # type: ignore
from dotenv import load_dotenv # type: ignore 
import os

envPath="./.env"
# Load environment variables from the .env file
if not load_dotenv(envPath):
    print("Failed to load .env file")

url = os.getenv("SUPABASE_URL")
apiKey = os.getenv("SUPABASE_API_KEY")

supabase: Client = create_client(url, apiKey)

def addProject(project):
    try:
        response = supabase.table("förslag").insert([project]).execute()
        return response
    except Exception as exception:
        return exception