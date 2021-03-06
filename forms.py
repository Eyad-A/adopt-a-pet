from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional


class AddPetForm(FlaskForm):
    """ Form for adding a pet """

    name = StringField("Pet Name", validators=[InputRequired()],)
    species = SelectField("Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")],)
    photo_url = StringField("Photo URL", validators=[Optional(), URL()],)
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)],)
    notes = TextAreaField("Notes", validators=[Optional(), Length(min=5)],)


class EditPetForm(FlaskForm):
    """ Form for editing a pet """ 
    photo_url = StringField("Photo URL", validators=[Optional(), URL()],)
    notes = TextAreaField("Notes", validators=[Optional(), Length(min=5)],)
    available = BooleanField("Available?")