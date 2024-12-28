def calculate_shooting_percentage(df):
    """Calculates shooting percentage by range."""
    player_range_stats = df.groupby(['SHOOTER', 'RANGE']).agg({'SHOT_ATTEMPTED': 'sum', 'SHOT_MADE': 'sum'})
    player_range_stats['SHOOTING_PERCENTAGE'] = player_range_stats['SHOT_MADE'] / player_range_stats['SHOT_ATTEMPTED']
    return player_range_stats

def calculate_shooting_percentage_by_distance(df):
    # Group by distance and calculate shooting percentage
    distance_stats = df.groupby('DISTANCE').agg({'SHOT_ATTEMPTED': 'sum', 'SHOT_MADE': 'sum'})
    distance_stats['SHOOTING_PERCENTAGE'] = distance_stats['SHOT_MADE'] / distance_stats['SHOT_ATTEMPTED']
    return distance_stats