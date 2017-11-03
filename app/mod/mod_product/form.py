from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    id_product = StringField('id_product', validators=[validators.optional()])
    name_product = StringField('name_product', validators=[validators.optional()])