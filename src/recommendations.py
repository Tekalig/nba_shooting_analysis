def generate_recommendations(stats):
    """Generates tailored recommendations based on shooting statistics."""
    recommendations = {}
    for player, group in stats.groupby('SHOOTER'):
        optimal_range = group['SHOOTING_PERCENTAGE'].idxmax()
        recommendations[player] = f"Focus on shots from {optimal_range} range."
    return recommendations