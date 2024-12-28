# NBA Shooting Data Analysis

## Project Overview
This project analyzes NBA shooting data to provide tailored recommendations for players based on their shooting performance during the 2021 NBA Playoffs. The analysis involves exploring player shooting patterns, calculating shooting percentages, and generating actionable insights to improve performance.

## Features
- **Data Preprocessing**: Load and preprocess the raw dataset to calculate shot attempts, made shots, and distances.
- **Visualization**: Create scatter plots and heatmaps to analyze player shot distributions.
- **Statistical Analysis**: Compute shooting percentages by distance and range.
- **Recommendations**: Generate player-specific insights based on shooting data.
- **Report Generation**: Summarize findings in a user-friendly format.

## Directory Structure
```
nba_shooting_analysis/
├── data/
│   └── nba_players_shooting.csv       # Raw dataset
├── src/
│   ├── __init__.py
│   ├── data_processing.py            # Data loading and preprocessing
│   ├── data_visualization.py         # Visualization functions
│   ├── statistical_analysis.py       # Analytical functions
│   ├── recommendations.py            # Recommendation generation
│   └── report_generation.py          # Report generation functions
├── notebooks/
│   └── exploratory_analysis.ipynb    # Initial exploration and prototyping
├── tests/
│   └── test_data_processing.py       # Unit tests for data processing
├── requirements.txt                  # Dependencies
└── README.md                         # Project documentation
```

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd nba_shooting_analysis
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the exploratory analysis notebook:
   ```bash
   jupyter notebook notebooks/exploratory_analysis.ipynb
