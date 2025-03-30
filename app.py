from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/heroes', methods = ['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes])

@app.route('/heroes/<int:id>', methods = ['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({'error': 'Hero not found'}), 404
    return jsonify(hero.to_dict())

@app.route('/powers', methods = ['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers])

@app.route('/powers/<int:id>', methods = ['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify( {'error': 'Power not found'} ), 404

    data = request.json
    if 'description' in data:
        try:
            power.description = data['description']
            db.session.commit()
        except ValueError as e:
            return jsonify({'error': str( e )}), 400

    return jsonify(power.to_dict())

@app.route('/hero_powers', methods = ['POST'])
def create_hero_power():
    data = request.json
    try:
        hero_power = HeroPower(
            strength = data['strength'],
            hero_id = data['hero_id'],
            power_id = data['power_id']
        )
        db.session.add(hero_power)
        db.session.commit()
        return jsonify(hero_power.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str( e )}), 400

if __name__ == '__main__':
    app.run(debug = True)
