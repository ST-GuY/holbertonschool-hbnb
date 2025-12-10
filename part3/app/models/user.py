from app import db, bcrypt
from .basemodel import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    # --- RELATIONSHIPS ---
    # Un User peut créer plusieurs Places
    places = db.relationship('Place', backref='user', lazy=True)

    # Un User peut écrire plusieurs Reviews
    reviews = db.relationship('Review', backref='author', lazy=True)

    # --- Password handling ---
    def hash_password(self, password):
        """Hash le mot de passe avant de le stocker."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Vérifie si le mot de passe fourni correspond au mot de passe stocké."""
        return bcrypt.check_password_hash(self.password, password)

    # --- Serialization ---
    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'is_admin': self.is_admin
        }
