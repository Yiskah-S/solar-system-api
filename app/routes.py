from flask import Blueprint, jsonify, abort, make_response


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

@planets_bp.route("", methods=["GET"])
def get_planets():
    planets_response = []
    for planet in planet_list:
        planets_response.append(planet.to_dict())

    return jsonify(planets_response), 200

@planets_bp.route("/<id>", methods=["GET"])
def get_planet(id):
    planet = validate_planet(id)

    return planet.to_dict()

def validate_planet(id):
    try:
        id = int(id)
    
    except:
        abort(make_response({"message": f"Planet {id} is invalid!"}, 400))
    
    for planet in planet_list:
        if planet.id == id:
            return planet

    abort(make_response({"message": f"Planet {id} is not found!"}, 404))

# # Wave 03: Connecting the Database, Read and Create Endpoints

# ## Database Setup

# Complete the following setup steps of the Solar System API repo:
# 1. Activate the virtual environment
# 1. Create the database `solar_system_development`
#     * *Every member of the group must create the database on their computer*
# 1. Setup the `Planet` model with the attributes `id`, `name`, and `description`, and one additional attribute
# 1. Create a migration to add a table for the `Planet` model and then apply it. 
#     * *Confirm that the `planet` table has been created as expected in postgres*.

# ## RESTful Endpoints: Create and Read

# Create or refactor the following endpoints, with similar functionality presented in the Hello Books API:

# As a client, I want to send a request...

# 1. ...with new valid `planet` data and get a success response, so that I know the API saved the planet data
# 1. ...to get all existing `planets`, so that I can see a list of planets, with their `id`, `name`, `description`, and other data of the `planet`.

# # Wave 04: Read, Update, Delete

# ## RESTful Endpoints: Read, Update, and Delete

# Create the following endpoints, with similar functionality presented in the Hello Books API:

# As a client, I want to send a request...

# 1. ...to get one existing `planet`, so that I can see the `id`, `name`, `description`, and other data of the `planet`.
# 1. ... with valid planet data to update one existing `planet` and get a success response, so that I know the API updated the `planet` data.
# 1. ... to delete one existing `planet` and get a success response, so that I know the API deleted the `planet` data..
#     * Each of the above endpoints should respond with a `404` for non-existing planets and a `400` for invalid `planet_id`.

# # Wave 05: Review and Refactor

# Review the requirements for Wave 01 - 04
# * Test the endpoints using postman
# * Complete or fix any incomplete or broken endpoints
# * Look for opportunities to refactor

# As time allows, add custom routes. 
# * Consider using query params

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


