import os
from dotenv import load_dotenv

load_dotenv()

from data_fetcher import fetch_data_from_API  # or fetch_data_from_file
from website_generator import generate_website

def main():
    """
    High-level flow:
      1. Ask the user for an animal name.
      2. Fetch data about that animal (from an API or local JSON, etc.).
      3. Generate the website (HTML) based on that data.
    """

    animal_name = input("Enter a name of an animal: ")

    # 1) Fetch data from API(Note: 2 functions were created for fetching data from file and from API
    # for scalability and future compatibility. animals_list = fetch_data_from_file("files/animals_data.json")
    animals_list = fetch_data_from_API(animal_name)

    # 2) Generate the website using the data gotten from step(1)
    generate_website(animals_list, animal_name)

    print("\nWebsite was successfully generated to the file 'animals.html'.")


if __name__ == "__main__":
    main()
