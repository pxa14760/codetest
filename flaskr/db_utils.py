import sqlite3
from flaskr.db import get_db
from flask import current_app, g
class Db_Insert:

    def __init__(self,id_value,category_value,price_value,rewards_scheme_value,reward_points,name_value,size_addon):
        self.id_value = id_value
        self.category_value = category_value
        self.price_value = price_value
        self.rewards_scheme_value = rewards_scheme_value
        self.rewards_points = reward_points
        self.name_value = name_value
        self.size_addon = size_addon

    def insert_into_db(self):
        db = get_db()
    #    db.execute(CREATE TABLE drink (id INTEGER PRIMARY KEY, category TEXT NOT NULL, price INTEGER NOT NULL, rewards_scheme TEXT NOT NULL,rewards_points INTEGER NOT NULL, drink_name TEXT NOT NULL,size TEXT NOT NULL);)

        if self.category_value == 'drink':
            sql_query_string = """
                               INSERT INTO drink
                               (id,category,price,rewards_scheme,rewards_points,drink_name,drink_size)
                               VALUES (?,?,?,?,?,?,?);"""
            data_tuple = (self.id_value,self.category_value,self.price_value,self.rewards_scheme_value,self.rewards_points,self.name_value,self.size_addon)
            db.execute(sql_query_string, data_tuple)
            db.commit()
        if self.category_value == 'sandwich':
            sql_query_string = """
                               INSERT INTO sandwich
                               (id,category,price,rewards_scheme,rewards_points,sandwich_name,addons)
                               VALUES (?,?,?,?,?,?,?);"""
            data_tuple = (self.id_value,self.category_value,self.price_value,self.rewards_scheme_value,self.rewards_points,self.name_value,self.size_addon)
            db.execute(sql_query_string, data_tuple)
            db.commit()
        if self.category_value == 'retail':
            sql_query_string = """
                               INSERT INTO retail
                               (id,category,price,rewards_scheme,rewards_points,retail_name)
                               VALUES (?,?,?,?,?,?);"""
            data_tuple = (self.id_value,self.category_value,self.price_value,self.rewards_scheme_value,self.rewards_points,self.name_value)
            db.execute(sql_query_string, data_tuple)
            db.commit()

        return "Success"
