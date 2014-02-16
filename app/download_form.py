from flask.ext.wtf import Form
from wtforms import TextField, BooleanField,RadioField
from wtforms.validators import Required

class DownloadForm(Form):
    url = TextField('url', validators = [Required()])
    download_mode=RadioField('download_mode', choices=[('uploaded','Uploaded.net'),('wget','Wget')],validators = [Required()])
