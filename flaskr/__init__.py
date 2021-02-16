import io
import os
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import numpy as np
import pandas as pd
from io import StringIO
from io import BytesIO
import base64
from flask import Flask, send_file, render_template, jsonify, request, json
from flaskr.ma import movingAverage 
import requests
from flaskr.reward_strategy import Rewards_Strategy
from flaskr.db_utils import Db_Insert


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/smv')
    def smv():
        return json.dumps({"project": "Moving Average"})
    
    @app.route('/movingAverage', methods=['GET'])
    def smovingAverage():
        return movingAverage()

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='auth.index')

    @app.route('/inputdata', methods=['PUT'])
    def data_process():
        id_value = request.args.get('id')
        category_value = request.args.get('category')
        price_value = request.args.get('price')
        rewards_scheme_value = request.args.get('rewards_scheme')
        name_value = request.args.get('name')
        rs = Rewards_Strategy(category_value,rewards_scheme_value)
        reward_points = rs.madeupStrategy()
        size_addon = request.args.get('size') or request.args.get('addon')
        dbi = Db_Insert(id_value,category_value,price_value,rewards_scheme_value,reward_points,name_value,size_addon)
        dbi.insert_into_db()
        return json.dumps({ "rewards_scheme_value" : size_addon })

    return app