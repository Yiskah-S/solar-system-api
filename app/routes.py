from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, earth_masses):
        self.id = id
        self.name = name
        self.description = description
        self.earth_masses = earth_masses

planet_list = [
    Planet(1, "Mercury", "Small, rocky planet closest to the Sun", 0.330),
    Planet(2, "Venus", "Hottest planet in the solar system with a thick atmosphere", 4.87),
    Planet(3, "Earth", "Home to a diverse range of life forms, including humans", 5.97),
    Planet(4, "Mars", "Red planet with a thin atmosphere and polar ice caps", 0.642),
    Planet(5, "Jupiter", "Largest planet in the solar system with a thick atmosphere and many moons", 1898),
    Planet(6, "Saturn", "Known for its prominent rings made of ice and dust", 568),
    Planet(7, "Uranus", "Blue-green planet with a tilted axis of rotation", 86.8),
    Planet(8, "Neptune", "Blue planet with a windy atmosphere and many storms", 102),
]

planets_bp = Blueprint('planets', __name__, url_prefix='/planets')

@planets_bp.route('', methods=['GET'])
def get_planets():
    planet_dict_list = []
    for planet in planet_list:
        planet_dict = {
            'id': planet.id,
            'name': planet.name,
            'description': planet.description,
            'Earth masses': planet.earth_masses
        }
        planet_dict_list.append(planet_dict)
    
    return jsonify(planet_dict_list), 200


