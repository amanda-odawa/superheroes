from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'heroes'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    super_name = db.Column(db.String, nullable = False)

    hero_powers = db.relationship('HeroPower', backref = 'hero', cascade = 'all, delete')

    def to_dict(self):
        return {
            'id':self.id,
            'name':self.name,
            'super_name':self.super_name,
            'hero_powers':[
                {
                    'id': hp.id,
                    'hero_id': hp.hero_id,
                    'power_id': hp.power_id,
                    'strength': hp.strength,
                    'power': hp.power.to_dict()
                } for hp in self.hero_powers
            ]
        }
    
class Power(db.Model):
    __tablename__ = 'powers'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    description = db.Column(db.String, nullable = False)

    hero_powers = db.relationship('HeroPower', backref = 'power', cascade = 'all, delete')

    @validates('description')
    def validate_description(self, key, description):
        if len(description) < 20:
            raise ValueError('Description must be present and at least 20 characters long')
        return description
    
    def to_dict(self):
        return {
            'description':self.description,
            'id':self.id,
            'name':self.name
        }
    
class HeroPower(db.Model):
    __tablename__ = 'hero_powers'
    id = db.Column(db.Integer, primary_key = True)
    strength = db.Column(db.String, nullable = False)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable = False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable = False)

    @validates('strength')
    def validate_strength(self, key, strength):
        if strength not in ['Strong', 'Weak', 'Average']:
            raise ValueError('Strength must be one of the following values: Strong, Weak, Average')
        return strength
    
    def to_dict(self):
        return {
            'id': self.id,
            'hero_id': self.hero_id,
            'power_id': self.power_id,
            'strength': self.strength,
            'hero': {
                'id': self.hero.id,
                'name': self.hero.name,
                'super_name': self.hero.super_name
            },
            'power': self.power.to_dict()
        }
