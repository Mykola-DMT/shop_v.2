from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,SelectField,SelectMultipleField,BooleanField,PasswordField
from wtforms.validators import DataRequired, ValidationError, Email,EqualTo
from app.models import User

class AddForm(FlaskForm):
    #numb=IntegerField(u'Number',validators=[DataRequired()])
    typename=StringField(u'Typename',validators=[DataRequired()])
    itemname=StringField(u'Itemname',validators=[DataRequired()])
    #sizes=SelectMultipleField('Selectsize',choices=[('36'),('38'),('40'),('42'),('44'),('46'),('48'),('50'),('52')], coerce=int,option_widget=None)
    size_i=IntegerField(u'Size',validators=[DataRequired()])
    price=IntegerField(u'Price',validators=[DataRequired()])
    # day=DateTimeField('Date')
    # isold=BooleanField('Sold')
    submit=SubmitField('Add')

class SearchForm(FlaskForm):
    param_types=[('Type','Type'),
    ('Name','Name'),
    ('Size','Size'),
    ('Price','Price'),
    ('Date','Date')]
    select=SelectField(u'Search for:',choices=param_types)
    search=StringField(u'',validators=[DataRequired()])
    submit=SubmitField('Search')

class LoginForm(FlaskForm):
    username=StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me=BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')