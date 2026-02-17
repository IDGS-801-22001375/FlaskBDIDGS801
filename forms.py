from wtforms import IntegerField, StringField, EmailField
from wtforms import Form, validators

class UserForm2(Form):
    id=IntegerField('id',[
        validators.number_range(min=1, max=20, message='Valor no valido')
    ]),
    nombre=StringField('nombre',[
        validators.DataRequired(message='El nombre es requerido')
    ])
    apaterno=StringField('nombre',[
        validators.DataRequired(message='El apellido es requerido')
    ])
    email=EmailField('nombre',[
        validators.DataRequired(message='El correo es requerido'),
        validators.Email(message='Ingrese un correo valido')
    ])
    