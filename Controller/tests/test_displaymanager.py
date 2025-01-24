import unittest
from unittest.mock import MagicMock, patch
import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from displayManager.displayManager import getProjects, filterProjects 

class TestScript(unittest.TestCase):
    
    def setUp(self):
        #mock environment variables
        os.environ["SUPABASE_URL"] = "https://mock.supabase.co"
        os.environ["SUPABASE_API_KEY"] = "mock_api_key"
        # Load test data from JSON file
        with open(os.path.join(os.path.dirname(__file__), "projectData.json")) as f:
            self.test_data = json.load(f)

    def test_getProjects(self):
        data = self.test_data["data"]
        projects = getProjects(data)
        self.assertEqual(len(projects), 5)
        
        #Make sure that a expected project is in projects(the retrieved)
        self.assertIn({ "id": 1,
        "isTaken": False,
        "title": "Web Application Development",
        "companyName": "Tech Innovators Inc.",
        "time": 20,
        "projectType": "Software",
        "additionalInfo": "Develop a Svelte and Flask-based web application.",
        "contactPerson": "Jane Doe"}, projects)

    def test_filterProjects(self):
        data = self.test_data["data"]
        criteria = {"isTaken": False}
        filtered = filterProjects(data, criteria)
        self.assertTrue(all(project["isTaken"] == False for project in filtered))
        self.assertGreater(len(filtered), 0)  # Ensure we have at least one match

        criteria = {"title": "Digital Marketing Strategy"}
        filtered = filterProjects(data, criteria)
        self.assertTrue(all(project["title"] == "Digital Marketing Strategy" for project in filtered))
        self.assertGreater(len(filtered), 0)  
        
        criteria = {"time": 15}
        filtered = filterProjects(data, criteria)
        self.assertTrue(all(project["time"] == 15 for project in filtered))
        self.assertGreater(len(filtered), 0)  

if __name__ == "__main__":
    unittest.main()