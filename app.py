from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# In your /app/routes or app.py file

@app.route('/search', methods=['POST'])
def search_newsletters():
    query = request.form.get('query')
    # Process the query, fetch data, generate newsletter, etc.
    # For this example, let's say you have a function that returns the rendered Markdown as HTML
    newsletter_html = generate_newsletter_from_query(query)
    return newsletter_html


if __name__ == '__main__':
    app.run(debug=True)
