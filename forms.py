from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email, Length
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class RegisterForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=5, max=12)])
    name: StringField = StringField(label='Ime i Prezime', validators=[DataRequired(), Length(max=20)])
    submit = SubmitField(label="Register")

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=5, max=12)])
    submit = SubmitField(label="Logiraj se idiote!")

class CommentForm(FlaskForm):
    body = CKEditorField("Komentiraj, znamo da oćeš:", validators=[DataRequired()])
    submit = SubmitField("Objavi komentar")