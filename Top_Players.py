from flask_table import Table, Col
import csv
import os


class TopPlayers:
    @staticmethod
    def top_10_players():  # This function returns a list with the 10 best players that are registered on the website.
        list_players_ratings = []  # We will store the username and ratings of the top ten players
        with open(os.getcwd() + "/users.csv", "r", newline='') as file:
            reader = csv.reader(file)
            for line in reader:
                # Adding the Username-rating pair as a dictionary to the list

                list_players_ratings.append({"Username": line[0], "Rating": line[2]})

        # Return the sorted list of dictionaries in descending order by the rating:
        data_list = sorted(list_players_ratings, key=lambda i: int(i['Rating']), reverse=True)
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
