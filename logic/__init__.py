# logic/__init__.py

from flask import Blueprint
from logic.database import init_database

# Initialize the database
init_database()

bp = Blueprint('main_app', __name__)

from logic.routes.index import landing_page
from logic.routes.complete_order import display_complete_order

# Add URL rules to the blueprint
bp.add_url_rule('/', 'landing_page', landing_page)
