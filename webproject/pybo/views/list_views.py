from datetime import datetime

from flask import Blueprint , url_for, request, render_template
from werkzeug.utils import redirect

from pybo import db
from pybo.models import Health_Data, Exercise_Data
from ..forms import InputForm

bp = Blueprint('list', __name__, url_prefix='/list')

@bp.route('/bodydata/')
def bodydatalist():
    page = request.args.get('page', type=int, default=1)
    bodydata_list = Health_Data.query.order_by(Health_Data.create_date.desc())
    bodydata_list = bodydata_list.paginate(page, per_page=10)
    return render_template('bodydata_list.html', bodydata_list=bodydata_list)


@bp.route('/exercisedata/')
def exercisedatalist():
    page = request.args.get('page', type=int, default=1)
    exercisedata_list = Exercise_Data.query.order_by(Exercise_Data.create_date.desc())
    exercisedata_list = exercisedata_list.paginate(page, per_page=10)
    return render_template('exercisedata_list.html', exercisedata_list=exercisedata_list)

@bp.route('/delete/bodydata/<int:bodydata_id>')
def delete_bodydata(bodydata_id):
    bodydata = Health_Data.query.get_or_404(bodydata_id)
    db.session.delete(bodydata)
    db.session.commit()
    return redirect(url_for('list.bodydatalist'))


@bp.route('/delete/exercisedata/<int:exercisedata_id>')
def delete_exercisedata(exercisedata_id):
    exercisedata = Exercise_Data.query.get_or_404(exercisedata_id)
    db.session.delete(exercisedata)
    db.session.commit()
    return redirect(url_for('list.exercisedatalist'))