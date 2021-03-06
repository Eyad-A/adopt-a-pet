from flask import Flask, render_template, redirect, flash, url_for, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet 
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "SEEEEKRET!"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app) 

connect_db(app)
db.create_all() 


##### ROUTES ######

@app.route('/')
def list_pets():
    """List all the pets on the home page"""

    pets = Pet.query.all() 
    return render_template("pet_list.html", pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """ Add a pet or handle add pet form submission"""

    form = AddPetForm()
    if form.validate_on_submit():
        new_pet = Pet(
            name = form.name.data,
            species = form.species.data,
            photo_url = form.photo_url.data,
            age = form.age.data,
            notes = form.notes.data
            )
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} has been added")
        return redirect('/')
    else:
        return render_template("add_pet.html", form=form)


@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    """Edit pet"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data,
        pet.notes = form.notes.data,
        pet.available = form.available.data
        db.session.commit()
        flash(f"{pet.name} has been updated")
        return redirect('/')
    else:
        return render_template('edit_pet.html', form=form, pet=pet)

    