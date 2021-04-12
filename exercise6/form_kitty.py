from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class addKitty(FlaskForm):
  name = StringField("Enter the Kitty name", validators=[DataRequired()])
  submit = SubmitField()

class delKitty(FlaskForm):
  kitty_id = IntegerField("ENter the kitty Id", validators=[DataRequired()])
  submit = SubmitField()
  
class addOwner(FlaskForm):
  name = StringField("Enter the Owner name", validators=[DataRequired()])
  kitty_id = IntegerField("Enter Kitty Id", validators=[DataRequired()])
  submit = SubmitField()

