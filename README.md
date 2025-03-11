# My-Zootopia_API

## Project Description
The project "MY-Zootopi_API" ia a Python-based application that fetches data about animals either from a local JSON file from your computer or from a public API and generates an HTML page to display that information in a user-friendly format. It was built to demonstrate clean code architecture, separation of responsibilities, and ease of use.

**Key Features**
- Fetches animal data from [Ninja's Animals API] (https://api-ninjas.com/api/animals) or from a local file.
- Filters, formats, and displays relevant details such as taxonomy,characteristics, locations, etc.
- Produces an HTML file automatically, making the content accessible via a simple web page.

## Usage

1. **Install Dependencies**
    See the README.txt file and ensure you have Python 3.9+ installed on your system.
    Install the project dependencies:
    '''bash
    pip install -r requirements.txt

2. **Run the Program**
    Run the main.py script to start the program:
    python main.py.

    . You will be prompted to enter the name of an animal(e.g., "RABBIT", "MONKEY",etc)
    . The program fetches data from the specified source (API or local JSON) and then generates an HTML file named animals.html in the project folder.

3. **View the Results**
    Below is a brief overview of the key Python files:
    . data_fetcher.py: Responsible for fetching animal data from an external API or a local JSON file.
    . website_generator.py: Contains functions to convert the fetched data into HTML and inject it into an HTML template.
    . main.py: Orchestrates the data fetching and website generation. Prompts the user for input, then calls the other modules.

## Contributing Guidelines
1. Fork the repository
2. Create a new branch for your feature or bugfix.
3. Commit your changes with clear and descriptive messages.
4. Submit a pull request describing your changes in detail.

### Feel free to reach out to me if you have questions or suggestions. Happy coding!
