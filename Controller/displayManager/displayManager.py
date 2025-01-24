#Gustav Ström
import os # type: ignore
from dotenv import load_dotenv # type: ignore
from supabase import create_client, Client # type: ign

envPath="./.env"

if not load_dotenv(envPath):
    print("Failed to load .env file")

url = os.getenv("SUPABASE_URL")
apiKey = os.getenv("SUPABASE_API_KEY")

if not url or not apiKey:
    print("Missing SUPABASE_URL or SUPABASE_API_KEY")

supabase: Client = create_client(url, apiKey)

def loadData(): 
    try:
        response = supabase.table("förslag").select("*").execute()
        print("Supabase Response:", response)   # Debugging: Print the full response
        data = response.data    # Accessing the data
        if not data:
            raise Exception("No data returned from the Supabase table.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")  # Print the error message
        data = []  # Return an empty list if there's an error
    return data

def getProjects(data):
    projectList= []
    for project in data:
        print(project)  # Print each project
        projectList.append(project)  # Add project to the new list
    return projectList

def filterProjects(data, criteria):
    filteredData=[]
    for project in data:
        if all(project.get(key) == value for key, value in criteria.items() if value is not None):  
                    filteredData.append(project)
    return filteredData 