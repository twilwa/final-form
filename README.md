
# Flask Newsletter Generator

This is a Flask web application that generates newsletters based on user queries. It utilizes the Gemini service for content generation and Dagster for data processing.

## Project Structure

The project has the following structure:

final-form/
├── app/
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── home.py
│   │   └── search.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── gemini_service.py
│   │   └── newsletter_generator.py
│   └── templates/
│       ├── base.html
│       ├── index.html
│       └── newsletter.html
├── app.py
├── pipelines/
├── scripts/
├── static/
│   ├── css/
│   │   └── newsletter.css
│   └── js/
└── requirements.txt

## Installation

1. Clone the repository:
git clone https://github.com/your-username/final-form.git
cd final-form

2. Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate


3. Install the required packages:
pip install -r requirements.txt

## Usage

1. Start the Flask development server:
python app.py
2. Open your web browser and navigate to `http://localhost:5000`.

3. Enter a query in the search form to generate a newsletter based on the query.

## Configuration

- The Flask application is configured in the `app.py` file.
- The routes are defined in the `app/routes` directory.
- The services, including the Gemini service and newsletter generator, are located in the `app/services` directory.
- HTML templates are stored in the `app/templates` directory.
- Static files (CSS and JavaScript) are located in the `static` directory.

## Dependencies

The project relies on the following main dependencies:

- Flask: Web framework for building the application.
- Jinja2: Template engine for rendering HTML templates.
- markdown2: Library for converting Markdown to HTML.
- google-cloud-aiplatform: Library for interacting with the Gemini service.

For a complete list of dependencies, refer to the `requirements.txt` file.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).