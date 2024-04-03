from flask_smorest import Blueprint
from . import rout

bp = Blueprint('cars', __name__, description="Routes for cars")

