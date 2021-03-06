from flask_sqlalchemy import SQLAlchemy 
db = SQLAlchemy()

DEFAULT_IMAGE = "https://sainfoinc.com/wp-content/uploads/2018/02/image-not-available.jpg"

def connect_db(app):
    """Connect to database"""

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pet"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        """Return image of pet or a generic image if one is not available"""

        return self.photo_url or DEFAULT_IMAGE

