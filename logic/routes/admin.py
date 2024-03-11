from flask import render_template, current_app, Blueprint, request, redirect, g, session, url_for
from logic.database import fetch_user_data, init_database
import sqlite3
import os

admin_bp = Blueprint('admin', __name__)

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'Hasten123456$'


@admin_bp.route('/admin', methods=['GET', 'POST'])
def display_admin():
    print("Request Method:", request.method)
    # Check if the user is already authenticated
    if not session.get('logged_in'):
        # If not authenticated, check if the login form is submitted
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')

            # Check the entered credentials against hardcoded values (demo purposes)
            if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
                # Set the user as authenticated
                session['logged_in'] = True
                return redirect(url_for('admin.display_admin'))  # Redirect to admin page upon successful login
            else:
                return render_template('login.html', login_error='Invalid credentials')
        
        # If not authenticated and no login form submitted, render the login page
        return render_template('login.html')
    else:
        # User is already authenticated, display the admin page
        user_data = fetch_user_data()
        return render_template('admin.html', user_data=user_data)
