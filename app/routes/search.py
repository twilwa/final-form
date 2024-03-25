import csv
from flask import Blueprint, request, render_template
from app.services.newsletter_generator import generate_newsletter_from_query

search_bp = Blueprint('search', __name__)

@search_bp.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    
    # Read the CSV file and extract the top stories
    with open('/home/anon/ubuntu-repos/dagster/tutorial/data/topstories.csv', 'r') as file:
        reader = csv.DictReader(file)
        top_stories = list(reader)

    # Generate the newsletter content using the top stories
    newsletter_content = "# Top Stories\n\n"
    for story in top_stories[:10]:  # Display only the top 10 stories
        newsletter_content += f"## {story['title']}\n"
        newsletter_content += f"[Read more]({story['url']})\n\n"

    # Render the newsletter template with the generated content
    return render_template('newsletter.html', newsletter_content=newsletter_content)