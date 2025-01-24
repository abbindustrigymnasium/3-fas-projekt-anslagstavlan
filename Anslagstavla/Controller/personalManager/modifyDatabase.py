#Gustav Ström
from supabase import create_client, Client # type: ignore
from dotenv import load_dotenv # type: ignore
import os

envPath="./.env"


if not load_dotenv(envPath):
    print("Failed to load .env file")

url = os.getenv("SUPABASE_URL")
apiKey = os.getenv("SUPABASE_API_KEY")

supabase: Client = create_client(url, apiKey)

def editRow(dataToUpdate, id): #dataToUpdate is a dict of the keys that should be updated with their new values
        response = supabase.table("förslag").update(dataToUpdate).eq("id", id).execute()
        if not response.data:
            print("project doesnt exist")
            return ("project does not exist")
        else:    
            return response

def deleteRow(id):    
    response = supabase.table("förslag").delete().eq("id", id).execute()

    if not response.data:
        print("row doesnt exist")
        return ("project does not exist")
    else:
        print("row exists")
        #print(response)
        return response
    
"""exampleUpdate={"isTaken": True, "time": 10}    
editRow(exampleUpdate, 1)
deleteRow(58)"""