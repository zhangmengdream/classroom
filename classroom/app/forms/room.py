from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, IntegerField, Form
from wtforms.validators import DataRequired, Length


class UploadForm(Form):
    title = StringField(validators=[DataRequired(), Length(1, 50, message='标题长度应该在1到50个字符之间')])
    author = StringField(validators=[DataRequired(), Length(1, 30, message='用户名长度应该在1到30个字符之间')])
    number = IntegerField(default=1)
    abstract = StringField(validators=[DataRequired(), Length(1, 1000, message='简介长度应该在1到1000个字符之间')])
    classify = StringField(validators=[DataRequired(), Length(1, 20, message='课程分类长度应该在1到20个字符之间')])

    # image = FileField(validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
    # video = FileField(validators=[FileRequired()])
