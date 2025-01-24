#Author Gustav Ström
#show and remove interest
from supabase import create_client, Client # type: ignore
from dotenv import load_dotenv # type: ignore
import os

envPath="./.env"

if not load_dotenv(envPath):
    print("Failed to load .env file")

url = os.getenv("SUPABASE_URL")
apiKey = os.getenv("SUPABASE_API_KEY")

if not url or not apiKey:
    print("Missing SUPABASE_URL or SUPABASE_API_KEY")

supabase: Client = create_client(url, apiKey)   #create supabase client

#Updates intresse row to link to a student and a project
def addInterest(project):
    try:
        response = supabase.table("intresse").insert([project]).execute()
        print(response)
        return response
    except Exception as exception:
        print("fel",exception)
        return exception

#Delete a row from itresse row
def removeIntrest(id):
    try:
        response = supabase.table('intresse').delete().eq('id', id).execute()
        print(response)
        if not response.data:
            print("row doesnt exist")
            return ("project does not exist")
        else:
            return response
    except Exception as exception:
        print("error deleting", exception)
        return exception


"""# Examaple function calls
data={"proj": 1,"elev": 2 }
#addInterest(data)
removeIntrest(4)
"""