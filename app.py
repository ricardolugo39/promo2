# app.py

from flask import Flask
from logic import bp

app = Flask(__name__, template_folder='logic/templates', static_folder='logic/static')

# Set a secret key for the session
app.secret_key = 'Hasten123456$'  # Replace with a strong, unique secret key

# Register the blueprint
app.register_blueprint(bp)


if __name__ == "__main__":
    app.run(debug=True)
