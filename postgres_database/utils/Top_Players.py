from flask_table import Table, Col
import csv
import os
from postgres_database.utils import connection_settings as cs
import pandas as pd


class TopPlayers:
    @staticmethod
    def top_10_players():  # This function returns a list with the 10 best players that are registered on the website.

        conn = cs.get_conn()
        df = pd.read_sql_query("select username, rating from chess.users order by rating desc limit 10;", conn)
        data_list = list()

        count = 0
        for row in df.iterrows():
            data_list.append(
                {
                    "Username": df.loc[count]['username'],
                    "Rating": df.loc[count]['rating']
                 })
            count += 1

        return data_list


class CreateTable(Table):  # Declaring the table
    classes = ["table table-sm table-dark table-hover table-striped"]
    table_id = "table"
    # Creating table headers and rows
    ranking = Col("Ranking")
    username = Col("Username")
    rating = Col("Rating")


class CreateTableItems(object):
    def __init__(self, ranking, username, rating):
        self.ranking = ranking
        self.username = username
        self.rating = rating
