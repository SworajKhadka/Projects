#here, we are creating our own API using Flask framework in Python.
# # This is a sample Python script.
from flask import Flask,jsonify,request
import ipl

from flask import jsonify, request
app = Flask(__name__)
@app.route('/')
def home():
    return "Welcome to the API project using Flask!"


@app.route('/api/teams')
def get_teams():
    teams = ipl.TeamsApi()
    return jsonify(teams)


@app.route('/api/teamvteam')
def teamvteam():
    team1=request.args.get('team1')
    team2=request.args.get('team2')
    teamvteam=ipl.teamvteam(team1,team2)

    return jsonify(teamvteam)
app.run(debug=True)
