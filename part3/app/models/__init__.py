from app import db
from .user import User
from .place import Place
from .review import Review
from .amenity import Amenity

# --- Table d'association Many-to-Many Place ↔ Amenity ---
place_amenity = db.Table(
    'place_amenity',
    db.Column('place_id', db.Integer, db.ForeignKey('places.id'), primary_key=True),
    db.Column('amenity_id', db.Integer, db.ForeignKey('amenities.id'), primary_key=True)
)

# --- Définition de la relation Many-to-Many dans Place ---
Place.amenities = db.relationship(
    'Amenity',
    secondary=place_amenity,
    lazy='subquery',
    backref=db.backref('places', lazy=True)
)

# --- Relations One-to-Many ---
# User → Place
User.places = db.relationship('Place', backref='user', lazy=True)

# User → Review
User.reviews = db.relationship('Review', backref='author', lazy=True)

# Place → Review
Place.reviews = db.relationship('Review', backref='place', lazy=True)
