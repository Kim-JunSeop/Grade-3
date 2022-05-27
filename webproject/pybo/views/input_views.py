from datetime import datetime

from flask import Blueprint , url_for, request, render_template
from werkzeug.utils import redirect

from pybo import db
from pybo.models import Health_Data, Exercise_Data
from ..forms import InputForm

bp = Blueprint('input', __name__, url_prefix='/input')

@bp.route('/')
def input_index():

    recent_month1 = Health_Data.query.order_by(Health_Data.id.desc())[0]
    recent_month2 = Health_Data.query.order_by(Health_Data.id.desc())[1]
    recent_month3 = Health_Data.query.order_by(Health_Data.id.desc())[2]


    '''exercise_list = Exercise_Data.query.filter(Exercise_Data.create_date.like('% %')).all() like안에 변수 넣고싶음 질문해보기'''
    exercise_list = Exercise_Data.query.filter(Exercise_Data.create_date.like('%-05-%')).all()
    return render_template('index.html', recent_month1=recent_month1, recent_month2=recent_month2,
                           recent_month3=recent_month3, exercise_list=exercise_list)




@bp.route('/inputdata1')
def input_data_html():
    return render_template('inputdata1.html')


@bp.route('/inputdata1', methods=('POST',))
def input_data1():
    height = request.form['height']
    weight = request.form['weight']
    body_fat = request.form['body_fat']
    body_muscle = request.form['body_muscle']
    data = Health_Data(height=height, weight=weight, body_fat=body_fat, body_muscle=body_muscle, create_date=datetime.now())
    db.session.add(data)
    db.session.commit()
    return render_template('complete.html')


@bp.route('/inputmonthdata1')
def input_month_data_html():
    return render_template('inputmonthdata1.html')

@bp.route('/inputmonthdata1', methods=('POST',))
def input_month_data1():
    exercise_type = request.form['exercise_type']
    exercise_time = request.form['exercise_time']
    exercise_note = request.form['exercise_note']
    data = Exercise_Data(exercise_type=exercise_type, exercise_time=exercise_time, exercise_note=exercise_note, create_date=datetime.now())
    db.session.add(data)
    db.session.commit()
    return render_template('complete.html')

@bp.route('/complete')
def input_complete():
    return render_template('complete.html')
