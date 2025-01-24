#Author Gustav Ström


from flask import Flask, render_template, jsonify, request # type: ignore
from displayManager import displayManager
from uploadManager import uploadManager
from personalManager import modifyDatabase, Interest
from supabase import create_client, Client # type: ignore
from dotenv import load_dotenv # type: ignore
from flask_cors import CORS
import os
app=Flask(__name__)
CORS(app)
envPath="./.env"
# Load environment variables from the .env file
if not load_dotenv(envPath):
    print("Failed to load .env file")

url = os.getenv("SUPABASE_URL")
apiKey = os.getenv("SUPABASE_API_KEY")

supabase: Client = create_client(url, apiKey)


"""@app.route('/', methods=['GET'])
def renderMain():
    return render_template('main.html')
"""

@app.route('/displayAllProjects', methods=['GET'])
def displayProjects():
    try:
        data = displayManager.loadData()  # Load data from displayManager
        projects = displayManager.getProjects(data)  # Process data
        return  projects  # Return JSON response
    except AttributeError as e:
        return jsonify({"error": f"AttributeError: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/addProjects', methods=['POST'])
def addProject():
    try:
        projectToAdd=request.get_json()
        uploadManager.addProject(projectToAdd)
        return jsonify(projectToAdd)
    except Exception as e:
        return (f"error adding project{e}")

@app.route('/filterProjects', methods=['POST'])
def filterProjects():
    try:
        # Load all project data
        data = displayManager.loadData()

        # Parse JSON payload for filtering criteria
        criteria = request.get_json()  # Get the JSON payload
        if not criteria or not isinstance(criteria, dict):
            return jsonify({"error": "Invalid JSON data. Please send a valid JSON object."}), 400

        # Apply filtering
        filtered_projects = displayManager.filterProjects(data, criteria)
        return jsonify(filtered_projects)  # Return filtered results as JSON
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500

@app.route('/delete_project/<int:projectId>', methods=['DELETE'])
def delete_project(projectId):
    try:
        #get the json payload with the id that should be deleted
        dataToDelete=request.get_json()
        if not dataToDelete:    
            return jsonify({"error": "No data provided"}), 400
        
        response=modifyDatabase.deleteRow(projectId) #try to delete data
        print(response)

        return jsonify(response.data)
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500
    
@app.route("/update_project/<int:projectId>", methods=['POST', 'GET', 'PUT'])
def update_project(projectId):
    try:
        # Parse the incoming JSON data
        dataToUpdate = request.get_json()
        if not dataToUpdate:
            return jsonify({"error": "No data provided"}), 400
         
        # Call the editRow function
        response = modifyDatabase.editRow(dataToUpdate, projectId)
        print(f"{response.data}")
        return jsonify(response.data)
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500
    
@app.route('/addInterest/<int:projectId>', methods=['POST'])
def addInterest_route(projectId):
    try:
        # Get JSON data from the request
        dataToUpdate = request.get_json()
        if not dataToUpdate:
            return jsonify({"error": "No data provided"}), 400

        # Add `projectId` to the data
        dataToUpdate['proj'] = projectId
        # Pass the updated data to the `addInterest` function
        response = Interest.addInterest(dataToUpdate)
        print("hej",response)
        print(response.data)

        # Handle response from `addInterest`
        if "error" in response:
            return jsonify({"error": response["error"]}), 500
        print(type(response))
        return jsonify({"message": f"Interest added successfully: {str(response.data)}"}), 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=5000)