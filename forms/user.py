from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, BooleanField, TextAreaField, SubmitField, EmailField, IntegerField, DateTimeField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    surname = StringField('Фамилия пользователя', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired()])
    position = StringField('position', validators=[DataRequired()])
    speciality = StringField('speciality', validators=[DataRequired()])
    address = StringField('address', validators=[DataRequired()])
    submit = SubmitField('Войти')


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class AddJobForm(FlaskForm):
    team_leader = IntegerField('Тим лидер')
    job = StringField('Название')
    work_size = IntegerField('Размер работы')
    collaborators = StringField('Колабораторы')
    start_date = DateTimeField('Начало работы', validators=[DataRequired()])
    end_date = DateTimeField('Конец работы', validators=[DataRequired()])
    submit = SubmitField('Добавить работу')