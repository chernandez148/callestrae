from sqlalchemy_serializer import SerializerMixin
from flask import session
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy import Enum
from sqlalchemy.ext.hybrid import hybrid_property
from bcrypt import hashpw, gensalt
from flask_bcrypt import Bcrypt
from config import db, app

bcrypt = Bcrypt(app)
# Models go here!

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    email = db.Column(db.String, unique=True, nullable=False)
    dob = db.Column(db.String)
    _password_hash = db.Column(db.String(128), nullable=False)

    characters = db.relationship('Character', backref='users')

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    serialize_rules = ('-characters', '-created_at', '-updated_at')

    @hybrid_property
    def password(self):
        return self._password_hash 

    @password.setter
    def password(self, password):
        salt = gensalt()
        self._password_hash = hashpw(password.encode('utf-8'), salt).decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))

    @validates('email')
    def validate_email(self, key, email):
        assert '@' in email, 'Email address must contain an @ symbol.'
        return email

class Character(db.Model, SerializerMixin):
    __tablename__ = 'characters'

    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String, nullable=False)
    character_sex = db.Column(db.String, nullable=False)
    character_region = db.Column(Enum(
        'Nemar', 'Cyneil', 'Corize', 'Naurra Isles', 'Ausstero'
    ), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    class_name_id = db.Column(db.Integer, db.ForeignKey('class_names.id'))

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    serialize_rules = ('-class_name_id', '-user_id', '-created_at', '-updated_at')


class ClassName(db.Model, SerializerMixin):
    __tablename__ = 'class_names'

    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String)
    male_class_image = db.Column(db.String)
    male_class_sprite_up = db.Column(db.String)
    male_class_sprite_left = db.Column(db.String)
    male_class_sprite_right = db.Column(db.String)
    male_class_sprite_down = db.Column(db.String)
    female_class_image = db.Column(db.String)
    female_class_sprite_up = db.Column(db.String)
    female_class_sprite_left = db.Column(db.String)
    female_class_sprite_right = db.Column(db.String)
    female_class_sprite_down = db.Column(db.String)
    lvl = db.Column(db.Integer)
    hp = db.Column(db.Integer)
    mg = db.Column(db.Integer)
    strg = db.Column(db.Integer)
    defn = db.Column(db.Integer)
    mind = db.Column(db.Integer)
    intl = db.Column(db.Integer)
    spd = db.Column(db.Integer)
    evad = db.Column(db.Integer)

    characters = db.relationship('Character', backref='class_name')
    knight_skills = db.relationship('KnightSkill', backref='class_name')

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    serialize_rules = ('-characters', '-knight_skills', '-created_at', '-updated_at')


class KnightSkill(db.Model, SerializerMixin):
    __tablename__ = 'knight_skills'

    id = db.Column(db.Integer, primary_key=True)
    skill_name = db.Column(db.String)
    skill_description = db.Column(db.String)
    skill_cost = db.Column(db.Integer)
    skill_level = db.Column(db.Integer)
    skill_icon = db.Column(db.String)

    class_name_id = db.Column(db.Integer, db.ForeignKey('class_names.id'))

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    serialize_rules = ('-class_name_id', '-created_at', '-updated_at')

class Inventory(db.Model, SerializerMixin):
    __tablename__ = 'inventories'

    id = db.Column(db.Integer, primary_key=True)
    qty = db.Column(db.Integer)
    name = db.Column(db.String)
    description = db.Column(db.String)
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    serialize_rules = ('-character_id', '-created_at', '-updated_at')







