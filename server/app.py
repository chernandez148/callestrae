#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, session, make_response, abort, jsonify
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

# Local imports
from config import app, db, api
from models import User, Character, ClassName, KnightSkill, Inventory

# Views go here!
class SignUp(Resource):

    def post(self):
        data = request.get_json()
        try:
            new_user = User(
                fname=data['fname'],
                lname=data['lname'],
                email=data['email'],
                dob=data['dob'],
                password=data['password']
            )
            db.session.add(new_user)
            db.session.commit()

            session['user_id'] = new_user.id

            response_dict = new_user.to_dict()
            response = jsonify(response_dict)
            response.status_code = 201
            return response
        
        except ValueError as e:
            abort(422, e.args[0])
        except IntegrityError as e:
            db.session.rollback()
            abort(422, "Email already exists.")

api.add_resource(SignUp, '/signup')

class Login(Resource):

    def post(self):
        data = request.get_json()
        check_user = User.query.filter(User.email == data['email']).first()

        if check_user and check_user.authenticate(data['password']):
            session['user_id'] = check_user.id
            return make_response(check_user.to_dict(), 200)
        return {'error': 'Unauthorized'}, 401
    
api.add_resource(Login, '/login')

class Logout(Resource):
    def delete(self):
        session['user_id'] = None 
        response = make_response('',204)
        return response
    
api.add_resource(Logout, '/logout')

class Users(Resource):
    
    def get(self):
        user = [u.to_dict() for u in User.query.all()]
        return make_response(jsonify(user), 200)

api.add_resource(Users, '/users')

class CharacterCreation(Resource):

    def post(self):
        data = request.get_json()

        new_character = Character(
            character_name=data['character_name'],
            character_sex=data['character_sex'],
            character_region=data['character_region'],
            class_name_id=data['class_name_id']
        )
        db.session.add(new_character)
        db.session.commit()

        response_dict = new_character.to_dict()
        response = make_response(
            response_dict,
            201
        )
        return response

api.add_resource(CharacterCreation, '/new_character')

class Characters(Resource):

    def get(self):
        character = [c.to_dict() for c in Character.query.all()]
        return make_response(jsonify(character), 200)
    
api.add_resource(Characters, '/characters')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
