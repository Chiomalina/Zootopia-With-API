def serialize_animal(animal_obj):
    """
    Converts a single animal dictionary into an HTML <li></li> element.
    """
    name = animal_obj.get("name", "Unknown Name")
    description = animal_obj.get("description", "Unknown Description")
    characteristics = animal_obj.get("characteristics", {})
    taxonomy = animal_obj.get("taxonomy", {})
    locations = animal_obj.get("locations", [])

    diet = characteristics.get("diet", "Unknown Diet")
    animal_type = characteristics.get("type", "Unknown Type")
    skin_type = characteristics.get("skin_type", "Unknown Skin Type")
    lifespan = characteristics.get("lifespan", "Unknown Lifespan")
    weight = characteristics.get("weight", "Unknown Weight")


    location_str = ", ".join(locations)
    taxonomy_str = ", ".join(f"{key}: {value}" for key, value in taxonomy.items())

    # Build the HTML snippet for one animal
    single_animal_output = f'\n<li class="cards__item">\n'
    single_animal_output += f'  <div class="card__title"><strong>{name}</strong></div>\n\n'
    single_animal_output += (
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
    return single_animal_output


def build_animals_html(animals_list, searched_name):
    """
    Given a list of animal dictionaries and the searched animal name,
    returns a single string of HTML.
      - If the list is empty, returns an error message block.
      - Otherwise, returns a <ul> containing the <li> for each animal.
    """
    if not animals_list:
        return f'<h2>The animal "{searched_name}" doesn\'t exist.</h2>'

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


def generate_website(animals_list, searched_name, template_file_path="files/animals.template.html"):
    """
    High-level function that:
      1. Builds the necessary HTML (<ul> ... </ul> or an error message)
      2. Replaces the placeholder in the template file
      3. Writes out the final file (animals.html by default)
    """
    html_snippet = build_animals_html(animals_list, searched_name)
    replace_placeholder_in_template(
        template_file_path=template_file_path,
        placeholder_text="__REPLACE_ANIMALS_INFO",
        replacement_html=html_snippet,
        output_file_path="animals.html"
    )
