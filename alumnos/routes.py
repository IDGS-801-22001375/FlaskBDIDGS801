from . import alumnos
from models import db, Alumnos
from flask import Flask, render_template, request, redirect, url_for
import forms

@alumnos.route("/alumnos", methods=['GET', 'POST'])
def lista_alumnos():
    create_form=forms.UserForm2(request.form)
    alumno=Alumnos.query.all()
    return render_template('/alumnos/lista_alumnos.html', form=create_form, alumnos=alumno)

@alumnos.route("/alumnos/registro", methods=['GET','POST'])
def registro_alumno():
	create_form=forms.UserForm2(request.form)
	if request.method=='POST':
		alumno=Alumnos(nombre=create_form.nombre.data, 
			apellidos=create_form.apellidos.data, 
			email=create_form.email.data,
			telefono=create_form.telefono.data)
		db.session.add(alumno)
		db.session.commit()
		return redirect(url_for('alumnos.lista_alumnos'))

	return render_template('alumnos/Alumnos.html', form=create_form)

@alumnos.route("/alumnos/detalles", methods=['GET','POST'])
def detalle_alumno():
	create_form=forms.UserForm2(request.form)
	if request.method=='GET':
		id=request.args.get('id')
		alumno=db.session.query(Alumnos).filter(Alumnos.id==id).first()
		id=request.args.get('id')
		nombre=alumno.nombre
		apellidos=alumno.apellidos
		email=alumno.email
		telefono=alumno.telefono
		
		return render_template('alumnos/detalles.html', id=id, nombre=nombre, apellidos=apellidos, email=email, telefono=telefono)

@alumnos.route("/alumnos/modificar", methods=['GET', 'POST'])
def modificar_alumno():
	create_form=forms.UserForm2(request.form)
	if request.method=='GET':
		id=request.args.get('id')
		alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
		create_form.id.data=request.args.get('id')
		create_form.nombre.data=str.rstrip(alum1.nombre)
		create_form.apellidos.data=alum1.apellidos
		create_form.email.data=alum1.email
		create_form.telefono.data=alum1.telefono
	if request.method=='POST':
		id=create_form.id.data
		alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
		alum1.id=id
		alum1.nombre=str.rstrip(create_form.nombre.data)
		alum1.apellidos=create_form.apellidos.data
		alum1.email=create_form.email.data
		alum1.telefono=create_form.telefono.data
		db.session.add(alum1)
		db.session.commit()
		return redirect(url_for('alumnos.lista_alumnos'))
	return render_template('alumnos/modificar.html', form=create_form)

@alumnos.route("/alumnos/eliminar", methods=['GET','POST'])
def eliminar_alumno():
	create_form=forms.UserForm2(request.form)
	if request.method=='GET':
		id=request.args.get('id')
		alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
		create_form.id.data=request.args.get('id')
		create_form.nombre.data=str.rstrip(alum1.nombre)
		create_form.apellidos.data=alum1.apellidos
		create_form.email.data=alum1.email
		create_form.telefono.data=alum1.telefono
		return render_template('alumnos/eliminar.html', form=create_form)

	if request.method=='POST':
		id=create_form.id.data
		alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
		if alum1:
			db.session.delete(alum1)
			db.session.commit()
		return redirect(url_for('alumnos.lista_alumnos'))
	return render_template('alumnos/eliminar.html', form=create_form)

@alumnos.route('/perfil/<nombre>')
def perfil(nombre):
    return f"Perfil de {nombre}"