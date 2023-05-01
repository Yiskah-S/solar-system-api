from app import db

class Planet(db.Model):
    __tablename__ = 'planets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    mass = db.Column(db.Numeric(precision=8, scale=3), nullable=False)
    moons = db.Column(db.Integer, nullable=False)
    distance_from_sun = db.Column(db.Numeric(precision=8, scale=3), nullable=False)
    surface_area = db.Column(db.Numeric(precision=8, scale=3), nullable=False)
    namesake = db.Column(db.String, nullable=False)
    visited_by_humans = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'<Planet {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'mass': self.mass,
            'moons': self.moons,
            'distance_from_sun': self.distance_from_sun,
            'surface_area': self.surface_area,
            'namesake': self.namesake,
            'visited_by_humans': self.visited_by_humans
        }


