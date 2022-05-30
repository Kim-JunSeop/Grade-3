from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email
from flask import *

class InputForm(FlaskForm):
    height = FloatField('키', validators=[DataRequired('키는 필수 입력 항목입니다.')])
    weight = FloatField('몸무게', validators=[DataRequired('몸무게는 필수 입력 항목입니다.')])
    body_fat = FloatField('체지방', validators=[DataRequired('체지방은 필수 입력 항목입니다.')])
    body_muscle = FloatField('골격근량', validators=[DataRequired('골격근량은 필수 입력 항목입니다.')])


class UserCreateForm(FlaskForm):
    name = StringField('사용자이름', validators=[DataRequired()])
    userid = StringField('', validators=[DataRequired(), Length(min=3, max=15)])
    password1 = PasswordField('', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('', validators=[DataRequired(), Email('이메일 형식이 옳지 않습니다')])
    address = StringField('주소', validators=[DataRequired()])
    phone_number = StringField('핸드폰', validators=[DataRequired()])

class UserLoginForm(FlaskForm):
    userid = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])