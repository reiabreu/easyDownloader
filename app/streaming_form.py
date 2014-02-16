from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required

class StreamingForm(Form):
    url = TextField('url', validators = [Required()])
