from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField
from flask_ckeditor import CKEditorField
from wtforms.validators import DataRequired



class PostForm(FlaskForm):
    title = StringField('Your Title', validators=[DataRequired()])
    content = CKEditorField('Your Content', validators=[DataRequired()])
    picture =FileField('Upload Your Post Image', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'webp'])])
    submit = SubmitField('Post')
