from flask import Blueprint, request, render_template
import json
from src.main.visualization import main

visualise = Blueprint('visualise', __name__)


@visualise.route("/", methods=['GET'])
def visualise_data():
    """Produce pair plot of the data."""
    main()
    return render_template("index.html", img='data_vis.png')
