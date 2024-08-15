import pandas as pd

# Load the data from CSV file
data_file = 'trackman.csv'  # Replace with your file path
df = pd.read_csv(data_file)

# 1. Descriptive Statistics
def descriptive_statistics(df):
    print("Descriptive Statistics:")
    print(df.describe(include='all'))

# 2. Pitch Analysis
def pitch_analysis(df):
    print("\nPitch Analysis:")
    # Average pitch speed
    avg_pitch_speed = df['RelSpeed'].mean()
    print(f"Average Pitch Speed: {avg_pitch_speed:.2f} mph")

    # Average spin rate
    avg_spin_rate = df['SpinRate'].mean()
    print(f"Average Spin Rate: {avg_spin_rate:.2f} RPM")

    # Average vertical and horizontal break
    avg_vert_break = df['VertBreak'].mean()
    avg_horz_break = df['HorzBreak'].mean()
    print(f"Average Vertical Break: {avg_vert_break:.2f} inches")
    print(f"Average Horizontal Break: {avg_horz_break:.2f} inches")

# 3. Batter Performance
def batter_performance(df):
    print("\nBatter Performance:")
    # Average exit speed
    avg_exit_speed = df['ExitSpeed'].mean()
    print(f"Average Exit Speed: {avg_exit_speed:.2f} mph")

    # Average launch angle
    avg_launch_angle = df['Angle'].mean()
    print(f"Average Launch Angle: {avg_launch_angle:.2f} degrees")

    # Count hit types
    hit_types = df['HitType'].value_counts()
    print("Hit Types Distribution:")
    print(hit_types)

# 4. Pitcher vs. Batter Analysis
def pitcher_batter_analysis(df):
    print("\nPitcher vs. Batter Analysis:")
    # Group by pitcher and calculate average pitch speed
    pitcher_avg_speed = df.groupby('Pitcher')['RelSpeed'].mean()
    print("Average Pitch Speed by Pitcher:")
    print(pitcher_avg_speed)

    # Group by batter and calculate average exit speed
    batter_avg_exit_speed = df.groupby('Batter')['ExitSpeed'].mean()
    print("Average Exit Speed by Batter:")
    print(batter_avg_exit_speed)

# 5. Correlation Analysis
def correlation_analysis(df):
    print("\nCorrelation Analysis:")
    # Calculate correlation matrix
    correlation_matrix = df[['RelSpeed', 'SpinRate', 'VertBreak', 'HorzBreak', 'ExitSpeed', 'Angle']].corr()
    print("Correlation Matrix:")
    print(correlation_matrix)

# Run all analyses
descriptive_statistics(df)
pitch_analysis(df)
batter_performance(df)
pitcher_batter_analysis(df)
correlation_analysis(df)
