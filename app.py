from flask import Flask, request, render_template
from app.routes.home import home_bp
from app.routes.search import search_bp
import os

app = Flask(__name__, template_folder='/home/anon/ubuntu-repos/final-form/app/templates', static_folder='/home/anon/ubuntu-repos/final-form/app/static')
app.register_blueprint(home_bp)
app.register_blueprint(search_bp)

if __name__ == '__main__':
    app.run(debug=True)
