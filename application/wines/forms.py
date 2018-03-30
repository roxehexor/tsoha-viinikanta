from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class WineForm(FlaskForm):
    name = StringField("Wine name", [validators.Length(min=2)])
    rate = IntegerField("Rating", [validators.NumberRange(min=0, max=5, 
                                    message='Rating must be in between of 0 and 5')])
 
    class Meta:
        csrf = False