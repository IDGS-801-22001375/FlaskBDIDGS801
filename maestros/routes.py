from . import maestros
from models import db, Maestros
from flask import Flask, render_template, request, redirect, url_for, flash
import forms

@maestros.route("/maestros", methods=['GET', 'POST'])
def lista_maestros():
    create_form=forms.UserFormMestros(request.form)
    maestro=Maestros.query.all()
    return render_template("/maestros/lista_maestros.html", form=create_form, maestros=maestro)

@maestros.route("/maestros/registro", methods=['GET','POST'])
def registro_maestro():
    create_form = forms.UserFormMestros(request.form)

    if request.method == 'POST':

        maestro_registrado = db.session.query(Maestros)\
            .filter(Maestros.matricula == create_form.matricula.data)\
            .first()

        if maestro_registrado:
            flash("Ya hay un maestro con la misma matrícula", "danger")
            return redirect(url_for("maestros.lista_maestros"))

        maestro = Maestros(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            email=create_form.email.data,
            matricula=create_form.matricula.data,
            especialidad=create_form.especialidad.data
        )

        db.session.add(maestro)
        db.session.commit()

        flash("Maestro registrado correctamente", "success")
        return redirect(url_for('maestros.lista_maestros'))

    return render_template('maestros/registro_maestro.html', form=create_form)

@maestros.route("/maestros/detalles", methods=['GET','POST'])
def detalles_maestro():
	create_form=forms.UserFormMestros(request.form)
	if request.method=='GET':
		matricula=request.args.get('matricula', type=int)
		maestro=db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		matricula=request.args.get('matricula', type=int)
		nombre=maestro.nombre
		apellidos=maestro.apellidos
		email=maestro.email
		especialidad=maestro.especialidad
		
		return render_template('maestros/detalles_maestro.html', matricula=matricula, nombre=nombre, apellidos=apellidos, email=email, especialidad=especialidad)

@maestros.route("/maestros/eliminar", methods=['GET','POST'])
def eliminar_maestro():
	create_form=forms.UserFormMestros(request.form)
	if request.method=='GET':
		matricula=request.args.get('matricula')
		maestro=db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		create_form.matricula.data=request.args.get('matricula')
		create_form.nombre.data=str.rstrip(maestro.nombre)
		create_form.apellidos.data=maestro.apellidos
		create_form.email.data=maestro.email
		create_form.especialidad.data=maestro.especialidad
		return render_template('maestros/eliminar_maestros.html', form=create_form)

	if request.method=='POST':
		matricula=create_form.matricula.data
		maestro=db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		if maestro:
			db.session.delete(maestro)
			db.session.commit()
		return redirect(url_for('maestros.lista_maestros'))
	return render_template('maestros/eliminar_maestros.html', form=create_form)

@maestros.route("/maestros/modificar", methods=['GET', 'POST'])
def modificar_maestro():
	create_form=forms.UserFormMestros(request.form)
	if request.method=='GET':
		matricula=request.args.get('matricula')
		maestro=db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		create_form.matricula.data=request.args.get('matricula')
		create_form.nombre.data=str.rstrip(maestro.nombre)
		create_form.apellidos.data=maestro.apellidos
		create_form.email.data=maestro.email
		create_form.especialidad.data=maestro.especialidad
	if request.method=='POST':
		matricula=create_form.matricula.data
		maestro=db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		maestro.matricula=matricula
		maestro.nombre=str.rstrip(create_form.nombre.data)
		maestro.apellidos=create_form.apellidos.data
		maestro.email=create_form.email.data
		maestro.especialidad=create_form.especialidad.data
		db.session.add(maestro)
		db.session.commit()
		return redirect(url_for('maestros.lista_maestros'))
	return render_template('maestros/modificar_maestros.html', form=create_form)

@maestros.route('/perfil/<nombre>')
def perfil(nombre):
    return f"Perfil de {nombre}"