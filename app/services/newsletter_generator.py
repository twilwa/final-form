from markdown2 import markdown
from flask import Markup

def generate_newsletter_from_query(query):
    # Fetch or generate your newsletter as Markdown
    newsletter_md = "# Newsletter Title\n\nSome content for **query**: " + query
    newsletter_html = markdown(newsletter_md)
    # Ensure that the HTML is marked safe for rendering in the template
    return Markup(newsletter_html)
