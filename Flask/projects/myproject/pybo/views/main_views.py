from flask import Blueprint, url_for
from werkzeug.utils import redirect

from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/') # 블루프린트 객체 생성

@bp.route('/hello') # 이 주소창으로 이동하면 함수가 실행되는 그런 느낌 !
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/') # bp를 앱 객체에 등록하면 라우트 함수를 관리를 할 수 가 있겠다 !
def index():
    question_list = Question.query.order_by(Question.create_date.desc())
    return redirect(url_for('question._list'))
