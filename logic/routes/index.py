from flask import render_template, redirect, url_for, request, current_app, render_template_string, Blueprint
from logic import bp
from logic.database import store_user_data
from logic.send_email import send_promo_email

fixed_promo_code = "PROMOHAS10"

@bp.route('/', methods=['GET', 'POST'])
def landing_page():

    promo_code = None
    error_message = None

    if request.method == 'POST':
        
        name = request.form.get('name')
        email = request.form.get('email')

        # Server-side validation
        if not name or not email:
            error_message = "Please fill out all required fields."
        
        else:
            # Store the form data in the database
            store_user_data(name, email)

            #send email
            send_promo_email(name, email)

            # Set the promo code for display
            promo_code = fixed_promo_code
        return render_template('complete.html', template_folder=current_app.template_folder)
    
        # Render a temporary page with a message
    return render_template('index.html', template_folder=current_app.template_folder, promo_code=promo_code, error_message=error_message)


    