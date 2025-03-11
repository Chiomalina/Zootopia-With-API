import os
from dotenv import load_dotenv
import requests
import json


# Load environment variables from .env file
load_dotenv()

# Retrieve API key
# API_KEY = os.getenv("API_KEY")
# print(API_KEY)

def fetch_data_from_API(animal_name):
	"""
	Fetches the animals data for the animal 'animal_name'.
	Returns: a list of animals, each animal is a dictionary
	"""

	# Retrieve the Ninja's API:
	API_KEY = os.getenv("API_KEY")
	api_url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
	headers = {'X-Api-Key': API_KEY}

	response = requests.get(api_url, headers=headers)

	# If something goes wrong, return an empty list
	if response.status_code != 200:
		print(f"Error fetching data: {response.status_code} {response.text}")
		return []

	# The API should return a list of JSON objects, each describing an animal.
	data = response.json()
	return data


def fetch_data_from_file(file_path):
	"""
	Fetches the animals data from a local JSON file (static).
	Returns: a list of animal dictionaries in the same format.
	"""
	with open(file_path, mode="r", encoding="utf-8") as fileobject:
		data = json.load(fileobject)
	return data


# OPTIONAL TESTING (Run this file as a script for quick testing, if you like):
if __name__ == "__main__":
	# Just a quick test
	test_animals = fetch_data_from_API("Fox")
	print("Fetched animals:", test_animals)
