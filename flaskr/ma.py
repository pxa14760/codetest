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
from flask import Flask, send_file, render_template
import functools
import sqlite3
from flaskr.db import get_db

def movingAverage():
    db = get_db()
    #dfd = pd.read_excel('/usr/local/bin/flask-codetest/flaskr/excel_files/drink.xlsx')
    dfd = pd.read_sql_query("select * from drink;", db)
    dfs = pd.read_sql_query("select * from sandwich;", db)
    dfr = pd.read_sql_query("select * from retail;", db)
    #dfs = pd.read_excel('/usr/local/bin/flask-codetest/flaskr/excel_files/sandwich.xlsx')
    #dfr = pd.read_excel('/usr/local/bin/flask-codetest/flaskr/excel_files/retail.xlsx')
    dfd['Drinks_MA'] = dfd['price'].rolling(2,win_type='triang').sum()
    dfd['Drinks_MA_pts'] = dfd['rewards_points'].rolling(2,win_type='triang').sum()
    dfs['Sandwich_MA'] = dfs['price'].rolling(2,win_type='triang').sum()
    dfs['Sandwich_MA_pts'] = dfs['rewards_points'].rolling(2,win_type='triang').sum()
    dfr['Retail_MA'] = dfr['price'].rolling(2,win_type='triang').sum()
    dfr['Retail_MA_pts'] = dfr['rewards_points'].rolling(2,win_type='triang').sum()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.get_xaxis().set_visible(False) 
    dfd.plot(ax=ax, y=['Drinks_MA','Drinks_MA_pts'])
    dfs.plot(ax=ax, y=['Sandwich_MA','Sandwich_MA_pts'])
    dfr.plot(ax=ax, y=['Retail_MA','Retail_MA_pts'])
    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode('ascii')
    return f"<img src='data:image/png;base64,{data}'/>"
    