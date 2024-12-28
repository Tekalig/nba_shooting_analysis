import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

def plot_shot_density(df):
    """Creates a heatmap of shot density on the court."""
    fig = px.density_heatmap(
        df,
        x='X',
        y='Y',
        nbinsx=30,
        nbinsy=30,
        color_continuous_scale='Viridis',
        title='Shot Density Heatmap'
    )
    fig.update_layout(
        xaxis_title="Horizontal Distance (ft)",
        yaxis_title="Vertical Distance (ft)",
        coloraxis_colorbar=dict(title="Shot Density")
    )
    fig.show()

def plot_shots(df):
    """Plots the shots made by each player based on X and Y positions."""
    made_shots = df[df['SCORE'] == 'MADE']
    plt.figure(figsize=(12, 8))
    sns.scatterplot(data=made_shots, x='X', y='Y', hue='SHOOTER', style='SHOOTER', palette='deep')
    plt.title('Shots Made by X and Y Position on the Court')
    plt.xlabel('Horizontal Distance (ft)')
    plt.ylabel('Vertical Distance (ft)')
    plt.legend(title='Player')
    plt.show()

def plot_shot_outcomes(df):
    """Scatter plot of shot outcomes (made vs. missed)."""
    fig = px.scatter(
        df,
        x='X',
        y='Y',
        color='SCORE',
        symbol='SCORE',
        title='Shot Outcomes (Made vs. Missed)',
        color_discrete_map={'MADE': 'green', 'MISSED': 'red'},
    )
    fig.update_layout(
        xaxis_title="Horizontal Distance (ft)",
        yaxis_title="Vertical Distance (ft)",
        legend_title="Shot Outcome"
    )
    fig.show()

def plot_player_heatmap(df):
    """Creates a heatmap of shot density for each player."""
    fig = px.density_heatmap(
        df,
        x='X',
        y='Y',
        facet_col='SHOOTER',
        nbinsx=30,
        nbinsy=30,
        color_continuous_scale='Blues',
        title='Player-Specific Shot Density Heatmap'
    )
    fig.update_layout(
        xaxis_title="Horizontal Distance (ft)",
        yaxis_title="Vertical Distance (ft)",
        coloraxis_colorbar=dict(title="Shot Density")
    )
    fig.show()


def plot_shooting_percentage_on_court(df, distance_stats):
    """Visualize shooting percentage on a basketball court."""
    distance_stats.reset_index(inplace=True)

    # Create the basketball court
    fig = go.Figure()

    # Add court lines
    court_shapes = [
        # Outer box
        dict(type="rect", x0=-25, y0=0, x1=25, y1=47, line=dict(color="black", width=2)),
        # Free throw circle
        dict(type="circle", x0=-6, y0=19, x1=6, y1=31, line=dict(color="black", width=2)),
        # Hoop
        dict(type="circle", x0=-0.75, y0=0, x1=0.75, y1=1.5, line=dict(color="black", width=2)),
        # Backboard
        dict(type="line", x0=-3, y0=0, x1=3, y1=0, line=dict(color="black", width=2)),
        # 3-point line arc
        dict(
            type="path",
            path="M -22,0 A 23,23 0 0,1 22,0",
            line=dict(color="black", width=2),
        ),
    ]

    for shape in court_shapes:
        fig.add_shape(shape)

    # Normalize distances for plotting on the court
    max_distance = df['DISTANCE'].max()
    distance_stats['scaled_distance'] = (distance_stats['DISTANCE'] / max_distance) * 23  # Scale to fit 3-point arc

    # Add shooting percentage as scatter points
    fig.add_trace(go.Scatter(
        x=distance_stats['scaled_distance'] * np.cos(np.linspace(0, 2 * np.pi, len(distance_stats))),
        y=distance_stats['scaled_distance'] * np.sin(np.linspace(0, 2 * np.pi, len(distance_stats))),
        mode='markers',
        marker=dict(
            size=distance_stats['SHOT_ATTEMPTED'] * 2,  # Marker size based on shot attempts
            color=distance_stats['SHOOTING_PERCENTAGE'],  # Color based on shooting percentage
            colorscale='Viridis',
            colorbar=dict(title="Shooting %"),
            showscale=True
        ),
        text=[f"{p:.2%}" for p in distance_stats['SHOOTING_PERCENTAGE']],  # Tooltip
        hoverinfo="text"
    ))

    # Update layout for better visualization
    fig.update_layout(
        title="Shooting Percentage on Basketball Court",
        xaxis=dict(title="Horizontal Distance (ft)", range=[-30, 30]),
        yaxis=dict(title="Vertical Distance (ft)", range=[-10, 50]),
        showlegend=False,
        height=600,
        width=600,
        shapes=court_shapes
    )

    fig.show()

