import pandas as pd
import numpy as np

# Load dataset
pldata = pd.read_csv('API-MATCHES.csv')

def TeamsApi():
    teams = list(set(list(pldata['team1']) + list(pldata['team2'])))
    teams_dict = {
        'teams': teams
    }
    return teams_dict

def teamvteam(team1, team2):
    """Return head-to-head summary between two teams.

    Returns a dict with keys:
      - total_games_played (int)
      - <team1>_wins (int)
      - <team2>_wins (int)
      - draws (int)

    If input is invalid or teams not found, returns an error dict.
    """
    # basic validation
    if not team1 or not team2:
        return {'error': 'Both team1 and team2 are required'}

    # confirm teams exist in the dataset
    all_teams = set(pldata['team1'].dropna().unique()).union(set(pldata['team2'].dropna().unique()))
    if team1 not in all_teams or team2 not in all_teams:
        return {'error': 'One or both teams not found in dataset'}

    # build mask for matches where the two teams played each other (either order)
    mask = ((pldata['team1'] == team1) & (pldata['team2'] == team2)) | ((pldata['team1'] == team2) & (pldata['team2'] == team1))
    temp_df = pldata[mask]

    total_games_played = int(temp_df.shape[0])
    matches_won_counts = temp_df['winner'].value_counts()
    matches_won_by_team1 = int(matches_won_counts.get(team1, 0))
    matches_won_by_team2 = int(matches_won_counts.get(team2, 0))
    draws = total_games_played - matches_won_by_team1 - matches_won_by_team2

    return {
        'total_games_played': total_games_played,
        f'{team1}_wins': matches_won_by_team1,
        f'{team2}_wins': matches_won_by_team2,
        'draws': draws
    }
