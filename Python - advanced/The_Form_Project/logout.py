from flask import Blueprint, session, redirect

logout_section = Blueprint('/logout', __name__)


@logout_section.route('/logout')
def logout():
    session.clear()

    return redirect('/')
