import csv
from flask import Blueprint, request, render_template
from app.services.newsletter_generator import generate_newsletter_from_query

search_bp = Blueprint('search', __name__)

@search_bp.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    newsletter_content = generate_newsletter_from_query(query)

    # Update the file path to the new location in the static folder
    with open('static/top_stories.csv', 'r') as file:
        reader = csv.DictReader(file)
        top_stories = list(reader)

    # Render the newsletter template with the generated content and top stories
    return render_template('newsletter.html', newsletter_content=newsletter_content, top_stories=top_stories)