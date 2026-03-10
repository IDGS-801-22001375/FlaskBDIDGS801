from . import inscripciones
from models import db, Inscripcion, Curso, Alumnos
from flask import Flask, render_template, request, redirect, url_for, flash
import forms

@inscripciones.route("/inscripciones", methods=['GET', 'POST'])
def lista_inscripciones():
    create_form = forms.UserFormInscripciones(request.form)
    alumno_id = request.args.get('id', type=int)

    if alumno_id:
        inscripciones = Inscripcion.query.filter_by(alumno_id=alumno_id).all()
    else:
        inscripciones = Inscripcion.query.all()

    return render_template("/inscripciones/lista_inscripciones.html", form=create_form, inscripciones=inscripciones)

@inscripciones.route("/inscripciones_alumno/<int:id>")
def lista_inscripciones_por_alumno(id):
    alumno = Alumnos.query.get(id)
    inscripciones = Inscripcion.query.filter_by(alumno_id=id).all()
    return render_template("inscripciones/lista_inscripciones_por_alumno.html", alumno=alumno, inscripciones=inscripciones)

@inscripciones.route("/inscripciones/registrar", methods=['GET', 'POST'])
def registrar_inscripcion():
    create_form = forms.UserFormInscripciones(request.form)

    cursos = Curso.query.all()
    alumno_id = request.args.get("alumno_id")

    if request.method == 'POST':

        curso_id = request.form.get("curso")
        inscripcion_existente = Inscripcion.query.filter_by(alumno_id=alumno_id, curso_id=curso_id).first()

        if inscripcion_existente:
            flash("El alumno ya está inscrito en este curso", "danger")
            return redirect(url_for('inscripciones.registrar_inscripcion', alumno_id=alumno_id))

        inscripcion = Inscripcion(
            alumno_id=alumno_id,
            curso_id=request.form.get("curso")
        )

        db.session.add(inscripcion)
        db.session.commit()

        flash("Alumno inscrito correctamente", "success")

        return redirect(url_for('alumnos.lista_alumnos'))

    return render_template("/inscripciones/registrar_inscripcion.html", form=create_form, cursos=cursos, alumno_id=alumno_id)

@inscripciones.route("/inscripciones/detalles", methods=['GET','POST'])
def detalle_inscripcion():
	create_form=forms.UserFormInscripciones(request.form)
	if request.method=='GET':
		id=request.args.get('id')
		inscripcion=db.session.query(Inscripcion).filter(Inscripcion.id==id).first()
		id=request.args.get('id')
		alumno_id=inscripcion.alumno_id
		curso_id=inscripcion.curso_id

		return render_template('inscripciones/detalles_inscripcion.html', id=id, inscripcion=inscripcion)

@inscripciones.route("/inscripciones/modificar", methods=['GET', 'POST'])
def modificar_inscripcion():
    create_form = forms.UserFormInscripciones(request.form)
    cursos = Curso.query.all()
    if request.method == 'GET':
        id = request.args.get('id')
        inscripcion = Inscripcion.query.filter_by(id=id).first()
        create_form.id.data = inscripcion.id
        create_form.alumno.data = inscripcion.alumno_id
        create_form.curso.data = inscripcion.curso_id

    if request.method == 'POST':
        id = create_form.id.data
        inscripcion = Inscripcion.query.filter_by(id=id).first()
        inscripcion.alumno_id = create_form.alumno.data
        inscripcion.curso_id = create_form.curso.data

        db.session.commit()
        flash("Inscripción modificada correctamente", "success")
        return redirect(url_for('inscripciones.lista_inscripciones'))

    return render_template('inscripciones/modificar_inscripcion.html', form=create_form, cursos=cursos)

@inscripciones.route("/inscripciones/eliminar", methods=['GET', 'POST'])
def eliminar_inscripcion():
    create_form = forms.UserFormInscripciones(request.form)

    if request.method == 'GET':
        id = request.args.get('id')
        inscripcion = db.session.query(Inscripcion).filter(Inscripcion.id == id).first()
        create_form.id.data = inscripcion.id
        create_form.alumno.data = inscripcion.alumno_id
        create_form.curso.data = inscripcion.curso_id
        return render_template('inscripciones/eliminar_inscripcion.html', form=create_form, alumno=inscripcion.alumno.nombre, curso=inscripcion.curso.nombre)

    if request.method == 'POST':
        id = create_form.id.data
        inscripcion = db.session.query(Inscripcion).filter(Inscripcion.id == id).first()
        if inscripcion:
            db.session.delete(inscripcion)
            db.session.commit()
            flash("Inscripción eliminada correctamente", "success")
        return redirect(url_for('inscripciones.lista_inscripciones'))

    return render_template('inscripciones/eliminar_inscripcion.html', form=create_form)