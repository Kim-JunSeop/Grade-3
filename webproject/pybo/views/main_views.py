from datetime import datetime

from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect

from pybo import db
from pybo.models import Health_Data, Exercise_Data,Signup_Data
from ..forms import UserCreateForm, UserLoginForm

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def main():
    return render_template('main.html')


@bp.route('/login')
def login_page():
    return render_template('login.html')



@bp.route('/signup', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = Signup_Data.query.filter_by(user_id=form.userid.data).first()
        if not user:
            user = Signup_Data(user_name=form.name.data,
                               user_id=form.userid.data,
                               user_password=generate_password_hash(form.password1.data),
                               email=form.email.data,
                               address=form.address.data,
                               phone=form.phone_number.data
                               )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.main'))
        else:
            flash('이미 존재하는 사용자입니다.')
    return render_template('/signup.html', form=form)

@bp.route('/login/', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = Signup_Data.query.filter_by(user_id=form.userid.data).first()
        if not user:
            error = "존재하지 않는 사용자입니다."

        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('main.main'))
        flash(error)
    return render_template('/login.html', form=form)


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = Signup_Data.query.get(user_id)


@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main.main'))