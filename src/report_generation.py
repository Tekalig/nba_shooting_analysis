def generate_report(recommendations):
    """Generates a report summarizing the recommendations."""
    for player, recommendation in recommendations.items():
        print(f"{player}: {recommendation}")