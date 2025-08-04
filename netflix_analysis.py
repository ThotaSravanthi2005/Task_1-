import pandas as pd
import matplotlib.pyplot as plt

def load_netflix_data(file_path):
    """Load Netflix data from CSV or Excel file"""
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith(('.xlsx', '.xls')):
        return pd.read_csv(file_path)
    else:
        raise ValueError("Unsupported file format. Please use CSV or Excel.")

def analyze_netflix_data(df):
    """Perform analysis on Netflix data"""
    # Filter movies and TV shows
    movies = df[df['type'] == 'Movie'].copy()
    tv_shows = df[df['type'] == 'TV Show'].copy()

    # Basic analysis
    print("\n=== Basic Statistics ===")
    print(f"Total entries: {len(df)}")
    print(f"Movies: {len(movies)}")
    print(f"TV Shows: {len(tv_shows)}")

    # Release year analysis
    print("\n=== Release Year Analysis ===")
    print("Movies by year:")
    print(movies['release_year'].value_counts().head(10))
    print("\nTV Shows by year:")
    print(tv_shows['release_year'].value_counts().head(10))

    # Duration analysis
    print("\n=== Duration Analysis ===")
    print("Movie durations:")
    print(movies['duration'].describe())
    print("\nTV Show seasons:")
    print(tv_shows['duration'].describe())

    # Visualization
    plt.figure(figsize=(12, 6))
    
    # Content by type pie chart
    plt.subplot(1, 2, 1)
    df['type'].value_counts().plot.pie(autopct='%1.1f%%')
    plt.title('Content Type Distribution')
    
    # Top 10 countries bar chart
    plt.subplot(1, 2, 2)
    df['country'].value_counts().head(10).plot.bar()
    plt.title('Top 10 Countries')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()

def main():
    try:
        # Replace with your actual file path
        file_path = 'netflix_titles.csv'  
        df = load_netflix_data(file_path)
        analyze_netflix_data(df)
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()