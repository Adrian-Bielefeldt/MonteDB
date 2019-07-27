from flask import render_template, request, flash

from .db import Person, PersonType, db
from .forms import PersonForm


def setup_views(app):

    @app.route('/add')
    def add():
        form = PersonForm()
        return render_template('add_edit.html', form=form)

    @app.route('/edit')
    def edit():
        edit_id = request.args.get('id', '')
        person = Person.query.filter_by(id=edit_id).first()
        form = PersonForm()
        form.personID.data = person.id
        form.lastname.data = person.lastname
        form.firstname.data = person.firstname
        return render_template('add_edit.html', form=form)

    @app.route('/people', methods=('GET', 'POST'))
    def hello():
        people = Person.query.all()

        form = PersonForm(request.form)

        if request.method == 'POST' and form.validate():
            edit_id = form.personID.data
            if edit_id != "":
                person = Person.query.filter_by(id=edit_id).first()
            else:
                person = Person()
            person.lastname = form.lastname.data
            person.firstname = form.firstname.data
            db.session.add(person)
            db.session.commit()
            people = Person.query.all()

        return render_template('person.html', people=people)

