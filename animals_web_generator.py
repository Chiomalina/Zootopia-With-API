import requests
import json

def fetch_data_from_api(animal_name):
    """
    Fetches data from the api-ninjas Animals API given an animal name.
    Returns a Python list of matching animals (each animal is a dict).
    If nothing matches, returns an empty list.
    """
    api_url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {'X-Api-Key': 'lxErmCJT/+uW/RleR7gAmA==5CjBhmp2nBaCgXE7'}

    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} {response.text}")
        return []


def serialize_animal(animal_obj):
    """
    Handles the HTML serialization of a single animal object.
    This function returns a string containing an <li> ... </li> block.
    """
    name = animal_obj.get("name", "Unknown Name")
    characteristics = animal_obj.get("characteristics", {})
    taxonomy = animal_obj.get("taxonomy", {})

    # Pull out fields safely, using defaults if missing
    diet = characteristics.get("diet", "Unknown Diet")
    locations = animal_obj.get("locations", [])
    location_str = ", ".join(locations)
    animal_type = characteristics.get("type", "N/A")
    skin_type = characteristics.get("skin_type", "Unknown")
    lifespan = characteristics.get("lifespan", "Unknown")
    weight = characteristics.get("weight", "Unknown")
    description = animal_obj.get("description", "Unknown Description")

    # Convert taxonomy dictionary into a readable string
    taxonomy_str = ", ".join(f"{key}: {value}" for key, value in taxonomy.items())

    # Build the HTML snippet for one animal
    output = f'\n<li class="cards__item">\n'
    output += f'  <div class="card__title">{name}</div>\n\n'
    output += (
        f'  <div class="card__text">'
        f'   <ul class="card__subtitle">\n'
        f'    <li><strong>Diet:</strong> {diet}</li>\n'
        f'    <li><strong>Location:</strong> {location_str}</li>\n'
        f'    <li><strong>Animal Type:</strong> {animal_type}</li>\n'
        f'    <li><strong>Lifespan:</strong> {lifespan}</li>\n'
        f'    <li><strong>Skin Type:</strong> {skin_type}</li>\n'
        f'    <li><strong>Weight:</strong> {weight}</li>\n'
        f'    <li><strong>Description:</strong> {description}</li>\n'
        f'    <li><strong>Taxonomy:</strong> {taxonomy_str}</li>\n'
        f'   </ul>\n'
        f'  </div>\n'
        f'</li>\n'
    )
    return output


def build_animals_html(animals_list, searched_name):
    """
    Given a list of animal objects and the searched animal name,
    returns a string of HTML that can either display:
      - a list of all matching animals, or
      - an error message if no animals were returned.
    """
    # If the API returned no animals, show a "doesn't exist" message
    if not animals_list:
        return f'<h2>The animal "{searched_name}" doesn\'t exist.</h2>'

    # Otherwise, build up a combined HTML string of all animals
    html_output = "<ul>\n"
    for animal in animals_list:
        html_output += serialize_animal(animal)
    html_output += "\n</ul>"
    return html_output


def replace_placeholder_in_template(
    template_file_path,
    placeholder_text,
    replacement_html,
    output_file_path="animals.html"
):
    """
    Reads the template HTML file, replaces the first occurrence of placeholder_text
    with replacement_html, and writes the result to output_file_path.
    """
    with open(template_file_path, mode="r", encoding="utf-8") as fileobject:
        file_content = fileobject.read()

    replaced_content = file_content.replace(placeholder_text, replacement_html, 1)

    with open(output_file_path, mode="w", encoding="utf-8") as fileobject:
        fileobject.write(replaced_content)


def main():
    """
    Milestones:
      (1) Fetch data from the API for 'Fox' (original milestone).
      (2) Prompt user for any animal name, fetch data from the API,
          generate and insert HTML for all returned animals.
      (3) If no animals are found, a friendly message is displayed in the website.
    """

    # Milestone 2: Prompt the user for an animal name
    animal_name = input("Enter a name of an animal: ")

    # Fetch the data from the API (replaces reading from local JSON)
    animals_data = fetch_data_from_api(animal_name)

    # Build the HTML snippet depending on results
    animals_html = build_animals_html(animals_data, animal_name)

    # Insert the generated HTML snippet into template
    replace_placeholder_in_template(
        template_file_path="files/animals.template.html",
        placeholder_text="__REPLACE_ANIMALS_INFO",
        replacement_html=animals_html,
        output_file_path="animals.html"
    )

    print("\nWebsite was successfully generated to the file 'animals.html'.")


if __name__ == "__main__":
    main()
