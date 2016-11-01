#encoding:utf-8
from flask.ext.wtf import Form
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length

class TodoListForm(Form):
    content=StringField(u'新增任务',validators=[DataRequired(),Length(1,20)])
    submit=SubmitField(label=u'添加')

class ModifyForm(Form):
    content = StringField(u'修改任务', validators=[DataRequired(), Length(1, 20)])
    submit=SubmitField(label=u'提交修改')