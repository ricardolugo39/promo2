# logic/__init__.py

from flask import Blueprint
from logic.database import init_database
from logic.routes.admin import admin_bp

# Initialize the database
init_database()

bp = Blueprint('main_app', __name__)

from logic.routes.index import landing_page
from logic.routes.admin import display_admin

# Add URL rules to the blueprint
bp.add_url_rule('/', 'landing_page', landing_page)
bp.add_url_rule('/admin', 'display_admin', display_admin)

