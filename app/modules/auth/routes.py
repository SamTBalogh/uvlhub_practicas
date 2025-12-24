from flask import redirect, render_template, url_for
from flask_login import current_user, login_user, logout_user

from app.modules.auth import auth_bp
from app.modules.auth.forms import LoginForm, SignupForm
from app.modules.auth.services import AuthenticationService
from app.modules.profile.services import UserProfileService

authentication_service = AuthenticationService()
user_profile_service = UserProfileService()

# Route constants
PUBLIC_INDEX_ROUTE = "public.index"
SIGNUP_TEMPLATE = "auth/signup_form.html"


@auth_bp.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if current_user.is_authenticated:
        return redirect(url_for(PUBLIC_INDEX_ROUTE))

    form = SignupForm()
    if form.validate_on_submit():
        email = form.email.data
        if not authentication_service.is_email_available(email):
            return render_template(SIGNUP_TEMPLATE, form=form, error=f"Email {email} in use")

        try:
            user = authentication_service.create_with_profile(**form.data)
        except Exception as exc:
            return render_template(SIGNUP_TEMPLATE, form=form, error=f"Error creating user: {exc}")

        # Log user
        login_user(user, remember=True)
        return redirect(url_for(PUBLIC_INDEX_ROUTE))

    return render_template(SIGNUP_TEMPLATE, form=form)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for(PUBLIC_INDEX_ROUTE))

    form = LoginForm()
    if form.validate_on_submit():  # Already checks POST internally
        if authentication_service.login(form.email.data, form.password.data):
            return redirect(url_for(PUBLIC_INDEX_ROUTE))

        return render_template("auth/login_form.html", form=form, error="Invalid credentials")

    return render_template("auth/login_form.html", form=form)


@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for(PUBLIC_INDEX_ROUTE))
