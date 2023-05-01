from flask import Blueprint, jsonify, abort, make_response, request
from app.models.planet import Planet

from app import db

planets_bp = Blueprint('planets', __name__, url_prefix='/planets')

@planets_bp.route("", methods=['POST'])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name = request_body["name"],
        description = request_body["description"],
        mass = request_body["mass"],
        moons = request_body["moons"],
        distance_from_sun = request_body["distance_from_sun"],
        surface_area = request_body["surface_area"],
        namesake = request_body["namesake"],
        visited_by_humans = request_body['visited_by_humans'],
    )

    db.session.add(new_planet)
    db.session.commit()

    message = f"New planet {new_planet.name} successfully created!"
    return make_response(message, 201)

@planets_bp.route("", methods=["GET"])
def get_planets():
    mass = request.args.get("mass")
    moons = request.args.get("moons")
    distance = request.args.get("distance")
    visited = request.args.get("visited")

    planets = Planet.query

    if mass:
        planets = planets.filter_by(mass=mass)

    if moons:
        planets = planets.filter_by(moons=moons)

    if distance:
        planets = planets.filter_by(distance_from_sun=distance)

    if visited:
        planets = planets.filter_by(visited_by_humans=visited.lower())

    planets = planets.all()

    request_body = []
    for planet in planets:
        request_body.append(
            dict(
                id=planet.id,
                name=planet.name,
                description=planet.description,
                mass=planet.mass,
                moons=planet.moons,
                distance_from_sun=planet.distance_from_sun,
                surface_area=planet.surface_area,
                namesake=planet.namesake,
                visited_by_humans=planet.visited_by_humans,
            )
        )
    return jsonify(request_body), 200



def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"Planet {planet_id} is invalid!"}, 400))
    
    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message": f"Planet {planet_id} was not found!"}, 404))

    return planet

@planets_bp.route("/<planet_id>", methods=['GET'])
def get_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = {
            "name": planet.name,
            "description": planet.description,
            "mass": planet.mass,
            "moons": planet.moons,
            "distance_from_sun": planet.distance_from_sun,
            "surface_area": planet.surface_area,
            "namesake": planet.namesake,
            "visited_by_humans" : planet.visited_by_humans
        }
    return jsonify(request_body), 200

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.mass = request_body["mass"]
    planet.moons = request_body["moons"]
    planet.distance_from_sun = request_body["distance_from_sun"]
    planet.surface_area = request_body["surface_area"]
    planet.namesake = request_body["namesake"]
    planet.visited_by_humans = request_body['visited_by_humans']

    db.session.commit()

    return make_response(f"Planet {planet_id} successfully updated to {planet.name}, {planet.description}, {planet.mass}, {planet.moons}, {planet.distance_from_sun}, {planet.surface_area}, {planet.namesake}, and it's {planet.visited_by_humans} that it has been visited by humans!")

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def remove_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet {planet_id} was succesfully deleted")

@planets_bp.route("/visited", methods=["GET"])
def get_visited_planets():
    visited_planets = Planet.query.filter_by(visited_by_humans=True).all()
    request_body = []
    for planet in visited_planets:
        request_body.append(
            dict(
                id=planet.id,
                name=planet.name,
                description=planet.description,
                mass=planet.mass,
                moons=planet.moons,
                distance_from_sun=planet.distance_from_sun,
                surface_area=planet.surface_area,
                namesake=planet.namesake,
                visited_by_humans=planet.visited_by_humans,
            )
        )
    return jsonify(request_body), 200




# # Wave 06: Writing Tests

# ## Setup

# Complete the following requirements, with similar functionality to the Hello Books API:

# 1. Create a `.env` file.
# 1. Populate it with two environment variables: `SQLALCHEMY_DATABASE_URI` and `SQLALCHEMY_TEST_DATABASE_URI`. Set their values to the appropriate connection strings.
# 1. Create a test database with the correct, matching name.
# 1. Refactor the `create_app` method to:
#    * Check for a configuration flag
#    * Read the correct database location from the appropriate environment variables
# 1. Manually test that our development environment still works.
# 1. Create a `tests` folder with the files:
#     -  `tests/__init__.py`
#     -  `tests/conftest.py`
#     -  `tests/test_routes.py`.
# 1. Populate `tests/conftest.py` with the recommended configuration.
# 1. Create a test to check `GET` `/planets` returns `200` and an empty array.
# 1. Confirm this test runs and passes.

# ## Writing Tests

# Create test fixtures and unit tests for the following test cases:

# 1. `GET` `/planets/1` returns a response body that matches our fixture
# 1. `GET` `/planets/1` with no data in test database (no fixture) returns a `404`
# 1. `GET` `/planets` with valid test data (fixtures) returns a `200` with an array including appropriate test data
# 1. `POST` `/planets` with a JSON request body returns a `201`

# ## Code Coverage

# Check your code coverage using `pytest-cov`. Review the [code coverage exercise](https://github.com/adaGold/code-coverage-exercise) on how to use `pytest-cov` to generate a code coverage report. We will need to change the directory where the application code is located from `student` to `app`.

# `pytest --cov=app --cov-report html --cov-report term`

# For this project, we will not expect to have high test coverage because we have not tested all of our CRUD routes. Still, it is helpful to practice checking coverage and reading reports of the code which detail the code that is tested, and the code that is not tested.


