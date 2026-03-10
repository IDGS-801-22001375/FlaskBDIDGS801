from wtforms import IntegerField, StringField, EmailField, SelectField
from wtforms import Form, validators

class UserForm2(Form):
    id=IntegerField('id',[
        validators.number_range(min=1, max=20, message='Valor no valido')
    ])
    nombre=StringField('nombre',[
        validators.DataRequired(message='El nombre es requerido')
    ])
    apellidos=StringField('apellidos',[
        validators.DataRequired(message='Los apellidos son requerido')
    ])
    email=EmailField('email',[
        validators.DataRequired(message='El correo es requerido'),
        validators.Email(message='Ingrese un correo valido')
    ])
    telefono=StringField('telefono',[
        validators.DataRequired(message='El telefono es requerido'),
        validators.number_range(min=10, message='Ingrese un telefono valido')
    ])
    
class UserFormMestros(Form):
    matricula=IntegerField('matricula',[
        validators.DataRequired(message='La matricula es requerida'),
        validators.number_range(min=7, message='Ingrese una matricula valida')
    ])
    nombre=StringField('nombre',[
        validators.DataRequired(message='El nombre es requerido')
    ])
    apellidos=StringField('apellidos',[
        validators.DataRequired(message='Los apellidos son requerido')
    ])
    email=EmailField('email',[
        validators.DataRequired(message='El correo es requerido'),
        validators.Email(message='Ingrese un correo valido')
    ])
    especialidad=StringField('especialidad',[
        validators.DataRequired(message='La especialidad es requerida'),
        validators.number_range(min=7, message='Ingrese una especialidad valida')
    ])

class UserFormCursos(Form):
    id=IntegerField('id',[
        validators.number_range(min=1, max=20, message='Valor no valido')
    ])
    nombre=StringField('nombre',[
        validators.DataRequired(message='El nombre es requerido')
    ])
    descripcion=StringField('descripcion',[
        validators.DataRequired(message='La descripcion es requerida')
    ])
    maestro=SelectField('maestro',[
        validators.DataRequired(message='Seleccione un maestro'),
    ])

class UserFormInscripciones(Form):
    id=IntegerField('id',[
        validators.number_range(min=1, max=20, message='Valor no valido')
    ])
    alumno=SelectField('alumno',[
        validators.DataRequired(message='Seleccione un alumno'),
    ])
    curso=SelectField('curso',[
        validators.DataRequired(message='Seleccione un curso'),
    ])