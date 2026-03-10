from . import cursos
from models import db, Curso, Maestros
from flask import Flask, render_template, request, redirect, url_for, flash
import forms

@cursos.route("/cursos", methods=['GET', 'POST'])
def lista_cursos():
    create_form=forms.UserFormCursos(request.form)
    curso=Curso.query.all()
    return render_template("/cursos/lista_cursos.html", form=create_form, cursos=curso)

@cursos.route("/cursos/registrar", methods=['GET', 'POST'])
def registrar_curso():
    create_form = forms.UserFormCursos(request.form)
    maestros = Maestros.query.all()

    if request.method == 'POST':

        curso_registrado = db.session.query(Curso)\
            .filter(Curso.nombre == create_form.nombre.data)\
            .first()

        if curso_registrado:
            flash("Ya hay un curso registrado con el mismo nombre", "danger")
            return redirect(url_for("cursos.lista_cursos"))

        curso = Curso(
            nombre=create_form.nombre.data,
            descripcion=create_form.descripcion.data,
            maestro_id=create_form.maestro.data
        )

        db.session.add(curso)
        db.session.commit()

        return redirect(url_for('cursos.lista_cursos'))

    return render_template("/cursos/agregar_curso.html", form=create_form, maestros=maestros)

@cursos.route("/cursos/detalles", methods=['GET','POST'])
def detalle_curso():
	create_form=forms.UserFormCursos(request.form)
	if request.method=='GET':
		id=request.args.get('id')
		curso=db.session.query(Curso).filter(Curso.id==id).first()
		id=request.args.get('id')
		nombre=curso.nombre
		descripcion=curso.descripcion
		maestro=curso.maestro
		
		return render_template('cursos/detalles_curso.html', id=id, nombre=nombre, descripcion=descripcion, maestro=maestro)

@cursos.route("/cursos/modificar", methods=['GET', 'POST'])
def modificar_curso():
    create_form = forms.UserFormCursos(request.form)
    maestros = Maestros.query.all()

    if request.method == 'GET':
        id = request.args.get('id')
        curso = db.session.query(Curso).filter(Curso.id == id).first()

        create_form.id.data = id
        create_form.nombre.data = curso.nombre
        create_form.descripcion.data = curso.descripcion
        create_form.maestro.data = curso.maestro_id

    if request.method == 'POST':

        curso_registrado = db.session.query(Curso)\
            .filter(
                Curso.nombre == create_form.nombre.data,
                Curso.id != create_form.id.data
            )\
            .first()

        if curso_registrado:
            flash("Ya hay un curso registrado con el mismo nombre", "danger")
            return redirect(url_for("cursos.lista_cursos"))

        id = create_form.id.data
        curso = db.session.query(Curso).filter(Curso.id == id).first()

        curso.nombre = create_form.nombre.data
        curso.descripcion = create_form.descripcion.data
        curso.maestro_id = create_form.maestro.data

        db.session.commit()

        return redirect(url_for('cursos.lista_cursos'))

    return render_template('cursos/modificar_curso.html', form=create_form, maestros=maestros)

@cursos.route("/cursos/eliminar", methods=['GET','POST'])
def eliminar_curso():
	create_form=forms.UserFormCursos(request.form)

	if request.method=='GET':
		id=request.args.get('id')
		curso=db.session.query(Curso).filter(Curso.id==id).first()
		create_form.id.data=request.args.get('id')
		create_form.nombre.data=str.rstrip(curso.nombre)
		create_form.descripcion.data=curso.descripcion
		create_form.maestro.data=curso.maestro_id
		return render_template('cursos/eliminar_curso.html', form=create_form, maestro=curso.maestro.nombre)

	if request.method=='POST':
		id=create_form.id.data
		curso=db.session.query(Curso).filter(Curso.id==id).first()
		if curso:
			db.session.delete(curso)
			db.session.commit()
		return redirect(url_for('cursos.lista_cursos'))
	return render_template('curso/eliminar_curso.html', form=create_form)